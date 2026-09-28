import json
# some JSON:
x =  '{ "name":"John", "age":30, "city":"New York"}'
y = json.loads(x)
print(y)
print(y["name"])
a = {
    "pet":"cat", "color":"red", "place":"beach"
}
z = json.dumps(a)
print(z)
try:
    json.parse(z)
except NameError:
    print("an error occurred")
except AttributeError:
    print("an error occurred")
finally:
    print("done")
