from app import db
from models.comments import CommentModel
from models.users import UserModel
from models.base import BaseModel



class ConditionsModel(db.Model, BaseModel):

    __tablename__ = "conditions"

    name = db.Column(db.Text, nullable=False, unique=True)
    about = db.Column(db.Text, nullable=False)
    info = db.Column(db.Text, nullable=False)
    advice = db.Column(db.Text, nullable=False)
    # ! Adding a column to connect conditions and users one to many.
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)

    comments = db.relationship(
        "CommentModel", backref="comments", cascade="all, delete"
    )
    # ! Adding the user model to our conditions.
    user = db.relationship("UserModel", back_populates="conditions")
