from flask_sqlalchemy import SQLAlchemy

database = SQLAlchemy()

class User(database.Model):
    user_id = database.Column(
        database.Integer,
        primary_key = True,
        autoincrement = True,
        unique = True,
        nullable = False
    )
    user_name = database.Column(
        database.String(50),
        nullable = False
    )
    user_email = database.Column(
        database.String(50),
        nullable = False
    )

    is_active = database.Column(
        database.Boolean,
        nullable = False,
    )