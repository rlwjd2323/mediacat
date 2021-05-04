"""
@author : 윤기정
@date : 2021-01-29
@brief : object relation mapper
@version :0.1
"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


# platform 
class PlatForm(Base):
    __tablename__ = 'TB_INFO_PLATFORM'

    SEQ = Column(Integer, primary_key=True)
    TC_PLATFORM = Column(String)
    TC_DOC_TYPE = Column(Integer)
    TC_USEYN = Column(String)
    TC_REGDATE = Column(String)

    def __init__(self 
                , SEQ
                , TC_PLATFORM
                , TC_DOC_TYPE
                , TC_USEYN
                , TC_REGDATE
                ):
        self.SEQ = SEQ
        self.TC_PLATFORM = TC_PLATFORM
        self.TC_DOC_TYPE = TC_DOC_TYPE
        self.TC_USEYN = TC_USEYN
        self.TC_REGDATE = TC_REGDATE


# domain 
class Domain(Base):
    __tablename__ = 'TB_INFO_DOMAIN'

    SEQ = Column(Integer, primary_key=True)
    TC_DOMAIN = Column(String)
    TC_USEYN = Column(String)
    TC_REGDATE = Column(String)

    def __init__(self 
                , SEQ
                , TC_DOMAIN
                , TC_USEYN 
                , TC_REGDATE
                ):
        self.SEQ = SEQ
        self.TC_DOMAIN = TC_DOMAIN
        self.TC_USEYN = TC_USEYN
        self.TC_REGDATE = TC_REGDATE


# url  
class Url(Base):
    __tablename__ = 'TB_INFO_URL'

    SEQ = Column(Integer, primary_key=True)
    TC_URL = Column(String)
    TC_DOMAIN_SEQ = Column(Integer)
    TC_PLATFORM_SEQ = Column(Integer)
    TC_USEYN = Column(String)
    TC_REGDATE = Column(String)

    def __init__(self
                 , SEQ
                 , TC_URL 
                 , TC_DOMAIN_SEQ 
                 , TC_PLATFORM_SEQ
                 , TC_USEYN
                 , TC_REGDATE
                 ):
        self.SEQ = SEQ
        self.TC_URL = TC_URL
        self.TC_DOMAIN_SEQ = TC_DOMAIN_SEQ
        self.TC_PLATFORM_SEQ = TC_PLATFORM_SEQ
        self.TC_USEYN = TC_USEYN
        self.TC_REGDATE = TC_REGDATE


						
# meta data 
class Meta(Base):
    __tablename__ = 'TB_INFO_DATA'

    TC_ID = Column(Integer, primary_key=True)
    TC_DATA_URL = Column(String)
    TC_DATE = Column(Integer)
    TC_TIME = Column(Integer)
    TC_PLATFORM = Column(String)
    TC_DOMAIN = Column(String)
    TC_CHANNEL = Column(String)
    TC_DOC_TYPE = Column(Integer)
    TC_TITLE = Column(String)
    TC_FILE_PATH = Column(String)
    TC_FILE_NAME = Column(String)
    TC_FILE_EXT = Column(String)
    TC_START_TIME = Column(String)
    TC_END_TIME = Column(String)
    TC_DURATION = Column(String)
    TC_PREPROCESS_YN = Column(Integer)

    def __init__(self
                , TC_ID
                , TC_DATA_URL
                , TC_DATE
                , TC_TIME
                , TC_PLATFORM
                , TC_DOMAIN
                , TC_CHANNEL
                , TC_DOC_TYPE
                , TC_TITLE
                , TC_FILE_PATH
                , TC_FILE_NAME
                , TC_FILE_EXT
                , TC_PREPROCESS_YN
                ):
        self.TC_ID = TC_ID
        self.TC_DATA_URL = TC_DATA_URL
        self.TC_DATE = TC_DATE
        self.TC_TIME = TC_TIME
        self.TC_PLATFORM = TC_PLATFORM
        self.TC_DOMAIN = TC_DOMAIN
        self.TC_CHANNEL = TC_CHANNEL
        self.TC_DOC_TYPE = TC_DOC_TYPE
        self.TC_TITLE = TC_TITLE
        self.TC_FILE_PATH = TC_FILE_PATH
        self.TC_FILE_NAME = TC_FILE_NAME
        self.TC_FILE_EXT = TC_FILE_EXT
        self.TC_PREPROCESS_YN = TC_PREPROCESS_YN

