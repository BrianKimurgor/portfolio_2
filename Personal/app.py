from flask import Flask, render_template, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    # Add your data here
    about_data = {
        'about_text': (
            "I'm a passionate software engineer and developer dedicated to leveraging technology "
            "to create innovative solutions and drive digital transformation. With a strong foundation "
            "in Python and its frameworks, along with expertise in frontend technologies such as HTML, "
            "CSS, and JavaScript, I specialize in designing and developing scalable, user-centric applications "
            "tailored to meet unique business needs."
        ),
        'personal_info': {
            'birthday': '28 Jan 2000',
            'website': 'www.example.com',
            'phone': '+254 748 983 103',
            'city': 'Nairobi, Kenya',
            'age': 24,
            'degree': 'Computer Science',
            # Add more personal info here
        },
        'additional_info': (
            "Committed to continuous learning and professional "
            "growth, I thrive in collaborative environments where I can contribute my technical skills, "
            "problem-solving abilities, and creative insights to deliver impactful results. Outside of "
            "coding, I enjoy exploring emerging technologies, participating in hackathons, and mentoring "
            "aspiring developers to inspire the next generation of innovators."
        ),
        # Add more data as needed
    }

    return render_template('about.html', data=about_data)



if __name__ == '__main__':
    app.run(debug=True)
