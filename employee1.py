from flask import Flask
from flask import request, make_response

import sqlalchemy as db
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker
engine = db.create_engine("sqlite:///employees.sqlite")
conn = engine.connect()

app = Flask(__name__)

    
metadata = db.MetaData()
employee = db.Table('Employee', metadata,

db.Column('id', db.Integer(), primary_key=True),
db.Column('name', db.String(255), nullable=False),
db.Column('address', db.String(1024), default="Nammane"),
db.Column('pic_id', db.String(1024), default="default")
)

metadata.create_all(engine)

Base = declarative_base()
session = sessionmaker(bind=engine)()

class Employee:
    __tablename__ = "employee"
    name = Column(String)
    id = Column(Integer, primary_key=True)
    address = Column(String)
    pic_id = Column(String)

    def __init__(self, name, id, address):
        self.name = name
        self.id = id
        self.address = address
    def __str__(self):
        return str({
            "id": self.id,
            "name": self.name,
            "address": self.address
        })
emp = Employee("Ram", 12, "Bangalore")
emp.save()
employees = {
    1: Employee("Prashanth", 1, "Bengaluru"),
    2: Employee("Shiva", 2, "Bengaluru"),
    3: Employee("Phaneendra", 3, "Mysore"),
    4: Employee("Pranav", 4, "Mysore"),
}

count = 4

@app.route("/api/employee/", methods=["POST"])
def create_employee():
    global count
    employee = request.json
    count += 1
    employee['id'] = count
    employees[count] = Employee(employee['name'], count, employee['address'])

    return employee

@app.route("/api/employee/<int:employee_id>", methods=["PUT"])
def alter_employee_data(employee_id):
    employee = request.json
    employees[employee_id].name = employee.get('name', employees[employee_id].name)
    employees[employee_id].address = employee.get('address',employees[employee_id].address)
    return str(employees[employee_id])

@app.route("/api/employee/<int:employee_id>", methods=["GET"])
def get_employee_information(employee_id):
    return str(employees[employee_id])

@app.route("/api/employee/<int:employee_id>", methods=["DELETE"])
def remove_employee_data(employee_id):
    del employees[employee_id]
    return make_response(""), 200