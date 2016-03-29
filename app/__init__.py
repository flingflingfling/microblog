#coding=utf-8
#!/home/purplemaple/py2/microblog/flaskt/bin/python
import os
from flask import Flask
from flask.ext.login import LoginManager
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.openid import OpenID
from config import basedir

app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)

lm = LoginManager()
lm.init_app(app)
lm.login_view = 'login'
oid = OpenID(app, os.path.join(basedir, 'tmp'))

from app import views, models
track_modifications = app.config.setdefault('SQLALCHEMY_TRACK_MODIFICATIONS', True)
app.config['SQLALCHEMY_TRACK_MODFICATIONS'] = True

