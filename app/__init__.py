from flask import Flask
from flask_babel import Babel
from flask_cors import CORS
from flask_menu import Menu
from flask_sqlalchemy import SQLAlchemy
import logging
import logging.config

app = Flask(__name__)
app.config.from_object('config.Dev')

# Initialize Babel.
babel = Babel(app)

# Initialize CORS.
CORS(app)

# Initialize Menu.
Menu(app)

# Initialize SQLAlchemy.
db = SQLAlchemy(app)

# Logging config.
logging.config.fileConfig('log.ini')
logger = logging.getLogger('waitress')

# Register blueprints.
from app.modules.index.blueprint import mod_index
from app.modules.roles.blueprint import mod_roles

app.register_blueprint(mod_index)
app.register_blueprint(mod_roles)

# Create all tables.
db.create_all()
