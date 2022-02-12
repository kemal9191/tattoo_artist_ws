from unicodedata import name
from app import db

class Tattoo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(), nullable=False)
    url = db.Column(db.String(), nullable=False)

    def __repr__(self):
        return f"Tattoo {self.name} has been uploaded"
