import json
a={"model": "BMW 230", "mpg": 27.5}
b=json.dumps(a)
print(b)
c=json.loads(b)
print(c)