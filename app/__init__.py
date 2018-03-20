from flask import Flask
from flask_bcrypt import Bcrypt
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

webapp = Flask(__name__)

CORS(webapp)

webapp.config.from_object('config.config')

bcrypt = Bcrypt(webapp)
db = SQLAlchemy(webapp)

import os
basedir = webapp.config.get("BASE_DIR")
sqlite_local_base = webapp.config.get("SQLALCHEMY_DATABASE_URI")
database_name = 'flask_jwt_auth'

from .controllers.index_controller import module
from .controllers.auth_controller import auth_blueprint

webapp.register_blueprint(module)
webapp.register_blueprint(auth_blueprint)


db.create_all()

from .modules.auth_module.models import User

user = User(email='admin', password= 'admin', admin=True)
db.session.add(user)
db.session.commit()