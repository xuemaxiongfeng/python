import unittest
from log import Logger
import warnings
from souphandler import SoupHandler
from requesthandler import RequestsHandler
class MyTestCase(unittest.TestCase):
    def setUp(self):
        #使用unittest框架时， 解决错误 ResourceWarning: Enable tracemalloc to get the object allocation traceback
        warnings.simplefilter('ignore', ResourceWarning)

    def test_something(self):
        #souphandler = SoupHandler()
        '''
        print(456)
        htmltext = RequestsHandler().get_single(url='https://www.guancha.cn/internation/2023_11_09_715080.shtml')
        print(123)
        rlst = SoupHandler.article_class_soup(htmlDoc=htmltext, tagName='div', className='content all-txt')
        print(rlst)


        print(456)
        htmltext = RequestsHandler().get_single(url='https://military.china.com/photo/13004178/20231109/45730919.html')
        print(htmltext)
        print(123)
        rlst = SoupHandler.article_id_soup(htmlDoc=htmltext, tagName='div', id='artiCon')
        print(rlst)
        '''

        '''
        htmltext = RequestsHandler().get_single(url='https://www.guancha.cn/internation?s=dhguoji')
        # print(htmltext)
        rlst = SoupHandler.index_guancha_soup(htmlDoc=htmltext)

        htmltext = RequestsHandler().get_single(url='https://world.huanqiu.com/')
        # print(htmltext)
        rlst = SoupHandler.index_huanqiu_soup(htmlDoc=htmltext)
        
        htmltext = RequestsHandler().get_single(url='https://www.ifeng.com/')
        # print(htmltext)
        rlst = SoupHandler.index_ifeng_soup(htmlDoc=htmltext)
        

        
        htmltext = RequestsHandler().get_single(url='http://www.news.cn/world/index.html')
        # print(htmltext)
        rlst = SoupHandler.index_news_soup(htmlDoc=htmltext)
        
        htmltext = RequestsHandler().get_single(url='http://world.people.com.cn/',encoding='GB2312')
        #print(htmltext)
        rlst = SoupHandler.index_people_soup(htmlDoc=htmltext)

        htmltext = RequestsHandler().get_single(url='https://www.chinanews.com.cn')
        # print(htmltext)
        rlst = SoupHandler.index_chinanews_soup(htmlDoc=htmltext)

        htmltext = RequestsHandler().get_single(url='http://www.china.com.cn/index.shtml')#http://military.china.com.cn/
        # print(htmltext)
        rlst = SoupHandler.index_china_soup(htmlDoc=htmltext)

        urlPrefix = 'https://world.gmw.cn/'
        htmltext = RequestsHandler().get_single(url='https://world.gmw.cn/')#https://world.gmw.cn/https://mil.gmw.cn/
        # print(htmltext)
        rlst = SoupHandler.index_gmw_soup(urlPrefix=urlPrefix,htmlDoc=htmltext)

        urlPrefix = 'https://mil.online.sh.cn'
        htmltext = RequestsHandler().get_single(url='https://mil.online.sh.cn/node/node_110679.htm')#https://mil.online.sh.cn/node/node_110679.htm  https://news.online.sh.cn/news/gb/node/global.htm
        #print(htmltext)
        rlst = SoupHandler.index_online_soup(urlPrefix=urlPrefix, htmlDoc=htmltext)

        htmltext = RequestsHandler().get_single(url='https://review.qianlong.com/')# https://world.qianlong.com/
        #print(htmltext)
        rlst = SoupHandler.index_qianlong_soup(htmlDoc=htmltext)

        htmltext = RequestsHandler().get_single(url='https://www.thepaper.cn/channel_122908')# https://www.thepaper.cn/
        #print(htmltext)
        rlst = SoupHandler.index_thepaper_soup(htmlDoc=htmltext)

        htmltext = RequestsHandler().get_single(url='http://cn.chinadaily.com.cn/')# http://world.chinadaily.com.cn/    http://china.chinadaily.com.cn/
        #print(htmltext)
        rlst = SoupHandler.index_chinadaily_soup(htmlDoc=htmltext)


        htmltext = RequestsHandler().get_single(url='http://www.81.cn/')#  http://www.81.cn/hj_208557/index.html
        #print(htmltext)
        rlst = SoupHandler.index_81_soup(htmlDoc=htmltext)

        htmltext = RequestsHandler().get_single(url='http://news.haiwainet.cn/')# http://www.haiwainet.cn/
        #print(htmltext)
        rlst = SoupHandler.index_haiwainet_soup(htmlDoc=htmltext)

        htmltext = RequestsHandler().get_single(url='https://news.youth.cn/sz/', encoding='GB2312')# https://news.youth.cn/gj/
        #print(htmltext)
        rlst = SoupHandler.index_youth_soup(htmlDoc=htmltext)


        htmltext = RequestsHandler().get_single(url='https://www.bjnews.com.cn/point', )#https://www.bjnews.com.cn/guoji  https://www.bjnews.com.cn/news
        #print(htmltext)
        rlst = SoupHandler.index_bjnews_soup(htmlDoc=htmltext)

        htmltext = RequestsHandler().get_single(url='https://www.bjd.com.cn/jbw/news/?classid=42', )#
        #print(htmltext)
        rlst = SoupHandler.index_bjd_soup(htmlDoc=htmltext)


        '''





        #########################################海外、港澳台 中文媒体####################################################
        '''
        htmltext = RequestsHandler().get_single(url='https://www.zaobao.com/news/world')
        # print(htmltext)
        rlst = SoupHandler.index_zaobao_soup(htmlDoc=htmltext)
        
        htmltext = RequestsHandler().get_single(
            url='https://chinese.joins.com/news/articleList.html?sc_section_code=S1N5&view_type=sm')  # https://chinese.joins.com/news/articleList.html?sc_section_code=S1N2&view_type=sm
        # print(htmltext)
        rlst = SoupHandler.index_jiemian_soup(htmlDoc=htmltext)
        
        htmltext = RequestsHandler().get_single(url='https://www.wenweipo.com/immed/inland')#https://www.wenweipo.com/immed/world
        #print(htmltext)
        rlst = SoupHandler.index_wenweipo_soup(htmlDoc=htmltext)
        
        htmltext = RequestsHandler().get_single(url='http://www.takungpao.com/news/232110/index.html')# http://www.takungpao.com/news/232112/index.html http://www.takungpao.com/news/232111/index.html
        #print(htmltext)
        rlst = SoupHandler.index_takungpao_soup(htmlDoc=htmltext)
        
        htmltext = RequestsHandler().get_single(url='https://www.stnn.cc/usa/')# https://www.stnn.cc/guoji/
        #print(htmltext)
        rlst = SoupHandler.index_stnn_soup(htmlDoc=htmltext)
        
        htmltext = RequestsHandler().get_single(url='http://www.crntt.com/crn-webapp/coluOutline.jsp?coluid=148')  #http://www.crntt.com/crn-webapp/coluOutline.jsp?coluid=70
        # print(htmltext)
        rlst = SoupHandler.index_crntt_soup(htmlDoc=htmltext)
        
        htmltext = RequestsHandler().get_single(url='https://www.exmoo.com/world', )#https://www.exmoo.com/  https://www.exmoo.com/
        #print(htmltext)
        rlst = SoupHandler.index_exmoo_soup(htmlDoc=htmltext)
        
        htmltext = RequestsHandler().get_single(url='http://www.hkcna.hk/index_col_else.jsp?channel=2808')#http://www.hkcna.hk/index_col_else.jsp?channel=2810  http://www.hkcna.hk/index_col_else.jsp?channel=2805
        #print(htmltext)
        rlst = SoupHandler.index_hkcna_soup(htmlDoc=htmltext)
        
        htmltext = RequestsHandler().get_single(url='https://www.chinatimes.com/chinese/?chdtv')#https://www.chinatimes.com/world/?chdtv
        #print(htmltext)
        rlst = SoupHandler.index_chinatimes_soup(htmlDoc=htmltext)
        
        htmltext = RequestsHandler().get_single(url='https://sputniknews.cn/category_guoji/')#https://sputniknews.cn/
        #print(htmltext)
        rlst = SoupHandler.index_sputniknews_soup(htmlDoc=htmltext)
        
        htmltext = RequestsHandler().get_single(url='https://china.kyodonews.net/news/global_news')#https://china.kyodonews.net/  https://china.kyodonews.net/news/japan_politics
        #print(htmltext)
        rlst = SoupHandler.index_kyodonews_soup(htmlDoc=htmltext)
        
        htmltext = RequestsHandler().get_single(url='https://cc-times.com/categories/korea')  #  https://cc-times.com/
        #print(htmltext)
        rlst = SoupHandler.index_cc_times_soup(htmlDoc=htmltext)
        
        
        #半岛电视台
        htmltext = RequestsHandler().get_single(url='https://chinese.aljazeera.net/economy/')  #
        #print(htmltext)
        rlst = SoupHandler.index_aljazeera_soup(htmlDoc=htmltext)

        '''

        #国资委
        htmltext = RequestsHandler().get_single(url='http://www.sasac.gov.cn/n16582853/n16582883/index.html')  #http://www.sasac.gov.cn/n2588025/index.html
        #print(htmltext)
        rlst = SoupHandler.index_sasac_soup(htmlDoc=htmltext)

        #######################################政府单位#############################################
        '''
        #中国海警
        htmltext = RequestsHandler().get_single(url='https://www.ccg.gov.cn/')  #
        #print(htmltext)
        rlst = SoupHandler.index_ccg_soup(htmlDoc=htmltext)
        
         #中国人民解放军  中国军网
        htmltext = RequestsHandler().get_single(url='http://www.81.cn/hj_208557/index.html')  #http://www.81.cn/  http://www.81.cn/jw_208551/index.html
        #print(htmltext)
        rlst = SoupHandler.index_81_soup(htmlDoc=htmltext)
        
        #中国国防部
        htmltext = RequestsHandler().get_single(url='http://www.mod.gov.cn/')  #
        #print(htmltext)
        rlst = SoupHandler.index_mod_soup(htmlDoc=htmltext)
        
        #中国外交部
        htmltext = RequestsHandler().get_single(url='https://www.mfa.gov.cn/')  #
        #print(htmltext)
        rlst = SoupHandler.index_mfa_soup(htmlDoc=htmltext)
        
        #国家发展和改革委员会
        htmltext = RequestsHandler().get_single(url='https://www.ndrc.gov.cn/')  #
        # print(htmltext)
        rlst = SoupHandler.index_ndrc_soup(htmlDoc=htmltext)
        
        #中国国家航天局
        htmltext = RequestsHandler().get_single(url='https://www.cnsa.gov.cn/')  #
        # print(htmltext)
        rlst = SoupHandler.index_cnsa_soup(htmlDoc=htmltext)
        
        #国家统计局
        htmltext = RequestsHandler().get_single(url='http://www.stats.gov.cn/')  #
        #print(htmltext)
        rlst = SoupHandler.index_stats_soup(htmlDoc=htmltext)
        
        #中国科学院
        htmltext = RequestsHandler().get_single(url='https://www.cas.cn/')  #
        #print(htmltext)
        rlst = SoupHandler.index_cas_soup(htmlDoc=htmltext)
        
        #国资委
        htmltext = RequestsHandler().get_single(url='http://www.sasac.gov.cn/n16582853/n16582883/index.html')  #http://www.sasac.gov.cn/n2588025/index.html
        #print(htmltext)
        rlst = SoupHandler.index_sasac_soup(htmlDoc=htmltext)
        '''

        #########################################国际机构网站/媒体####################################################

        #########################################海外 外语媒体####################################################


        # print(rlst)
        for item in rlst.items():
            #print(key + ':' + value)
            print(item)
            pass
if __name__ == '__main__':
    unittest.main()
