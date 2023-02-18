from flask import Flask

app = Flask(__name__)

@app.route("/home")
def home():
    return "Hello from Swati v.0.0.2!"