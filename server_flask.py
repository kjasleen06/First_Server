from flask import Flask, jsonify  # import from Flask library

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello, Worldddddd!"

@app.route("/json")
def json_data():
    return jsonify({"message": "Hello, JSON World!"})

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=8000) # auto-reload enabled