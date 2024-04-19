# This is the URI we use to talk to the database.
# # ! Note: sqlalchemy does not make conditions_db for us,
# ? we need to run the command `createdb conditions_db`

# db_URI = "psotgresql://localhost:5432/conditions_db"

# secret = "Randomcheesecamelgreen"

import os

db_URI = os.getenv("DATABASE_URL", "postgresql://localhost:5432/<conditions_db>")
secret = os.getenv("secret", "correcthorsebatterystaple")

if db_URI.startswith("postgres://"):
    db_URI = db_URI.replace("postgres://", "postgresql://", 1)
