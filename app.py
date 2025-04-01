from flask import Flask, request, jsonify, render_template, flash, redirect, url_for
from models.student import Student
from utils.db import db, init_db
import os

print("Starting application...")

app = Flask(__name__)

# Get absolute path for the database
BASE_DIR = os.path.abspath(os.path.dirname(__file__))
DB_PATH = os.path.join(BASE_DIR, 'instance', 'students.db')

# Configure database and app
app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_PATH}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'your-secret-key-here'  # Required for flash messages

print(f"Database path: {DB_PATH}")
print("Initializing database...")
# Initialize database
init_db(app)
print("Database initialized successfully!")

# Page Routes
@app.route('/')
def home():
    return render_template('home.html')

@app.route('/add')
def add_student_page():
    return render_template('add_student.html')

@app.route('/list')
def list_students_page():
    return render_template('list_students.html')

# API Routes
@app.route('/student/add', methods=['POST'])
def add_student():
    try:
        data = request.get_json()
        new_student = Student(
            name=data['name'],
            age=data['age'],
            course=data['course']
        )
        db.session.add(new_student)
        db.session.commit()
        return jsonify({
            'id': new_student.id,
            'name': new_student.name,
            'age': new_student.age,
            'course': new_student.course
        }), 201
    except Exception as e:
        print(f"Error: {str(e)}")
        return jsonify({'error': str(e)}), 400

@app.route('/student/lists', methods=['GET'])
def get_students():
    students = Student.query.all()
    return jsonify([{
        'id': student.id,
        'name': student.name,
        'age': student.age,
        'course': student.course
    } for student in students])

@app.route('/student/get/<int:id>', methods=['GET'])
def get_student(id):
    student = Student.query.get_or_404(id)
    return jsonify({
        'id': student.id,
        'name': student.name,
        'age': student.age,
        'course': student.course
    })

@app.route('/student/delete/<int:id>', methods=['DELETE'])
def delete_student(id):
    student = Student.query.get_or_404(id)
    db.session.delete(student)
    db.session.commit()
    return jsonify({'message': 'Student deleted successfully'})

@app.route('/student/update/<int:id>', methods=['PATCH'])
def update_student(id):
    student = Student.query.get_or_404(id)
    data = request.get_json()
    
    if 'name' in data:
        student.name = data['name']
    if 'age' in data:
        student.age = data['age']
    if 'course' in data:
        student.course = data['course']
    
    db.session.commit()
    return jsonify({
        'id': student.id,
        'name': student.name,
        'age': student.age,
        'course': student.course
    })

if __name__ == '__main__':
    print("Starting Flask server...")
    app.run(debug=True, host='0.0.0.0', port=5000)
