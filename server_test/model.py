from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Record(db.Model):
    __tablename__ = "collection"
    index = db.Column(db.Integer, primary_key=True)
    Artist = db.Column(db.Text)
    Title = db.Column(db.Text)
    Label = db.Column(db.Text)
    Released = db.Column(db.Text)
