from flask import Flask
from flask import jsonify

app = Flask(__name__)


@app.route("/")
def hello():
    data = {
    "name" : "takayuki",
    "age" : 34,
    "message": "Hello API",
    }
    return jsonify(data)


if __name__ == "__main__":
    app.run(debug=True)
