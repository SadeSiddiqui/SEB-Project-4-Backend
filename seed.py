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
            name="Crohn's Disease",
            about="My name is Evyn-Rose. I am 26 years old and have had Crohns since 2020. I have a severe case throughout my entire intestinal tract.",
            info="Crohn's Disease is an Inflammatory Bowel Disease, autoimmune in nature and affects many different body parts, especially the digestive tract. It has a similar nature to Lupus.",
            advice="Don't let anyone try to tell you what you can and can't eat. That is for you to decide.",
            user_id=user.id,
        )
        CrohnsDisease.save()

        Lupus = ConditionsModel(
            name="Lupus",
            about="My name is Anya. I am 22 years old and have had Lupus for one year at this point! I really struggle with my day to day and am still not in remission.",
            info="Lupus is a chronic autoimmune disease where the body's immune system attacks its own tissues and organs. Lupus can affect various parts of the body, including the skin, joints, kidneys, heart, lungs, brain, and blood cells.",
            advice="Prioritize your self care days! Don't feel guilty for it!",
            user_id=user.id,
        )

        Lupus.save()

        MultipleSclerosis = ConditionsModel(
            name="MS - Multiple Sclerosis",
            about="My name is Charles and I have MS! I am 67 years old and have spent quite a few years battling this!",
            info="Multiple sclerosis is a chronic autoimmune condition that affects the central nervous system, leading to damage of the myelin sheath and disruption of nerve signals, often resulting in various neurological symptoms.",
            advice="Look into all methods of medication and don't be afraid to seek different opinions",
            user_id=user.id,
        )
        MultipleSclerosis.save()

        comment1 = CommentModel(
            content="I have Crohns, too! It really affects my skin and eyes.",
            title="Crohn's Sisters!",
            conditions_id=CrohnsDisease.id,
        )
        comment1.save()

        comment2 = CommentModel(
            content="Lupus is so hard to deal with, my friend has it and struggles each day.",
            title="Thanks for sharing.",
            conditions_id=Lupus.id,
        )
        comment2.save()

        comment3 = CommentModel(
            content="I appreciate your advice so much!",
            title="MS is hard!",
            conditions_id=MultipleSclerosis.id,
        )
        comment3.save()

        print("Database seeded!")
    except Exception as e:
        print(e)
