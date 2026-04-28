from flask import Flask
from flask_sqlalchemy import SQLAlchemy

#Create the app instance
app = Flask(__name__)

#Setting up a connection to the database
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://andresquesada@localhost:5432/the_maze_db'

#Creating a database
db = SQLAlchemy(app)

from main import routes