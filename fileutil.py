import os
from log import Logger


CUR_PATH = os.path.dirname(os.path.realpath(__file__))  # history是存放日志的路径
HISTORY_PATH = os.path.join(CUR_PATH, 'history')
SITE_PATH = os.path.join(CUR_PATH, 'SITE')


class FileUtil(object):

    @classmethod
    def read_history_file(cls,fileName='', encoding='utf-8'):
        data = None
        fileDir = os.path.join(HISTORY_PATH, fileName)
        with open(fileDir, encoding=encoding, mode='r+') as file:
            data = file.read()

        return data

    @classmethod
    def update_history_file(cls, fileName='', data='', encoding='utf-8'):
        # logger = Logger(file='history.log')
        fileDir = os.path.join(HISTORY_PATH, fileName)
        with open(fileDir, encoding=encoding, mode= 'w+') as file:
            file.write(data)
        return data

    @classmethod
    def read_site_file(cls,fileName='', encoding='utf-8'):
        fileDir = os.path.join(SITE_PATH, fileName)
        lines = None
        with open(fileDir, encoding=encoding, mode='r+') as file:
            lines = file.readlines()
        return lines