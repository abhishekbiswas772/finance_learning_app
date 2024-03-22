from db import db

class Chapter(db.Model):
    __tablename__ = "chapters"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=False)
    time_to_complete = db.Column(db.String(50), nullable=False)
    subchapters = db.relationship('SubChapter', backref='chapter', lazy=True)

class SubChapter(db.Model):
    __tablename__ = "subchapters"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=False)
    time_to_complete = db.Column(db.String(50), nullable=False)
    chapter_id = db.Column(db.Integer, db.ForeignKey('chapters.id'), nullable=False)
