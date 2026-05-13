from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy

#Create the app instance
app = Flask(__name__)

# Recognizes our react app as not a malicious third party
CORS(app)


#Setting up a connection to the database
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://andresquesada@localhost:5432/the_maze_db'

#Creating a database
db = SQLAlchemy(app)

from main import routes