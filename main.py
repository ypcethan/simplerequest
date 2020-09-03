# encoding=utf-8
import json
import sys
import simplehttp

# r = simplehttp.post_json("https://httpbin.org/status/400")
# try:
#     r = simplehttp.post_json("https://httpbin.org/status/400")
# except Exception as e:
#     print(e)
#     print('asdf')
#     print(sys.last_value.status_code)
#     ttype, value, tb = sys.exc_info()
#     print(ttype)
#     print(value)
#     print(tb)
#     sys.last_value = value
#     print(sys.last_value.status_code)


def encode_dict(obj):
    for k in obj:
        obj[k] = obj[k].encode('utf-8')
    return obj


def case2():
    url_target = "https://httpbin.org/get?debug=true"
    params = {"name": u"常⾒見見問題 q&a"}
    r = simplehttp.get_json(url_target, params)
    assert r['args'] == {'debug': 'true', 'name': u'常⾒見見問題 q&a'}


def case3():
    url_target = "https://httpbin.org/post"
    data = {"isbn": "9789863479116", "title": u"流暢的 Python"}
    params = {"debug": "true"}
    r = simplehttp.post_json(url_target, params, data)
    # print type(r['json'])
    assert r['args'] == {'debug': 'true'}


def noneValidJson():
    url_target = "https://google.com"
    r = simplehttp.get_json(url_target)


def connectionError():
    url_target = "https://google.com/sawer"
    r = simplehttp.get_json(url_target)


if __name__ == '__main__':
    noneValidJson()
