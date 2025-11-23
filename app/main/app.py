from flask import Flask
from app.settings.config import Config
from app.extensions.db import db
from app.extensions.cache import cache
from app.extensions.login import login_manager


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    # Initialize extensions
    db.init_app(app)
    cache.init_app(app)
    login_manager.init_app(app)

    # Register blueprints
    from app.blueprints.auth import auth_bp
    from app.blueprints.blog import blog_bp
    from app.blueprints.api import api_bp

    app.register_blueprint(auth_bp, url_prefix='/auth')
    app.register_blueprint(blog_bp, url_prefix='/blog')
    app.register_blueprint(api_bp, url_prefix='/api')

    # Create database tables if they don't exist
    with app.app_context():
        # Import models to ensure they are registered with SQLAlchemy
        from app.models import user, post
        db.create_all()

        # Load initial data from JSON file
        from app.utils.seed import load_seed_data
        load_seed_data()

    return app
