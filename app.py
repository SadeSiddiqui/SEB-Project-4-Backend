from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_bcrypt import Bcrypt

from config.environment import db_URI

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = db_URI
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)

marsh = Marshmallow(app)

# ! Instantiate bcrypt
bcrypt = Bcrypt(app)

# ! Import users AND conditions
from controllers import conditions, users

app.register_blueprint(conditions.router, url_prefix="/api")
# ! Register the users
app.register_blueprint(users.router, url_prefix="/api")
