#  -*- coding: UTF-8 -*-
import requests
from bs4 import BeautifulSoup
import random
'''
1.爬取IP
2.网页：http://www.xicidaili.com/nn/
3.使用   requests.get(url, headers=headers, proxies=proxies)
'''
#模拟浏览器
headers = {
"User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36"
}

#爬取IP地址，组装成：ip+port
def Get_Ip():
    response = requests.get("http://www.xicidaili.com/nn/", headers=headers).text
    soup = BeautifulSoup(response, "lxml")
    ips = soup.find_all("tr", class_='odd')
    ip_list = []
    for ip in ips:
        td = ip.find_all("td")
        ip_list.append(td[1].text + ":" + td[2].text)
    return ip_list

#随机返回一个ip
#proxies = {	"http" : "http://111.155.124.78:8123" # 代理ip }

def Rand_ip(ip_list):
    proxie_list = []
    for ip in ip_list:
        proxie_list.append("http://"+ip)
    proxy_ip = random.choice(proxie_list)
    proxies = {'http':proxy_ip}
    return proxies

if __name__=="__main__":
    list_ip = Get_Ip()
    proxty = Rand_ip(list_ip)
    print(proxty)

