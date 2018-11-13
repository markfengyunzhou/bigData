# coding=utf-8
import requests
from requests.exceptions import ProxyError, Timeout, ConnectionError, ChunkedEncodingError
import time
import urllib.parse
from fake_useragent import UserAgent
import re, threading, math
from lxml import etree
from concurrent.futures import ThreadPoolExecutor
import logging

false = False
true = True
null = None

logger = logging.getLogger(__name__)
logger.setLevel(level = logging.DEBUG)
fhandler = logging.FileHandler("spider.log")
chandler = logging.StreamHandler()
#console.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
fhandler.setFormatter(formatter)
chandler.setFormatter(formatter)

logger.addHandler(chandler)
logger.addHandler(fhandler)

class MyCrawl:

    def __init__(self):
        self.proxy = None
        self.ua = UserAgent()
        self.headers = self.get_header()

    def get_proxy(self):
        r = requests.get('http://localhost:5000/get')
        proxy = r.text
        return proxy

    def get_header(self):
        headers = {'User-Agent': self.ua.random}
        return headers

    def get_count_proxys(self):
        r = requests.get('http://localhost:5000/count')
        proxys = r.text
        return proxys

    def crawl(self, url, use_proxy=False):
        '''
        if use_proxy:
            self.proxy = self.get_proxy()
            proxies = {'http': self.proxy}
            r = requests.get(url, proxies=proxies, headers=self.headers, timeout=6)
            return r
        else:
            r = requests.get(url, headers=self.headers, timeout=6)
            return r
        '''
        # try 3 times
        r = None
        for i in range(3):
            try:
                if use_proxy:
                    self.proxy = self.get_proxy()
                    proxies = {'http': self.proxy}
                    r = requests.get(url, proxies=proxies, headers=self.headers, timeout=5)
                else:
                    r = requests.get(url, headers=self.headers, timeout=5)
                if r and r.status_code == 200: break
            except Exception as e: #(ProxyError, Timeout, ConnectionError, ChunkedEncodingError) as e:
                logger.error('==={url}===try {i} times==={type}==={e}==='.format(url = url, i=i, type=type(e), e=str(e)))
                # change header
                self.headers = self.get_header()

        return r


class Job:
    def __init__(self):
        self.jobName = None
        self.companyName = None
        self.salary = None
        self.city = None
        self.workingExp = None
        self.eduLevel = None
        self.companyType = None
        self.emplType = None
        self.jobType = None
        self.jobLight = None


class Searchjob:
    def __init__(self, keyword, city, limit=-1):
        self.keyword = keyword
        self.city = city
        self.limit = limit
        self.orginUrl = "https://fe-api.zhaopin.com/c/i/sou?start={start}&pageSize=100&cityId=" + \
                        "{city}" + \
                        "&workExperience=-1&education=-1&companyType=-1&employmentType=-1&jobWelfareTag=-1&kw=" + \
                        "{keyword}" + \
                        "&kt=3"
        self.urlRegex = re.compile('positionURL":"(.*?)",')
        self.crawler = None
        self.lines = []
        # self.fileWriter = Writer(keyword+'_'+city+'_')

    def crawl_data(self):
        try:
            logger.info(self.city + ',' + self.keyword)
            self.crawler = MyCrawl()
            indexHtml = self.crawler.crawl(self.orginUrl.format(city=urllib.parse.quote(self.city),
                                                                keyword=urllib.parse.quote(self.keyword),
                                                                start=0))
            pageCount = 0
            if indexHtml:
                pageCount = self.__get_max_count(indexHtml.text)

            for i in range(pageCount + 1):
                indexHtml = self.crawler.crawl(self.orginUrl.format(city=urllib.parse.quote(self.city),
                                                                    keyword=urllib.parse.quote(self.keyword),
                                                                    start=i * 100))
                # print (indexHtml)
                if indexHtml:  # .status_code == 200:
                    self.__job_process(indexHtml.text)

            if len(self.lines) > 0:
                writer.append(self.lines)
        except Exception as e:
            logger.error(self.keyword + self.city + str(e))

        logger.info(self.keyword + self.city + 'task end at '+ str(time.time()))

    def __get_max_count(self, indexPag):
        d = eval(indexPag)
        return min(60, math.floor(d['data']['numFound'] / 100))

    def __job_process(self, indexPag):
        # results = self.urlRegex.findall(indexPag, re.S)
        d = eval(indexPag)
        for job in eval(indexPag)['data']['results']:
            # self.fileWriter.addData(str(job))
            self.__add_line(str(job))
            self.__job_detail(job['positionURL'])

    def __job_detail(self, url):
        # print ('=========' + url)
        html = self.crawler.crawl(url)
        if html:  # .status_code == 200:
            html = etree.HTML(html.text)
            if 'xiaoyuan' in url:
                jobDetail = html.xpath("//div[@class='cJob_Detail f14']//text()")
            else:
                jobDetail = html.xpath("//div[@class='responsibility pos-common']//text()")
            # self.fileWriter.addData(url + ':' + str(content))
            self.__add_line(url + ':' + str(jobDetail))

    def __add_line(self, line):
        self.lines.append(line + '\n')
        if len(self.lines) > 500:
            writer.append(self.lines)
            self.lines = []


class Writer:
    def __init__(self, filename):
        self.dataList = []
        self.filename = filename

    def addData(self, line):
        self.dataList.append(str(line) + '\n')
        if len(self.dataList) > 200:
            self.flushData()

    def flushData(self):
        f = open(self.filename + str(time.time()), 'w')
        f.writelines(self.dataList)
        self.dataList = []
        f.close()


class writer():

    dataList = []

    @classmethod
    def append(cls, lines):
        cond.acquire()
        writer.dataList.extend(lines)
        if len(writer.dataList) > 10000:
            writer.flush()

        cond.notify_all()
        cond.release()

    @classmethod
    def flush(cls):
        f = open(str(time.time()), 'w')
        f.writelines(writer.dataList)
        f.close()
        writer.dataList = []


cond = threading.Condition(lock=threading.Lock())

if __name__ == '__main__':
    keywords = ['大数据', 'python', 'java', '软件开发', '算法工程', '人工智能', '区块链', '云计算']
    cities = ['北京', '上海', '广州', '成都', '武汉', '青岛', '深圳', '天津', '杭州', '济南', '苏州', '西安', '大连']


    def getdata(filter):
        s = Searchjob(keyword=filter[0], city=filter[1])
        s.crawl_data()

    #getdata(("大数据", "北京"))


    with ThreadPoolExecutor(20) as executor:
        executor.map(getdata, [(kw, city) for kw in keywords for city in cities])

    writer.flush()

    logger.info("Finish.")
