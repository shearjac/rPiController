import json

data = {
    "name" : "John Johnson",
    "info" : { "city" : "Marshall", "state" : "Minnesota" }
}

y=json.dumps(data)

print(y)
