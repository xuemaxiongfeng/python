#coding:utf-8
import logging
import unittest
from log import Logger
import warnings
class MyTestCase(unittest.TestCase):

    def setUp(self):
        #使用unittest框架时， 解决错误 ResourceWarning: Enable tracemalloc to get the object allocation traceback
        warnings.simplefilter('ignore', ResourceWarning)

    def test_something(self):
        logger = Logger(file='logtest.log')
        #logging.disable(logging.DEBUG)     #禁用相应级别的日志
        logger.debug('This message should go to the log file')
        logger.info('So should this')
        logger.warning('And this, too')
        logger.error('And non-ASCII stuff, too, like resund and Malmö')
        logger.critical('So should critical')



if __name__ == '__main__':
    unittest.main()
