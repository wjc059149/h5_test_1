import time,unittest
from test_suites.testBass import TestBase
from pageobjects.pageobjects import Cloud
from selenium import webdriver
from  framework.base_page import BasePage
from  framework.base_page import BasePage
import requests


class InvoiceCase(TestBase,BasePage):


    #@unittest.skip('不需要执行')
    def test_url_ok(self):   #验证URL是否正确
        """
        这里一定要test开头，把测试逻辑代码封装到一个test开头的方法里。
        :return:
         """

        input = Cloud(self.driver)#input变量可以调用Cloud得方法
        url = "http://invoice.sunmi.com/?orderSn=AUTOtest0000000008"
        input.open(url)
        time.sleep(2)
        a = input.Get_url()#获取当前页面的url

        try:
            assert url in a
            print(' Test Pass.')
        except Exception as e:
            input.get_windows_img()  # 调用基类截图方法
            print('Test Fail.',format(e))

    #@unittest.skip('不需要执行')
    def test_person_error_ok(self): #输入框验证错误提示
        """
        这里一定要test开头，把测试逻辑代码封装到一个test开头的方法里。
        :return:
         """
        input = Cloud(self.driver)  # input变量可以调用Cloud得方法
        url = "http://invoice.sunmi.com/?orderSn=AUTOtest0000000008"
        input.open(url)
        time.sleep(2)
        # 切换到个人开票
        input.click('xpath', '//*[@id="root"]/div/div/div[2]/div/div/div[1]/div/div/div/div/div[1]/div[1]')
        #点击提交
        input.click('xpath','//form/div[4]/div/div/span/button')#pageobjects包内的方法
        a = input.Get_text('xpath','//form/div[2]/div/div/div')

        try:
            assert "邮箱地址为必填项" == a
            print('Test Pass.')
        except Exception as e:
            input.get_windows_img()  # 调用基类截图方法
            print('Test Fail.', format(e))

    #@unittest.skip('不需要执行')
    def test_person_name_ok(self): #个人姓名输入框
        input = Cloud(self.driver)  # input变量可以调用Cloud得方法
        url = "http://invoice.sunmi.com/?orderSn=AUTOtest0000000008"
        input.open(url)
        time.sleep(2)
        #//*[@id="root"]/div/div/div[2]/div/div/div[3]/div[1]/div[2]/form/div[1]/div/div/span/span 个人
        #//*[@id="root"]/div/div/div[2]/div/div/div[3]/div[2]/div[2]/form/div[1]/div/div/span/div/div/span 企业
        #切换到个人开票
        input.click('xpath', '//*[@id="root"]/div/div/div[2]/div/div/div[1]/div/div/div/div/div[1]/div[1]')
        #捕获个人开票默认值
        a = input.Get_attribute('css_selector','input[id="buyerName"]','value')
        input.clear('css_selector','input[id="buyerName"]')
        input.send_keys('css_selector','input[id="buyerName"]','吴进城')
        #再次捕获个人姓名输入值
        b = input.Get_attribute('css_selector','input[id="buyerName"]','value')
        try:
            assert "个人" == a
            assert "吴进城" == b
            print('Test Pass.')
        except Exception as e:
            input.get_windows_img()  # 调用基类截图方法
            print('Test Fail.', format(e))

    #@unittest.skip('不需要执行')
    def test_person_email_ok(self): #个人邮件地址输入框
        input = Cloud(self.driver)  # input变量可以调用Cloud得方法
        url = "http://invoice.sunmi.com/?orderSn=AUTOtest0000000008"
        input.open(url)
        time.sleep(2)
        # 切换到个人开票
        #//*[@id="root"]/div/div/div[2]/div/div/div[3]/div[1]/div/form/div[2]/div/div/span/span  个人
        #//*[@id="root"]/div/div/div[2]/div/div/div[3]/div[2]/div[2]/form/div[3]/div/div/span/span 企业
        input.click('xpath', '//*[@id="root"]/div/div/div[2]/div/div/div[1]/div/div/div/div/div[1]/div[1]')
        # 清除当前输入框的值
        input.clear('xpath', '//div[3]/div[1]/div[2]/form/div[2]/div/div/span/span/input')
        input.send_keys('xpath', '//div[3]/div[1]/div[2]/form/div[2]/div/div/span/span/input', 'w154519@163.com')
        # 再次捕获个人邮箱输入值
        a = input.Get_attribute('xpath', '//*[@id="root"]/div/div/div[2]/div/div/div[3]/div[1]/div[2]/form/div[2]/div/div/span/span/input', 'value')
        try:
            assert "w154519@163.com" == a
            print('Test Pass.')
        except Exception as e:
            input.get_windows_img()  # 调用基类截图方法
            print('Test Fail.', format(e))

    #@unittest.skip('不需要执行')
    def test_person_phone(self): #个人手机号输入框
        input = Cloud(self.driver)  # input变量可以调用Cloud得方法
        url = "http://invoice.sunmi.com/?orderSn=AUTOtest0000000008"
        input.open(url)
        time.sleep(2)
        # 切换到个人开票
        input.click('xpath', '//*[@id="root"]/div/div/div[2]/div/div/div[1]/div/div/div/div/div[1]/div[1]')
       #//*[@id="root"]/div/div/div[2]/div/div/div[3]/div[2]/div[2]/form/div[4]/div/div[2]/div/div[1]/div/div/span/span 企业
        #//*[@id="root"]/div/div/div[2]/div/div/div[3]/div[1]/div[2]/form/div[3]/div/div/span/span   个人
        #清空手机号输入框
        input.clear('xpath','//div[3]/div[1]/div[2]/form/div[3]/div/div/span/span/input')
        #输入手机号
        input.send_keys('xpath','//div[3]/div[1]/div[2]/form/div[3]/div/div/span/span/input','13356788888')
        #获取手机号
        a =  input.Get_attribute('xpath','//div[3]/div[1]/div[2]/form/div[3]/div/div/span/span/input','value')
        try:
            assert "13356788888" == a
            print('Test Pass.')
        except Exception as e:
            input.get_windows_img()  # 调用基类截图方法
            print('Test Fail.', format(e))

    #@unittest.skip('不需要执行')
    def test_person_clear(self):#个人清空按钮
        input = Cloud(self.driver)  # input变量可以调用Cloud得方法
        url = "http://invoice.sunmi.com/?orderSn=AUTOtest0000000008"
        input.open(url)
        time.sleep(2)
        # 切换到个人开票
        input.click('xpath', '//*[@id="root"]/div/div/div[2]/div/div/div[1]/div/div/div/div/div[1]/div[1]')
        #输入数据
        input.clear('css_selector', 'input[id="buyerName"]')
        input.send_keys('css_selector', 'input[id="buyerName"]', '吴进城')
        input.clear('xpath',
                    '//div[3]/div[1]/div[2]/form/div[2]/div/div/span/span/input')
        input.send_keys('xpath',
                        '//div[3]/div[1]/div[2]/form/div[2]/div/div/span/span/input',
                        'w154519@163.com')
        input.clear('xpath',
                    '//div[3]/div[1]/div[2]/form/div[3]/div/div/span/span/input')
        # 输入手机号
        input.send_keys('xpath',
                        '//div[3]/div[1]/div[2]/form/div[3]/div/div/span/span/input',
                        '13356788888')
        #点击清空按钮
        input.click('xpath','//div[3]/div[1]/div[2]/form/button')

        #//*[@id="root"]/div/div/div[2]/div/div/div[3]/div[2]/div[2]/button 企业清空
        a = input.Get_attribute('css_selector', 'input[id="buyerName"]','value')
        b = input.Get_attribute('xpath','//form/div[2]/div/div/span/span/input','value')
        c = input.Get_attribute('xpath','//form/div[3]/div/div/span/span/input','value')
        try:
            assert "" == a
            assert "" == b
            assert "" == c
            print('Test Pass.')
        except Exception as e:
            input.get_windows_img()  # 调用基类截图方法
            print('Test Fail.', format(e))

    def test_person_crossing(self): #点击输入框清除图标
        input = Cloud(self.driver)  # input变量可以调用Cloud得方法
        url = "http://invoice.sunmi.com/?orderSn=AUTOtest0000000008"
        input.open(url)
        time.sleep(2)
        # 切换到个人开票
        input.click('xpath', '//*[@id="root"]/div/div/div[2]/div/div/div[1]/div/div/div/div/div[1]/div[1]')
        a = input.Get_attribute('css_selector', 'input[id="buyerName"]', 'value')
        #点击输入框内的清空标识
        input.click('xpath','//*[@id="root"]/div/div/div[2]/div/div/div[3]/div[1]/div[2]/form/div[1]/div/div/span/span/span')

        b = input.Get_attribute('css_selector', 'input[id="buyerName"]', 'value')
        try:
            assert "个人" == a
            assert "" == b
            print('Test Pass.')
        except Exception as e:
            input.get_windows_img()  # 调用基类截图方法
            print('Test Fail.', format(e))



    #@unittest.skip('不需要执行')
    def test_enterprise_fuzzyquery_ok(self):#企业模糊查询
        """
        这里一定要test开头，把测试逻辑代码封装到一个test开头的方法里。
        :return:
         """
        input = Cloud(self.driver)  # 命名一个对象
        url = "http://invoice.sunmi.com/?orderSn=AUTOtest0000000008"
        input.open(url)
        time.sleep(2)
        #切换到企业开票
        input.click('xpath','//*[@id="root"]/div/div/div[2]/div/div/div[1]/div/div/div/div/div[1]/div[2]')
        #打开选填操作
        #input.click('xpath', '//*[@id="root"]/div/div/div[2]/div/div/div[3]/div[2]/div[2]/form/div[4]/div/div[1]')

        # 点击邮件输入框，输入邮件地址
        #input.send_keys('css_selector','#takerEmail','wujincheng@sunmi.com')
        #time.sleep(3)
        # 点击企业全称输入框
        input.send_keys('xpath',
                        '//div[3]/div[2]/div[2]/form/div[1]/div/div/span/div/div[1]/span/input',
                        '腾讯')
        time.sleep(2)
        # 选中模糊查询结果第一个
        input.click('xpath', '//div[3]/div[2]/div[2]/form/div[1]/div/div/span/div/div[2]/div[1]')

        a = input.Get_attribute('xpath',
                           '//div[3]/div[2]/div[2]/form/div[1]/div/div/span/div/div[1]/span/input','value')

        b = input.Get_attribute('xpath', '//*[@id="buyerTaxpayerNum"]','value')
        #将鼠标移动到邮箱地址输入框，因为界面需要滑动
        #input.move_element('_by_xpath(//*[@id="takerEmail"])','_by_xpath(//*[@id="takerEmail"])')
        #self.driver.find_element_by_xpath('//*[@id="takerEmail"]')



        try:
            assert "腾讯科技（北京）有限公司" == a
            assert "91110108772551611J" == b
            #assert "wujincheng@sunmi.com" == c
            print('Test Pass')

        except Exception as e:
            input.get_windows_img()  # 调用基类截图方法
            print('Test Fail.', format(e))

    #@unittest.skip('不需要执行')
    def test_enterprise_email_ok(self): #企业邮箱地址
        input = Cloud(self.driver)  # input变量可以调用Cloud得方法
        url = "http://invoice.sunmi.com/?orderSn=AUTOtest0000000008"
        input.open(url)
        print(0)
        #切换到企业开票
        input.click('xpath', '//*[@id="root"]/div/div/div[2]/div/div/div[1]/div/div/div/div/div[1]/div[2]')
        time.sleep(2)
        print(1)
        #企业邮箱地址输入
        input.send_keys('xpath','// div[3] / div[2] / div[2] / form / div[3] / div / div / span / span /input','wujincheng@sunmi.com')
        time.sleep(2)
        print(2)
        #捕获企业邮箱地址输入框的元素属性
        a = input.Get_attribute('xpath','//  div[3] / div[2] / div[2] / form / div[3] / div / div / span / span /input','value')
        time.sleep(2)
        print(3)
        print(a)
        try:
            assert 'wujincheng@sunmi.com' == a
            print(' Test Pass.')
        except Exception as e:
            input.get_windows_img()  # 调用基类截图方法
            print('Test Fail.', format(e))

    #@unittest.skip('不需要执行')
    def test_enterprise_optional(self):#企业选填按钮
        input = Cloud(self.driver)  # input变量可以调用Cloud得方法
        url = "http://invoice.sunmi.com/?orderSn=AUTOtest0000000008"
        input.open(url)
        # 切换到企业开票
        input.click('xpath', '//*[@id="root"]/div/div/div[2]/div/div/div[1]/div/div/div/div/div[1]/div[2]')
        #点击选填按钮
        time.sleep(1)
        input.click('xpath','//*[@id="root"]/div/div/div[2]/div/div/div[3]/div[2]/div[2]/form/div[4]/div/div[1]')
        #获取元素属性通过查看元素的值的变化来确认选填菜单是否弹出
        time.sleep(3)
        a = input.Get_attribute('xpath','//*[@id="root"]/div/div/div[2]/div/div/div[3]/div[2]/div[2]/form/div[4]/div','class')
        #class="ant-collapse-item ant-collapse-item-active"
        print(a)
        try:
            assert 'ant-collapse-item ant-collapse-item-active' == a
            print(' Test Pass.')
        except Exception as e:
            input.get_windows_img()  # 调用基类截图方法
            print('Test Fail.', format(e))

    #@unittest.skip('不需要执行')
    def test_enterprise_other(self):#选填输入
        input = Cloud(self.driver)  # input变量可以调用Cloud得方法
        url = "http://invoice.sunmi.com/?orderSn=AUTOtest0000000008"
        input.open(url)
        print(0)
        # 切换到企业开票
        input.click('xpath', '//*[@id="root"]/div/div/div[2]/div/div/div[1]/div/div/div/div/div[1]/div[2]')
        time.sleep(1)
        # 点击选填按钮
        input.click('xpath', '//*[@id="root"]/div/div/div[2]/div/div/div[3]/div[2]/div[2]/form/div[4]/div/div[1]')
        #选填输入框输入
        time.sleep(1)
        input.send_keys('xpath','//div[3]/div[2]/div[2]/form/div[4]/div/div[2]/div/div[1]/div/div/span/span/input ','15501236789')#手机号
        a = input.Get_attribute('xpath','//div[3]/div[2]/div[2]/form/div[4]/div/div[2]/div/div[1]/div/div/span/span/input','value')
        time.sleep(1)
        input.send_keys('xpath','//*[@id="buyerAddress"]','上海杨浦区')#企业地址
        b = input.Get_attribute('xpath', '//*[@id="buyerAddress"]', 'value')
        time.sleep(1)
        input.send_keys('xpath', '//*[@id="buyerBankName"] ','上海银行')  # 企业开户银行
        c = input.Get_attribute('xpath', '//*[@id="buyerBankName"]', 'value')
        time.sleep(1)
        input.send_keys('xpath', '//*[@id="buyerBankAccount"] ','1234567812345678')  # 企业开户银行账号
        d = input.Get_attribute('xpath', '//*[@id="buyerBankAccount"] ', 'value')
        time.sleep(1)
        input.send_keys('xpath', '//*[@id="buyerTel"]','01234512')  # 企业电话号码
        e = input.Get_attribute('xpath', '//*[@id="buyerTel"] ', 'value')

        try:
            assert '15501236789' == a
            assert '上海杨浦区' == b
            assert '上海银行' == c
            assert '1234567812345678' == d
            assert '01234512' == e
            print(' Test Pass.')
        except Exception as e:
            input.get_windows_img()  # 调用基类截图方法
            print('Test Fail.', format(e))

    #@unittest.skip('不需要执行')
    def test_enterprise_clear(self):#请空选填按钮
        input = Cloud(self.driver)  # input变量可以调用Cloud得方法
        url = "http://invoice.sunmi.com/?orderSn=AUTOtest0000000008"
        input.open(url)
        print(0)
        # 切换到企业开票
        input.click('xpath', '//*[@id="root"]/div/div/div[2]/div/div/div[1]/div/div/div/div/div[1]/div[2]')
        time.sleep(1)
        # 点击选填按钮
        input.click('xpath', '//*[@id="root"]/div/div/div[2]/div/div/div[3]/div[2]/div[2]/form/div[4]/div/div[1]')
        #选填输入框输入
        time.sleep(1)
        input.send_keys('xpath','//div[3]/div[2]/div[2]/form/div[4]/div/div[2]/div/div[1]/div/div/span/span/input ','15501236789')#手机号
        time.sleep(1)
        input.send_keys('xpath','//*[@id="buyerAddress"]','上海杨浦区')#企业地址
        time.sleep(1)
        input.send_keys('xpath', '//*[@id="buyerBankName"] ','上海银行')  # 企业开户银行
        time.sleep(1)
        input.send_keys('xpath', '//*[@id="buyerBankAccount"] ','1234567812345678')  # 企业开户银行账号
        time.sleep(1)
        input.send_keys('xpath', '//*[@id="buyerTel"]','01234512')  # 企业电话号码
        #点击清空按钮
        input.click('xpath','//div[3]/div[2]/div[2]/button')
        a = input.Get_attribute('xpath','//div[3]/div[2]/div[2]/form/div[4]/div/div[2]/div/div[1]/div/div/span/span/input','value')
        b = input.Get_attribute('xpath', '//*[@id="buyerAddress"]', 'value')
        c = input.Get_attribute('xpath', '//*[@id="buyerBankName"]', 'value')
        d = input.Get_attribute('xpath', '//*[@id="buyerBankAccount"] ', 'value')
        e = input.Get_attribute('xpath', '//*[@id="buyerTel"] ', 'value')
        try:
            assert '' == a
            assert '' == b
            assert '' == c
            assert '' == d
            assert '' == e
            print(' Test Pass.')
        except Exception as e:
            input.get_windows_img()  # 调用基类截图方法
            print('Test Fail.', format(e))

    @unittest.skip('不需要执行')
    def test_enterprise_invoice_fail(self): #企业点击提交
        """
        这里一定要test开头，把测试逻辑代码封装到一个test开头的方法里。
        :return:
         """
        input = Cloud(self.driver)  # input变量可以调用Cloud得方法
        url = "http://invoice.sunmi.com/?orderSn=AUTOtest0000000008"
        input.open(url)
        time.sleep(2)
        #获取url
        nowurl = input.Get_url()
        if nowurl == "http://invoice.sunmi.com/?orderSn=AUTOtest0000000008":
            # 切换到企业开票
            input.click('xpath', '//*[@id="root"]/div/div/div[2]/div/div/div[1]/div/div/div/div/div[1]/div[2]')
            # 点击企业全称输入框
            input.send_keys('xpath',
                            '//div[3]/div[2]/div[2]/form/div[1]/div/div/span/div/div[1]/span/input',
                            '腾讯')
            time.sleep(2)
            # 选中模糊查询结果第一个
            input.click('xpath', '//div[3]/div[2]/div[2]/form/div[1]/div/div/span/div/div[2]/div[1]')
            # 清空企业纳税人识别号,通过点击清空×
            input.click('xpath',
                        '//*[@id="root"]/div/div/div[2]/div/div/div[3]/div[2]/div[2]/form/div[2]/div/div/span/span/span')
            # 输入特定的纳税人识别号，一定失败
            input.send_keys('xpath', '//div[3]/div[2]/div[2]/form/div[2]/div/div/span/span/input',
                            'A12345678912345X12AA')
            # 企业邮箱地址输入
            input.send_keys('xpath', '// div[3] / div[2] / div[2] / form / div[3] / div / div / span / span /input',
                            'wujincheng@sunmi.com')
            time.sleep(2)

            # 点击提交
            input.click('xpath',
                        '//*[@id="root"]/div/div/div[2]/div/div/div[3]/div[2]/div[2]/form/div[5]/div/div/span/button')
            time.sleep(5)
            # 捕获当前文本
            a = input.Get_text('xpath', '//*[@id="root"]/div/div/div/div/div/p')

            try:
                assert a in ('请稍后重试', '开票申请已提交')
                print(' Test Pass.')
            except Exception as e:
                input.get_windows_img()  # 调用基类截图方法
                print('Test Fail.', format(e))
        else:
            # 捕获当前文本
            a = input.Get_text('xpath', '//*[@id="root"]/div/div/div/div/div/p')

            try:
                assert a in ( '开票申请已提交')
                print(' Test Pass.')
            except Exception as e:
                input.get_windows_img()  # 调用基类截图方法
                print('Test Fail.', format(e))

    #@unittest.skip('不需要执行')
    def test_noindent(self):# 不存在的订单
        input = Cloud(self.driver)  # input变量可以调用Cloud得方法
        url = "http://invoice.test.sunmi.com/?orderSn=dsklajlksajfk" # 不存在的订单
        input.open(url)
        time.sleep(2)
        # 捕获当前文本
        a = input.Get_text('xpath', '//*[@id="root"]/div/div/div/div/div/p')

        try:
            assert a == '请求超时，请稍后重试。'
            print(' Test Pass.')
        except Exception as e:
            input.get_windows_img()  # 调用基类截图方法
            print('Test Fail.', format(e))

    def test_enterprise_invoice_OK(self): #企业点击提交
        """
        这里一定要test开头，把测试逻辑代码封装到一个test开头的方法里。
        :return:
         """
        sn = 'T203193B40683'
        orderSn = BasePage.random_32(4)
        amount = 0.01
        shopOrderSn = BasePage.random_32(5)
        Url = "http://api.sunmi.com/api/invoice/app/invoice/1.0/?service=/syncInvoiceOrder&14c4b06b824ec593239362517f538b29=8afe757107b215bb4799880a14b8d4a1&76a2173be6393254e72ffa4d6df1030a=6bf4947b8998e1f9030a719ac3305509"
        r = BasePage.syncInvoiceOrder(amount, sn, shopOrderSn, orderSn, Url)

        input = Cloud(self.driver)  # input变量可以调用Cloud得方法
        url = "http://invoice.sunmi.com/?orderSn="+orderSn
        input.open(url)
        time.sleep(2)
        #获取url
        nowurl = input.Get_url()
        if nowurl == "http://invoice.sunmi.com/?orderSn="+orderSn:
            # 切换到企业开票
            input.click('xpath', '//*[@id="root"]/div/div/div[2]/div/div/div[1]/div/div/div/div/div[1]/div[2]')
            # 点击企业全称输入框
            input.send_keys('xpath',
                            '//div[3]/div[2]/div[2]/form/div[1]/div/div/span/div/div[1]/span/input',
                            '腾讯')
            time.sleep(2)
            # 选中模糊查询结果第一个
            input.click('xpath', '//div[3]/div[2]/div[2]/form/div[1]/div/div/span/div/div[2]/div[1]')

            # 企业邮箱地址输入
            input.send_keys('xpath', '// div[3] / div[2] / div[2] / form / div[3] / div / div / span / span /input',
                            'wujincheng@sunmi.com')
            time.sleep(2)

            # 点击提交
            input.click('xpath',
                        '//*[@id="root"]/div/div/div[2]/div/div/div[3]/div[2]/div[2]/form/div[5]/div/div/span/button')
            time.sleep(5)
            # 捕获当前文本
            a = input.Get_text('xpath', '//*[@id="root"]/div/div/div/div/div/p')

            try:
                assert a in ('开票已完成', '开票申请已提交')
                print(' Test Pass.')
            except Exception as e:
                input.get_windows_img()  # 调用基类截图方法
                print('Test Fail.', format(e))
        else:
            # 捕获当前文本
            a = input.Get_text('xpath', '//*[@id="root"]/div/div/div/div/div/p')

            try:
                assert a in ( '开票申请已提交')
                print(' Test Pass.')
            except Exception as e:
                input.get_windows_img()  # 调用基类截图方法
                print('Test Fail.', format(e))


    #@unittest.skip('数据唯一性还未解决')
    def test_person_submit_ok(self):  # 个人点击提交
        """
        这里一定要test开头，把测试逻辑代码封装到一个test开头的方法里。
        :return:
         """
        sn = 'T203193B40683'
        orderSn = BasePage.random_32(1)
        amount = 0.01
        shopOrderSn = BasePage.random_32(3)
        Url = "http://api.sunmi.com/api/invoice/app/invoice/1.0/?service=/syncInvoiceOrder&14c4b06b824ec593239362517f538b29=8afe757107b215bb4799880a14b8d4a1&76a2173be6393254e72ffa4d6df1030a=6bf4947b8998e1f9030a719ac3305509"
        r = BasePage.syncInvoiceOrder(amount, sn, shopOrderSn, orderSn, Url)

        input = Cloud(self.driver)  # input变量可以调用Cloud得方法
        url = "http://invoice.sunmi.com/?orderSn=" + orderSn
        input.open(url)
        time.sleep(2)
        # 获取url
        nowurl = input.Get_url()
        if nowurl == "http://invoice.sunmi.com/?orderSn=" + orderSn:
            # 切换到个人开票
            input.click('xpath', '//*[@id="root"]/div/div/div[2]/div/div/div[1]/div/div/div/div/div[1]/div[1]')
            # 点击邮件输入框，输入邮件地址
            input.send_keys('xpath', '//div[3]/div[1]/div[2]/form/div[2]/div/div/span/span/input', 'wujincheng@sunmi.com')
            # 点击提交
            input.click('xpath','//form/div[4]/div/div/span/button')#pageobjects包内的方法
            a = input.Get_text('xpath', '//*[@id="root"]/div/div/div/div/div/p')

            try:
                assert a in ('开票已完成', '开票申请已提交')
                print(' Test Pass.')
            except Exception as e:
                input.get_windows_img()  # 调用基类截图方法
                print('Test Fail.', format(e))
        else:
            # 捕获当前文本
            a = input.Get_text('xpath', '//*[@id="root"]/div/div/div/div/div/p')
            try:
                assert a in ('开票申请已提交')
                print(' Test Pass.')
            except Exception as e:
                input.get_windows_img()  # 调用基类截图方法
                print('Test Fail.', format(e))

