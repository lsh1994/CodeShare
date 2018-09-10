import requests
import re
from bs4 import BeautifulSoup



#content:文本内容  
def analysis(content):
    res=[]
    b=BeautifulSoup(content,"lxml").select("#article_list > div.article_item")
    for page in b:
        url=page.select_one(".article_title .link_title a").attrs['href']
        title=page.select_one(".article_title .link_title").get_text().strip()
        time=page.select_one(".link_postdate").get_text()
        read_count=str(page.select_one(".link_view").get_text()).strip()[3:-1]
        comment=str(page.select_one(".link_comments a").next_sibling).strip()[1:-1]
        res.append([url,title,time,read_count,comment])
    return res
def getData():
    r=requests.get(host+mysite)
    yield analysis(r.text)
    while(True):
        rp = BeautifulSoup(r.text, 'lxml').select("#papelist > div > nav > ul > li")
        q = re.search(r'href="(.*?)".*?rel="next"', str(rp[len(rp) - 1]))
        if q==None:
            break
        r=requests.get(q.group(1))
        yield analysis(r.text)

host = "http://blog.csdn.net/"
mysite = "nima1994"




