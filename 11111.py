import readConfig
#创建一个读取配置文件的实例
readconfig = readConfig.ReadConfig()
#读取config文件中的MYSQL文件内容

host = readconfig.get_mysql("host")
user = readconfig.get_mysql("user")
password = readconfig.get_mysql("password")
db = readconfig.get_mysql("db")
port = readconfig.get_mysql("port")
charset = readconfig.get_mysql("charset")

print(type(int(port)),port)
