import requests


res = requests.get('http://www.sina.com')
print(type(res))
print(len(res.text))
print(res.text[:222])

res = requests.get("http://www.sina.com/txt.txt")
try:
    res.raise_for_status()
except Exception as exc:
    print('There was a problem: %s' % exc)


res = requests.get('http://www.sina.com')
res.raise_for_status()
htmlFile = open('sina.html', 'wb')
for chunk in res.iter_content(100000):
    htmlFile.write(chunk)

htmlFile.close()
