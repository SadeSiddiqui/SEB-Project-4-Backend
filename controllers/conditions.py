# * Here is my controller for conditions (as well as views)

from http import HTTPStatus

from flask import Blueprint, request, g  # ! import g
from marshmallow.exceptions import ValidationError

from models.conditions import ConditionsModel

from models.comments import CommentModel

from serializers.conditions import ConditionsSchema

from serializers.comments import CommentSchema


from middleware.secure_route import secure_route

conditions_schema = ConditionsSchema()
comment_schema = CommentSchema()

router = Blueprint("conditions", __name__)


@router.route("/conditions", methods=["GET"])
def get_conditions():
    # ? This tells SQLAlchemy to run the following SQL (roughly):
    # * SELECT * FROM conditions;
    conditions = ConditionsModel.query.all()

    return conditions_schema.jsonify(conditions, many=True)


@router.route("/conditions/<int:conditions_id>", methods=["GET"])
def get_single_condition(conditions_id):
    conditions = ConditionsModel.query.get(conditions_id)

    return conditions_schema.jsonify(conditions)


@router.route("/conditions", methods=["POST"])
@secure_route
def create():
    conditions_dictionary = request.json
    # ! Add the current user to the conditions_dictionary here BEFORE its saved
    conditions_dictionary["user_id"] = g.current_user.id

    try:
        conditions = conditions_schema.load(conditions_dictionary)
        conditions.save()
    except ValidationError as e:
        return {"errors": e.messages, "message": "Something went wrong"}

    return conditions_schema.jsonify(conditions)


@router.route("/conditions/<int:conditions_id>", methods=["PUT", "PATCH"])
@secure_route
def update_condition(conditions_id):

    conditions_dictionary = request.json

    existing_conditions = ConditionsModel.query.get(conditions_id)

    if not existing_conditions:
        return {"message": "No conditions found"}, HTTPStatus.NOT_FOUND

    try:
        # ! Is this person the conditioner owner or not?
        if existing_conditions.user_id != g.current_user.id:
            return {
                "message": "This is not your condition. Please assist others in your own way."
            }, HTTPStatus.UNAUTHORIZED

        conditions = conditions_schema.load(
            conditions_dictionary, instance=existing_conditions, partial=True
        )

        conditions.save()
    except ValidationError as e:
        return {"errors": e.messages, "message": "Something went wrong"}
    return conditions_schema.jsonify(conditions), HTTPStatus.OK


@router.route("/conditions/<int:conditions_id>", methods=["DELETE"])
@secure_route
def remove_condition(conditions_id):

    conditions = ConditionsModel.query.get(conditions_id)

    if not conditions:
        return {"message": "No condition found"}, HTTPStatus.NOT_FOUND

    conditions.remove()

    return "", HTTPStatus.NO_CONTENT


@router.route("/posts/<int:conditions_id>", methods=["POST"])
@secure_route
def create_comment(conditions_id):

    comment_dictionary = request.json
    comment_dictionary["conditions_id"] = conditions_id
    comment_dictionary["user_id"] = g.current_user.id

    existing_conditions = ConditionsModel.query.get(conditions_id)
    if not existing_conditions:
        return {"message": "No condition found"}, HTTPStatus.NOT_FOUND

    try:
        print("Hey")
        comment = comment_schema.load(comment_dictionary)
        print("hello")
        comment.conditions_id = conditions_id
        comment.save()
    except ValidationError as e:
        return {"errors": e.messages, "message": "Something went wrong"}

    return comment_schema.jsonify(comment), HTTPStatus.CREATED


@router.route("/posts/<int:comment_id>", methods=["DELETE"])
@secure_route
def remove_comment(comment_id):
    current_user = g.current_user  # Get the current user from the g object
    comment = CommentModel.query.get(comment_id)
    if not comment:
        return {"message": "No comment found"}, HTTPStatus.NOT_FOUND
    # Check if the current user is the author of the comment
    if comment.user_id != current_user.id:
        return {
            "message": "You are not authorized to delete this comment"
        }, HTTPStatus.UNAUTHORIZED
    comment.remove()
    return "", HTTPStatus.NO_CONTENT
