"""
    封装数据
    框架搭建:
        核心:api + case + data
            api:封装请求业务
            case:集成unittest 实现,调用api
            data:封装测试数据

        报告:report + tools + run_suite.py

        配置: app.py

        日志:log


"""
import os
import logging.handlers

# 封装接口的 URL 前缀

BASE_URL = "http://182.92.81.159"

# 封装项目路径
FILE_PATH = os.path.abspath(__file__)
PRO_PATH = os.path.dirname(FILE_PATH)
print(PRO_PATH)
# 代码简化
# PRO_PATH2 = os.getcwd()
# print(PRO_PATH2)

# 定义一个变量

TOKEN = None
USER_ID = None


# 日志
def my_log_config():
    # 获取日志对象
    logger = logging.getLogger()
    # 为日志对象设置日志输出级别
    logger.setLevel(logging.INFO)
    # 设置日志的输出目标
    sh = logging.StreamHandler()
    th = logging.handlers.TimedRotatingFileHandler(PRO_PATH + "/log/ihrm.log",
                                                   when="h",
                                                   interval=12,
                                                   backupCount=10,
                                                   encoding="utf-8")
    # 指定输出格式
    formatter = logging.Formatter(
        "%(asctime)s %(levelname)s [%(name)s] [%(filename)s(%(funcName)s:%(lineno)d)] - %(message)s")
    # 组合
    sh.setFormatter(formatter)
    th.setFormatter(formatter)
    logger.addHandler(sh)
    logger.addHandler(th)


# 调用
# my_log_config()
# logging.info("IHRM增删改查")
# logging.warning("warning")
