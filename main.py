# Flask Server and Routing
from flask import Flask, send_from_directory
from flask_mobility import Mobility
from flask_talisman import Talisman

# Date
from datetime import datetime

from random import randint

# File management
import codecs
import os

# Threading
from threading import Thread

# WSGIServer
from gevent.pywsgi import WSGIServer

# Logging
import logging

# Disable Warnings
import warnings

warnings.filterwarnings("ignore")

# Logging configuration set to debug on debug.log file
logging.basicConfig(filename="debug.log", level=logging.DEBUG)
logging.basicConfig(format="%(asctime)s %(message)s", datefmt="%m/%d/%Y %I:%M:%S %p")

# Disable unneeded dependencies logging
werkzeugLog = logging.getLogger("werkzeug")
werkzeugLog.disabled = True
requestsLog = logging.getLogger("urllib3.connectionpool")
requestsLog.disabled = True


def run():
    # WSGIServer
    WSGIServer(("", 8081), app).serve_forever()


# Thread
def keep_alive():
    t = Thread(target=run)
    t.start()


# Flask App initialization
app = Flask(__name__)
# Serverside Mobile Differentiation
Mobility(app)
# SSL
Talisman(app, content_security_policy=None)


# Main Endpoint
@app.route("/")
def main():
    # index.html
    t = datetime.today().strftime("%Y-%m-%d-%H-%M-%S")

    main_color = "E2C044"
    alt_color = "413C58"

    if randint(0, 1):
        return codecs.open("web/index.html", "r", "utf-8").read().replace("REPLACE", t)
    else:
        return (
            codecs.open("web/index.html", "r", "utf-8")
            .read()
            .replace("REPLACE", t)
            .replace(main_color, alt_color)
            .replace("sourscode.svg", "sourscode_w.svg")
        )


# Favicon
@app.route("/favicon.ico")
def favicon():
    return send_from_directory(
        os.path.join(app.root_path, "static"),
        "favicon.ico",
        mimetype="image/vnd.microsoft.icon",
    )


# Service Worker
@app.route("/service-worker.js")
def service_worker():
    return send_from_directory(
        os.path.join(app.root_path, "static"),
        "service-worker.js",
        mimetype="application/javascript",
    )


# PWA Manifest
@app.route("/manifest.json")
def manifest():
    return send_from_directory(
        os.path.join(app.root_path, "static"),
        "manifest.json",
        mimetype="application/json",
    )


if __name__ == "__main__":
    # Run server forever
    keep_alive()
