"""
    测试员工模块的增删改查实现
"""

# 导包
import logging
import unittest
import requests

# 创建测试类
# from pip.utils import logging

import app
from api.emp_api import EmpCRUD


class Test_Emp(unittest.TestCase):
    # 初始化函数
    def setUp(self) -> None:
        self.session = requests.session()
        self.emp_obj = EmpCRUD()

    # 资源卸载函数
    def tearDown(self) -> None:
        self.session.close()

    # 测试函数-增
    #  token:
    # token 提取
    # token
    def test_add(self):
        logging.info("新增信息")
        # 请求
        response = self.emp_obj.add(self.session, username="tomatoabab33",
                                    mobile="15108571455")
        # 断言
        print("-" * 100)
        print("员工新增响应结果", response.json())
        self.assertEqual(True, response.json().get("success"))
        self.assertEqual(10000, response.json().get("code"))
        self.assertIn("操作成功", response.json().get("message"))
        # 提取ID
        id1 = response.json().get("data").get("id")
        app.USER_ID = id1
        print("新增员工id:", id1)

    # 测试函数-改
    def test_update(self):
        logging.info("修改信息")
        # 请求
        response = self.emp_obj.update(self.session, app.USER_ID, "potapo123")
        print("-" * 100)
        print("修改后的响应结果", response.json())
        # 断言
        self.assertEqual(True, response.json().get("success"))
        self.assertEqual(10000, response.json().get("code"))
        self.assertIn("操作成功", response.json().get("message"))

    # 测试函数-查
    def test_get(self):
        logging.info("查询信息")
        response = self.emp_obj.get(self.session, app.USER_ID)
        print("-" * 100)
        print("查询的响应结果", response.json())
        # 断言
        self.assertEqual(True, response.json().get("success"))
        self.assertEqual(10000, response.json().get("code"))
        self.assertIn("操作成功", response.json().get("message"))

    # 测试函数-删
    def test_delete(self):
        logging.info("删除信息")
        response = self.emp_obj.delete(self.session, app.USER_ID)
        print("-" * 100)
        print("删除后响应结果", response.json())
        # 断言
        self.assertEqual(True, response.json().get("success"))
        self.assertEqual(10000, response.json().get("code"))
        self.assertIn("操作成功", response.json().get("message"))
