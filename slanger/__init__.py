from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
import sys, os

load_dotenv()

app = Flask(__name__)
api = Api( app )
#app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('SQLALCHEMY_DATABASE_URI')
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('JAWSDB_URL')
# print( os.getenv('SQLALCHEMY_DATABASE_URI') )

db = SQLAlchemy( app )

from .models.models import *
from .views.views import *

import slanger.resources

api.init_app( app )

#if ( 'database.db' not in os.listdir() ):
#    db.create_all()

# db.create_all()
