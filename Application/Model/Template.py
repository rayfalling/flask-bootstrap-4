from ..Application import db


# TODO Modify the class
class Template(db.Model):
    __table_name__ = "template"

    Id = db.Column(db.Integer, index=True, primary_key=True, autoincrement=True, nullable=False)
    Username = db.Column(db.VARCHAR(16), nullable=False)
    Password = db.Column(db.VARCHAR(16), nullable=False)
    MonthLimit = db.Column(db.Integer, nullable=False)  # 每月限制

    def __init__(self, username, password, month_limit):
        self.Username = username
        self.Password = password
        self.MonthLimit = month_limit


__all__ = ["User"]
