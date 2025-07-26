# 🎓 Student Management System

<p align="center">
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white" alt="Flask">
  <img src="https://img.shields.io/badge/SQLite-003B57?style=for-the-badge&logo=sqlite&logoColor=white" alt="SQLite">
  <img src="https://img.shields.io/badge/SQLAlchemy-CCA776?style=for-the-badge&logo=sqlalchemy&logoColor=white" alt="SQLAlchemy">
</p>

<p align="center">
  <b>A simple, user-friendly web application for managing student records.</b><br>
  <i>Built with Flask, SQLAlchemy, and SQLite for easy CRUD operations and RESTful API access.</i>
</p>

---

## 📚 Project Overview

This repository contains a Flask-based web application that allows users to manage student information efficiently. The system provides a complete CRUD (Create, Read, Update, Delete) interface for student records, both via a web UI and RESTful API endpoints. Ideal for learning web development, REST APIs, and database integration with Python.

---

## 🗂️ Folder Structure

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

---

## 🚀 Getting Started

### 1. Prerequisites

- Python 3.8 or higher
- `pip` package manager

### 2. Installation

1. **Clone the repository:**
    ```sh
    git clone https://github.com/bchaitanya92/Student_Mgmt_app.git
    cd Student_Mgmt_app
    ```

2. **Create and activate a virtual environment:**
    ```sh
    # For Windows
    python -m venv venv
    venv\Scripts\activate

    # For macOS/Linux
    python3 -m venv venv
    source venv/bin/activate
    ```

3. **Install dependencies:**
    ```sh
    pip install -r requirements.txt
    ```

4. **Run the application:**
    ```sh
    python app.py
    ```

5. **Open your browser and navigate to:**
    ```
    http://localhost:5000
    ```

---

## ✨ Features

- Add new students with name, age, and course information
- View a list of all students
- Edit existing student information
- Delete student records
- User-friendly web interface
- RESTful API endpoints for integration

---

## 🔗 API Endpoints

| Method | Endpoint                   | Description                |
|--------|---------------------------|----------------------------|
| POST   | `/student/add`            | Add a new student          |
| GET    | `/student/lists`          | Get all students           |
| GET    | `/student/get/<id>`       | Get student by ID          |
| PATCH  | `/student/update/<id>`    | Update student details     |
| DELETE | `/student/delete/<id>`    | Delete student             |

---

## 🛠️ Technologies Used

- Python
- Flask
- SQLAlchemy
- SQLite
- HTML/CSS
- JavaScript

---

## 👨‍💻 Author & Credits

Developed by:  
**B. Chaitanya**  

- GitHub: [bchaitanya92](https://github.com/bchaitanya92)
- LinkedIn: [BOURISETTI CHAITANYA](https://www.linkedin.com/in/bourisetti-chaitanya/)

Feel free to explore, modify, and use this project for your learning or as a starter for your own applications.  
Contributions and feedback are always welcome. Happy Coding! 🎉

---

## 📄 License

This project is open source.  
