<<<<<<< HEAD
# Student Management System

A Flask-based web application for managing student information. This application provides a complete CRUD (Create, Read, Update, Delete) interface for student records.

## Features

- Add new students with name, age, and course information
- View list of all students
- Edit existing student information
- Delete student records
- User-friendly web interface
- RESTful API endpoints

## Installation

1. Clone the repository:
```bash
git clone https://github.com/bchaitanya92/Student_Mgmt_app.git
cd Student_Mgmt_app
```

2. Create a virtual environment and activate it:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Run the application:
```bash
python app.py
```

5. Open your browser and navigate to:
```
http://localhost:5000
```

## API Endpoints

- `POST /student/add` - Add a new student
- `GET /student/lists` - Get all students
- `GET /student/get/<id>` - Get student by ID
- `DELETE /student/delete/<id>` - Delete student
- `PATCH /student/update/<id>` - Update student details

## Project Structure

```
Student_Mgmt_app/
├── app.py
├── requirements.txt
├── instance/
│   └── students.db
├── models/
│   ├── __init__.py
│   └── student.py
├── utils/
│   ├── __init__.py
│   └── db.py
└── templates/
    ├── base.html
    ├── home.html
    ├── add_student.html
    └── list_students.html
```

## Technologies Used

- Python
- Flask
- SQLAlchemy
- HTML/CSS
- JavaScript
- SQLite

## Contributing

Feel free to fork this repository and submit pull requests to contribute to this project.

## License

This project is licensed under the MIT License. 
=======
# Student_Mgmt_app
>>>>>>> 8778ee55a5bd16e1e8ff804291c8f4d718a3fe3a
