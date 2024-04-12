from app import app, db
from models.conditions import ConditionsModel
from models.comments import CommentModel

# ! User seeding
from models.users import UserModel


with app.app_context():

    try:
        print("Creating our database...")
        db.drop_all()
        db.create_all()

        print("Seeding the database!")
        # ! User seeding
        user = UserModel(
            email="admin@admin.com", username="admin", password="Admin#123"
        )
        user.save()

        CrohnsDisease = ConditionsModel(
            name="Crohns Disease",
            about="My name is Evyn-Rose. I am 26 years old and have had crohns since 2020.",
            info="Crohn's Disease is IBD.",
            advice="Try not to eat things that upset your stomach.",
            user_id=user.id,
        )
        CrohnsDisease.save()

        comment = CommentModel(
            content="Don't soil yourself!", conditions_id=CrohnsDisease.id
        )
        comment.save()

        print("Database seeded!")
    except Exception as e:
        print(e)
