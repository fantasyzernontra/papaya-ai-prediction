from flask import Flask

app = Flask(__name__)


@app.route("/")
def index():
    return "Hi There! We're group 3, named 'Papaya Token'."


@app.route('/post', methods=["POST"])
def postJa():
    return {
        'text': "test"
    }
