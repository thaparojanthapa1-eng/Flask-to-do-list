from flask import Blueprint, render_template, url_for, redirect, request, flash

auth=Blueprint("auth", __name__)

@auth.route("login", methods=["POST", "GET"])
def login():
    if request.method=="POST":
        email=request.form.get("email")
        password=request.form.get("password")

    return render_template("login.html")