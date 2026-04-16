from flask import Blueprint, render_template, url_for, redirect, request, flash
from . import Db
from flask_login import login_user, logout_user, login_required

auth=Blueprint("auth", __name__)

@auth.route("/login", methods=["POST", "GET"])
def login():
    if request.method=="POST":
        email=request.form.get("email")
        password=request.form.get("password")

        return redirect(url_for("signup"))

    return render_template("login.html")

@auth.route("/signup", methods=["POST", "GET"])
def signup():
    return render_template("signup.html")

@auth.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("login"))