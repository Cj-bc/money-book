from flask import Flask, current_app
from .routes import api
from .models import db
#from .swagger import swag

API_VERSION = 0.1

app = Flask(__name__)
app.register_blueprint(api.bp, url_prefix=f'/api/{API_VERSION}')
#swag.init_app(app)


def init_db(app):
    db.init_app(app)
