from utils.db import db

class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    course = db.Column(db.String(100), nullable=False)

    def __init__(self, name, age, course):
        self.name = name
        self.age = age
        self.course = course

    def __repr__(self):
        return f'<Student {self.name}>'


        
