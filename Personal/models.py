from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)  # You should hash this.

class Contact(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    email = db.Column(db.String(120), nullable=False)
    subject = db.Column(db.String(200), nullable=False)
    message = db.Column(db.Text, nullable=False)

class Project(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False)
    description = db.Column(db.Text, nullable=False)
    technologies = db.Column(db.String(200), nullable=False)  # Store as comma-separated values or another method.
    image_urls = db.Column(db.Text)  # Store as a comma-separated list or another method.
    github_url = db.Column(db.String(300))
    live_url = db.Column(db.String(300))

class Testimonial(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    testimonial_text = db.Column(db.Text, nullable=False)
    photo_url = db.Column(db.String(300))
    company = db.Column(db.String(200))
