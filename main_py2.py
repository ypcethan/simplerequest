# encoding=utf-8
import sys
import json
import urllib
import urllib2
# from simplehttp.utils import process_url
# from simplehttp.error import HttpError


def make_request(method, url, params=None, data=None):

    params = params or {}
    data = data or {}
    url_parts = process_url(url, params)
    try:
        import http.client
    except ImportError:
        import urllib2
        extended_url = url_parts['protocal'] + \
            "://" + url_parts['host'] + url_parts['path']
        if method == 'GET':
            req = urllib2.Request(extended_url)
        elif method == 'POST':

            headers = {'Content-Type': "application/json"}
            data_str = json.dumps(data)

            req = urllib2.Request(extended_url, data_str, headers)

        try:
            response = urllib2.urlopen(req)
        except urllib2.HTTPError as e:
            print e
            status = str(e.getcode())
            print status
        print response
        if status.startswith('4') or status.startswith('5'):
            # raise HttpError(f"HTTP Status Code: {status}", int(status))
            raise HttpError(status)
        body = response.read()
        json_data = json.loads(body)
        status = str(response.getcode())

        print status
        print body
        print json_data['data']


def case2():
    url_target = "https://httpbin.org/get?debug=true"
    params = {"name": "常⾒見見問題 q&a"}
    make_request('GET', url_target, params)


def case3():
    url_target = "https://httpbin.org/post"
    data = {"isbn": "9789863479116", "title": u"流暢的 Python"}
    params = {"debug": "true"}
    make_request('POST', url_target, params, data)


def case4():
    url_target = "https://httpbin.org/status/400"
    make_request('GET', url_target)


def urllibExample():
    # url_target = "https://httpbin.org/get?debug=true"
    url_target = "https://httpbin.org/status/400"
    headers = {'Accept': "application/json"}
    req = urllib2.Request(url_target, headers=headers)
    response = urllib2.urlopen(req)
    status = response.getcode()
    print(response.read())
    print(status)


if __name__ == '__main__':

    # case4()
    urllibExample()
