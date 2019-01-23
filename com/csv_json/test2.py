import json


stringOfJsonData = '{"name": "Zophie", "isCat": true, "miceCaught": 0, "felineIQ": null}'
jsonDataAsPythonValue = json.loads(stringOfJsonData)
print(jsonDataAsPythonValue)

pythonValue = {"name": "Zophie", "isCat": True, "miceCaught": 0, "felineIQ": None}
stringOfJsonData2 = json.dumps(pythonValue)
print(stringOfJsonData2)