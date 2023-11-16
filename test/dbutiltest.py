# -*- coding:utf-8 -*-

import unittest
from dbutil import DBUtil
import warnings
class MyTestCase(unittest.TestCase):
    def setUp(self):
        # 使用unittest框架时， 解决错误 ResourceWarning: Enable tracemalloc to get the object allocation traceback
        warnings.simplefilter('ignore', ResourceWarning)
    def test_something(self):

        sql = 'insert into international_news(time,sitename,title,address,countryarea,mainbody,cls,clskeyword,contentkeyword,content) values(%s,%s,%s,%s,%s,%s,%s,%s,%s);'

        #"time",   "2005-11-5 13:21:25",
        params = [("2023-01-14","环球网","2","3","4","5","6","7","8","9"),
                  ("2023-01-15","环球网","2","3","4","5","6","7","8","9"),
                  ("2023-01-16","环球网","2","3","4","5","6","7","8","9")]

        DBUtil.uids_many(sql, params)
        #DBUtil.get_conn()

if __name__ == '__main__':
    unittest.main()
