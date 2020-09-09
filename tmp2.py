# encoding=utf-8
import simplehttp


def case2():
    url_target = "https://httpbin.org/get?debug=true"
    params = {"name": u"常⾒見見問題 q&a"}
    r = simplehttp.get_json(url_target, params)
    print(r)
    assert r['args'] == {'debug': 'true', 'name': u'常⾒見見問題 q&a'}


if __name__ == '__main__':
    # noneValidJson()
    # errorCode()
    case2()
