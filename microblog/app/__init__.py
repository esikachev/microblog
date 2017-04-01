from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config.from_object('microblog.config')
db_object = SQLAlchemy(app)

from microblog.app import views
from microblog.app.db import models
