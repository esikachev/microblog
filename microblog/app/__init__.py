from flask import Flask

app = Flask(__name__)
from microblog.app import views
