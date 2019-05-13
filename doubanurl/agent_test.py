import  requests
from bs4 import BeautifulSoup
header={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36'}
proxies = {'http': '77.77.17.48:50102',
           }
url="https://movie.douban.com/subject/5031426/"
header={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36'}
req=requests.get(url,headers=header,proxies=proxies,timeout=5)
html=req.text
soup=BeautifulSoup(html,'lxml')
print(soup.text)
