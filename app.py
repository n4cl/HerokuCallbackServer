from datetime import datetime
from flask import Flask, request, jsonify


app = Flask(__name__)


def logging_request(_data: dict, file_type: str):
    print({"timestamp": datetime.now(),
           "data": _data,
           "file_type": file_type})

@app.get('/')
def hello():
    return jsonify({"message": "Hello"})

@app.post('/')
def post():
    if request.content_type == "application/json":
        logging_request(request.get_json(), "application/json")
    if request.form:
        logging_request(dict(request.form), "form")

    return jsonify({"message": "post"})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)
