from flask import Flask
import os

app = Flask(__name__)

@app.route("/")
def home():
    message = os.getenv("APP_MESSAGE", "Hello from Docker!")
    return f"<h1>{message}</h1>"

@app.route("/save")
def save():
    os.makedirs("/data", exist_ok=True)

    with open("/data/test.txt", "w") as file:
        file.write("My Docker volume data is persistent!")

    return "Data saved successfully!"

@app.route("/read")
def read():
    with open("/data/test.txt", "r") as file:
        return file.read()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
