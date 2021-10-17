from james_code.ai import *
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


@app.route('/predict')
def predictFunction():
    answers = predict()
    return {"answers": answers}


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
