import requests
from bs4 import BeautifulSoup

class spider(object):
    def getsource(self,url):
        html=requests.get(url)
        return html.text

    def getbooks(self,html):
        soup=BeautifulSoup(html,"html.parser")
        critical=soup.find_all("div",{"class":"zg_itemRow"})
        for each in critical:
            title=each.img.get("title")
            href=each.a.get("href").strip()

            print(title+'\n')
            print(href+'\n')




if __name__=='__main__':
    url="https://www.amazon.cn/gp/bestsellers/digital-text/116169071/ref=sa_menu_kindle_l3_116169071"
    amazon=spider()
    html=amazon.getsource(url)
    amazon.getbooks(html)
