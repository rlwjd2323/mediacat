"""
@author : 윤기정
@date : 2021-02-01
@brief : 데이터 수집
@version :0.1
"""
from bs4 import BeautifulSoup
from multiprocessing import Pool

import requests, re, datetime, time, os
import collections

from dbConn import DBConn, Meta
from crawler import NaverNewsCrawler
from util import create_folder, today_dir_name, convert24, remove_special_char, logger



path = os.environ['path']+today_dir_name()
ext = os.environ['ext']



# 최신 뉴스 url 수집
def get_current_news_url(_url):
    news_ls = []
    try:
        response = requests.get(_url, headers={'User-Agent':'Mozilla/5.0'})
        source = BeautifulSoup(response.text, 'html.parser', from_encoding='utf-8')
        ls = source.find_all('ul', class_='type06_headline')[0].find_all('a', class_='nclicks(fls.list)')
        if len(ls)>0:
            news_ls = [href.attrs['href'] for href in ls]
        return news_ls
    except Exception as e:
        print(e)


# 본문 txt파일로 저장
def resgist_news_data(data):   

    meta = None    
    os.path.exists(path+'ws.'+ext)
    try:
        fileInfo = path+'/'+data.id+'.'+ext
        if not os.path.exists(fileInfo):
            f = open(fileInfo, 'w', encoding='utf-8')
            f.write(remove_special_char(data.content))
            f.close()
            logger().info('Data To Txt sucssess !')
            meta = Meta(
                    TC_ID = data.id
                    , TC_DATA_URL = data.url
                    , TC_DATE = data.date
                    , TC_TIME = convert24(data.time)
                    , TC_PLATFORM = data.platform
                    , TC_DOC_TYPE = data.doctype
                    , TC_DOMAIN = data.domain
                    , TC_CHANNEL = data.channel
                    , TC_TITLE = remove_special_char(data.title)
                    , TC_FILE_NAME = data.id
                    , TC_FILE_PATH = path
                    , TC_FILE_EXT = ext
                    , TC_PREPROCESS_YN = 0
                )
            return meta
    except:
        logger().info('Data To Txt fail !')



# 서브 프로세스
def do_work(param):
    source_info = collections.namedtuple('info', ('url', 'platform', 'doctype', 'domain'))
    info = source_info(*param)
    print(info.url)
    result = []
    news_ls = list(set(get_current_news_url(info.url)))
    
    if len(news_ls)>0:
        for _url in news_ls:
            logger().info(_url)
            result_data = NaverNewsCrawler().get_data(_url, info.platform, info.doctype, info.domain)
            if result_data is not None:
                meta = resgist_news_data(result_data)
                if meta is not None:
                    result.append(meta)
            time.sleep(1)
    return result

# 메인 프로세스
def run_main(source_ls):
    create_folder(path)
    pool = Pool(len(source_ls))
    results = pool.map(do_work, source_ls)
    pool.close()
    pool.join()
    # 메타데이터 DB 저장
    for result in results:
        dbconn.regist_meta(result)
        time.sleep(0.1)

if __name__=='__main__':
    # DB 연동
    dbconn = DBConn(os.environ['id'], os.environ['pw'], os.environ['host'], os.environ['port'], os.environ['db'])
    # while True:
    dbconn.set_session()
    # 탐색할 URL 
    source_ls = dbconn.get_url()
    # 프로세스 실행
    run_main(source_ls)





