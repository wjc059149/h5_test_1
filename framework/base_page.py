#定义一个页面基类，让所有页面都继承这个类，封装一些常用的页面操作方式
import  time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.select import Select
import os.path
from framework.logger import Logger
import os
import json
import xlrd
from datetime import datetime
import traceback
import csv
import paramiko
from readConfig import ReadConfig
#from common import configHttp
import re
import pymysql
import readConfig
import random
import hashlib
import requests
#创建一个日志实例
logger = Logger(logger = "BasePage").getlog()
code = ''
admin_id = ''
partner_id = ''
merchant_id = ''
md5_new = ''
md5_new1 = ''
md5_new2 = ''
md5_new3 = ''
md5_new4 = ''
md5_new5 = ''
md5_new6 = ''
md5_new7 = ''


class BasePage(object):

    def __init__(self,driver):
        self.driver = driver

    def open(self,url):
        self.driver.get(url)
    #打开网页

    def quit_browser(self):
        self.driver.quit()
    #关闭所有窗口

    def forward(self):
        self.driver.forward()
        logger.info("Click forward on current page.")# 日志显示在当前页面点击前进
    #浏览器前进

    def back(self):
        self.driver.back()
        logger.info("Click back on current page.")
    #浏览器后退

    def wait(self,loc,seconds):
        try:
            wait_ = WebDriverWait(self.driver,seconds)
            wait_.until(lambda driver:driver.find_element(*loc))
            logger.info("wait for %d seconds." % seconds)
        except NameError as e:
            logger.error("Failed to load the element with %s" % e)
    #显式等待

    def get_windows_img(self):
        #把file_path保存到我们项目根目录的一个文件夹.\Screenshots下
        file_path =  "../screenshots/"
        rq = time.strftime("%Y%m%d%H%M%S",time.localtime(time.time()))
        scree_name = file_path + rq +".png"
        try:
            self.driver.get_screenshot_as_file(scree_name)
            logger.info("Had take screenshot and save to folder : /screenshots")#日志提示截图文件已经保存在文件夹
        except NameError as e:
            logger.error("Failed to take screenshot! %s" % e)

    #保存图片

    # 定位元素方法
    def find_element(self, loc):
        """
        :return: element
        """
        return self.driver.find_element(loc)

        # 输入

    def send_keys1(self, selector, text):

        el = self.find_element(selector)
        el.clear1()
        try:
            el.send_keys1(text)
            logger.info("Had type \' %s \' in inputBox" % text)
        except NameError as e:
            logger.error("Failed to select in input box with %s" % e)
            self.get_windows_img()

        # 清除文本框

    def clear1(self, selector):

        el = self.find_element(selector)
        try:
            el.clear1()
            logger.info("Clear text in input box before typing.")
        except NameError as e:
            logger.error("Failed to clear in input box with %s" % e)
            self.get_windows_img()

        # 点击元素

    def click1(self, selector):

        el = self.find_element(selector)
        try:
            el.click1()
            logger.info("The element \'%s\' was clicked." % el.text)
        except NameError as e:
            logger.error("Failed to click the element with %s" % e)

        # 鼠标事件（左键点击）

    def move_element(self, loc, sloc):
        mouse = self.find_element(loc)
        try:
            ActionChains(self.driver).move_to_element(mouse).perform()
            self.click1(sloc)
            pass
        except Exception as e:
            logger.error("Failed to click move_element with %s" % e)
            self.get_windows_img()

        # 强制等待

    @staticmethod
    def sleep(seconds):
        time.sleep(seconds)
        logger.info("Sleep for %d seconds" % seconds)

    # 验证元素是否存在
    def Check_element(self, type, value):
        if type == "css_selector":
            self.driver.find_element_by_css_selector(value)
        elif type == "xpath":
            self.driver.find_element_by_xpath(value)
        elif type == "id":
            self.driver.find_element_by_id(value)
        elif type == "name":
            self.driver.find_element_by_name(value)
        elif type == "link_text":
            self.driver.find_element_by_link_text(value)
        elif type == "partial_link_text":
            self.driver.find_element_by_partial_link_text(value)

    # 获取子元素
    def Select_child_elements(self, type, value1, value2):
        if type == "xpath":
            Select(self.driver.find_element_by_xpath(value1)).select_by_visible_text(value2)
        elif type == "id":
            Select(self.driver.find_element_by_id(value1)).select_by_visible_text(value2)
        elif type == "name":
            Select(self.driver.find_element_by_name(value1)).select_by_visible_text(value2)
        elif type == "link_text":
            Select(self.driver.find_element_by_link_text(value1)).select_by_visible_text(value2)
        elif type == "partial_link_text":
            Select(self.driver.find_element_by_partial_link_text(value1)).select_by_visible_text(value2)

    # 获取输入框的值,get_attribute获取相应元素便签的内容
    #value2 = 你想要捕获的元素名，捕获到对应得值
    def Get_attribute(self, type, value1, value2):
        if type == "css_selector":
            Value =self.driver.find_element_by_css_selector(value1).get_attribute(value2)
            return Value
        elif type == "xpath":
            Value = self.driver.find_element_by_xpath(value1).get_attribute(value2)
            return Value
        elif type == "name":
            Value = self.driver.find_element_by_name(value1).get_attribute(value2)
            return Value
        elif type == "link_text":
            Value = self.driver.find_element_by_link_text(value1).get_attribute(value2)
            return Value
        elif type == "class_name":
            Value = self.driver.find_element_by_class_name(value1).get_attribute(value2)
            return Value
        elif type == "id":
            Value = self.driver.find_element_by_id(value1).get_attribute(value2)
            return Value

     # 获取下拉框的文本的值

    #获取文本值
    def Get_text(self, type, value):
        if type == "css_selector":
            text =self.driver.find_element_by_css_selector(value).text
            return text
        elif type == "xpath":
            text = self.driver.find_element_by_xpath(value).text
            return text
        elif type == "name":
            text = self.driver.find_element_by_name(value).text
            return text
        elif type == "link_text":
            text = self.driver.find_element_by_link_text(value).text
            return text
        elif type == "class_name":
            text = self.driver.find_element_by_class_name(value).text
            return text
        elif type == "id":
            text = self.driver.find_element_by_id(value).text
            return text

    #获取当前页面得title
    def Get_title(self):
        title = self.driver.title
        return title

    #获取当前页面得url
    def Get_url(self):
        now_url = self.driver.current_url
        return now_url
# 输入内容方法
    def send_keys(self, type, value, inputvalue):
        if type == "css_selector":
            self.driver.find_element_by_css_selector(value).send_keys(inputvalue)
        elif type == "xpath":
            self.driver.find_element_by_xpath(value).send_keys(inputvalue)
        elif type == "class_name":
            self.driver.find_element_by_class_name(value).send_keys(inputvalue)
        elif type == "id":
            self.driver.find_element_by_id(value).send_keys(inputvalue)
        elif type == "name":
            self.driver.find_element_by_name(value).send_keys(inputvalue)
        elif type == "link_text":
            self.driver.find_element_by_link_text(value).send_keys(inputvalue)
        elif type == "partial_link_text":
            self.driver.find_element_by_partial_link_text(value).send_keys(inputvalue)

    # 点击操作
    def click(self, type, value):
        if type == "css_selector":
            self.driver.find_element_by_css_selector(value).click()
        elif type == "xpath":
            self.driver.find_element_by_xpath(value).click()
        elif type == "class_name":
            self.driver.find_element_by_class_name(value).click()
        elif type == "id":
            self.driver.find_element_by_id(value).click()
        elif type == "name":
            self.driver.find_element_by_name(value).click()
        elif type == "link_text":
            self.driver.find_element_by_link_text(value).click()
        elif type == "partial_link_text":
            self.driver.find_element_by_partial_link_text(value).click()

    # 清空输入框的内容
    def clear(self, type, value):
        if type == "css_selector":
            self.driver.find_element_by_css_selector(value).clear()
        elif type == "xpath":
            self.driver.find_element_by_xpath(value).clear()
        elif type == "id":
            self.driver.find_element_by_id(value).clear()
        elif type == "name":
            self.driver.find_element_by_name(value).clear()
        elif type == "link_text":
            self.driver.find_element_by_link_text(value).clear()
        elif type == "partial_link_text":
            self.driver.find_element_by_partial_link_text(value).clear()

    def random_32(change=1):  # 随机数
        """
        change值代表在一次的脚本执行中随机32位字符串是否变化，值1代表每次都变化，值0代表值保持不变，2表示16位的不变随机数，3456 代表另一个不变的随机数
        """
        random_num = random.random()  # 生成在[0,1)范围内的随机浮点数
        str_one = str(random_num).encode()  # 将浮点数转换为字符串并做二进制处理
        md5 = hashlib.md5(str_one).hexdigest()  # 32位字符串
        # global md5_new,md5_new1,md5_new2,md5_new3,md5_new4,md5_new5,md5_new6,md5_new7
        if change == 1:
            return md5
        elif change == 0:
            global md5_new
            if md5_new == '':
                md5_new = md5
            return md5_new
        elif change == 2:
            global md5_new1
            if md5_new1 == '':
                md5_new1 = md5[-16:0]
            return md5_new1
        elif change == 3:
            global md5_new2
            if md5_new2 == '':
                md5_new2 = md5
            return md5_new2
        elif change == 4:
            global md5_new3
            if md5_new3 == '':
                md5_new3 = md5
            return md5_new3
        elif change == 5:
            global md5_new4
            if md5_new4 == '':
                md5_new4 = md5
            return md5_new4
        elif change == 6:
            global md5_new5
            if md5_new5 == '':
                md5_new5 = md5
            return md5_new5
        elif change == 7:
            global md5_new6
            if md5_new6 == '':
                md5_new6 = md5
            return md5_new6
        elif change == 8:
            global md5_new7
            if md5_new7 == '':
                md5_new7 = md5
            return md5_new7

    def random_int(self):
        random_1 = random.random()

    def syncInvoiceOrder(Amount, sn, shopOrderSn, orderSn, postUrl):  # 生成订单接口
        postLoad = {'amount': Amount, 'sn': sn, 'shopOrderSn': shopOrderSn, 'orderSn': orderSn,'tradeDate': '1557387360'}
        r = requests.post(postUrl, params=postLoad)
        return r.json()

# ******************************************html报告文件处理展示***************************************
###############################################配置发送邮件#############################################################
def listdir(path, list_name, file_type):
    """筛选出某个路径（path）下特定类型（file_type）文件（不包括其子目录），并将所有此类型文件的路径放在一个列表中"""
    #D:\unittest_h5_test\test_report [] report.html
    for file in os.listdir(path):
        file_path = os.path.join(path, file)
        if file[16:] == file_type:
            list_name.append(file_path)
    return list_name

def dir_result_1():
    """返回test_report文件夹路径"""
    #pro_dir = os.path.split(os.path.realpath(__file__))[0]  # 当前文件所在文件夹路径，非执行文件路径
    pro_dir = os.getcwd()
    #prr = os.path.abspath(os.path.dirname(pro_dir) + os.path.sep + ".")  # 当前文件夹父路径
    # result_path = os.path.join(prr, "test_report")  # 报告文件所在文件夹路径
    prr = "\\test_report\\"
    result_path = pro_dir + prr
    #print(result_path)
    return result_path

def dir_result():
    """返回test_report文件夹路径"""
    pro_dir = os.path.split(os.path.realpath(__file__))[0]  # 当前文件所在文件夹路径，非执行文件路径
    prr = os.path.abspath(os.path.dirname(pro_dir) + os.path.sep + ".")  # 当前文件夹父路径
    result_path = os.path.join(prr, "test_report")  # 报告文件所在文件夹路径
    return result_path

def newest_file(list_name):
    """根据日期及时间数字获取最新文件"""
    lis = []
    for file in list_name:
        stri = ''
        for i in file:
            if i in '1234567890':
                stri += i
        lis.append(int(stri))
    ind = lis.index(max(lis))
    return list_name[ind]


def new_html(name):
    """获取到最新的html文件的路径"""
    report_path = dir_result()  # 获取到result文件夹路径
    lis = []
    type_file = name + '.html'
    file_list = listdir(report_path, lis, type_file)
    return newest_file(file_list)

def find_word(file, word):
    """查找文件file文件中的字符串word内容"""
    n = 1
    read_list = open(file, 'rb').readlines()  # 以byte方式读取文件
    for line in read_list:
        if word.encode() in line:  # 将word内容转换为byte类型，进行校验
            return True
        else:
            n += 1
    if n > len(read_list):
        return False

# ***************************************操作数据库****************************************
def execute_sql(host,user,password,db,port,charset,sql):
    """访问数据库，并执行sql语句"""
    #连接数据库
    connection = pymysql.connect(
        host=host,
        port=int(port),
        user=user,
        password=password,
        database=db,
        charset=charset
    )
    #通过cursor创建游标
    cursor = connection.cursor()

    try:
        #执行sql
        cursor.execute(sql)
        #提交事务
        connection.commit()
        #提交之后，获取刚插入的数据的ID
        #last_id = cursor.lastrowid
        #当有需要时，可以return 返回last_id
    except Exception as e:
        #有异常，回滚事务
        connection.rollback()
    #关闭光标对象
    cursor.close()
    #关闭数据库连接
    connection.close()



