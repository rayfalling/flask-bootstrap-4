from .Application import app, db
from .Model import Template
from .Router import *

db.create_all()

# TODO add your database init code

print("Database initialized.")

__all__ = ["app", "db"]
