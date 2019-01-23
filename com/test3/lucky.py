#! /usr/bin/env python3
import requests, sys, webbrowser, bs4

# <h3 class ="t" >
# < a data-click="{
# 'F': '778717E8',
# 'F1': '9D73E1E4',
# 'F2': '4CA6DE6B',
# 'F3': '54E5243D',
# 'T': '1545360860',
# 'y': 'FF9DF59E'
#
# }" href="
# http: // www.baidu.com / link?url = tO55dLDT21M2jawgwG67Q1l5KIr82ZGWNBpY_NddNKt9UnvX1IX - aYWllSoirGK2TCqBXN92qr00ssAh7B6XB8ud2IJOgoQZJlmK04iOKDy
# " target="
# _blank
# ">济南<em>遥墙机场停车场</em>怎么收费?大概需要停四五天_百度知道</a></h3>
print('baiduing...')
url = 'http://www.baidu.com/s?word=' + ' '.join(sys.argv[1:])
print(url)
res = requests.get(url)

res.raise_for_status()
soup = bs4.BeautifulSoup(res.text, "lxml")
linkElems = soup.select('.t a')
print(type(linkElems))
print(len(linkElems))
numOpen = min(5, len(linkElems))
for i in range(numOpen):
    print(linkElems[i].get('href'))
    webbrowser.open(linkElems[i].get('href'))
