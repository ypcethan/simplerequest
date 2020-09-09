import sys
import json
import logging
from simplehttp.utils import process_url
from simplehttp.error import HttpError

try:
    # Python 3
    # import http.client
    from simplehttp.request3 import http_get
except ImportError:
    # Python 2
    # import urllib2
    from simplehttp.request2 import http_get

#
# def http_get(url_parts):
#     conn = http.client.HTTPSConnection(url_parts['host'])
#     conn.request('GET', url_parts['path'])
#     response = conn.getresponse()
#
#     return response.status, response.read()
#
#
# def http_get_py2(url_parts):
#     extended_url = url_parts['protocal'] + \
#         '://' + url_parts['host'] + url_parts['path']
#     req = urllib2.Request(extended_url)
#     try:
#         response = urllib2.urlopen(req)
#         status_code = response.getcode()
#     except urllib2.HTTPError as error:
#         response = ""
#         status_code = error.getcode()
#         # raise HttpError(error.getcode())
#     return status_code, response
#


def make_get_request(url, params):
    """
    Making http GET request for both Python2 and Python3

    Args:
        url (string): URL path
        params (dict, optional):Addtional parameters
            to  be added to the query string.

    Raises:
        HttpError: Client or server error, indicated by
            status code starts with either 4 or 5.

    Returns:
        [dict]: Reponse body in JSON (Python dictionary) format
    """
    url_parts = process_url(url, params)

    try:
        status, body = http_get(url_parts)
    except Exception as err:
        logging.error(err)
        raise UnexpectedHttpError(err)

    if status.startswith('4') or status.startswith('5'):
        raise HttpError(status)

    return body


def make_post_request(url, params, data):
    pass
# def make_post_request(url, params, data):
#     """
#     Making http POST request for both Python2 and Python3
#
#     Args:
#         url (string): URL path
#         params (dict, optional): Addtional parameters
#             to  be added to the query string.
#
#     Raises:
#         HttpError: Client or server error, indicated by
#             status code starts with either 4 or 5.
#
#     Returns:
#         [dict]: Reponse body in JSON (Python dictionary) format
#     """
#     url_parts = process_url(url, params)
#     headers = {'Content-Type': 'application/json'}
#     data_str = json.dumps(data)
#
#     try:
#         conn = http.client.HTTPSConnection(url_parts['host'])
#         conn.request('POST', url_parts['path'],
#                      body=data_str, headers=headers)
#         try:
#             response = conn.getresponse()
#         except Exception as error:
#             logging.error(error)
#             raise
#         status = str(response.status)
#         if status.startswith('4') or status.startswith('5'):
#             raise HttpError(status)
#
#     except NameError:
#         extended_url = url_parts['protocal'] + \
#             "://" + url_parts['host'] + url_parts['path']
#
#         req = urllib2.Request(extended_url, data_str, headers)
#         try:
#             response = urllib2.urlopen(req)
#         except urllib2.HTTPError as error:
#             raise HttpError(error.getcode())
#
#     body = response.read()
#
#     return json.loads(body)


def make_request(method, url, params=None, data=None):
    """[summary]

    Args:
        method (string): Either GET or POST
        url (string): URL path
        params (dict, optional): Addtional parameters
            to  be added to the query string.
        data (dict, optional): Request body for POST request. Defaults to {}.

    Raises:
        HttpError: Client or server error, indicated by
            status code starts with either 4 or 5.

    Returns:
        [dict]: Reponse body in JSON (Python dictionary) format
    """

    params = params or {}
    data = data or {}

    if method == 'GET':
        return make_get_request(url, params)
    if method == 'POST':
        return make_post_request(url, params, data)
    return {}


def get_json(url, params=None):
    """API for sending GET reuqest

    Args:
        url (string): URL path
        params (dict, optional):Addtional parameters
            to  be added to the query string.

    Returns:
        [dict]: Reponse body in JSON (Python dictionary) format
    """
    params = params or {}
    try:
        response = make_request('GET', url, params)

    except Exception as error:
        sys.last_value = error
        # re-raise the exception (allow the caller to handle)
        raise
    return response


def post_json(url, params=None, data=None):
    """API for sending POST reuqest

    Args:
        url (string): URL path
        params (dict, optional): Addtional parameters
            to  be added to the query string.
        data (dict, optional): Request body.

    Returns:
        [dict]: Reponse body in JSON (Python dictionary) format
    """

    params = params or {}
    data = data or {}
    try:
        response = make_request('POST', url, params, data)
    except Exception as error:
        sys.last_value = error
        raise
    return response
