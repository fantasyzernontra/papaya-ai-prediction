from werkzeug.datastructures import FileStorage
from james_code.ai import *
from flask import Flask, request, Response
import jsonpickle


app = Flask(__name__)


@app.route("/")
def index():
    return "Hi There! We're group 3, named 'Papaya Token'."


@app.route('/post', methods=["POST"])
def postJa():
    return {
        'text': "test"
    }


@app.route('/predict',  methods=["POST"])
def predictFunction():
    try:
        sendedPictures = request.files['predicted-pictures'].read()
        answers = predict(sendedPictures)
        print('answers', answers)
        # return {"answers": answers}
    except Exception as err:
        response_msg = jsonpickle.encode({"message": err})
        return Response(response=response_msg, status=400, mimetype="application/json")


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
