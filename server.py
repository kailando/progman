from os.path import join, abspath
from flask import Flask, send_from_directory, render_template

app=Flask(__name__, template_folder=abspath("web"))
assets=join(app.root_path, "assets")
@app.route("/")
def home():
    return render_template("main_page/index.html")

@app.route("/favicon.ico")
def favicon():
    return send_from_directory(
        assets,
        "favicon.png",
        mimetype="image/png"
    )

app.run(debug=False, use_reloader=True)
