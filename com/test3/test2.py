import requests, bs4


# res = requests.get('http://nostarch.com')
# res.raise_for_status()
# noStarchSoup = bs4.BeautifulSoup(res.text)
# print(type(noStarchSoup))
exampleFile = open('example.html')
# exampleSoup = bs4.BeautifulSoup(exampleFile, "lxml")
# print(type(exampleSoup))
exampleSoup = bs4.BeautifulSoup(exampleFile.read(), "lxml")
elems = exampleSoup.select('#author')

print(type(elems))
print(len(elems))
print(type(elems[0]))
print(elems[0].getText())
print(str(elems[0]))
print(elems[0].attrs)


pElems = exampleSoup.select('p')
print(str(pElems[0]))
print(pElems[0].getText())

print(str(pElems[1]))
print(pElems[1].getText())

print(str(pElems[1]))
print(pElems[1].getText())