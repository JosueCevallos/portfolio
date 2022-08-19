from flask import Flask
import os


def create_app():
    app = Flask(__name__)

    app.config.from_mapping(
        SENDGRIG_KEY =os.environ.get("SENDGRID_KEY")
    )

    from app import portfolio
    
    app.register_blueprint(portfolio.bp)

    return app