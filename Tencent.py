# coding:utf-8
#!/usr/bin/python3
#author:冰茶
from bs4 import BeautifulSoup
import datetime
import requests
import re
headers = {
            "User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.90 Safari/537.36"
            }
i = datetime.datetime.now()
print(i)
htime = re.findall(r'\d{4}-\d{2}-\d{2}', str(i))
mtime = re.findall(r'\d{2}:\d{2}', str(i))
# 当前时间，年月日
# 当前时间,小时
nh_time = mtime[0].split(":")[0]

# 当前时间，分钟
mtime = mtime[0].split(":")[1]
def tencent(url):
    html = requests.get(url, headers=headers).text
     # 服务器返回响应
    html = html.encode("ISO-8859-1")
    html = html.decode('utf-8')
    # print (html)
    soup = BeautifulSoup(html, "html.parser")
    #获取标题
    title = soup.find_all('h3')
    #获取时间
    time = soup.find_all('div', class_='time')
    ##获取年月日
    ntime = re.findall(r'\d{2}:\d{2}', str(time))
    ytime = re.findall(r'\d{4}-\d{2}-\d{2}', str(time))
    whtime = ntime[0].split(":")[0]
    #获取详情地址
    url = soup.find_all('a')
    # 循环爬取
    if (str(ytime[0])==str(htime[0]) and int(nh_time)==int(whtime)) or  (str(ytime[0])==str(htime[0]) and int(nh_time)-int(whtime)==1) :
        for i in range(len(title)):
           res  = title[i].contents[0].string
           res1 = time[i].string
           # print (res+res1)
           # print ('https://s.tencent.com/' + str(url[i + 5]['href']))
           datamsg = {"text":res, "desp": 'https://s.tencent.com/' + str(url[i + 5]['href'])}
           requests.post("http://sc.ftqq.com/" + "server酱key" + ".send",
                         data=datamsg)
           break






if __name__=='__main__':
    tencent('https://s.tencent.com/research/bsafe/')
