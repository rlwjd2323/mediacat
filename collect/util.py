import re, datetime, os
import urllib.parse
import logging.handlers

# 로그
def logger():

    log = logging.getLogger('log')

    if len(log.handlers) > 0:
        return log  # Logger already exists

    log.setLevel(logging.DEBUG)

    formatter = logging.Formatter('%(message)s')

    # 콘솔 출력을 지정합니다
    streamHandler = logging.StreamHandler()
    streamHandler.setFormatter(formatter)

    # # 파일 출력을 지정합니다.
    # log_dir = './logs'
    # log_file = './logs'+'/'+'logs.log'
    # if not os.path.exists(log_dir):
    #     os.makedirs(log_dir)

    log.addHandler(streamHandler)

    return log

# 날짜를 24시간 형식으로 변경
def convert24(tt:'tt:mm:ss') -> str: 

    if len(tt.split(':')[0]) == 1:
        tt = '0'+tt
        
    strftime = datetime.datetime.today().strftime('%p')

    if strftime == 'AM' and tt[:2] == '12': 
        return '00' + tt[2:len(tt)] 
   
    elif strftime == 'AM': 
        return tt 
      
    elif strftime == 'PM' and tt[:2] == '12': 
        return tt
          
    else: 
        return str(int(tt[:2]) + 12) + tt[2:8] 


# 일자별 디렉토리 이름 생성
def today_dir_name()->str:
    return datetime.datetime.today().strftime('%Y%m%d')


# 일자별 디렉토리 생성
def create_folder(path):
    try:
        if not os.path.exists(path):
            os.makedirs(path)
    except OSError:
        print ('Error: Creating directory.')

# 특수문자 제거
def remove_special_char(char) -> str:
    return re.sub('[-=+,#/\?:^$.@*\"※~&%ㆍ!』\\‘|\(\)\[\]\<\>`\'…》△▲\"\'◆■●■◇]', '', char)