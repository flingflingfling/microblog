#!/home/purplemaple/py2/microblog/flaskt/bin/python
from app import app
app.run(debug = True)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True



