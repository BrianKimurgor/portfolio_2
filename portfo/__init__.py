from flask import Flask
from flask_sqlalchemy import SQLAlchemy
#from forms import RegistrationForm


app = Flask(__name__)
app.config['SEKRET_KEY'] = 'sectret'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)

from portfo import routes
