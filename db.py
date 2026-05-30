from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from config.settings import Config
mysql_db = SQLAlchemy()

db_string = f"mysql://{Config.DB_USER}:{Config.DB_PASSWORD}@{Config.DB_HOST}/{Config.DB_NAME}"

def initialized_db(app):
    """Use this function for initializing db."""

    app.config['SQLALCHEMY_DATABASE_URI'] = db_string
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # Avoids a warning
    mysql_db.init_app(app)

    Migrate(app, mysql_db)

    @app.before_request
    def create_tables():
        app.before_request_funcs[None].remove(create_tables)
        mysql_db.create_all()