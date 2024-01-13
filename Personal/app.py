from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'  # SQLite database
app.config['SECRET_KEY'] = 'your_secret_key_here'  # For session and flash messages
db = SQLAlchemy(app)

# Define models for Contact, Project, and Testimonial
# For brevity, I'll provide a basic structure. You can expand upon these.
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
    technologies_used = db.Column(db.String(300), nullable=False)
    image_urls = db.Column(db.Text, nullable=False)
    github_url = db.Column(db.String(500), nullable=True)
    live_url = db.Column(db.String(500), nullable=True)

class Testimonial(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    testimonial_text = db.Column(db.Text, nullable=False)
    photo_url = db.Column(db.String(500), nullable=True)
    company = db.Column(db.String(200), nullable=True)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/portfolio-details')
def portfolio_details():
    return render_template('portfolio-details.html')

# Route for contact form submission
@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        subject = request.form['subject']
        message = request.form['message']

        # Save this data to the database
        new_contact = Contact(name=name, email=email, subject=subject, message=message)
        db.session.add(new_contact)
        db.session.commit()

        flash('Your message has been sent!', 'success')
        return redirect(url_for('index'))

    return render_template('contact.html')  # Create a contact.html template

# You can similarly add routes and functions to manage projects and testimonials.
# ... [previous imports and configurations remain unchanged] ...

@app.route('/projects', methods=['GET', 'POST'])
def projects():
    # Fetch all projects from the database
    all_projects = Project.query.all()  # This assumes you have a Project model and it has a query.all() method

    # Pass the projects list to the 'projects.html' template
    return render_template('projects.html', projects=all_projects)
# def projects():
#     if request.method == 'POST':
#         name = request.form['name']
#         description = request.form['description']
#         technologies_used = request.form['technologies_used']
#         image_urls = request.form['image_urls']
#         github_url = request.form['github_url']
#         live_url = request.form['live_url']

#         new_project = Project(name=name, description=description, technologies_used=technologies_used,
#                               image_urls=image_urls, github_url=github_url, live_url=live_url)
#         db.session.add(new_project)
#         db.session.commit()
#         flash('New project added successfully!', 'success')
#         return redirect(url_for('projects'))

#     # Fetch all projects from the database to display
#     all_projects = Project.query.all()
#     return render_template('projects.html', projects=all_projects)

# from flask import render_template


@app.route('/project/<int:project_id>')
def project_details(project_id):
    # Fetch the project from the database based on the project_id
    project = Project.query.get_or_404(project_id)

    # Split the image URLs into a list to use in the template
    image_urls = project.image_urls.split('assets/img/portfolio/portfolio-1.jpg", "assets/img/portfolio/portfolio-2.jpg", "assets/img/portfolio/portfolio-3.jpg')

    return render_template('portfolio-details.html', project=project, image_urls=image_urls)


@app.route('/testimonials', methods=['GET', 'POST'])
def testimonials():
    if request.method == 'POST':
        name = request.form['name']
        testimonial_text = request.form['testimonial_text']
        photo_url = request.form['photo_url']
        company = request.form['company']

        new_testimonial = Testimonial(name=name, testimonial_text=testimonial_text,
                                      photo_url=photo_url, company=company)
        db.session.add(new_testimonial)
        db.session.commit()
        flash('New testimonial added successfully!', 'success')
        return redirect(url_for('testimonials'))

    # Fetch all testimonials from the database to display
    all_testimonials = Testimonial.query.all()
    return render_template('testimonials.html', testimonials=all_testimonials)
@app.route('/fetch-testimonials', methods=['GET'])
def fetch_testimonials():
    testimonials = Testimonial.query.all()
    testimonial_list = [{
        'name': testimonial.name,
        'testimonial_text': testimonial.testimonial_text,
        'photo_url': testimonial.photo_url,
        'company': testimonial.company
    } for testimonial in testimonials]
    return jsonify(testimonial_list)


# Additional routes can be added for updating and deleting projects and testimonials
# For instance, routes like:
# - /projects/<int:id>/edit
# - /projects/<int:id>/delete
# - /testimonials/<int:id>/edit
# - /testimonials/<int:id>/delete

if __name__ == '__main__':
    with app.app_context():  # This ensures that the following code runs within the app context
        db.create_all()  # Create tables based on models
    app.run(debug=True)
