from flask import render_template, url_for, redirect, session

from ..Application import app


@app.route("/")
def root():
    return redirect(url_for("index"))


@app.route("/index", methods=["GET", "POST"])
def index():
    tip = TipHelper.check_tips(session)
    if session.__dict__ is None:
        session["login"] = False
    return render_template("index.html", tip=tip)


__all__ = ["root", "index"]