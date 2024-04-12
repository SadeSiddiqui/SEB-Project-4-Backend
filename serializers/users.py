from app import marsh
from models.users import UserModel
from marshmallow import fields, ValidationError
import re


# ! Here is a function for validating my password
def validate_password(password):
    # ! check that length is < 8 chars long
    if len(password) < 8:
        raise ValidationError("Make sure your password is at least 8 characters.")
    # ! If there's no A-Z characters (uppercase) in my string, error!
    elif re.search("[A-Z]", password) is None:
        raise ValidationError("Make sure your password contains a capital letter.")


class UserSchema(marsh.SQLAlchemyAutoSchema):

    # ! Add a password field so we can serialize it.
    password = fields.String(required=True, validate=validate_password)

    class Meta:
        model = UserModel
        load_instance = True
        # ! exclude will exclude from both serialization/deserialization
        exclude = ("password_hash",)  # ! don't forget the comma!
        # ! Only be expected when you deserialize.
        load_only = ("email", "password")
