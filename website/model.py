from . import Db
from flask_login import UserMixin
from sqlalchemy.sql import func

class StatusEnum:
    ongoing = "ongoing"
    postponed = "postponed"
    completed = "completed"

class User(Db.Model, UserMixin):
    id = Db.Column(Db.Integer, primary_key=True)
    email = Db.Column(Db.String(150), unique=True, nullable=False)
    username = Db.Column(Db.String(150), unique=True, nullable=False)
    password = Db.Column(Db.String(150), nullable=False)
    date_created = Db.Column(Db.DateTime(timezone=True), default=func.now())
    tasks = Db.relationship("Task", backref="author", passive_deletes=True)

class Task:
    id = Db.Column(Db.Integer, primary_key=True)
    text = Db.Column(Db.Text, nullable=False)
    status = Db.Column(Db.Enum(StatusEnum), nullable=False, default=StatusEnum.ongoing)
    deadline = Db.Column(Db.DateTime(timezone=True), nullable=True)
    date_created = Db.Column(Db.DateTime(timezone=True), default=func.now())
    author_id = Db.Column(Db.Integer, Db.ForeignKey("user.id", ondelete="CASCADE"), nullable=False)