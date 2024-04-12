from app import marsh
from models.comments import CommentModel


class CommentSchema(marsh.SQLAlchemyAutoSchema):

    class Meta:
        model = CommentModel
        load_instance = True
