import flask
from flask import Flask

print(flask.__version__)

app = Flask(__name__)


@app.route("/")
def index():
    return "my blog"


if __name__ == "__main__":
    app.run()
