pipeline {
    agent any

    environment {
        IMAGE_NAME = 'flask-first-server'
        IMAGE_TAG = 'latest'
        DOCKER_HUB_USER = 'yourusername' // Replace with your Docker Hub username
    }

    stages {

        stage('Checkout') {
            steps {
                echo "Code checked out from Git (handled by Pipeline script from SCM)"
            }
        }

        stage('Setup Python & Install Dependencies') {
            steps {
                echo "Creating virtual environment and installing dependencies"
                bat 'python -m venv venv'
                bat '.\\venv\\Scripts\\python.exe -m pip install --upgrade pip'
                bat '.\\venv\\Scripts\\python.exe -m pip install -r requirements.txt'
            }
        }

        stage('Run Tests') {
            steps {
                echo "Running pytest"
                bat '.\\venv\\Scripts\\python.exe -m pytest'
            }
        }

        stage('Build Docker Image') {
            steps {
                echo "Building Docker image"
                bat "docker build -t %IMAGE_NAME% ."
            }
        }

        stage('Tag Docker Image') {
            steps {
                echo "Tagging Docker image for Docker Hub"
                bat "docker tag %IMAGE_NAME%:latest %DOCKER_HUB_USER%/%IMAGE_NAME%:%IMAGE_TAG%"
            }
        }

        stage('Push to Docker Hub') {
            steps {
                echo "Logging in and pushing Docker image to Docker Hub"
                withCredentials([usernamePassword(credentialsId: 'docker-hub-cred', usernameVariable: 'USERNAME', passwordVariable: 'PASSWORD')]) {
                    bat 'echo %PASSWORD% | docker login -u %USERNAME% --password-stdin'
                    bat "docker push %DOCKER_HUB_USER%/%IMAGE_NAME%:%IMAGE_TAG%"
                }
            }
        }

        stage('Run Container Locally') {
            steps {
                echo "Stopping old container (if exists) and running new container"
                catchError(buildResult: 'SUCCESS', stageResult: 'FAILURE') {
                    bat 'docker stop flask-first-server || echo No container running'
                    bat 'docker rm flask-first-server || echo No container to remove'
                    bat 'docker run -d -p 8000:8000 --name flask-first-server %DOCKER_HUB_USER%/%IMAGE_NAME%:%IMAGE_TAG%'
                }
            }
        }
    }
}