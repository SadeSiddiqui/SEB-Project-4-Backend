from app import db
from models.base import BaseModel


class CommentModel(db.Model, BaseModel):

    __tablename__ = "comments"

    content = db.Column(db.Text, nullable=False)
    title = db.Column(db.Text, nullable=False)

    # ! ForeignKey tells you which column to point at (conditions.id)
    # ! so that every comment points to a specific unique condition.
    # ! You usually give it the primarykey of a table, e.g. conditions.id
    conditions_id = db.Column(
        db.Integer, db.ForeignKey("conditions.id"), nullable=False
    )

    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)

    user = db.relationship(
        "UserModel", backref="users", cascade="all, delete"
    )
