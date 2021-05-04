from abc import *

class CrawlerBase(metaclass=ABCMeta):

    def __init__(self):
        self.news_data = collections.namedtuple('news_data', ('id', 'url', 'platform', 'domain', 'channel', 'date', 'time', 'title', 'content'))
        self.bNext = True

    @abstractmethod
    def get_data(self):
        pass

    @abstractmethod
    def get_date(self):
        pass

    @abstractmethod
    def get_meta_info(self):
        pass

    @abstractmethod
    def get_content(self):
        pass