from flask import Flask

app = Flask(__name__)


@app.route('/')
def financeapp():
    return 'Hello, World!'