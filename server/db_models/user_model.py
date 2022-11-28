from flask_sqlalchemy import SQLAlchemy
from uuid import uuid4

db = SQLAlchemy()


def get_uuid():
    return uuid4().hex


class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.String(32), primary_key=True, unique=True, default=get_uuid)
    username = db.Column(db.String(20), nullable=False)
    forename = db.Column(db.String(20), nullable=False)
    surename = db.Column(db.String(20), nullable=False)
    password = db.Column(db.Text, nullable=False)

    def __repr__(self) -> str:
        return f'<User @{self.username} | {self.forename.capitalize()} {self.surename.capitalize()} >'