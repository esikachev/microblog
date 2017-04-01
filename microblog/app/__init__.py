from flask import Flask

app = Flask(__name__)
app.config.from_object('microblog.config')

from microblog.app import views
