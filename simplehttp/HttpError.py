import sys


class HttpError(Exception):
    def __init__(self, message, status_code):
        self.message = message
        self.status_code = status_code
        # sys.last_value = {}
        # sys.last_value.status_code = status_code
