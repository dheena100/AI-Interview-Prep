from flask import Flask, render_template, request, redirect, session
from flask_mysqldb import MySQL
from werkzeug.security import generate_password_hash, check_password_hash
from werkzeug.utils import secure_filename

import os

from utils.resume_parser import extract_resume_text
from utils.skill_extractor import extract_skills
from utils.answer_checker import evaluate_answer
from utils.question_generator import generate_questions

# -----------------------------------

# Flask App Configuration

# -----------------------------------

app = Flask(__name__)

app.config.from_pyfile('config.py')

app.secret_key = 'your_secret_key'

# -----------------------------------

# Upload Folder Configuration

# -----------------------------------

UPLOAD_FOLDER = 'static/uploads'

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# -----------------------------------

# MySQL Connection

# -----------------------------------

mysql = MySQL(app)

# -----------------------------------

# Home Page

# -----------------------------------

@app.route('/')
def home():
    return render_template('index.html')


# -----------------------------------

# Register Page

# -----------------------------------

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = generate_password_hash(
            request.form['password']
        )

        cursor = mysql.connection.cursor()
        cursor.execute(
            """
            INSERT INTO users(username, email, password)
            VALUES(%s,%s,%s)
            """,
            (username, email, password)
        )

        mysql.connection.commit()
        cursor.close()

        return redirect('/login')

    return render_template('register.html')


# -----------------------------------

# Login Page

# -----------------------------------

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        cursor = mysql.connection.cursor()
        cursor.execute(
            "SELECT * FROM users WHERE email=%s",
            (email,)
        )

        user = cursor.fetchone()
        cursor.close()

        if user and check_password_hash(user[3], password):
            session['user_id'] = user[0]
            session['username'] = user[1]
            return redirect('/dashboard')

    return render_template('login.html')


# -----------------------------------

# Dashboard

# -----------------------------------

@app.route('/dashboard')
def dashboard():
    if 'user_id' not in session:
        return redirect('/login')

    return render_template(
        'dashboard.html',
        username=session.get('username')
    )


# -----------------------------------

# Upload Resume

# -----------------------------------

@app.route('/upload-resume', methods=['GET', 'POST'])
def upload_resume():
    if 'user_id' not in session:
        return redirect('/login')

    if request.method == 'POST':
        # Get uploaded file
        file = request.files['resume']

        # Secure filename
        filename = secure_filename(file.filename)

        # File path
        filepath = os.path.join(
            app.config['UPLOAD_FOLDER'],
            filename
        )

        # Save file
        file.save(filepath)

        # -----------------------------------
        # Extract Resume Text
        # -----------------------------------
        resume_text = extract_resume_text(filepath)

        # -----------------------------------
        # Extract Skills
        # -----------------------------------
        skills = extract_skills(resume_text)

        # -----------------------------------
        # Generate Score
        # -----------------------------------
        score = len(skills) * 10
        if score > 100:
            score = 100

        # -----------------------------------
        # Render Result Page
        # -----------------------------------
        return render_template(
            'result.html',
            skills=skills,
            score=score,
            resume_text=resume_text[:1500]
        )

    return render_template('upload_resume.html')


# -----------------------------------

# Interview Page

# -----------------------------------

@app.route('/interview')
def interview():

    if 'user_id' not in session:
        return redirect('/login')

    skills = session.get('skills', [])

    questions = generate_questions(skills)

    return render_template(
        'interview.html',
        questions=questions
    )


# -----------------------------------

# Logout

# -----------------------------------

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')


# -----------------------------------

# Run Flask App

# -----------------------------------

@app.route('/submit-answer', methods=['POST'])
def submit_answer():

    answers = []

    for key in request.form:

        answers.append(request.form[key])

    total_score = 0

    feedback_list = []

    for answer in answers:

        result = evaluate_answer(answer)

        total_score += result['score']

        feedback_list.extend(result['feedback'])

    average_score = total_score // len(answers)

    return render_template(
        'final_result.html',
        score=average_score,
        feedback=feedback_list
    )



if __name__ == '__main__':
    app.run(debug=True)

