"""
Joey Mock's Flask API.
"""

from flask import Flask
from flask import send_file
import os
import configparser

app = Flask(__name__)

@app.route("/")
def hello():
    return "UOCIS docker demo!\n"

@app.route("/<filename>")
def serve_file(filename):
    dir_path = "pages/"
    if ('~' in filename or '..' in filename):
        return open(dir_path + "403.html"), 403
    try:

        return open(dir_path + filename), 200
    except FileNotFoundError:
        return open(dir_path + "404.html"), 404

def parse_config(config_paths):
    config_path = None
    for f in config_paths:
        if os.path.isfile(f):
            config_path = f
            break

    if config_path is None:
        raise RuntimeError("Configuration file not found!")

    config = configparser.ConfigParser()
    config.read(config_path)
    return config

config = parse_config(["credentials.ini", "default.ini"])
port = config["SERVER"]["PORT"]
debug = config["SERVER"]["DEBUG"]
print(port + "\n" + debug)

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
