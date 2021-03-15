import os
from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__name__))
load_dotenv = (os.path.join(basedir, '.env'))

# Windows = Documents\codingtemple-may2020\week5\in-class\
# Mac & Linux = Documents/codingtemple-may2020/week5/in-class/

class Config():
    SECRET_KEY = os.getenv('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = os.getenv('SQLALCHEMY_DATABASE_URI')
    SQLALCHEMY_TRACK_MODIFICATIONS = os.getenv('SQLALCHEMY_TRACK_MODIFICATIONS')
    FLASK_ENV=development = os.getenv('FLASK_ENV')
