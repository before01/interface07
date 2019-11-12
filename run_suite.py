"""
    测试套件:
            按需求组合被执行的测试函数
"""

# 导包
import unittest

import app
from case.test_ihrm_login import Test_Login
from case.test_ihrm_emp import Test_Emp
from tools.HTMLTestRunner import HTMLTestRunner
# 实例化套件对象 组织被执行的测试函数

suite = unittest.TestSuite()
suite.addTest(Test_Login("test_login_success"))
suite.addTest(Test_Emp("test_add"))   #新增员工的测试函数
suite.addTest(Test_Emp("test_update"))   #员工修改的测试函数
suite.addTest(Test_Emp("test_get"))    #组织员工查询的测试函数
suite.addTest(Test_Emp("test_delete"))  #删除员工的测试函数
# 执行套件,生成测试报告
# runner = unittest.TextTestRunner()

with open(app.PRO_PATH + "/report/report.html","wb") as f:
    runner = HTMLTestRunner(f,title="人力资源管理系统测试报告",description="增删改查")
    runner.run(suite)

