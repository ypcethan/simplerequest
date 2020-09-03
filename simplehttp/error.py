import sys


class NoneJSONReourceError(Exception):
    def __init__(self):
        message = "Requested resource is not valid JSON"
        super().__init__(message)


class HttpError(Exception):
    def __init__(self,  status_code):
        self.message = 'HTTP Status Code: %s' % str(status_code)
        self.status_code = int(status_code)
