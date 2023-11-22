import time
from flask import Flask
from flask import request, make_response
 
app = Flask(__name__)


class Student:
    name = ''
    usn = ''
    age = ''
 
    def __init__(self, name, usn,age):
        self.name = name
        self.usn = usn
        self.age = age
 
    def __str__(self):
        return str({
            "usn": self.usn,
            "name": self.name,
            "age": self.age
        })
    def validate(self):
        val_name = len(self.name) > 0 and len(self.name) < 20
        val_age = len(self.age) > 0 and len(self.age) < 2
        return val_name and val_age
   
students= {
1: Student("Ram", 1, 22),
2: Student("Sham", 2,21 ),
}

count=2

class BaseException(Exception):
    status = 400
    message = ""
    def __init__(self, status, message) -> None:
        super().__init__()
        self.status = status
        self.message = message
    def __str__(self):
        return str({'status': self.status, 'message': self.message})
    
class ValidationError(BaseException):
    def __init__(self) -> None:
        super().__init__(400, "Invalid Input Parameter")


class StudentNotFoundError(BaseException):
    def __init__(self) -> None:
        super().__init__(404, "Student not Present")

def setup_logger(called):
    def f(*args, **kwargs):
        request.logger = app.logger
        return called(*args, **kwargs)
    f.__name__ = called.__name__
    return f

def time_request(called):
    def f(*args, **kwargs):
        request.start_time = time.time() * 1000
        res = called(*args, **kwargs)
        request.end_time = time.time() * 1000
        request.time = request.end_time - request.start_time
        app.logger.info('request time: {}'.format(request.time))
        return res
    f.__name__ = called.__name__
    return f

def setup_tracing(called):
    def f(*args, **kwargs):
        request.req_usn = 'req_{}'.format(time.time() * 1000)
        res, status = called(*args, **kwargs)
        res_send = make_response(res)
        res_send.headers['X-Request-Usn'] = request.req_usn
        return res_send, status
    f.__name__ = called.__name__
    return f

@app.route("/api/student/", methods=["POST"])
@setup_logger
@time_request
@setup_tracing
def create_student():
    global count
    student = request.json
    count += 1
    student['usn'] = count
    std = Student(student['name'], count, student['age'])
 
    log_message = {'tracking_id': request.req_usn,
                    'operation': 'create student',
                    'status': 'processing'}
    
    request.logger.info(str(log_message))
    # Validation error
    if not std.validate():
        log_message['status'] = 'unsuccessful'
        request.logger.error(str(log_message))
        err = ValidationError()
        return str(err), err.status
    
    students[count] = std
    log_message['status'] = 'successful'
    request.logger.info(str(log_message))
    return students, 201
 


@app.route("/api/student/<int:student_usn>", methods=["GET"])
@setup_logger
@setup_tracing
@time_request
def get_student_information(student_usn):

    log_message = {
        'tracking_usn': request.req_usn,
        'operation': 'get student',
        'status': 'processing'
        }
    
    request.logger.info(str(log_message))

    try:
        std = students[student_usn]
    except KeyError as e:
        err = StudentNotFoundError()
        return str(err), err.status
 

    log_message['status'] = 'unsuccesful'
    request.logger.info(str(log_message))
    return str(std), 200
 

@app.route("/api/student/<int:student_usn>", methods=["DELETE"])
def remove_student_data(student_usn):
    try:
        std = students[student_usn]
    except KeyError as e:
        err = StudentNotFoundError()
        return str(err), err.status

    del students[student_usn]
    return make_response(""), 200