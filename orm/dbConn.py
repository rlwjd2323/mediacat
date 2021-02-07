from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from util import logger
from .model import PlatForm, Domain, Url, Meta

class DBConn:
    def __init__(self, id, pw, host, port, db):
        connection = 'mysql+pymysql://{}:{}@{}:{}/{}'.format(id, pw, host, port, db)
        logger().info('==============================================================================================>'+connection)
        try:            
            engine = create_engine(connection, echo=True)
            engine.execute("select 1")
            self.Session = sessionmaker(bind=engine)
            self.set_session()
            logger().info('=========================================================================================>DB connection success!')
        except Exception as e:
            logger().error('=========================================================================================>DB connection fail!')
            logger().error(e)

    def set_session(self):
        self.session = self.Session()

    def get_url(self):
        session = self.session
        return \
        [
            row for row in session.query(
                Url.TC_URL
                , PlatForm.TC_PLATFORM
                , PlatForm.TC_DOC_TYPE
                , Domain.TC_DOMAIN 
                ) 
                .filter(Url.TC_PLATFORM_SEQ == PlatForm.SEQ) 
                .filter(Url.TC_DOMAIN_SEQ == Domain.SEQ) 
                .filter(Url.TC_USEYN == 'Y') 
                .filter(PlatForm.TC_USEYN == 'Y') 
                .filter(Domain.TC_USEYN == 'Y') 
        ]

    def regist_meta(self, meta):
        session = self.session
        try:
            session.add_all(meta)
            session.commit()
            logger().info('regist meta data success!')
        except Exception as e:
            logger().error('regist meta data success!')
            logger().error(e)

