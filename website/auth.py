from flask import Blueprint, render_template, url_for, redirect, request, flash
from . import Db
from flask_login import login_user, logout_user, login_required
from .model import User

auth=Blueprint("auth", __name__)

@auth.route("/login", methods=["POST", "GET"])
def login():
    if request.method=="POST":
        email=request.form.get("email")
        password=request.form.get("password")

        user=User.query.filter_by(email=email).first()
        if user:
            if password==user.password:
                flash("Logged in!", category="success")
                login_user(user, remember=True)
                return redirect(url_for("views.home"))
            else:
                flash("Password is incorrect", category="error")
        else:
            flash("User doesn't exist", category="error")

    return render_template("login.html")

@auth.route("/signup", methods=["POST", "GET"])
def signup():
    return render_template("signup.html")

@auth.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("login"))