from app import marsh
from models.conditions import ConditionsModel
from marshmallow import fields


class ConditionsSchema(marsh.SQLAlchemyAutoSchema):

    comments = fields.Nested("CommentSchema", many=True)


    class Meta:
        model = ConditionsModel
        load_instance = True
        # ! Now include the user_id when serializing.
        include_fk = True
