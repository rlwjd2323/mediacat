#!bin/bash

# 파일 저장 경로
export path='/data/NewsData/'
export ext='txt'

#db 접속 정보
export id='solugate'
export pw='!epdlxj23'
export host='192.168.0.238'
export port='3306'
export db='NewsCrawler'

# 크롤러 실행
/mnt/d/workpython/anaconda3/envs/NewsCrawler/bin/python /mnt/d/workpython/workspace/NewsCrawler/runCrawler.py