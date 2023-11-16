import logging
import unittest
import warnings
from requesthandler import RequestsHandler
class MyTestCase(unittest.TestCase):

    def setUp(self):
        #使用unittest框架时， 解决错误 ResourceWarning: Enable tracemalloc to get the object allocation traceback
        warnings.simplefilter('ignore', ResourceWarning)
    def test_something(self):
        requests_handler = RequestsHandler()
        #text = requests_handler.get_single(url='https://www.guancha.cn/XiYaZhou/2023_10_22_712961.shtml')

        #text = requests_handler.get_single(url='http://asean.gxnews.com.cn/',encoding='gb2312')
        #text = requests_handler.get_single(url='https://world.huanqiu.com/')
        text = requests_handler.get_single(url='https://mil.ifeng.com/')
        print(text)

        urls = ['https://www.guancha.cn/internation?s=dhguoji',
                'https://world.huanqiu.com/',
                'https://www.guancha.cn/military-affairs?s=dhjunshi']
        requests_handler.get_threads(urls)

if __name__ == '__main__':
    logging.debug(1234)
    unittest.main()
