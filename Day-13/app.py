from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello():
    return "Hey .. This my basic app with Flask"


if __name__ == '__main__':
    app.run(debug=True)
