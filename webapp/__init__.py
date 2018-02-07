from flask import Flask
from sqlalchemy.orm import sessionmaker
app = Flask(__name__)

from webapp.hello_module.controller import module

app.register_blueprint(module)