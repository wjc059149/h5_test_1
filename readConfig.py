import os
import codecs
import configparser

proDir = os.path.split(os.path.realpath(__file__))[0]
configPath = os.path.join(proDir, "config.ini")


class ReadConfig:
    def __init__(self):
        fd = open(configPath, encoding="UTF-8")
        data = fd.read()
        #  remove BOM
        if data[:3] == codecs.BOM_UTF8:
            data = data[3:]
            file = codecs.open(configPath, "w")
            file.write(data)
            file.close()
        fd.close()

        self.cf = configparser.ConfigParser()
        self.cf.read(configPath, encoding="utf-8-sig")  # 解码ini文件的中文需要utf-8-sig格式

    def get_email(self, name):
        value = self.cf.get("EMAIL", name)
        return value

    def get_http(self, name):
        value = self.cf.get("HTTP", name)
        return value

    def get_mysql(self, name):
        value = self.cf.get("MYSQL", name)
        return value

    # def get_headers(self, name):
    #     value = self.cf.get("HEADERS", name)
    #     return value

    def get_appheader(self):
        value = self.cf.items("APPHEADERS")
        val = dict(value)
        return val

    def get_webheader(self):
        value = self.cf.items('WEBHEADERS')
        val = dict(value)
        return val

    def set_headers(self, name, value):
        self.cf.set("HEADERS", name, value)
        with open(configPath, 'w+') as f:
            self.cf.write(f)

    def get_linux_dir(self, name):
        value = self.cf.get("LINUXDIR", name)
        return value

    def get_db_test(self, name):
        value = self.cf.get("DATABASE_TEST", name)
        return value

    def get_db_uat(self, name):
        value = self.cf.get("DATABASE_UAT", name)
        return value

    def get_case(self, name):
        value = self.cf.get('CASEFILE', name)
        return value

    def get_sheet_doc(self):
        value = self.cf.items('SHEETDOC')
        val = dict(value)
        return val

    def get_callback(self):
        value = self.cf.items('CALLBACK')
        val = dict(value)
        return val


# import configparser
# # 加载现有配置文件
# conf = configparser.ConfigParser()
# conf.read("KKD.ini", encoding="utf-8-sig")  # 此处是utf-8-sig，而不是utf-8
#
# # 以下两种方法读取文件内容效果一样
# print(conf.get('rclog', 'kkdqg_in'))
# print(conf['rclog']['kkdnanx_out2'])