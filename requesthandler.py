# -*- coding:utf-8 -*-
import logging

import requests
from concurrent.futures import  ThreadPoolExecutor
from log import Logger

class RequestsHandler(object):
    def __init__(self, timeout=60, iRetryNum = 3):
        self.header = {
                'User-Agent':'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.76 Mobile Safari/537.36',
            }
        self.timeout = timeout      #超时设定，默认60s，可以动态设定
        self.iRetryNum = iRetryNum  #http连接异常的场合，重新连接的次数，默认为3，可以动态设定
        self.responses = {}         #

    def get_single(self, url='', encoding='utf-8', iLoop=1):
        response = None
        status_code = None
        logger = Logger(file='httpRequests.log')
        # 如果达到最大重连次数，连接后提交结束
        if iLoop == self.iRetryNum:
            try:
                response = requests.get(url=url, headers=self.header, timeout=self.timeout)
                status_code = response.status_code
                response.raise_for_status() #如果发送失败请求(非200响应)，我们可以通过Response.raise_for_status()抛出异常
                logger.debug(url)
                logger.debug(response.apparent_encoding)  # 网页使用的编码方式
                response.encoding = encoding
                text = response.text

                #text = response.content
                #text = text.decode(response.apparent_encoding)        #字符串 转换成 Unicode 编码
                #text = text.encode(encoding)                            #将 Unicode 编码格式字符串 转换成utf-8
                return text
            except Exception as err:
                logger.error("url=" + url + "     " + "status_code=" + str(status_code) + str(err))
                return None
            finally:
                del logger
        # 未达到最大连接数，如果出现异常，则重新连接尝试
        else:
            try:
                response = requests.get(url=url, headers=self.header, timeout=self.timeout)
                response.raise_for_status()     #如果发送失败请求(非200响应)，我们可以通过Response.raise_for_status()抛出异常
                response.encoding = response.apparent_encoding      #在不知道编码格式的前提下使用该方式
                logger.debug(url)
                logger.debug(response.apparent_encoding)  # 网页使用的编码方式
                response.encoding = response.apparent_encoding
                response.encoding = encoding
                text = response.text
                # text = response.content
                # text = text.decode(response.apparent_encoding)        #字符串 转换成 Unicode 编码
                # text = text.encode(encoding)                            #将 Unicode 编码格式字符串 转换成utf-8
                return text
            except Exception as err:
                logger.error("url=" + url + "     " + "status_code=" + str(status_code) + str(err))
                iLoop += 1
                self.get_single(url=url, iLoop=iLoop)
                return None
            finally:
                del logger


    def get_threads(self, urls, threadsNum=5):
        logger = Logger(file='httpRequests.log')
        reslts = None
        try:
            # 线程池并发执行，iThreadNum为并发数
            with ThreadPoolExecutor(threadsNum) as executor:
                reslts = executor.map(self.get_single, urls)
        except Exception as err:
            logger.error('ThreadPoolExecutor error: ' + str(err))
        finally:
            del logger
            return reslts