import sys
import json
from simplehttp.error import HttpError

try:
    import http.client
except ImportError:
    import urllib2


def http_get(url_parts):
    if sys.version_info[0] > 2:
        if url_parts['host'] == 'http':
            conn = http.client.HTTPConnection(url_parts['host'])
        else:
            conn = http.client.HTTPSConnection(url_parts['host'])
        conn.request('GET', url_parts['path'])
        response = conn.getresponse()
        status_code = str(response.status)
        data = response.read()

    else:
        extended_url = url_parts['protocal'] + \
            '://' + url_parts['host'] + url_parts['path']
        req = urllib2.Request(extended_url)
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

    return status_code, data_json


def http_post(url_parts, data):

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

    return status_code, data_json
