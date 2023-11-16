# -*- coding:utf-8 -*-

import os
from log import Logger
from bs4 import BeautifulSoup
from urllib.parse import quote,unquote
import re

class SoupHandler(object):

    #通过class获取文章
    @classmethod
    def article_class_soup(cls,  htmlDoc='', tagName='', className='', parser='html.parser'):
        soup = None
        rlst = None
        logger = Logger(file='soup_html_doc.log')
        try:
            soup = BeautifulSoup(htmlDoc, parser)
            soup = BeautifulSoup(htmlDoc, parser)
            rlst = soup.find(name=tagName, attrs={'class': className})
        except Exception as err:
            logger.error('获取文章失败：tagName=' + tagName + ', className=' + className + ', ' + str(err))
            logger.error('获取文章失败 htmlDoc：' + str(htmlDoc))
        finally:
            del logger
            return rlst

    # 通过id获取文章
    @classmethod
    def article_id_soup(cls, htmlDoc='', tagName='', id='', parser='html.parser'):
        soup = None
        rlst = None
        logger = Logger(file='soup_html_doc.log')
        try:
            soup = BeautifulSoup(htmlDoc, parser)
            rlst = soup.find(name=tagName, attrs={'id':id})
        except Exception as err:
            logger.error('获取文章失败：tagName=' + tagName + ', id=' + id + ', ' + str(err))
            logger.error('获取文章失败 htmlDoc：' + str(htmlDoc))
        finally:
            del logger
            return rlst

    #观察者网  所有
    @classmethod
    def index_guancha_soup(cls, htmlDoc='', parser='html.parser'):
        soup = None
        rlst = {}
        logger = Logger(file='soup_html_doc.log')
        try:
            soup = BeautifulSoup(htmlDoc, parser)
            h4s = soup.findAll("h4")
            for href in h4s:
                #logger.debug(href.a.string)
                #logger.debug('https://www.guancha.cn' + href.a['href'])
                try:
                    rlst['https://www.guancha.cn' + href.a['href']] = href.a.string
                except Exception as err:
                    pass

        except Exception as err:
            logger.error('观察者首页解析错误：' + str(err))
        finally:
            del logger
            return rlst

    #环球网   index
    @classmethod
    def index_huanqiu_soup(cls, htmlDoc='', parser='html.parser'):
        soup = None
        rlst = {}
        logger = Logger(file='soup_html_doc.log')
        try:
            soup = BeautifulSoup(htmlDoc, parser)
            #divs = soup.findAll("div", attrs={"class":"feed-item feed-item-a"})
            hrefs = soup.findAll("a")#, attrs={"class":"cs-link"}
            for href in hrefs:
                if href.string == None:
                    continue
                if len(href.string) < 10:
                    continue
                if 'article' not in href['href']:
                    continue
                if len(href['href']) < 15:
                    continue
                if 'health' in href['href']:
                    continue
                if 'lx.' in href['href']:
                    continue
                if 'go.' in href['href']:
                    continue
                if 'society' in href['href']:
                    continue
                if 'city' in href['href']:
                    continue
                if 'sports' in href['href']:
                    continue
                if 'auto' in href['href']:
                    continue
                if 'quality' in href['href']:
                    continue
                if 'capital' in href['href']:
                    continue
                if 'fashion' in href['href']:
                    continue
                if 'ent' in href['href']:
                    continue
                if 'luxury' in href['href']:
                    continue
                if 'hope' in href['href']:
                    continue
                try:
                    if 'https:' not in href['href']:
                        rlst['https:' + href['href']] = href.string
                        # logger.debug('https:' + href['href'] + ':' + href.string)
                    else:
                        rlst[href['href']] = href.string
                        # logger.debug(href['href'] + ':' + href.string)
                except Exception as err:
                    pass

        except Exception as err:
            logger.error('环球网首页解析错误：' + str(err))
        finally:
            del logger
            return rlst

    #凤凰网   index
    @classmethod
    def index_ifeng_soup(cls, htmlDoc='', parser='html.parser'):
        soup = None
        rlst = {}
        logger = Logger(file='soup_html_doc.log')
        try:
            soup = BeautifulSoup(htmlDoc, parser)
            hrefs = soup.findAll("a")
            for href in hrefs:
                try:
                    if href.string == None:
                        continue
                    if len(href.string) < 13:
                        continue
                    if len(href['href']) < 15:
                        continue
                    if '//news.' in href['href']:
                        rlst[href['href']] = href.string
                        continue
                    if '//v.' in href['href']:
                        rlst[href['href']] = href.string
                        continue
                    if '//phtv.' in href['href']:
                        rlst[href['href']] = href.string
                        continue
                    if '//na.' in href['href']:
                        rlst[href['href']] = href.string
                        continue
                    if '//tech.' in href['href']:
                        rlst[href['href']] = href.string
                        continue
                    if '//finance.' in href['href']:
                        rlst[href['href']] = href.string
                        continue
                except Exception as err:
                    pass

                '''    
                if 'mall.' in href['href']:
                    continue
                if 'travel.' in href['href']:
                    continue
                if 'auto.' in href['href']:
                    continue
                if 'sports.' in href['href']:
                    continue
                if 'ent.' in href['href']:
                    continue
                if 'foodnwine.' in href['href']:
                    continue
                if 'fashion.' in href['href']:
                    continue
                if 'pingce.' in href['href']:
                    continue
                if 'house.' in href['href']:
                    continue
                if 'culture.' in href['href']:
                    continue
                if 'health.' in href['href']:
                    continue
                if 'guoxue.' in href['href']:
                    continue
                if 'fo.' in href['href']:
                    continue
                if 'home.' in href['href']:
                    continue
                if 'yc.' in href['href']:
                    continue
                if 'jiu.' in href['href']:
                    continue
                if 'fengcx.' in href['href']:
                    continue
                if 'ds.' in href['href']:
                    continue
                if 'gongyi.' in href['href']:
                    continue
                '''
                #logger.warning(href)
                # logger.debug('https://www.guancha.cn' + href.a['href'])


        except Exception as err:
            logger.error('凤凰网首页解析错误：' + str(err))
        finally:
            del logger
            return rlst


    #新华网   频道首页
    @classmethod
    def index_news_soup(cls, htmlDoc='', parser='html.parser'):
        soup = None
        rlst = {}
        logger = Logger(file='soup_html_doc.log')
        try:
            soup = BeautifulSoup(htmlDoc, parser)
            hrefs = soup.findAll("a")
            for href in hrefs:
                try:
                    if href.string==None or len(href.string.strip())<10:
                        #logger.warning(href)
                        continue
                    #logger.debug(href)
                    rlst[href['href']] = href.string.strip()
                except Exception as err:
                    pass

        except Exception as err:
            logger.error('网页首页解析错误：' + str(err))
        finally:
            del logger
            return rlst

    #人民网   频道首页
    @classmethod
    def index_people_soup(cls, htmlDoc='', parser='html.parser'):
        soup = None
        rlst = {}
        logger = Logger(file='soup_html_doc.log')
        try:
            soup = BeautifulSoup(htmlDoc, parser)
            hrefs = soup.findAll("a")
            for href in hrefs:
                # logger.debug(href.a.string)
                # logger.debug('https://www.guancha.cn' + href.a['href'])
                try:
                    if href.string == None or len(href.string.strip()) < 10:
                        # logger.warning(href)
                        continue
                    if href['href'] in rlst.keys() or ('http://world.people.com.cn'+ href['href']) in rlst.keys():
                        continue
                    if 'http:' not in href['href']:
                        #logger.warning(href)
                        rlst['http://world.people.com.cn'+ href['href']] = href.string.strip()
                        continue
                    rlst[href['href']] = href.string.strip()
                except Exception as err:
                    pass

        except Exception as err:
            logger.error('网页首页解析错误：' + str(err))
        finally:
            del logger
            return rlst

    #中国新闻网
    @classmethod
    def index_chinanews_soup(cls, htmlDoc='', parser='html.parser'):
        soup = None
        rlst = {}
        logger = Logger(file='soup_html_doc.log')
        try:
            soup = BeautifulSoup(htmlDoc, parser)
            hrefs = soup.findAll("a")
            for href in hrefs:
                try:
                    if href.string == None or len(href.string.strip()) < 10:
                        continue
                    if 'gn' in href['href'] or 'cj' in href['href'] or 'gj' in href['href'] or 'ga' in href['href'] or 'shipin' in href['href']:        #国内
                        if 'https:' in href['href']:
                            rlst[href['href']] = href.string.strip()
                            continue
                        if 'www.' in href['href']:
                            rlst['https:' + href['href']] = href.string.strip()
                            continue
                        rlst['https://www.chinanews.com.cn' + href['href']] = href.string.strip()

                    #logger.warning(href)
                except Exception as err:
                    pass

        except Exception as err:
            logger.error('中国新闻网解析错误：' + str(err))
        finally:
            del logger
            return rlst

    #中国网
    @classmethod
    def index_china_soup(cls, htmlDoc='', parser='html.parser'):
        soup = None
        rlst = {}
        logger = Logger(file='soup_html_doc.log')
        try:
            soup = BeautifulSoup(htmlDoc, parser)
            hrefs = soup.findAll("a")
            for href in hrefs:

                # logger.debug('https://www.guancha.cn' + href.a['href'])
                try:
                    if href.string == None or len(href.string.strip()) < 10:
                        # logger.warning(href)
                        continue
                    rlst[href['href']] = href.string.strip()
                except Exception as err:
                    pass

        except Exception as err:
            logger.error('中国网首页解析错误：' + str(err))
        finally:
            del logger
            return rlst

        #

    #光明网
    @classmethod
    def index_gmw_soup(cls,urlPrefix='', htmlDoc='', parser='html.parser'):
        soup = None
        rlst = {}
        logger = Logger(file='soup_html_doc.log')
        try:
            soup = BeautifulSoup(htmlDoc, parser)
            hrefs = soup.findAll("a")
            for href in hrefs:

                # logger.debug('https://www.guancha.cn' + href.a['href'])
                try:
                    if href.string == None or len(href.string.strip()) < 10:
                        #logger.warning(href)
                        continue
                    if 'topic' in href['href']:
                        continue
                    if 'https:' in href['href'] :
                        rlst[href['href']] = href.string.strip()
                        continue
                    rlst[urlPrefix + href['href']] = href.string.strip()
                    logger.debug(href)
                except Exception as err:
                    pass

        except Exception as err:
            logger.error('光明网首页解析错误：' + str(err))
        finally:
            del logger
            return rlst

    #上海热线
    @classmethod
    def index_online_soup(cls, urlPrefix = '',htmlDoc='', parser='html.parser'):
        soup = None
        rlst = {}
        logger = Logger(file='soup_html_doc.log')
        try:
            soup = BeautifulSoup(htmlDoc, parser)
            hrefs = soup.findAll("a")
            for href in hrefs:

                # logger.debug('https://www.guancha.cn' + href.a['href'])
                try:
                    if href.string == None or len(href.string.strip()) < 10:
                        #logger.warning(href)
                        continue
                    if 'http' in href['href']:
                        continue
                    rlst[urlPrefix + href['href'][2:]] = href.string.strip()
                except Exception as err:
                    pass

        except Exception as err:
            logger.error('上海热线解析错误：' + str(err))
        finally:
            del logger
            return rlst

    # 千龙网
    @classmethod
    def index_qianlong_soup(cls, htmlDoc='', parser='html.parser'):
        soup = None
        rlst = {}
        logger = Logger(file='soup_html_doc.log')
        try:
            soup = BeautifulSoup(htmlDoc, parser)
            hrefs = soup.findAll("a")
            for href in hrefs:

                # logger.debug('https://www.guancha.cn' + href.a['href'])
                try:
                    if href.string == None or len(href.string.strip()) < 10:

                        h3 = href.find('h3')
                        if h3 != None:
                            #logger.warning(href)
                            rlst[href['href'].strip()] = h3.string.strip()
                        continue
                    rlst[href['href']] = href.string.strip()
                    #logger.debug(href)
                except Exception as err:
                    pass

        except Exception as err:
            logger.error('千龙网解析错误：' + str(err))
        finally:
            del logger
            return rlst

    @classmethod
    def index_thepaper_soup(cls, htmlDoc='', parser='html.parser'):
        soup = None
        rlst = {}
        logger = Logger(file='soup_html_doc.log')
        try:
            soup = BeautifulSoup(htmlDoc, parser)
            hrefs = soup.findAll("a")
            for href in hrefs:

                # logger.debug('https://www.guancha.cn' + href.a['href'])
                try:
                    if href.string == None or len(href.string.strip()) < 10:
                        #logger.warning(href)
                        continue
                    #logger.debug(href.string.strip())
                    #logger.debug(href)
                    rlst['https://www.thepaper.cn'+href['href']] = href.string.strip()
                except Exception as err:
                    pass

        except Exception as err:
            logger.error('网页首页解析错误：' + str(err))
        finally:
            del logger
            return rlst

    #海峡网
    @classmethod
    def index_hxnews_soup(cls, htmlDoc='', parser='html.parser'):
        soup = None
        rlst = {}
        logger = Logger(file='soup_html_doc.log')
        try:
            soup = BeautifulSoup(htmlDoc, parser)
            hrefs = soup.findAll("a")
            for href in hrefs:

                # logger.debug('https://www.guancha.cn' + href.a['href'])
                try:
                    if href.string == None or len(href.string.strip()) < 10:
                        #logger.warning(href)
                        continue
                    if 'tp/' in href['href'] or 'sp/' in href['href'] or 'hxwz' in href['href'] or 'fj' in href['href']:
                        continue
                    #logger.debug(href)
                    rlst[href['href']] = href.string.strip()
                except Exception as err:
                    pass

        except Exception as err:
            logger.error('海峡网解析错误：' + str(err))
        finally:
            del logger
            return rlst

    #中国日报
    @classmethod
    def index_chinadaily_soup(cls, htmlDoc='', parser='html.parser'):
        soup = None
        rlst = {}
        logger = Logger(file='soup_html_doc.log')
        try:
            soup = BeautifulSoup(htmlDoc, parser)
            hrefs = soup.findAll("a")
            for href in hrefs:

                # logger.debug('https://www.guancha.cn' + href.a['href'])
                try:
                    if href.string == None or len(href.string.strip()) < 10 or 'http' in href['href'] or 'www.' in href['href']:
                        #logger.warning(href)
                        continue
                    logger.debug(href)
                    rlst['http:' + href['href']] = href.string.strip()
                except Exception as err:
                    pass

        except Exception as err:
            logger.error('中国日报解析错误：' + str(err))
        finally:
            del logger
            return rlst

    #海外网   中国日报海外版
    @classmethod
    def index_haiwainet_soup(cls, htmlDoc='', parser='html.parser'):
        soup = None
        rlst = {}
        logger = Logger(file='soup_html_doc.log')
        try:
            soup = BeautifulSoup(htmlDoc, parser)
            h4s = soup.findAll("h4")
            for h4 in h4s:

                # logger.debug('https://www.guancha.cn' + href.a['href'])
                try:
                    #logger.warning(h4)
                    href = h4.find('a')
                    if href==None or len(href.string.strip())<10:
                        continue
                    rlst[href['href']] = href.string.strip()
                except Exception as err:
                    logger.debug(str(err))
                    pass

        except Exception as err:
            logger.error('解析错误：' + str(err))
        finally:
            del logger
            return rlst

    #中国军网
    @classmethod
    def index_81_soup(cls, htmlDoc='', parser='html.parser'):
        soup = None
        rlst = {}
        logger = Logger(file='soup_html_doc.log')
        try:
            soup = BeautifulSoup(htmlDoc, parser)
            hrefs = soup.findAll("a")
            for href in hrefs:

                # logger.debug('https://www.guancha.cn' + href.a['href'])
                try:
                    if href.string == None or len(href.string.strip()) < 10:
                        span = href.find('span', attrs={'class':'text'})
                        div = href.find('div', attrs={'class':'title'})
                        if span == None and div == None:
                            continue
                        if span != None and len(span.string.strip()) > 10:
                            rlst[href['href']] = span.string.strip()
                            continue
                        if div != None:
                            text = ''
                            for string in div.strings:
                                # logger.warning(string)
                                text += string
                            text = text.strip()
                            if len(text) < 10:
                                continue
                            rlst[href['href']] = text
                            continue
                        #logger.warning(href)
                        continue
                    if '81' not in href['href']:
                        continue
                    rlst[href['href']] = href.string.strip()
                    #logger.debug(href)
                except Exception as err:
                    pass

        except Exception as err:
            logger.error('中国军网解析错误：' + str(err))
        finally:
            del logger
            return rlst

    #中国青年网
    @classmethod
    def index_youth_soup(cls, htmlDoc='', parser='html.parser'):
        soup = None
        rlst = {}
        logger = Logger(file='soup_html_doc.log')
        try:
            soup = BeautifulSoup(htmlDoc, parser)
            hrefs = soup.findAll("a")
            for href in hrefs:

                # logger.debug('https://www.guancha.cn' + href.a['href'])
                try:
                    if href.string == None or len(href.string.strip()) < 10:
                        #logger.warning(href)
                        continue
                    if 'http' in href['href']:
                        continue
                    rlst['http:'+href['href']] = href.string.strip()
                    logger.debug(href)
                except Exception as err:
                    pass

        except Exception as err:
            logger.error('中国青年网解析错误：' + str(err))
        finally:
            del logger
            return rlst

    #新京报
    @classmethod
    def index_bjnews_soup(cls, htmlDoc='', parser='html.parser'):
        soup = None
        rlst = {}
        logger = Logger(file='soup_html_doc.log')
        try:
            soup = BeautifulSoup(htmlDoc, parser)
            hrefs = soup.findAll("a")
            for href in hrefs:

                # logger.debug('https://www.guancha.cn' + href.a['href'])
                try:
                    if 'bjnews' not in href['href']:
                        continue
                    if href.string != None and len(href.string.strip()) > 10:
                        #logger.debug(href)
                        rlst[href['href']] = href.string.strip()
                        continue
                    else:
                        text = href.get_text().strip().replace("\n", "").replace(' ', '')
                        if len(text) > 10:

                            i = href.find('i', attrs={'class':'num'})
                            if i != None:
                                rlst[href['href']] = text[1:]
                                #logger.debug(rlst)
                                continue
                            rlst[href['href']] = text




                    #logger.debug(href)
                except Exception as err:
                    pass

        except Exception as err:
            logger.error('解析错误：' + str(err))
        finally:
            del logger
            return rlst

    #北京日报网    京报网
    @classmethod
    def index_bjd_soup(cls, htmlDoc='', parser='html.parser'):
        soup = None
        rlst = {}
        logger = Logger(file='soup_html_doc.log')
        try:
            soup = BeautifulSoup(htmlDoc, parser)
            hrefs = soup.findAll("a")
            for href in hrefs:

                # logger.debug('https://www.guancha.cn' + href.a['href'])
                try:
                    text = href.get_text().strip()
                    text = text.replace("\n", "")
                    text = text.replace("\r", "")
                    if len(text) < 10 or len(text)>30:
                        logger.debug(href['href'] +'       ' + text)
                        continue
                    if 'bjd.' not in href['href']:
                        logger.debug(href['href'] +'       ' + text)
                        continue
                    #rlst[href['href']] = text
                    #logger.warning(href)
                    #logger.debug(href['href'] +'       ' + text)
                    rlst[href['href']] = text
                except Exception as err:
                    pass

        except Exception as err:
            logger.error('北京日报网解析错误：' + str(err))
        finally:
            del logger
            return rlst

    #中工网
    @classmethod
    def index_workercn_soup(cls, htmlDoc='', parser='html.parser'):
        soup = None
        rlst = {}
        logger = Logger(file='soup_html_doc.log')
        try:
            soup = BeautifulSoup(htmlDoc, parser)
            hrefs = soup.findAll("a")
            for href in hrefs:

                # logger.debug('https://www.guancha.cn' + href.a['href'])
                try:
                    if 'www.' in href['href']:
                        #logger.debug(href)
                        continue
                    if href.string == None or len(href.string.strip()) < 10:
                        h3 = href.find('h3')
                        if h3.string != None and len(h3.string.strip()) > 10:
                            rlst['https://www.workercn.cn' + href['href']] = h3.string.strip()
                            #logger.info(href)
                        continue
                    #logger.debug(href)
                    rlst['https://www.workercn.cn' + href['href']] = href.string.strip()
                except Exception as err:
                    pass

        except Exception as err:
            logger.error('解析错误：' + str(err))
        finally:
            del logger
            return rlst

    #半岛电视台
    @classmethod
    def index_aljazeera_soup(cls, htmlDoc='', parser='html.parser'):
        soup = None
        rlst = {}
        logger = Logger(file='soup_html_doc.log')
        try:
            soup = BeautifulSoup(htmlDoc, parser)
            hrefs = soup.findAll("a")
            for href in hrefs:

                # logger.debug('https://www.guancha.cn' + href.a['href'])
                try:
                    if href.string == None or len(href.string.strip()) < 10:
                        #logger.warning(href)
                        continue
                    if 'http' in href['href']:
                        continue
                    url = unquote(href['href'])
                    #logger.debug(url)
                    rlst['https://chinese.aljazeera.net' + url] = href.get_text().strip()
                except Exception as err:
                    pass

        except Exception as err:
            logger.error('解析错误：' + str(err))
        finally:
            del logger
            return rlst
    '''
    #
    @classmethod
    def index__soup(cls, htmlDoc='', parser='html.parser'):
            soup = None
            rlst = {}
            logger = Logger(file='soup_html_doc.log')
            try:
                soup = BeautifulSoup(htmlDoc, parser)
                hrefs = soup.findAll("a")
                for href in hrefs:
                    
                    # logger.debug('https://www.guancha.cn' + href.a['href'])
                    try:
                        if href.string == None or len(href.string.strip()) < 10:
                            # logger.warning(href)
                            continue
                        logger.debug(href)
                    except Exception as err:
                        pass

            except Exception as err:
                logger.error('解析错误：' + str(err))
            finally:
                del logger
                return rlst
            '''

    ############################################海外、港澳台媒体###############################################################



    # 联合早报   所有 新加坡
    @classmethod
    def index_zaobao_soup(cls, htmlDoc='', parser='html.parser'):
        soup = None
        rlst = {}
        logger = Logger(file='soup_html_doc.log')
        try:
            soup = BeautifulSoup(htmlDoc, parser)
            hrefs = soup.findAll("a")
            for href in hrefs:
                try:
                    if len(href['href']) < 15:
                        # logger.debug(href)
                        continue
                    if href.string != None and len(href.string) < 10:
                        # logger.debug(href)
                        continue

                    div = href.find(name='div', attrs={"class": "m-eps"})
                    span = href.find(name='span', attrs={"class": "eps"})
                    if div == None and 'title' not in href.attrs:
                        # logger.debug(href)
                        continue

                    if 'title' in href.attrs:
                        if len(href['title'].strip()) < 10:
                            continue
                        rlst['https://www.zaobao.com' + href['href']] = href['title'].strip()
                        continue
                    if div != None:
                        # logger.warning(href)
                        # logger.debug(href['href'])
                        if len(div.string.strip()) < 10:
                            continue
                        rlst['https://www.zaobao.com' + href['href']] = div.string.strip()
                except Exception as err:
                    pass

        except Exception as err:
            logger.error('联合早报首页解析错误：' + str(err))
        finally:
            del logger
            return rlst

    # 韩国中央日报社
    @classmethod
    def index_jiemian_soup(cls, htmlDoc='', parser='html.parser'):
        soup = None
        rlst = {}
        logger = Logger(file='soup_html_doc.log')
        try:
            soup = BeautifulSoup(htmlDoc, parser)
            hrefs = soup.findAll("a")
            for href in hrefs:

                # logger.debug('https://www.guancha.cn' + href.a['href'])
                try:
                    # logger.debug(href)
                    if href.string != None and len(href.string.strip()) < 10:
                        #logger.warning(href)
                        continue

                    strong = href.strong
                    if strong != None:
                        rlst[href['href']] = strong.string.strip()
                        continue

                except Exception as err:
                    pass

        except Exception as err:
            logger.error('网页首页解析错误：' + str(err))
        finally:
            del logger
            return rlst

    #文汇网
    @classmethod
    def index_wenweipo_soup(cls, htmlDoc='', parser='html.parser'):
        soup = None
        rlst = {}
        logger = Logger(file='soup_html_doc.log')
        try:
            soup = BeautifulSoup(htmlDoc, parser)
            hrefs = soup.findAll("a")
            for href in hrefs:

                try:
                    if len(href['title'].strip()) < 13:
                        #logger.warning(href)
                        continue

                    #logger.debug(href)
                    rlst[href['href']] = href['title'].strip()
                except Exception as err:
                    pass

        except Exception as err:
            logger.error('文汇网解析错误：' + str(err))
        finally:
            del logger
            return rlst

    #大公报
    @classmethod
    def index_takungpao_soup(cls, htmlDoc='', parser='html.parser'):
        soup = None
        rlst = {}
        logger = Logger(file='soup_html_doc.log')
        try:
            soup = BeautifulSoup(htmlDoc, parser)
            hrefs = soup.findAll("a")
            for href in hrefs:

                # logger.debug('https://www.guancha.cn' + href.a['href'])
                try:
                    if len(href['title'])<10:
                        #logger.warning(href)
                        continue

                    logger.debug(href)
                    rlst[href['href']] = href['title'].strip()
                except Exception as err:
                    pass

        except Exception as err:
            logger.error('大公报解析错误：' + str(err))
        finally:
            del logger
            return rlst

    #星岛环球网
    @classmethod
    def index_stnn_soup(cls, htmlDoc='', parser='html.parser'):
        soup = None
        rlst = {}
        logger = Logger(file='soup_html_doc.log')
        try:
            soup = BeautifulSoup(htmlDoc, parser)
            hrefs = soup.findAll("a")
            for href in hrefs:

                # logger.debug('https://www.guancha.cn' + href.a['href'])
                try:
                    if href.string == None or len(href.string.strip()) < 10:
                        #logger.warning(href)
                        continue
                    #logger.debug(href)
                    rlst['https://www.stnn.cc/'+href['href']] = href.string.strip()
                except Exception as err:
                    pass

        except Exception as err:
            logger.error('网页首页解析错误：' + str(err))
        finally:
            del logger
            return rlst

    #中评网
    @classmethod
    def index_crntt_soup(cls, htmlDoc='', parser='html.parser'):
        soup = None
        rlst = {}
        logger = Logger(file='soup_html_doc.log')
        try:
            soup = BeautifulSoup(htmlDoc, parser)
            hrefs = soup.findAll("a")
            for href in hrefs:

                # logger.debug('https://www.guancha.cn' + href.a['href'])
                try:
                    if href.string == None or len(href.string.strip()) < 10 or '#'==href['href']:
                        #logger.warning(href)
                        continue
                    #logger.debug(href)
                    rlst['http://www.crntt.com'+href['href']] = href.string.strip()
                except Exception as err:
                    pass

        except Exception as err:
            logger.error('解析错误：' + str(err))
        finally:
            del logger
            return rlst

    #澳門力報
    @classmethod
    def index_exmoo_soup(cls, htmlDoc='', parser='html.parser'):
        soup = None
        rlst = {}
        logger = Logger(file='soup_html_doc.log')
        try:
            soup = BeautifulSoup(htmlDoc, parser)
            hrefs = soup.findAll("a")
            #hrefs = soup.findAll("a")
            for href in hrefs:
                # logger.debug('https://www.guancha.cn' + href.a['href'])
                try:
                    if href.string != None and len(href.string.strip())>8:
                        #logger.info(href)
                        #logger.info(href['class'][0])
                        if 'sub' in href['class'][0]:
                            rlst[href['href']] = href.string.strip()
                        if 'main' in href['class'][0] and href['href'] in rlst:
                            #logger.info(href)
                            rlst[href['href']] = rlst.get(href['href']) + ':' + href.string.strip()
                    else:
                        h4 = href.find('h4')
                        h3 = href.find('h3')
                        title = ''
                        if h4 == None and h3 == None:
                            #logger.warning(href)
                            continue
                        if h4 != None and h3 != None:
                            title = h4.string.strip()
                            title += ':' + h3.string.strip()
                        else:
                            if h4 != None:
                                title = h4.string.strip()
                            else:
                                title = h3.string.strip()
                        rlst[href['href']] = title
                except Exception as err:
                    pass

        except Exception as err:
            logger.error('澳門力報解析错误：' + str(err))
        finally:
            del logger
            return rlst

    #香港新闻网
    @classmethod
    def index_hkcna_soup(cls, htmlDoc='', parser='html.parser'):
        soup = None
        rlst = {}
        logger = Logger(file='soup_html_doc.log')
        try:
            soup = BeautifulSoup(htmlDoc, parser)
            hrefs = soup.findAll("a")
            for href in hrefs:

                # logger.debug('https://www.guancha.cn' + href.a['href'])
                try:
                    if href.string == None or len(href.string.strip()) < 10:
                        #logger.warning(href)
                        continue
                    text = href.get_text()
                    text = text.strip()
                    rlst['http://www.hkcna.hk' + href['href'][1:]] = text
                    logger.debug(href)
                except Exception as err:
                    pass

        except Exception as err:
            logger.error('解析错误：' + str(err))
        finally:
            del logger
            return rlst

    #中时新闻网  台湾
    @classmethod
    def index_chinatimes_soup(cls, htmlDoc='', parser='html.parser'):
        soup = None
        rlst = {}
        logger = Logger(file='soup_html_doc.log')
        try:
            soup = BeautifulSoup(htmlDoc, parser)
            hrefs = soup.findAll("a")
            #attrs = {'class':['ellipsis-1','ellipsis-2','video-text']}
            for href in hrefs:

                # logger.debug('https://www.guancha.cn' + href.a['href'])
                try:
                    if href.string == None or len(href.string.strip()) < 10:
                        #logger.warning(href)
                        continue

                    #logger.debug(href)
                    rlst[href['href']] = href.string.strip()
                except Exception as err:
                    pass

        except Exception as err:
            logger.error('解析错误：' + str(err))
        finally:
            del logger
            return rlst


    #俄罗斯卫星通讯社
    @classmethod
    def index_sputniknews_soup(cls, htmlDoc='', parser='html.parser'):
        soup = None
        rlst = {}
        logger = Logger(file='soup_html_doc.log')
        try:
            soup = BeautifulSoup(htmlDoc, parser)
            hrefs = soup.findAll("a")
            for href in hrefs:

                # logger.debug('https://www.guancha.cn' + href.a['href'])
                try:
                    if 'https' in href['href']:
                        continue
                    if href.string != None and len(href.string.strip()) > 10:
                        #logger.debug(href)
                        #logger.warning(href)
                        rlst[href['href']] = href.string.strip()
                        continue
                    if href.has_attr('title') and len(href['title'].strip())>10:
                        #logger.debug(href)
                        rlst[href['href']] = href['title'].strip()
                        continue

                    #logger.warning(href)

                except Exception as err:
                    pass

        except Exception as err:
            logger.error('解析错误：' + str(err))
        finally:
            del logger
            return rlst

    #日本共同网
    @classmethod
    def index_kyodonews_soup(cls, htmlDoc='', parser='html.parser'):
        soup = None
        rlst = {}
        logger = Logger(file='soup_html_doc.log')
        try:
            soup = BeautifulSoup(htmlDoc, parser)
            hrefs = soup.findAll("a")
            for href in hrefs:

                # logger.debug('https://www.guancha.cn' + href.a['href'])
                try:
                    if href.string != None and len(href.string.strip()) > 10:
                        # logger.warning(href)
                        rlst['https://china.kyodonews.net' + href['href']] = href.string.strip()
                        continue

                    div = href.find('div', attrs={'class':'latest-title'})
                    if div != None:
                        rlst['https://china.kyodonews.net' + href['href']] = div.string.strip()
                        continue

                    h3 = href.find('h3')
                    if h3 != None:
                        rlst['https://china.kyodonews.net' + href['href']] = h3.string.strip()
                        continue

                    h2 = href.find('h2')
                    if h2 != None:
                        rlst['https://china.kyodonews.net' + href['href']] = h2.string.strip()
                        continue
                    h1 = href.find('h1')
                    if h1 != None:
                        rlst['https://china.kyodonews.net' + href['href']] = h1.string.strip()
                    #logger.debug(href)
                except Exception as err:
                    pass

        except Exception as err:
            logger.error('解析错误：' + str(err))
        finally:
            del logger
            return rlst

    #柬中时报
    @classmethod
    def index_cc_times_soup(cls, htmlDoc='', parser='html.parser'):
        soup = None
        rlst = {}
        logger = Logger(file='soup_html_doc.log')
        try:
            soup = BeautifulSoup(htmlDoc, parser)
            hrefs = soup.findAll("a")
            for href in hrefs:

                # logger.debug('https://www.guancha.cn' + href.a['href'])
                try:
                    div = href.find('div', attrs={'class': ['title', 'exclusive-title']})
                    if div != None:
                        rlst['https://cc-times.com' + href['href']] = div.string.strip()
                        continue

                    span = href.find('span')
                    if span != None and span.string != None:
                        if span.has_attr('class'):
                            continue
                        rlst['https://cc-times.com' + href['href']] = span.string.strip()
                        #logger.debug(href)
                        continue

                    if 'tel' in href['href']:
                        continue

                    if len(href.get_text().strip()) > 10:
                        rlst['https://cc-times.com' + href['href']] = href.get_text().strip()

                    #logger.warning(href)
                except Exception as err:
                    pass

        except Exception as err:
            logger.error('解析错误：' + str(err))
        finally:
            del logger
            return rlst




    ###########################################政府单位##########################################################
    #中国海警
    @classmethod
    def index_ccg_soup(cls, htmlDoc='', parser='html.parser'):
        soup = None
        rlst = {}
        logger = Logger(file='soup_html_doc.log')
        try:
            soup = BeautifulSoup(htmlDoc, parser)
            hrefs = soup.findAll("a")
            for href in hrefs:

                # logger.debug('https://www.guancha.cn' + href.a['href'])
                try:
                    if not href.has_attr('title') or len(href['title'].strip()) < 10:
                        #logger.warning(href)
                        continue

                    if 'ccg' not in href['href']:
                        continue
                    #logger.debug(href)
                    rlst[href['href']] = href['title'].strip()
                except Exception as err:
                    pass

        except Exception as err:
            logger.error('解析错误：' + str(err))
        finally:
            del logger
            return rlst

    #中国人民解放军  中国军网
    @classmethod
    def index_81_soup(cls, htmlDoc='', parser='html.parser'):
        soup = None
        rlst = {}
        logger = Logger(file='soup_html_doc.log')
        try:
            soup = BeautifulSoup(htmlDoc, parser)
            hrefs = soup.findAll("a")
            for href in hrefs:

                # logger.debug('https://www.guancha.cn' + href.a['href'])
                try:
                    div = href.find('div', {'class':'title'})
                    if div != None:
                        rlst[href['href']] = div.get_text().strip()
                        continue

                    h3 = href.find('h3')
                    if h3 != None:
                        rlst[href['href']] = h3.string.strip()
                        continue

                    if href.string == None or len(href.string.strip()) < 10:
                        #logger.warning(href)
                        continue
                    #logger.debug(href)
                    rlst[href['href']] = href.string.strip()
                except Exception as err:
                    pass

        except Exception as err:
            logger.error('解析错误：' + str(err))
        finally:
            del logger
            return rlst

    #中国国防部
    @classmethod
    def index_mod_soup(cls, htmlDoc='', parser='html.parser'):
        soup = None
        rlst = {}
        logger = Logger(file='soup_html_doc.log')
        try:
            soup = BeautifulSoup(htmlDoc, parser)
            hrefs = soup.findAll("a")
            for href in hrefs:

                # logger.debug('https://www.guancha.cn' + href.a['href'])
                try:
                    span = href.find('span', {'class': 'text'})
                    if span != None:
                        rlst[href['href']] = span.get_text().strip()
                        continue

                    span = href.find('span', {'class': 'title'})
                    if span != None:
                        rlst[href['href']] = span.get_text().strip()
                        continue

                    if href.string != None and len(href.string.strip()) > 10:
                        rlst[href['href']] = href.string.strip()

                    #logger.warning(href)
                except Exception as err:
                    pass

        except Exception as err:
            logger.error('解析错误：' + str(err))
        finally:
            del logger
            return rlst

    #中国外交部
    @classmethod
    def index_mfa_soup(cls, htmlDoc='', parser='html.parser'):
        soup = None
        rlst = {}
        logger = Logger(file='soup_html_doc.log')
        try:
            soup = BeautifulSoup(htmlDoc, parser)
            hrefs = soup.findAll("a")
            for href in hrefs:

                # logger.debug('https://www.guancha.cn' + href.a['href'])
                try:

                    if href.string == None or len(href.string.strip()) < 10:
                        #logger.warning(href)
                        continue

                    if 'http' in href['href']:
                        continue
                    logger.debug(href)
                    rlst['https://www.mfa.gov.cn/' + href['href'][2:]] = href.string.strip()

                except Exception as err:
                    pass

        except Exception as err:
            logger.error('解析错误：' + str(err))
        finally:
            del logger
            return rlst

    #国家发展和改革委员会
    @classmethod
    def index_ndrc_soup(cls, htmlDoc='', parser='html.parser'):
        soup = None
        rlst = {}
        logger = Logger(file='soup_html_doc.log')
        try:
            soup = BeautifulSoup(htmlDoc, parser)
            hrefs = soup.findAll("a")
            for href in hrefs:

                # logger.debug('https://www.guancha.cn' + href.a['href'])
                try:
                    if href.string == None or len(href.string.strip()) < 10:
                        continue
                    if 'http' in href['href'] or '#' in href['href'] :
                        #logger.warning(href)
                        continue
                    # logger.debug(href)
                    rlst[href['href']] = href.string.strip()
                except Exception as err:
                    pass

        except Exception as err:
            logger.error('解析错误：' + str(err))
        finally:
            del logger
            return rlst

    #中国国家航天局
    @classmethod
    def index_cnsa_soup(cls, htmlDoc='', parser='html.parser'):
        soup = None
        rlst = {}
        logger = Logger(file='soup_html_doc.log')
        try:
            soup = BeautifulSoup(htmlDoc, parser)
            hrefs = soup.findAll("a")
            for href in hrefs:

                # logger.debug('https://www.guancha.cn' + href.a['href'])
                try:
                    img = href.find('img')
                    if img != None and img.has_attr('title'):
                        rlst['https://www.cnsa.gov.cn/' + href['href']] = img['title'].strip()
                        continue
                    if href.string == None or len(href.string.strip()) < 10:
                        #logger.warning(href)
                        continue
                    if 'http' in href['href']:
                        continue
                    # logger.debug(href)
                    rlst['https://www.cnsa.gov.cn/' + href['href']] = href.string.strip()
                except Exception as err:
                    pass

        except Exception as err:
            logger.error('解析错误：' + str(err))
        finally:
            del logger
            return rlst

    #国家统计局
    @classmethod
    def index_stats_soup(cls, htmlDoc='', parser='html.parser'):
        soup = None
        rlst = {}
        logger = Logger(file='soup_html_doc.log')
        try:
            soup = BeautifulSoup(htmlDoc, parser)
            hrefs = soup.findAll("a")
            for href in hrefs:

                # logger.debug('https://www.guancha.cn' + href.a['href'])
                try:
                    if 'http' in href['href']:
                        continue

                    if href.has_attr('title') and len(href['title'].strip()) > 10:
                        rlst['http://www.stats.gov.cn' + href['href'][1:]] = href['title'].strip()
                        #logger.debug(href)
                        continue

                    if href.string == None or len(href.string.strip()) < 10:
                        #logger.warning(href)
                        continue

                    # logger.debug(href)
                    rlst['http://www.stats.gov.cn' + href['href'][1:]] = href.string.strip()
                except Exception as err:
                    pass

        except Exception as err:
            logger.error('解析错误：' + str(err))
        finally:
            del logger
            return rlst

    #中国科学院
    @classmethod
    def index_cas_soup(cls, htmlDoc='', parser='html.parser'):
        soup = None
        rlst = {}
        logger = Logger(file='soup_html_doc.log')
        try:
            soup = BeautifulSoup(htmlDoc, parser)
            hrefs = soup.findAll("a")
            for href in hrefs:
                if 'http' in href['href'] or 'cas.' not in href['href']:
                    continue

                if href.has_attr('title') and len(href['title'].strip()) > 10:
                    rlst['https:' + href['href']] = href['title'].strip()
                    # logger.debug(href)
                    continue
                # logger.debug('https://www.guancha.cn' + href.a['href'])
                try:
                    if href.string == None or len(href.string.strip()) < 10 or len(href.string.strip()) > 30:
                        #logger.warning(href)
                        continue
                    # logger.debug(href)
                    rlst['https:' + href['href']] = href.string.strip()
                except Exception as err:
                    pass

        except Exception as err:
            logger.error('解析错误：' + str(err))
        finally:
            del logger
            return rlst

    #国资委
    @classmethod
    def index_sasac_soup(cls, htmlDoc='', parser='html.parser'):
        soup = None
        rlst = {}
        logger = Logger(file='soup_html_doc.log')
        try:
            soup = BeautifulSoup(htmlDoc, parser)
            hrefs = soup.findAll("a")
            for href in hrefs:

                # logger.debug('https://www.guancha.cn' + href.a['href'])
                try:
                    if href.has_attr('title') and len(href['title'].strip()) > 10:
                        rlst['http://www.sasac.gov.cn/' + href['href'][3:]] = href['title'].strip()
                        # logger.debug(href)
                        continue

                    if len(href.get_text().strip()) > 10:
                        rlst['http://www.sasac.gov.cn/' + href['href'][3:]] = href['title'].strip()
                        # logger.debug(href)
                        continue

                    if href.string == None or len(href.string.strip()) < 10:
                        #logger.warning(href)
                        continue
                    # logger.debug(href)
                    rlst['http://www.sasac.gov.cn/' + href['href'][3:]] = href.string.strip()
                except Exception as err:
                    pass

        except Exception as err:
            logger.error('解析错误：' + str(err))
        finally:
            del logger
            return rlst

    @classmethod
    def index__soup(cls, htmlDoc='', parser='html.parser'):
        soup = None
        rlst = {}
        logger = Logger(file='soup_html_doc.log')
        try:
            soup = BeautifulSoup(htmlDoc, parser)
            hrefs = soup.findAll("a")
            for href in hrefs:

                # logger.debug('https://www.guancha.cn' + href.a['href'])
                try:
                    if href.string == None or len(href.string.strip()) < 10:
                        #logger.warning(href)
                        continue
                    # logger.debug(href)
                    rlst[href['href']] = href.string.strip()
                except Exception as err:
                    pass

        except Exception as err:
            logger.error('解析错误：' + str(err))
        finally:
            del logger
            return rlst
    '''
    @classmethod
    def index__soup(cls, htmlDoc='', parser='html.parser'):
        soup = None
        rlst = {}
        logger = Logger(file='soup_html_doc.log')
        try:
            soup = BeautifulSoup(htmlDoc, parser)
            hrefs = soup.findAll("a")
            for href in hrefs:

                # logger.debug('https://www.guancha.cn' + href.a['href'])
                try:
                    if href.string == None or len(href.string.strip()) < 10:
                        logger.warning(href)
                        continue
                    #logger.debug(href)
                    rlst[href['href']] = href.string.strip()
                except Exception as err:
                    pass

        except Exception as err:
            logger.error('解析错误：' + str(err))
        finally:
            del logger
            return rlst
    '''
    #########################################国际机构网站/媒体####################################################

    #########################################海外 外语媒体####################################################




