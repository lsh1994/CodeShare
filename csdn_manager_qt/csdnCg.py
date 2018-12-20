import requests
from selenium import webdriver
from bs4 import BeautifulSoup

opt = webdriver.ChromeOptions()
opt.headless = True
browser = webdriver.Chrome(options=opt)
totalpage=0

#content:文本内容  
def analysis(content):
    global totalpage
    res=[]
    b=BeautifulSoup(content,"lxml").select(".article-list > div.article-item-box")[1:]
    for page in b:
        url=page.select_one("h4 a").attrs['href']
        title=page.select_one("h4 a span").next_sibling.strip()
        time=page.select("div p")[0].get_text().strip()
        read_count=int(page.select("div p")[1].get_text().strip()[4:])
        comment=int(page.select("div p")[2].get_text().strip()[4:])
        res.append([url,title,time,read_count,comment])
    totalpage = int(BeautifulSoup(content, "lxml").select("#pageBox li")[-3].get_text())
    return res

def getData():
    browser.get(host+mysite)
    yield analysis(browser.page_source)

    global totalpage
    for i in range(2,totalpage+1):
        url="https://blog.csdn.net/nima1994/article/list/"+str(i)

        browser.get(url)
        yield analysis(browser.page_source)

host = "http://blog.csdn.net/"
mysite="nima1994"




