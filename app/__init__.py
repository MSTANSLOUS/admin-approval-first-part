from flask import Flask
from .model.user import database
from config import Config

def create_app():
    app = Flask(__name__)

    #configign the app
    app.config.from_object(Config)

    database.init_app(app)

    with app.app_context():
        database.create_all()

    #register a blueprint
    from .route.user import user_bp
    app.register_blueprint(user_bp)

    from .route.admin import admin_bp
    app.register_blueprint(admin_bp)

    return app