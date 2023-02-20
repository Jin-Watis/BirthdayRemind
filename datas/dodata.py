# coding=UTF-8
import json

with open(r"data.json", 'r', encoding='utf-8') as f:
    data = json.load(f)

print(data)


def func(data):
    return 1


newdata = func(data)
print(newdata)
