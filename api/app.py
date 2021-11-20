from werkzeug.datastructures import FileStorage
from james_code.ai import *
from flask import Flask, request, Response
import jsonpickle
import os


app = Flask(__name__)


@app.route("/", methods=['GET'])
def index():
    return "Hi There! We're group 3, named 'Papaya Token'."


@app.route('/post', methods=["POST"])
def postJa():
    return "Greeting Krub! We're from POST method."


@app.route('/predict',  methods=["POST"])
def predictFunction():
    try:
        answers = []
        sendedPictures = request.files.getlist('predicted-pictures')
        for idx, pic in enumerate(sendedPictures):
            pic.save('pic.jpg')
            answers.append(predict('pic.jpg'))

        response = jsonpickle.encode({"answers": answers})
        return Response(response=response, status=200, mimetype="application/json")
    except Exception as err:
        response_msg = jsonpickle.encode({"message": err})
        return Response(response=response_msg, status=400, mimetype="application/json")


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))
