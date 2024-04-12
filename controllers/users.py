from http import HTTPStatus

from flask import Blueprint, request
from marshmallow.exceptions import ValidationError

# ! import user model
from models.users import UserModel

from serializers.users import UserSchema

user_schema = UserSchema()

router = Blueprint("users", __name__)


@router.route("/signup", methods=["POST"])
def signup():
    user_dictionary = request.json

    try:
        user = user_schema.load(user_dictionary)
        user.save()
    except ValidationError as e:
        return {"errors": e.messages, "messsages": "Something went wrong"}

    return user_schema.jsonify(user)


@router.route("/login", methods=["POST"])
def login():
    # ! user provides a email & password
    user_dictionary = request.json
    # ! Check if the user with this email exists..
    user = UserModel.query.filter_by(email=user_dictionary["email"]).first()
    # ! If there's no user found:
    if not user:
        return {
            "message": "Your email or password was incorrect."
        }, HTTPStatus.UNAUTHORIZED
    # ! Validate the password against database password
    if not user.validate_password(user_dictionary["password"]):
        return {
            "message": "Your email or password was incorrect."
        }, HTTPStatus.UNAUTHORIZED
    # ! Make a token and send it back!
    token = user.generate_token()

    return {"token": token, "message": "Welcome back!"}
