# -*- coding:utf-8 -*-

import logging
import os
import colorlog
from logging.handlers import RotatingFileHandler

#日志文件夹
CUR_PATH = os.path.dirname(os.path.realpath(__file__))  # log_path是存放日志的路径
LOGS_PATH = os.path.join(CUR_PATH, 'logs')
#警告日志文件
WARN_LOG_FILE = 'warn.log'

#定义不同日志等级颜色
log_colors_config = {
    "DEBUG" : 'bold_cyan',
    "INFO" : 'bold_green',
    "WARNING" : 'bold_yellow',
    "ERROR" : 'bold_red',
    "CRITICAL" : 'red',
}

class Logger(logging.Logger):
    def __init__(self,name=None,level=logging.DEBUG,file=None,encoding='utf-8'):
        super().__init__(name)
        self.encoding = encoding
        self.level = level
        self.file = file

        if self.file != None:
            # Create file dir
            if not os.path.exists(LOGS_PATH):
                os.mkdir(LOGS_PATH)  # 创建文件夹
            self.file = os.path.join(LOGS_PATH, self.file)

        fileFormatter = '%(asctime)s|%(levelname)-8s     %(filename)-15s%(module)-15s%(funcName)-20s%(lineno)5d    %(message)s'

        #针对所需要的日志信息，手动调整颜色
        self.formatter = colorlog.ColoredFormatter(
            '%(log_color)s%(asctime)s%(reset)s|%(message_log_color)s%(levelname)-8s%(reset)5s'
            '%(log_color)s[%(filename)-15s:%(reset)s%(log_color)s%(module)s%(reset)-15s:%(log_color)s%(funcName)s%(reset)-15s:%(log_color)s%(lineno)-5d]'
            '%(reset)s- %(white)s%(message)s',
            reset = True,
            log_colors = log_colors_config,
            secondary_log_colors = {
                'message' : {
                    "DEBUG" : 'blue',
                    "INFO" : 'blue',
                    "WARNING" : 'blue',
                    "ERROR" : 'red',
                    "CRITICAL" : 'bold_red',
                }
            },
            style = '%'
        )

        #控制台   debug或指定
        colSH = colorlog.StreamHandler()
        colSH.setLevel(self.level)
        colSH.setFormatter(self.formatter)
        self.addHandler(colSH)
        self.setLevel(self.level)

        #默认文件    只是WARN     程序的警告信息会聚集记录到这里
        warnHandler = logging.handlers.RotatingFileHandler(filename=os.path.join(LOGS_PATH, WARN_LOG_FILE), maxBytes=1024 * 1024 * 50, backupCount=2, mode='a', encoding=self.encoding)
        warnHandler.setFormatter(logging.Formatter(fileFormatter))
        filter = logging.Filter()
        filter.filter = lambda record:record.levelno == logging.WARNING #设置过滤器
        warnHandler.addFilter(filter)
        warnHandler.setLevel(logging.WARNING)
        self.addHandler(warnHandler)


        #指定文件    Error  critical
        if self.file != None:
            rotatingFileHandler = logging.handlers.RotatingFileHandler(filename=self.file, maxBytes=1024*1024*50, backupCount=2, mode='a',encoding=self.encoding)
            rotatingFileHandler.setFormatter(logging.Formatter(fileFormatter))
            rotatingFileHandler.setLevel(logging.ERROR)
            self.addHandler(rotatingFileHandler)




