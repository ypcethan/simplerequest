import sys
import json
from simplehttp.error import HttpError
from simplehttp.utils import process_url

try:
    import http.client
except ImportError:
    import urllib2


def http_get(url, params=None):
    """A wrapper for making http GET request for both
       Python2 and Python3

    Args:
        url (string): URL path
        params (dict, optional):Addtional parameters
            to  be added to the query string.

    Raise:
        URLError , HTTPError from urllib2


    Returns:
        [dict]: Reponse body in JSON (Python dictionary) format
    """
    params = params or {}
    url_parts = process_url(url, params)
    if sys.version_info[0] > 2:
        if url_parts['host'] == 'http':
            conn = http.client.HTTPConnection(url_parts['host'])
        else:
            conn = http.client.HTTPSConnection(url_parts['host'])
        conn.request('GET', url_parts['path'])
        # TODO: Here may have ConnectionError
        response = conn.getresponse()
        status_code = str(response.status)
        data = response.read()

    else:
        extended_url = url_parts['protocal'] + \
            '://' + url_parts['host'] + url_parts['path']
        req = urllib2.Request(extended_url)
        try:
            # TODO: "Maybe write our own error class to wrap
            # whatever error urlopen may raise.
            response = urllib2.urlopen(req)
            status_code = response.getcode()
            data = response.read()
        except urllib2.HTTPError as error:
            # TODO: What if json.loads raise error ?"
            data = ""
            status_code = error.getcode()
        status_code = str(status_code)

    if status_code.startswith('4') or status_code.startswith('5'):
        raise HttpError(status_code)

    try:
        data_json = json.loads(data)
    except (ValueError, JSONDecodeError):
        data_json = {}

    return data_json


def http_post(url, params={}, data={}):

    params = params or {}
    data = data or {}
    url_parts = process_url(url, params)
    headers = {'Content-Type': 'application/json'}
    data_str = json.dumps(data)
    if sys.version_info[0] > 2:
        conn = http.client.HTTPSConnection(url_parts['host'])
        conn.request('POST', url_parts['path'],
                     body=data_str, headers=headers
                     )
        response = conn.getresponse()
        status_code = str(response.status)
        data = response.read()

    else:

        extended_url = url_parts['protocal'] + \
            '://' + url_parts['host'] + url_parts['path']
        req = urllib2.Request(extended_url, data_str, headers)

        try:
            response = urllib2.urlopen(req)
            status_code = response.getcode()
            data = response.read()
        except urllib2.HTTPError as error:
            # TODO: What if json.loads raise error ?"
            data = ""
            status_code = error.getcode()
        status_code = str(status_code)

    if status_code.startswith('4') or status_code.startswith('5'):
        raise HttpError(status_code)

    try:
        data_json = json.loads(data)
    except (ValueError, JSONDecodeError):
        data_json = {}

    return data_json
