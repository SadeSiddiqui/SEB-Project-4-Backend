from datetime import datetime, timedelta, timezone

import jwt

from sqlalchemy.ext.hybrid import hybrid_property

from app import db, bcrypt

from config.environment import secret

from models.base import BaseModel


class UserModel(db.Model, BaseModel):

    __tablename__ = "users"

    username = db.Column(db.Text, nullable=False, unique=True)
    email = db.Column(db.Text, nullable=False, unique=True)

    password_hash = db.Column(db.Text, nullable=True)

    # ! Add opposite relationship here
    conditions = db.relationship("ConditionsModel", back_populates="user")

    @hybrid_property
    def password(self):
        pass

    @password.setter
    def password(self, password_plaintext):
        encoded_pw = bcrypt.generate_password_hash(password_plaintext)
        self.password_hash = encoded_pw.decode("utf-8")

    def validate_password(self, password_plaintext):
        return bcrypt.check_password_hash(self.password_hash, password_plaintext)

    def generate_token(self):

        payload = {
            "exp": datetime.now(timezone.utc) + (timedelta(days=1)),  # Expiry date
            "iat": datetime.now(timezone.UTC),
            "sub": self.id,
        }

        token = jwt.encode(payload, secret, algorithm="HS256")

        return token
