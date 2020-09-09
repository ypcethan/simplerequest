# encoding=utf-8
import simplehttp
import pdb


def case2():
    url_target = "https://httpbin.org/get?debug=true"
    params = {"name": u"常⾒見見問題 q&a"}
    r = simplehttp.get_json(url_target, params)
    print(r)
    assert r['args'] == {'debug': 'true', 'name': u'常⾒見見問題 q&a'}


def case3():
    url_target = "https://httpbin.org/status/500"
    params = {}
    pdb.set_trace()
    r = simplehttp.get_json(url_target, params)
    print(r)


if __name__ == '__main__':
    # noneValidJson()
    # errorCode()
    case3()
