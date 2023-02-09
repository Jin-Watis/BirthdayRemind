# coding=UTF-8
import json

with open(r"data.json", 'r', encoding='utf-8') as f:
    data = json.load(f)

print(data)

newdata = {}
for name in data:
    dateList = data[name]
    for date in dateList:
        date = (date['month'], date['day'])
        try:
            newdata[date].append(name)
        except KeyError:
            # 原来没有这个日期
            newdata[date] = [name]

print(newdata)


