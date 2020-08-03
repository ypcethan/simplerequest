import json
import sys
import simplehttp

# try:
#     r = simplehttp.post_json("https://httpbin.org/status/400")
# except Exception as e:
#     print(e)
#     print('asdf')
#     print(sys.last_value.status_code)
#     # ttype, value, tb = sys.exc_info()
#     # print(ttype)
#     # print(value)
#     # print(tb)
#     # sys.last_value = value
#     # print(sys.last_value.status_code)

r2 = simplehttp.get_json("https://httpbin.org/get?debug=true",
                         params={"name": "常⾒見見問題 Q&A"})
print(r2)
print(json.loads(r2))
