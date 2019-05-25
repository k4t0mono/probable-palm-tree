from app import ma, db


class Person(db.Model):
    idx = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(125), unique=True)

    def __init__(self, name):
        self.name = name