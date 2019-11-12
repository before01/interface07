"""
封装unittest
"""

# 导包
import json
import unittest
import requests

import app
from api.login_api import Login

# 参数化 --导包
from parameterized import parameterized


# 参数化 --解析
def read_json_file():
    # 创建空列表
    data = []
    # 解析文件流
    with open(app.PRO_PATH + "/data/tp_login_data.json", "r", encoding="utf-8") as f:
        for v in json.load(f).values():
            mobile = v.get("mobile")
            password = v.get("password")
            success = v.get("success")
            code = v.get("code")
            message = v.get("message")
            ele = (mobile, password, success, code, message)
            data.append(ele)
    # 返回列表
    return data


# 创建测试类:


class Test_Login(unittest.TestCase):

    def setUp(self) -> None:
        # 初始化 session
        self.session = requests.session()

        # 初始化api
        self.login_obj = Login()

    def tearDown(self) -> None:
        self.session.close()

    # 测试函数--登录
    # 参数化
    @parameterized.expand(read_json_file())
    def test_login(self, mobile, password, success, code, message):
        # 参数化
        print("-" * 100)
        # print((mobile, password, success, code, message))
        # 请求业务
        response = self.login_obj.login(self.session, mobile, password)
        print("登录响应结果:", response.json())
        # 断言业务
        self.assertEqual(success, response.json().get("success"))
        self.assertEqual(code, response.json().get("code"))
        self.assertIn(message, response.json().get("message"))

    # 编写登录成功测试函数
    def test_login_success(self):
        # 请求
        response = self.login_obj.login(self.session, "13800000002", "123456")
        # 断言
        print("登录成功响应结果", response.json())
        self.assertEqual(True, response.json().get("success"))
        self.assertEqual(10000, response.json().get("code"))
        self.assertIn("操作成功", response.json().get("message"))
        # 提取token
        token = response.json().get("data")
        print("登录后响应token:",token)
        # 允许其他文件调用token,可扩大作用域(app.py定义一个变量)
        app.TOKEN = token


if __name__ == '__main__':
    unittest.main()
