from flask import Flask

app = Flask(__name__)


@app.route("/")
def index():
    return (
        "Welcome to ScratchDBUpgraded. You can find documentation on the forum thread."
    )
