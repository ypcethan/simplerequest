import sys


class HttpError(Exception):
    def __init__(self,  status_code):
        self.message = 'HTTP Status Code: %s' % str(status_code)
        self.status_code = int(status_code)
