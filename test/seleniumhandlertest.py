#-*-coding:utf-8-*-

import logging
import unittest
import warnings
from selenium.common.exceptions import TimeoutException

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service


from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC






import seleniumhandler


class MyTestCase(unittest.TestCase):

    def setUp(self):
        #使用unittest框架时， 解决错误 ResourceWarning: Enable tracemalloc to get the object allocation traceback
        warnings.simplefilter('ignore', ResourceWarning)

    def test_something(self):
        #第一步： 设置chromedriver地址。一定要指定驱动的位置。
        #第二步：初始化驱动
        #第三步：获取目标网页
        #第四步：解析。以下就可以进行解了。使用webMagic、jsoup等进行必要的解析。

        print(seleniumhandler.DRIVER_PATH)

        chrome_options = Options()
        # 设置无界面模式
        chrome_options.add_argument("--headless")
        # 禁用gpu
        chrome_options.add_argument("--disable-gpu")
        driverpath = Service(executable_path=seleniumhandler.DRIVER_PATH)

        driver = webdriver.Chrome(options=chrome_options, service=driverpath)

        #等待加载
        driver.implicitly_wait(10)
        driver.get("https://weibo.com/u/1743951792")
        try:
            #app = driver.find_element(by=By.ID,value='app')
            #app = WebDriverWait(driver, 10).until(EC.presence_of_element_located(('id', 'app')))

            WebDriverWait(driver, 5, 0.5).until(lambda x: x.find_element(By.CLASS_NAME, 'detail_wbtext_4CRf9'))  #presence_of_element_located(())

            #app = driver.find_element(By.CLASS_NAME, 'detail_wbtext_4CRf9')  #'',
            #app.find_element(By.CLASS_NAME, 'woo-picture-img')

        except Exception as e:
            print(e)



        '''
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option('excludeSwitches',['enable-automation'])
        selenium = Service(executable_path=chrome_driver)
        driver = webdriver.Chrome(options=chrome_options, service=Service)
        driver.get("http://www.baidu.com")

        
        driver = webdriver.Chrome(options=chrome_options, service=chrome_driver)
        driver.get("https://www.deppon.com/deptlist/")
        '''
        html = driver.page_source
        driver.close()
        print(html)

        pass


if __name__ == '__main__':
    unittest.main()
