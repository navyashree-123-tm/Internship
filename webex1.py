from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Step 2: Create a SQLAlchemy model
Base = declarative_base()

class Employee(Base):
    __tablename__ = 'employees'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    salary = Column(Integer)

# Step 3: Configure SQLite database connection
DATABASE_URL = "sqlite:///./employees.db"
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})

# Create the table in the database
Base.metadata.create_all(bind=engine)

# Step 4: Modify existing code to use SQLite database
class EmployeeService:
    def __init__(self):
        self.Session = sessionmaker(autocommit=False, autoflush=False, bind=engine)

    def add_employee(self, name, salary):
        session = self.Session()
        employee = Employee(name=name, salary=salary)
        session.add(employee)
        session.commit()
        session.close()

    def get_employee(self, employee_id):
        session = self.Session()
        employee = session.query(Employee).filter_by(id=employee_id).first()
        session.close()
        return employee

    def get_all_employees(self):
        session = self.Session()
        employees = session.query(Employee).all()
        session.close()
        return employees

    def update_employee(self, employee_id, new_name, new_salary):
        session = self.Session()
        employee = session.query(Employee).filter_by(id=employee_id).first()
        employee.name = new_name
        employee.salary = new_salary
        session.commit()
        session.close()

    def delete_employee(self, employee_id):
        session = self.Session()
        employee = session.query(Employee).filter_by(id=employee_id).first()
        session.delete(employee)
        session.commit()
        session.close()

# Example usage:
employee_service = EmployeeService()
employee_service.add_employee("John Doe", 50000)
employees = employee_service.get_all_employees()
print("All Employees:", employees)
