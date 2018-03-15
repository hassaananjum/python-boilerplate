from flask import Flask
from sqlalchemy.orm import sessionmaker
app = Flask(__name__)

from .controllers.hello_controller import module

app.register_blueprint(module)