import requests, os, bs4, threading


url = 'http://xkcd.com'
os.makedirs('xkcd2', exist_ok=True)


def downloadXkcd(startComic, endComic):
    for urlNumber in range(startComic, endComic):
        print('Downloading page %s/%s...' % (url, urlNumber))
        res = requests.get(url+'/%s' % urlNumber)
        res.raise_for_status()

        soup = bs4.BeautifulSoup(res.text, 'lxml')

        comicElem = soup.select('#comic img')
        if comicElem == []:
            print('Could not find comic image.')
        else:
            comicUrl = 'http:' + comicElem[0].get('src')
            print('Downloding image %s...' % comicUrl)
            try:
                res = requests.get(comicUrl)
                res.raise_for_status()

                imageFile = open(os.path.join('xkcd2', os.path.basename(comicUrl)), 'wb')
                for chunk in res.iter_content(100000):
                    imageFile.write(chunk)
                imageFile.close()
            except Exception as e:
                print(e)


downloadThreads = []
for i in range(0, 1400, 100):
    downloadThread = threading.Thread(target=downloadXkcd, args=(i, i + 99))
    downloadThreads.append(downloadThread)
    downloadThread.start()

for downloadThread in downloadThreads:
    downloadThread.join()

print('Done.')






# while not url.endswith('#'):
#     print('Downloading ppage %s...' % url)
#     res = requests.get(url)
#     res.raise_for_status()
#
#     soup = bs4.BeautifulSoup(res.text, "lxml")
#
#     comicElem = soup.select('#comic img')
#     if comicElem == []:
#         print('Could not find comic image.')
#     else:
#         comicUrl = 'http:' + comicElem[0].get('src')
#         print('Downloding image %s...' % comicUrl)
#         try:
#             res = requests.get(comicUrl)
#             res.raise_for_status()
#
#             imageFile = open(os.path.join('xkcd', os.path.basename(comicUrl)), 'wb')
#             for chunk in res.iter_content(100000):
#                 imageFile.write(chunk)
#             imageFile.close()
#         except Exception as e:
#             print(e)
#
#     prevLink = soup.select('a[rel="prev"]')[0]
#     url = 'http://xkcd.com' + prevLink.get('href')
#
# print('Done.')
