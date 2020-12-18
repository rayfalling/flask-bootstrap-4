from .Application import app, db
from .Model import User, Bookkeeping, Category
from .Router import *

db.create_all()

if len(db.session.query(Category).filter_by(Name="收入").all()) == 0:
    category_in = Category(Name="收入")
    db.session.add(category_in)
    db.session.commit()

print("Database initialized.")

__all__ = ["app", "db"]
