import http.client
import json
from simplehttp.utils import process_url


def get_json(url, params={}):
    url_parts = process_url(url, params)
    conn = http.client.HTTPSConnection(url_parts['host'])
    conn.request('GET', url_parts['path'])
    response = conn.getresponse()
    body = response.read()
    return json.loads(body)
