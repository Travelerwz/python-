# -*- coding:UTF-8 -*-
from bs4 import BeautifulSoup
import requests,sys

class Biquwen(object):
    def __init__(self):
        self.url = "https://www.biqukan.com/0_790/"
        self.url2 = "https://www.biqukan.com"
        self.name = []
        self.nums = []
        self.urls = []
    def get_url(self):
        response = requests.get(self.url).text
        #解析网页
        #class_是为了避免和python中的关键字class冲突
        soup = BeautifulSoup(response,'lxml')
        divs = soup.find_all('dd')
        self.nums = len(divs[12:])
        for div in divs:
            #取标签和路径
            self.name.append(div.string)
            self.urls.append(self.url2+div.a.get('href'))
    '''
    @获取每章节的内容
    '''
    def get_text(self,url2):
        response = requests.get(url = url2).text
        soup = BeautifulSoup(response,"lxml")
        divs = soup.find_all('div',class_="showtxt")
        divs = divs[0].get_text()
        return divs

    '''
    @写入文件
    '''
    def write_text(self,name,path,tet):
        with open(path,'a', encoding='utf-8') as f:
            #print(tet)
            f.write(name + '\n')
            f.write(str(tet))
            f.write('\n\n')

if __name__=="__main__":
    bi = Biquwen()
    bi.get_url()
    for num in range(bi.nums):
        #print(bi.get_text(bi.urls[num]))
        bi.write_text(bi.name[num],"元尊.txt",bi.get_text(bi.urls[num]))












