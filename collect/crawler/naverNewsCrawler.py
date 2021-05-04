from bs4 import BeautifulSoup
import collections, requests, re, datetime, time, os
from util import convert24, remove_special_char, logger
from .crawlerBase import CrawlerBase


class NaverNewsCrawler(CrawlerBase):
    def __init__(self):
        self.news_data = collections.namedtuple('news_data', ('id', 'url', 'platform', 'doctype', 'domain', 'channel', 'date', 'time', 'title', 'content'))
        self.bNext = True
        
    # url의 html 가져오기
    def get_data(self, _url, platform, doctype, domain):
        self.url = _url

        logger().info(f'news url : {self.url}')
        logger().info('-'*50)
        id = self.url[37:len(self.url)+1]
        try:
            response = requests.get(_url, headers={"User-Agent":"Mozilla/5.0"})
            self.soup = BeautifulSoup(response.text, 'html.parser', from_encoding='utf-8')
            if len(self.soup) > 0: 
                self.get_date()
            if self.bNext:
                news_data = self.news_data(*(id, self.url, platform, doctype, domain, self.channel, self.date, self.time, self.title, self.contents))
                return news_data
        except Exception as e:
            self.soup = []
        
    # 날짜 및 시간 파싱
    def get_date(self):    
        try:
            res = self.soup.find_all("span", class_="t11")[0].find_all(text=True)[0]
            self.date = res[0:10].replace(".","-")
            self.time = convert24(res[15:20]+":00")
            if len(self.date) > 0 and len(self.time) > 0:  
                logger().info(f'news date : {self.date}')
                logger().info('-'*50)
                logger().info(f'news time : {self.time}')
                logger().info('-'*50)
                self.get_meta_info()
            else:
                self.bNext = False
        except:
            self.bNext = False

    # 신문사, 뉴스 분야, 제목 파싱
    def get_meta_info(self):
        try:
            for meta in self.soup.find_all('meta'):
                if meta.attrs.get('property', '') == 'me2:category1':
                    self.channel = meta.attrs.get('content', '')
                    logger().info(f'news channel : {self.channel}')
                    logger().info('-'*50)
                elif meta.attrs.get('property', '') == 'og:title':
                    self.title = remove_special_char(meta.attrs.get('content', ''))
                    logger().info(f'news title : {self.title}')
                    logger().info('-'*50)
            if len(self.channel) > 0 and len(self.title) > 0:  
                self.get_content()
            else:
                self.bNext = False
        except:
            self.bNext = False


        
    # 뉴스 내용 파싱
    def get_content(self):

        try:                
            textBS = self.soup.find_all("div", class_="_article_body_contents")  
            textBS = textBS[0]
            text = str(textBS)        
            script = textBS.find_all("script")
            if len(script)>0: text = text.replace(str(script[0]), "")
            text = re.sub('<.+?>', '', text, 0)
            cont = ""
            textLs = text.split("\n")[5].split("다.")
            for i, sntc in enumerate(textLs):
                if i < len(textLs)-2 and sntc != '':
                    sntc = sntc.strip()
                    cont += "%s다.%s" % (sntc,"\n")
            if len(cont) > 200:
                self.contents = remove_special_char(cont)
                logger().info(f'news contents : {self.contents}')
                logger().info('-'*50)
            else:
                self.bNext = False
        except:
                self.bNext = False


