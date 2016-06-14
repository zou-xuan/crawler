import requests
import sys
import re
reload(sys)

class spider(object):

    def getsource(self,url):
        html=requests.get(url)
        html.encoding='utf-8'
        html.text.encode('utf-8')
        return html.text

    def changepage(self,url,total_page):
        now_page=int(re.search('pageNum=(\d+)',url,re.S).group(1))
        page_group=[]
        for i in range(now_page,total_page+1):
            link=re.sub('pageNum=\d+','pageNum=%s'%i,url,re.S)
            page_group.append(link)
        return page_group

    def geteveryclass(self,source):
        everyclass=re.findall('(<li id=.*?</li>)',source,re.S)
        return everyclass

    def getinfo(self,eachclass):
        info={}

        info['title']=re.search('title=(.*?)alt',eachclass,re.S).group(1)
    #    print info['title']
        info['content']=re.search('display: none;">\n\t*(.*?)</p>',eachclass,re.S).group(1)
        timeandlevel=re.findall('<em>(.*?)</em>',eachclass,re.S)
        info['classtime']=re.sub("\n\t*","",timeandlevel[0])
        info['classlevel']=timeandlevel[1]
        info['learnnum']=re.search('learn-number">(.*?)</em>',eachclass,re.S).group(1)
        return info

    def saveinfo(self,classinfo):
        f = open('info.txt','a')
        for each in classinfo:

            title='title: '+each['title']+'\n'
            content='content: '+each['content']+'\n'
            classtime='classtime: '+each['classtime']+'\n'
            classlevel='classlevel: '+each['classlevel']+'\n'
            learnnum='learnnum: '+each['learnnum']+'\n'
            f.writelines(title.encode('utf-8'))
            f.writelines(content.encode('utf-8'))
            f.writelines(classtime.encode('utf-8'))
            f.writelines(classlevel.encode('utf-8'))
            f.writelines(learnnum.encode('utf-8'))
        f.close()


if s
    classinfo=[]
    url='http://www.jikexueyuan.com/course/?pageNum=1'
    jikespider=spider()
    all_links=jikespider.changepage(url,5)
    for link in all_links:
        print 'Processing: '+link
        html=jikespider.getsource(link)
        everyclass=jikespider.geteveryclass(html)
        for each in everyclass:ih
            info=jikespider.getinfo(each)
            classinfo.append(info)
    jikespider.saveinfo(classinfo)






            double
