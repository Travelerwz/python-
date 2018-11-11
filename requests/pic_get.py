import requests
from bs4 import BeautifulSoup
import os
#获取html
f = requests.get('http://www.mmjpg.com/').text
#用BS解析html
s = BeautifulSoup(f,'lxml')
s_imgs = s.find_all('img')
#逐个将图片保存到本地
i=1
for s_img in s_imgs:
    img_url = s_img['src']
    print(img_url)
    img_content = requests.get(img_url).content
    print(img_content)
    file_name = str(i) + '.jpg'
    with open('C:\\Users\\Administrator\\Desktop\\11'+'/'+file_name, 'wb') as wf:
        wf.write(img_content)
    i += 1
