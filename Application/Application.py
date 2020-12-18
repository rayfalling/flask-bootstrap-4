from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_apscheduler import APScheduler
from pymysql import install_as_MySQLdb

from .Config import AppConfig

# install MySQLdb
install_as_MySQLdb()

# creating flask instance
app = Flask(__name__, static_url_path='/static', static_folder='static', template_folder='templates')

# Flask程序配置
app.config.from_object(AppConfig)

scheduler = APScheduler()
scheduler.init_app(app)
scheduler.start()

# handling database
db = SQLAlchemy(app)

__all__ = ["app", "db", "scheduler"]
