import unittest
from HTMLTestRunner import HTMLTestRunner
import time
import os,send_email
from framework import report_template,base_page
from readConfig import ReadConfig
http_dir = ReadConfig().get_linux_dir('http_dir')
# 定义输出的文件位置和名字
#DIR = os.path.dirname(os.path.abspath(__file__))[0:15] #当前文件位置
#DIR = './test_case/' #当前文件位置
#将testrunner放在根目录下时，logger的路径也要改为./当目录层

dir = os.getcwd()  #当前文件位置
now = time.strftime("%Y%m%d_%H%M%S", time.localtime(time.time()))
report_title = '电子发票H5的详细测试报告'
report_description = '用例执行结果：'

report_dir = './test_report/'  #../是返回上级目录 ./表示当前目录层
#report_dir = './test_report/'
filename = now + "-report.html"
report_name = report_dir +  filename


summary_name = now + '-summary.html'
summary_path = dir + '/test_report/' + summary_name
summary_html = open(summary_path, 'w', encoding='utf-8')

# discover方法执行测试套件
#testsuite = unittest.defaultTestLoader.discover(start_dir = DIR +'test_case/ ' ,pattern='test*.py',top_level_dir=None)#pattern 是方法的格式，start_dir是待执行用例的目录，


def create_suite():
    """设置获取case的文件夹位置及包含case的文件"""
    suite = unittest.TestSuite()
    #all_cases = unittest.defaultTestLoader.discover( DIR +'test_case ','test*.py',top_level_dir=None)
    all_cases = unittest.defaultTestLoader.discover( './test_case/' ,'test*.py',top_level_dir=None)
    for case in all_cases:
        suite.addTests(case)
    return suite
#这个方法用来将用例组织起来按顺序执行
def generate_report(path, title, description):
    """校验详细测试报告文件是否生成，以及文件内容是否正确"""
    try:
        if filename in os.listdir(dir + '/test_report'):
            # report = open(report_path, 'rb').read()  # 另一种校验方法，内容是否存在
            # if report.find(report_description.encode('utf-8')) >= 1 and report.find(report_title.encode('utf-8')) >= 1
            if base_page.find_word(path, title) and base_page .find_word(path, description):
                print("所有脚本执行完成，报告已生成！")
                return True
            else:
                print("脚本执行出错，报告内容错误！")
                return False
        else:
            print("脚本执行出错，未生成测试报告！")
            return False
    except Exception as e:
        print("脚本执行失败！报错信息如下\n", e)
        return False
"""
with open(report_name, 'wb') as f:
    runner = HTMLTestRunner(stream=f,verbosity=2,title='gateway UI report', description='执行情况' )
    result_run = runner.run(create_suite())
	result.close()  # 关闭报告文件
	"""

import  datetime
def main(h=0, m=0):
    while True:
        # 判断是否达到设定时间，例如0:00
        while True:
            now = datetime.datetime.now()
            # 到达设定时间，结束内循环
            if now.hour == h and now.minute == m:
                break
            # 不到时间就等20秒之后再次检测
            time.sleep(50)
        # 做正事，一天做一次

if __name__ == '__main__':


    result = open(report_name, 'wb')
    runner = HTMLTestRunner(stream=result,
                            title=report_title,
                            description=report_description)
    result_run = runner.run(create_suite())  # 运行测试用例
    result.close()  # 关闭报告文件
    remote_path = http_dir + report_name
    pass_count = result_run.success_count
    fail_count = result_run.failure_count
    error_count = result_run.error_count
    start_time = runner.getReportAttributes(result_run)[0][1]
    duration = runner.getReportAttributes(result_run)[1][1]
    content = report_template.html_summary_content(pass_count, fail_count, error_count, start_time, duration)

    content_report_path = report_template.html_report_path(remote_path)  # 简要测试报告中包含的详情报告地址信息
    if generate_report(report_name, report_title, report_description) is True:  # 执行测试完成，报告生成
        summary_html.write(content)  # 详细测试报告未能上传到服务器，简要报告不包含访问地址
        summary_html.close()
        if int(fail_count) > 0 or int(error_count)> 0:
            send_email.send_email(False, None, report_name, summary_path, True)
        else:
            print("测试通过，未发送邮件")
        #send_email.send_email(False, None, report_name, summary_path, True)
        """
        if base_page.upload_file(report_name) is False:  # 文件上传到服务器失败，将文件放在邮件附件中发送出去
            summary_html.write(content)  # 详细测试报告未能上传到服务器，简要报告不包含访问地址
            summary_html.close()
            send_email.send_email(False, None, report_name, summary_path, True)
        else:
            summary_html.write(content+content_report_path)  # 详细测试报告上传到服务器，简要报告包含访问地址

            summary_html.close()
            send_email.send_email(True, remote_path, report_name, summary_path, False)  # 邮件不发送附件
            """
    else:  # 报告生成失败，将result文件夹下最新文件以附件方式邮件发送，不再上传到服务器
        print("报告生成失败")
        #send_email.send_email(False, None, None, None, True)
        if int(fail_count) > 0 or int(error_count)> 0:
            send_email.send_email(False, None, report_name, summary_path, True)
        else:
            print("测试通过，未发送邮件")


#send_email.send_email(False, None, None, None, True)
