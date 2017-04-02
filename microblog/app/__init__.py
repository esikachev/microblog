import os
from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.login import LoginManager
from flask.ext.openid import OpenID
from microblog.config import basedir


app = Flask(__name__)
app.config.from_object('microblog.config')

db_object = SQLAlchemy(app)

lm = LoginManager()
lm.init_app(app)
lm.login_view = 'login'

oid = OpenID(app, '/tmp/microblog')

from microblog.app import views
from microblog.app.db import models
