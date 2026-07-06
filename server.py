from os.path import join
from flask import Flask, send_from_directory

app=Flask(__name__)
assets=join(app.root_path, "assets")
@app.route("/")
def home():
    return "Test"

@app.route("/favicon.ico")
def favicon():
    return send_from_directory(
        assets,
        "favicon.png",
        mimetype="image/png"
    )
app.run()