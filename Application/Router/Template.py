from flask import render_template, url_for, redirect, session

from ..Application import app


# TODO your router here
@app.route("/")
def root():
    return redirect(url_for("index"))


@app.route("/index", methods=["GET", "POST"])
def index():
    return render_template("index.html")


__all__ = ["root", "index"]
