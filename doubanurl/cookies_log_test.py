import requests

cookies = {'cookie':
               '__yadk_uid=VfiqijjXlR9v6KcdL3EepDfMup3UzkJ8; ll="118282"; bid=TI5hJBe91iU; push_noty_num=0; push_doumail_num=0; __gads=ID=8068745557b868e8:T=1557309449:S=ALNI_Mb8yfexuiCe2swSyCn5VJzhgmiwew; __utmc=30149280; __utmz=30149280.1557383321.2.2.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; __utmc=223695111; __utmz=223695111.1557383321.8.5.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; ap_v=0,6.0; trc_cookie_storage=taboola%2520global%253Auser-id%3Dcde732ac-5f91-4fd7-a925-d6caea01f243-tuct3cc4235; _vwo_uuid_v2=DDE7AF532406401AC0710C3994E5381A3|fc9a606217ff4c260afb8ffb9fdaf05b; ps=y; _pk_ref.100001.4cf6=%5B%22%22%2C%22%22%2C1557388915%2C%22https%3A%2F%2Fwww.baidu.com%2Flink%3Furl%3D953T6GZCnaBzwr4YqPFUT2HnJf7VXrmMP3sI-DGqL9SOz2ymr_1y_mhwYathq_uzGHTGwl_kU0yLTy0KExWx9K%26wd%3D%26eqid%3De2861700000179b9000000065cd3c894%22%5D; _pk_ses.100001.4cf6=*; __utma=30149280.520939229.1557309449.1557383321.1557388921.3; __utma=223695111.1675748125.1557141961.1557383321.1557388921.9; __utmb=223695111.0.10.1557388921; dbcl2="196218217:MZAbrVePuTE"; ck=3Hcg; __utmt=1; __utmv=30149280.19621; __utmb=30149280.6.10.1557388921; _pk_id.100001.4cf6=3633057893591058.1557141961.13.1557389351.1557386640.'
           }
url = 'https://movie.douban.com/subject/4074035/'
headers = {
'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
'Accept-Encoding': 'gzip, deflate, br',
'Accept-Language': 'zh-CN,zh;q=0.9',
'Cache-Control': 'max-age=0',
'Connection': 'keep-alive',
'Host': 'movie.douban.com',
#'Referer': 'https://accounts.douban.com/passport/login?source=main',
'Upgrade-Insecure-Requests': '1',
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36',
}

r = requests.get(url, cookies=cookies, headers=headers)
print("asked")
#
with open('douban.txt', 'w', encoding='utf-8') as f:
    print(r.url)
    f.write(r.text) #把登陆主页后返回的数据保存到文件中
