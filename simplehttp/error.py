import sys


class RequestError(Exception):
    pass


class HttpError(RequestError):
    def __init__(self,  status_code):
        message = 'HTTP Status Code: %s' % str(status_code)
        super(HttpError, self).__init__(message)
        self.message = message
        self.status_code = int(status_code)


class UnexpectedHttpError(RequestError):

    def __init__(self, err):
        message = 'Some unexpected errors have occured'
        super(UnexpectedHttpError, self).__init__(message)
        self.message = message
        self.original_error = err
