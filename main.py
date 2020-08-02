import sys
import json
import simplehttp

# print(simplehttp.get_json('https://httpbin.org/get'))

# data = {"isbn": "9789863479116", "title": "流暢的 Python"}
# r = simplehttp.post_json("https://httpbin.org/post",
#                          params={"debug": "true"}, data=data)
# # r = simplehttp.post_json("https://httpbin.org/post",
# #                          params=data)
# print(r)
# print(r['data'])
# print(json.loads(r['data']))
r = simplehttp.get_json("https://httpbin.org/status/400")
print(r)

print(sys.last_value.status_code)
