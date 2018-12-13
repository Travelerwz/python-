import requests
import time
url1 = 'http://neihanshequ.com/joke/?is_json=1&app_name=neihanshequ_web&max_time=1521075470.0'
#获取段子信息  Json文件
html = requests.get(url1)
print(html)
print (html.text)
timestamp = html.json()['data']['max_time']
header = {'Accept':'application/json, text/javascript, */*; q=0.01',
        'Accept-Encoding':'gzip, deflate',
        'Accept-Language':'zh-CN,zh;q=0.8',
        'Connection':'keep-alive',
        'Cookie':'uuid="w:1cc888778bf94e5683cdd81fc877be7e"; tt_webid=6532783295012013576; csrftoken=d18962da5ac606fd9608d792273b1e9e; _ga=GA1.2.177855175.1521032137; _gid=GA1.2.1824019791.1521032137; _gat=1',
        'Host':'neihanshequ.com',
        'Referer':'http://neihanshequ.com/',
        'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.101 Safari/537.36',
        'X-CSRFToken':'d18962da5ac606fd9608d792273b1e9e',
        'X-Requested-With':'XMLHttpRequest'}
while type(timestamp)==float or type(timestamp)==int:
    time.sleep(3)
    url1 = 'http://neihanshequ.com/joke/?is_json=1&app_name=neihanshequ_web&max_time='+str(timestamp)
    with open('C:\\Users\\Administrator\\Desktop\\内涵段子.txt','a',encoding = 'utf-8') as f:
        html = requests.get(url1, headers=header)
        for n in range(len(html.json()['data']['data'])):
           data = html.json()['data']['data'][n]['group']['content']
           f.write(data +'\n')
    timestamp = html.json()['data']['max_time']
    print(timestamp)
#写入本地
