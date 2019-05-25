from app import ma, db
from .person import Person


class Sona(db.Model):
    idx = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(125), unique=True)
    specie = db.Column(db.String(125))
    owner_idx = db.Column(db.Integer, db.ForeignKey('person.idx'))
    owner = db.relationship('Person', backref='Sonas')

    def __init__(self, idx, name, specie):
        self.idx = idx
        self.name = name
        self.specie = specie