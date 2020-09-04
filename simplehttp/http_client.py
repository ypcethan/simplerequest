import sys
import json
import logging
from simplehttp.utils import process_url
from simplehttp.error import HttpError

try:
    # Python 3
    import http.client
    from urllib.parse import urlencode
except ImportError:
    # Python 2
    import urllib2


def make_get_request(url, params):
    url_parts = process_url(url, params)

    try:
        conn = http.client.HTTPSConnection(url_parts['host'])
        conn.request('GET', url_parts['path'])
        try:
            response = conn.getresponse()
        except Exception as e:
            logging.error(e)
            raise
        status = str(response.status)
        if status.startswith('4') or status.startswith('5'):
            raise HttpError(status)

    except NameError:
        extended_url = url_parts['protocal'] + \
            "://" + url_parts['host'] + url_parts['path']
        req = urllib2.Request(extended_url)

        try:
            response = urllib2.urlopen(req)
        except urllib2.HTTPError as e:
            raise HttpError(e.getcode())

    body = response.read()
    print(body)

    json_data = json.loads(body)
    return json.loads(body)


def make_post_request(url, params, data):
    url_parts = process_url(url, params)
    headers = {'Content-Type': "application/json"}
    data_str = json.dumps(data)

    try:
        conn = http.client.HTTPSConnection(url_parts['host'])
        conn.request('POST', url_parts['path'],
                     body=data_str, headers=headers)
        try:
            response = conn.getresponse()
        except Exception as e:
            logging.error(e)
            raise
        status = str(response.status)
        if status.startswith('4') or status.startswith('5'):
            raise HttpError(status)

    except NameError:
        extended_url = url_parts['protocal'] + \
            "://" + url_parts['host'] + url_parts['path']

        req = urllib2.Request(extended_url, data_str, headers)
        try:
            response = urllib2.urlopen(req)
        except urllib2.HTTPError as e:
            raise HttpError(e.getcode())

    body = response.read()

    json_data = json.loads(body)
    return json.loads(body)


def make_request(method, url, params=None, data=None):
    """[summary]

    Args:
        method (string): either GET or POST 
        url (string): 
        params (dict, optional):  Addtional parameters wish to add to the query string. Defaults to {}.
        data (dict, optional): Request body for POST request. Defaults to {}.

    Raises:
        HttpError: Client or server error, indicated by
            status code starts with either 4 or 5. 

    Returns:
        [dict]: Reponse body in JSON (Python dictionary) format 
    """

    params = params or {}
    data = data or {}
    # try:
    if method == 'GET':
        return make_get_request(url, params)
    elif method == 'POST':
        return make_post_request(url, params, data)
    else:
        return {}


def get_json(url, params={}):
    """API for sending GET reuqest

    Args:
        url (string): 
        params (dict, optional): Addtional parameters wish to add to the query string. Defaults to {}.

    Returns:
        [dict]: Reponse body in JSON (Python dictionary) format
    """
    try:
        response = make_request('GET', url, params)

    except Exception as e:
        sys.last_value = e
        # re-raise the exception (allow the caller to handle)
        raise
    return response


def post_json(url, params={}, data={}):
    """API for sending POST reuqest

    Args:
        url (string): 
        params (dict, optional): Addtional parameters wish to add to the query string. Defaults to {}.
        data (dict, optional): Request body.

    Returns:
        [dict]: Reponse body in JSON (Python dictionary) format
    """
    try:
        response = make_request('POST', url, params, data)
    except Exception as e:
        sys.last_value = e
        raise
    return response

# def post_json(url, params={}, data={}):
#     url_parts = process_url(url, params)
#     conn = http.client.HTTPSConnection(url_parts['host'])
#     headers = {'Content-Type': "application/json"}
#     conn.request('POST', url_parts['path'],
#                  body=json.dumps(data), headers=headers)
#     response = conn.getresponse()
#     status = str(response.status)
#     if not status.startswith('2'):
#         raise simplehttp.HttpError(f"HTTP Status Code: {status}", status)
#     body = response.read()
#     return json.loads(body)
