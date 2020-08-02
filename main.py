import json
import simplehttp

# print(simplehttp.get_json('https://httpbin.org/get'))

data = {"isbn": "9789863479116", "title": "流暢的 Python"}
r = simplehttp.post_json("https://httpbin.org/post",
                         params={"debug": "true"}, data=data)
# r = simplehttp.post_json("https://httpbin.org/post",
#                          params=data)
print(r)
print(r['data'])
print(json.loads(r['data']))
