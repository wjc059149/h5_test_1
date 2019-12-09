#将对页面的操作视为一个对象，定义一个方法，将这些方法统合在一起
from framework.base_page import BasePage
from selenium.webdriver.common.by import By
from framework.logger import Logger
from  selenium import webdriver
import  time

logger = Logger(logger="cloud_page").getlog()
class Cloud(BasePage):
    input_box = (By.ID,'kw')
    search_submit = (By.XPATH,'//*[@id="root"]/div/div/div[2]/div/div/div[3]/div[1]/div[2]/form/div[4]/div/div/span/button')
    def value_input(self,text):
        self.wait(self.input_box,5)
        self.send_keys(self.input_box,text)
    def submit_btn(self):
        self.click(self.search_submit)
        logger.info("show results!")
        self.sleep(2)
    def mgt_login(self):
        time.sleep(2)
        # 输入用户名
        self.click("xpath", "//input[@type='text'and @placeholder='登录名/邮箱/手机号']")
        self.clear("xpath", "//input[@type='text'and @placeholder='登录名/邮箱/手机号']")
        self.send_keys("xpath", "//input[@type='text'and @placeholder='登录名/邮箱/手机号']", "Admin")
        # 输入密码
        self.click("xpath", "//input[@type='password'and @placeholder='密码']")
        self.clear("xpath", "//input[@type='password'and @placeholder='密码']")
        self.send_keys("xpath", "//input[@type='password'and @placeholder='密码']", "Admin123")
        # 点击登陆
        self.click("css_selector", "#sunmi-button-wrap > button")
        time.sleep(1)
    def mgt_click_invoice(self):
        #点击电子发票一级菜单
        self.click("css_selector","div[aria-owns='电子发票$Menu']")
    def mgt_click_SHJJGL(self):
        #点击商户进件管理二级菜单
        self.click("link_text","商户进件管理")
    def mgt_click_search(self,phone,name,source,plan):
        """
        :param phone: 搜索的手机号
        :param name: 搜索的商户名称
        :param source: 搜索的进件来源
        :param plan: 搜索的税务共建计划
        :return: 没有返回，只有事件操作
        """
        #点击搜索按钮
        self.send_keys("css_selector","input[placeholder='请输入商户手机号']",phone)  # 输入手机号
        self.send_keys("css_selector","input[placeholder='请输入商户名称']",name)  # 输入商户名称
        # 点击进件来源下拉框
        self.click("css_selector","#root > div > main > div > div.content__children > div > div > div.sui-panel-head > div.sui-panel-head-title > div > div:nth-child(3) > div > div > div")  #
        if source == 0:
            #选择全部
            pass
        elif source == 1:
            #选择钩子程序
            self.click("css_selector","body > div:nth-child(14) > div > div > div > ul > li:nth-child(2)")
        elif source == 2:
            #选择商米电商
            self.click("css_selector","body > div:nth-child(14) > div > div > div > ul > li:nth-child(3)")
        elif source == 3:
            #选择增值服务部
            self.click("css_selector", "body > div:nth-child(14) > div > div > div > ul > li:nth-child(4)")
        elif source == 4 :
            #选择店铺中心
            self.click("css_selector", "body > div:nth-child(14) > div > div > div > ul > li:nth-child(5)")
        # 点击税务共建计划下拉框
        self.click("css_selector","#root > div > main > div > div.content__children > div > div > div.sui-panel-head > div.sui-panel-head-title > div > div:nth-child(4) > div > div > div > div")
        if plan == 0:
            #选择全部
            pass
        elif plan == 1:
            #选择是
            self.click("css_selector","body > div:nth-child(16) > div > div > div > ul > li:nth-child(2)")
        elif plan == 2:
            #选择否
            self.click("css_selector","body > div:nth-child(16) > div > div > div > ul > li:nth-child(3)")
        #选择完成后，点击搜索按钮
        self.click("css_selector","#root > div > main > div > div.content__children > div > div > div.sui-panel-head > div.sui-panel-head-title > div > button")

    def mgt_insert_user(self,taxpayerNum,enterpriseName,phone):
        """
        :param taxpayerNum: 纳税人识别号
        :param enterpriseName: 企业名称
        :param phone: 联系人手机号
        :return: 没有返回，只有事件操作
        """
        #点击新增
        self.click("css_selector","#root > div > main > div > div.content__children > div > div > div.sui-panel-head > div.sui-panel-head-extra > button")
        #输入联系人手机号
        self.send_keys("link_text","请输入联系人手机号",phone)
        #输入纳税人识别号
        self.send_keys("link_text","请输入纳税人识别号",taxpayerNum)
        #输入企业名称
        self.send_keys("link_text","请输入企业名称",enterpriseName)
        #点击保存
        self.click("css_selector","body > div:nth-child(25) > div > div.ant-modal-wrap.invoice-modal > div > div.ant-modal-content > div.ant-modal-footer > button")