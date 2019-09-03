import requests
from bs4 import BeautifulSoup
import os
import urllib

topic=input("要看哪個版：")\
#topic="joke"
url = r'https://www.ptt.cc/bbs/'+topic+'/index.html'
rs = requests.Session()
payload ={
        "from":"bbs/"+topic+"/index.html",
        "yes":"yes"
}
r = rs.post("https://www.ptt.cc/ask/over18?from=%2Fbbs%2F"+topic+"%2Findex.html",payload)
r = rs.get(url)

url_list=[]
i = 0
tc = 0
for i in range(1): #往上爬1頁
    try:
        r = requests.get(url)
        soup = BeautifulSoup(r.text,"html.parser")
        sel = soup.select("div.title a") #標題
        u=soup.select("div.btn-group.btn-group-paging a") #a標籤        
        url = "https://www.ptt.cc" + u[1]["href"] #上一頁的網址
    except:
        r = requests.get(url)
        r = rs.post("https://www.ptt.cc/ask/over18?from=%2Fbbs%2F"+topic+"%2Findex.html",payload)
        r = rs.get(url)
        soup = BeautifulSoup(r.text,"html.parser")
        sel = soup.select("div.title a") #標題
        u=soup.select("div.btn-group.btn-group-paging a") #a標籤        
        url = "https://www.ptt.cc" + u[1]["href"] #上一頁的網址
    for s in sel: #印出網址跟標題
        url_list.append('https://www.ptt.cc'+s["href"])
        print(tc,s.text)
        tc += 1

num=eval(input("要看第幾個標題："))

r_inside = rs.get(url_list[num])
soup2 = BeautifulSoup(r_inside.text,"html.parser")
print_form = ('\n{}\n\n{}')
title = soup2.select("title")[0].text
description = soup2.select("meta")[7]['content']

quote = soup2.select("span.f3")
print(print_form.format(title,description))
img_list=[]
for link in soup2.find_all('a'):
    if link.get('href').find(r'https://i') > -1:
        img_list.append(link.get('href'))
        print(link.get('href'))
for q in range(len(quote)):
    print('q :{}'.format(quote[q].text))

x=1
for link in range(len(img_list)):
	local = os.path.join('c:\py\%s.jpg' % x)
	urllib.urlretrieve(link,local) #link是下載的網址 local是儲存圖片的檔案位址
	x+=1
