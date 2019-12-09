import time,unittest
from test_suites.testBass import TestBase
from pageobjects.pageobjects import Cloud
from selenium import webdriver
from  framework import base_page
from  framework.base_page import BasePage
import requests
import readConfig
#创建一个读取配置文件的实例
readconfig = readConfig.ReadConfig()
#读取config文件中的MYSQL文件内容
mail_host = readconfig.get_email("mail_host")
host = readconfig.get_mysql("host")
user = readconfig.get_mysql("user")
password = readconfig.get_mysql("password")
db = readconfig.get_mysql("db")
port = readconfig.get_mysql("port")
charset = readconfig.get_mysql("charset")

class InvoiceCase(TestBase,BasePage):
    @unittest.skip('不需要执行')
    def test_login(self):   #登陆
        """
        这里一定要test开头，把测试逻辑代码封装到一个test开头的方法里。
        :return:
         """
        driver = Cloud(self.driver)#driver变量可以调用BasePage得方法
        url = "http://mgt.test.sunmi.com/"
        driver.open(url)
        driver.mgt_login()
        a = driver.Get_url()
        """
        try:
            assert a == url
            print(' Test Pass.')
        except Exception as e:#将所有输出都截取到测试报告中
            driver.get_windows_img()  # 调用基类截图方法
            print('Test Fail.',format(e))
        """
        assert a == url

        print(' Test Pass.')

    @unittest.skip('不需要执行')
    def test_search(self):#进入电子发票
        driver = Cloud(self.driver)
        driver.open("http://mgt.test.sunmi.com/")
        #登陆MGT
        driver.mgt_login()
        #打开一级菜单
        driver.mgt_click_invoice()
        #打开二级菜单
        driver.mgt_click_SHJJGL()
        time.sleep(1)
        #搜索订单
        driver.mgt_click_search("13975059149","公司",0,0)
        #断言
        a = driver.Get_text("xpath","//*[@id='root']/div/main/div/div[2]/div/div/div[2]/div[2]/div/div/div/div/div/table/tbody/tr[1]/td[6]/span")

        assert  a == "编辑"
        print("Test Pass")

    # @unittest.skip('不需要执行')
    def test_insert_user(self):
        driver = Cloud(self.driver)
        driver.open("http://mgt.test.sunmi.com/")
        #登陆MGT
        driver.mgt_login()
        #打开一级菜单
        driver.mgt_click_invoice()
        #打开二级菜单
        driver.mgt_click_SHJJGL()
        time.sleep(1)
        #删除数据库的user
        sql = "delete from invoice_user where taxpayer_num = '91310117350739745P1'"
        base_page.execute_sql(host,user,password,db,port,charset,sql)
        #新增商户
        driver.mgt_insert_user('91310117350739745P1','界面自动化测试','13975059149',)
        #断言
        #1、搜索刚新增的商户
        driver.mgt_click_search('13975059149','界面自动化',0,0)
        #2、获取搜索结果的企业名称
        name = driver.Get_text("link_text","界面自动化测试")

        assert name == "界面自动化测试"
        print("Test Pass")



