from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Contact(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    email = db.Column(db.String(120), nullable=False)
    subject = db.Column(db.String(200), nullable=False)
    message = db.Column(db.Text, nullable=False)

class Project(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    technologies_used = db.Column(db.String(200), nullable=False)
    image_urls = db.Column(db.String(500), nullable=False)
    github_url = db.Column(db.String(200), nullable=True)
    live_url = db.Column(db.String(200), nullable=True)

class Testimonial(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    testimonial_text = db.Column(db.Text, nullable=False)
    photo_url = db.Column(db.String(300))
    company = db.Column(db.String(200))
