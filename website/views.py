from flask import Blueprint, redirect, render_template, request, flash, url_for
from flask_login import login_required, current_user
from . import Db
from .model import User, Task

views=Blueprint("views", __name__)

@views.route("/")
@views.route("/home")
@login_required
def home():
    tasks=Task.query.all()
    return render_template("home.html", user=current_user, tasks=tasks)

@views.route("/addtask", methods=["POST", "GET"])
def add_task():
    if request.method=="POST":
        text=request.form.get("text")

        if not text:
            flash("Post can't be empty", category="error")
        else:
            task=Task(text=text, author_id=current_user.id)
            Db.session.add(task)
            Db.session.commit()
            flash("Task added", category="success")
            return(redirect(url_for("views.home")))
        
    return render_template("addtask.html")