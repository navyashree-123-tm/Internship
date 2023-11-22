import os

from flask import Flask
from flask import request, send_file

class BaseException(Exception):
    status = 400
    message = ""

    def __init__(self, status, message) -> None:
        super().__init__()
        self.status = status
        self.message = message
    def __str__(self):
        return str({'status': self.status, 'message': self.message})
class CertificateExistsException(BaseException):
    def __init__(self) -> None:
        super().__init__(400, "Certificate with id already exists")
        
class CertificateDoesNotExistsException(BaseException):
    def __init__(self) -> None:
        super().__init__(400, "Certificate with id does not exist")

app = Flask(__name__)

@app.route('/api/certificate/', methods=['POST'])
def create_certificate():
    log_message = {
    'operation': 'create certificate',
    'status': 'processing'
}
    app.logger.info(str(log_message))

    # Access the text part of the mulipart request.
    data = dict(request.form)
    certificate_name = data.get('name')
    certificate_id = data.get('certificate_id')
    certificate_path = os.getcwd() + '\storage\\'
    # Access the file object
    file = request.files['certificate']

    overwrite = data.get('overwrite', False)

    if not overwrite and os.path.isfile(certificate_id):
        log_message['status'] = 'unsuccessful'
        log_message['reason'] = 'Certificate Already exists'
        app.logger.error(str(log_message))
        err = exceptions.CertificateExistsException()
        return str(err), err.status
    else:
        log_message['status'] = 'successful'
        app.logger.info(str(log_message))
        file.save(certificate_path + certificate_id)
        return "", 200
@app.route('/api/certificate/<certificate_id>', methods=['GET'])
def get_file(file_id):
    log_message = {
    'operation': 'get file',
    'status': 'processing'
}
    app.logger.info(str(log_message))

    file_path = os.getcwd() + '\storage\\{}'.format(file_id)
# Check if the file exists.
    if not os.path.isfile(file_path):
        log_message['status'] = 'unsuccessful'
        log_message['reason'] = 'Certificate Does not exist'
        app.logger.error(str(log_message))
        err = exceptions.CertificateDoesNotExistsException()
        return str(err), err.status
    else:
        log_message['status'] = 'successful'
        app.logger.info(log_message)
        return send_file(file_path), 200
@app.route('/api/certificate/<certificate_id>', methods=['DELETE'])
def remove_file(file_id):
    log_message = {
    'operation': 'remove file',
    'status': 'processing'
}
    app.logger.info(str(log_message))
    certificate_path = os.getcwd() + '\storage\\{}'.format(certificate_id)

# Check if the file exists.
    if not os.path.isfile(certificate_path):
        log_message['status'] = 'unsuccessful'
        log_message['reason'] = 'Certificate Does not exist'
        app.logger.error(str(log_message))
        err = exceptions.CertificateDoesNotExistsException()
        return str(err), err.status
    else:
        # Delete the file.
        os.remove(certificate_path)
        log_message['status'] = 'successful'
        app.logger.info(log_message)
        return "", 200