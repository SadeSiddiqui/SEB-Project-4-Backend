from http import HTTPStatus

from flask import Blueprint, request, jsonify

from marshmallow.exceptions import ValidationError

from models.users import UserModel

from serializers.users import UserSchema


# Assuming UserModel and UserSchema are imported and defined somewhere in your code

user_schema = UserSchema()

router = Blueprint("users", __name__)


@router.route("/signup", methods=["POST"])
def signup():
    user_dictionary = request.json
    if user_dictionary["passwordConfirmation"] != user_dictionary["password"]:
        return {"error": "Password does not match"}

    del user_dictionary["passwordConfirmation"]

    try:
        user = user_schema.load(user_dictionary)
        user.save()
    except ValidationError as e:
        return {
            "errors": e.messages,
            "message": "Something went wrong",
        }, HTTPStatus.BAD_REQUEST

    return jsonify(user_schema.dump(user))


@router.route("/login", methods=["POST"])
def login():
    user_dictionary = request.json
    user = UserModel.query.filter_by(email=user_dictionary["email"]).first()
    if not user:
        return {
            "message": "Your email or password was incorrect."
        }, HTTPStatus.UNAUTHORIZED

    if not user.validate_password(user_dictionary["password"]):
        return {
            "message": "Your email or password was incorrect."
        }, HTTPStatus.UNAUTHORIZED

    token = user.generate_token()

    return {"token": token, "message": "Welcome back!"}


@router.route("/user", methods=["GET"])
def get_all_users():
    users = UserModel.query.all()
    serialized_users = user_schema.dump(users, many=True)
    return jsonify(serialized_users)


@router.route("/user/<int:user_id>", methods=["GET"])
def get_user_by_id(user_id):
    user = UserModel.query.get(user_id)
    if user:
        serialized_user = user_schema.dump(user)
        return jsonify(serialized_user)
    else:
        return {"error": "User not found"}, HTTPStatus.NOT_FOUND
