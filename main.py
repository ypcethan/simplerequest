import sys
import simplehttp

try:
    r = simplehttp.get_json("https://httpbin.org/status/400")
except Exception as e:
    print(e)
    ttype, value, tb = sys.exc_info()
    print(ttype)
    print(value)
    print(tb)
    sys.last_value = value
    print(sys.last_value.status_code)
