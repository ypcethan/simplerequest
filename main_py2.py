#encoding=utf-8
import sys
import json
import urllib
from simplehttp.utils import process_url

def make_request(method , url , params = None, data=None):

    params = params or {} 
    data = data or {} 
    url_parts = process_url(url, params)
    try:
        import http.client
    except ImportError:
        import urllib2
        extended_url = url_parts['protocal'] + "://"+ url_parts['host'] + url_parts['path']
        if method == 'GET':
            req = urllib2.Request(extended_url)
        elif method == 'POST':

            headers = {'Content-Type': "application/json"}
            data_str = json.dumps(data)
            
            req = urllib2.Request(extended_url, data_str 
, headers)
        response = urllib2.urlopen(req)
        body = response.read()
        json_data =  json.loads(body)
        print json_data['args']

def case2():
    url_target = "https://httpbin.org/get?debug=true"
    params = {"name": "常⾒見見問題 q&a"}
    make_request('GET' , url_target, params)

def case3():
    url_target = "https://httpbin.org/post"
    data = {"isbn": "9789863479116", "title": "流暢的 Python"}
    params = {"debug": "true"}
    make_request('POST' , url_target, params,data)

if __name__ == '__main__':

    # url_target = 'https://httpbin.org/get'
    # url_target2 = "https://httpbin.org/get?debug=true"
    # params = {"name": "常⾒見見問題 q&a"}
    # make_request('get' , url_target2, params)
    # case2()
    case3()

