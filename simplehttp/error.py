import sys


class HttpError(Exception):
    def __init__(self,  status_code):
        message = 'HTTP Status Code: %s' % str(status_code)
        super(HttpError, self).__init__(message)
        self.message = message
        self.status_code = int(status_code)
