from flask import Flask, render_template
from flask_socketio import SocketIO, emit

app = Flask(__name__, static_url_path='/static')
app.config["SECRET_KEY"] = "SECRET_KEY_LIVE_MESSAGE"

socketio = SocketIO(app)


@app.route("/")
def hello_world():
    return "Hello, World!"


@app.route("/messages")
def render_messages():
    return render_template("index.html")


@socketio.on("message")
def handle_message(msg):
    emit("message", msg, broadcast=True)


if __name__ == "__main__":
    app.run(debug=True)
