import unittest
import warnings
import ast

from fileutil import FileUtil
from requesthandler import RequestsHandler
from souphandler import SoupHandler
from log import Logger

class MyTestCase(unittest.TestCase):
    def test_something(self):
        # 使用unittest框架时， 解决错误 ResourceWarning: Enable tracemalloc to get the object allocation traceback
        warnings.simplefilter('ignore', ResourceWarning)

    def test_something(self):
        try:

            lines = FileUtil.read_site_file(fileName='government_units.site')
            #print(lines)
            guonei = {}
            guoji = {}
            caijing = {}
            keji = {}
            junshi = {}

            for line in lines:
                line = line.replace('\n','')
                line = line.split('=')
                num = int(line[1])
                match num:
                    case 1: guonei[line[0]] = line[2]
                    case 2: guoji[line[0]] = line[2]
                    case 3: caijing[line[0]] = line[2]
                    case 4: keji[line[0]] = line[2]
                    case 5: junshi[line[0]] = line[2]
            hrefs = {}
        except Exception as err:
            print('erroooooooooooooooor:' +str(err))


if __name__ == '__main__':
    unittest.main()
