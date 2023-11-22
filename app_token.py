from flask import Flask

from flask import request, make_response

import jwt

class BaseException(Exception):
    status = 400
    message = ""
    def __init__(self, status, message) -> None:
        super().__init__()
        self.status = status
        self.message = message
    def __str__(self):
        return str({'status': self.status, 'message': self.message})
    
class TokenGenerationError(BaseException):
    def __init__(self) -> None:
        super().__init__(500, "Unable to generate the token")

class TokenCheckingError(BaseException):
    def __init__(self) -> None:
        super().__init__(402, "Invalid id")

app = Flask(__name__)

@app.route('/api/token/<int:employee_id>', methods=['POST'])
def fetch_token(employee_id):
    log_message = {
        'operation': 'fetch token',
        'status': 'processing'
        }
    
    app.logger.info(str(log_message))

    payload = {
        'id': employee_id,
        'iss': 'DSCE',
        'sub': 'Employee Microservice Token'
        }

    try:
        token = jwt.encode(payload,
            key="mysecretkey")

    except:
        log_message['status'] = 'unsuccessful'
        log_message['reason'] = 'Token generation error'
        app.logger.error(str(log_message))
        err = exceptions.TokenGenerationError()
        return str(err), err.status

    app.logger.info(str(log_message))
    return {'token': token}, 200

@app.route("/api/token/verify/<int:employee_id>", methods=["GET"])
def fetch_token_verify(employee_id):

    log_message = {
       
        'operation': 'fetch token',
        'status': 'processing'
        }
    
    app.logger.info(str(log_message))
    
    try:
        token_string=request.json
        token_payload = jwt.decode(token_string['token'], 'mysecretkey', algorithms = ['HS256'])
       
    except KeyError as e:
        log_message['status'] = 'unsuccessful'
        log_message['status'] = 'Token Fetching error'
        request.logger.error(str(log_message))
        
        err = EmployeeNotPresentError()
        return str(err), err.status
    
    if token_payload['id']==employee_id:
        return {"payload":token_payload},200
    else:
        err=TokenCheckingError()
        return str(err), err.status
