from flask import Flask

def create_app():
    app = Flask(__name__)

    #register a blueprint
    from .route.user import user_bp
    app.register_blueprint(user_bp)

    return app