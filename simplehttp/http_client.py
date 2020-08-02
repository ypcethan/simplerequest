import http.client
import json
from simplehttp.utils import process_url
import simplehttp
from urllib.parse import urlencode


def get_json(url, params={}):
    url_parts = process_url(url, params)
    conn = http.client.HTTPSConnection(url_parts['host'])
    conn.request('GET', url_parts['path'])
    response = conn.getresponse()
    status = str(response.status)
    if not status.startswith('2'):
        raise simplehttp.HttpError(f"HTTP Status Code: {status}")
    body = response.read()
    return json.loads(body)


def post_json(url, params={}, data={}):
    url_parts = process_url(url, params)
    conn = http.client.HTTPSConnection(url_parts['host'])
    headers = {'Content-Type': "application/json"}
    conn.request('POST', url_parts['path'],
                 body=json.dumps(data), headers=headers)
    response = conn.getresponse()
    status = str(response.status)
    if not status.startswith('2'):
        raise simplehttp.HttpError(f"HTTP Status Code: {status}")
    body = response.read()
    return json.loads(body)
