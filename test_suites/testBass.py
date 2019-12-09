from selenium import webdriver
import unittest,os
from framework.base_page import BasePage
class TestBase(unittest.TestCase,BasePage):
    def setUp(self):
        self.driver = webdriver.Chrome()#驱动浏览器
        self.driver.implicitly_wait(10)#隐式等待
        self.driver.maximize_window()#最大化浏览器



    def tearDown(self):
        self.driver.quit()
if __name__=='__main__':
    unittest.main()