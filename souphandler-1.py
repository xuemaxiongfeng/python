# -*- coding:utf-8 -*-

import os
from log import Logger

#日志文件夹
CUR_PATH = os.path.dirname(os.path.realpath(__file__))  # log_path是存放日志的路径
SITE_PATH = os.path.join(CUR_PATH, 'site')

class SoupHandler(object):

    def __init__(self,fileName=''):
        self.file = os.path.join(SITE_PATH,fileName)

    def index_soup(self):
        logger = Logger(file='beautifulsoup.log')

        netAddress = []
        encodings = []
        sites = []
        with open(self.file,"r",encoding='UTF-8') as file:
            for line in file.readlines():
                items = line.split()
                netAddress.append(items[0])
                encodings.append(items[1])
                sites.append(items[2])



