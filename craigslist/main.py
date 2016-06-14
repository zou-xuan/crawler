import requests
import re
import sys
import string

reload(sys)


class spider(object):
    def getsource(self, url):
        html = requests.get(url)
        return html.text

    def geteveryhouse(self, source):
        everyclass = re.findall('<p class="row"(.*?)</p>', source, re.S)
        return everyclass

    def changepage(self, url):
        page_group = []
        start_num = [0, 100, 200]
        for i in start_num:
            link = re.sub('s=\d+', 's=%s' % i, url, re.S)
            page_group.append(link)
        return page_group

    def getinfo(self, house):
        info = {}
        info['href'] = 'https://sfbay.craigslist.org' + \
                       re.search('<a href="(.*?)"', house, re.S).group(1)
        info['description'] = re.search('<span id="titletextonly">(.*?)</span>', house, re.S).group(1)
        info['price'] = re.search('<span class="price">(.*?)</span>', house, re.S).group(1)
        houseinfo = ""
        try:
            houseinfo = re.search('<span class="housing">(.*?)</span>', house, re.S).group(1)
            info['bedroom'] = re.search('/ (.*?)br', houseinfo, re.S).group(1)
            price_string = info['price'][1:]
            priceInt = int(price_string)
            bedroomInt = int(info['bedroom'])
            averagePrice = priceInt * 1.0 / bedroomInt
            if (averagePrice < 1000):
                info['averagePrice'] = priceInt
            else:
                info['averagePrice'] = averagePrice
        except AttributeError:
            info['bedroom'] = ""
            info['averagePrice'] = ""
        try:
            size = re.search('.* (.*?)ft', houseinfo, re.S).group(1)
            info['size'] = size

        except AttributeError:
            info['size'] = ""
        info['location'] = re.search('<small> \((.*?)\)</small>', house, re.S).group(1)

        return info

    def saveinfo(self, houseinfo):
        f = open('houseinfo.txt', 'a')
        for each in houseinfo:
            f.writelines('description: ' + each['description'] + '\n')
            f.writelines('location: ' + each['location'] + '\n')
            f.writelines('href: ' + each['href'] + '\n')
            f.writelines('size: ' + each['size'] + '\n')
            f.writelines('bedroom: ' + each['bedroom'] + '\n')
            f.writelines('price: ' + each['price'] + '\n')
            f.writelines('averagePrice: ' + str(each['averagePrice']) + '\n')
            f.writelines('-----------------------------------------------------------' + '\n')
        f.close()

    def saveAveragePrice(self, houseinfo):
        f = open('averagePrice.txt', 'a')
        for each in houseinfo:
            if (each['averagePrice'] != ""):
                print each['averagePrice']
                f.writelines(str(each['averagePrice']) + '\n')
        f.close()


if __name__ == '__main__':
    houseinfo = []
    url = "https://sfbay.craigslist.org/search/apa?query=uc+berkeley&s=0"
    craigslist = spider()
    page_group = craigslist.changepage(url)
    for page in page_group:
        print "processing " + page
        source = craigslist.getsource(page)
        houses = craigslist.geteveryhouse(source)
        for each in houses:
            info = craigslist.getinfo(each)
            houseinfo.append(info)

    craigslist.saveinfo(houseinfo)
    craigslist.saveAveragePrice(houseinfo)
