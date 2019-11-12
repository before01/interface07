"""
    # 设计员工模块的增删改查
"""
import app


class EmpCRUD:
    # 初始化函数---封装资源路径
    def __init__(self):
        self.emp_url = app.BASE_URL + "/api/sys/user"

    # 增-请求
    def add(self, session, username=None, mobile=None, timeOfEntry=None,
            formOfEmployment=None, workNumber=None, departmentName=None,
            departmentId=None, correctionTime=None):
        my_add_data = {"username": username,
                       "mobile": mobile,
                       "timeOfEntry": timeOfEntry,
                       "formOfEmployment": formOfEmployment,
                       "workNumber": workNumber,
                       "departmentName": departmentName,
                       "departmentId": departmentId,
                       "correctionTime": correctionTime}
        return session.post(self.emp_url, json=my_add_data,
                            headers={"Authorization": "Bearer " + app.TOKEN})

    # 改请求
    def update(self, session,id2,username):
        return session.put(self.emp_url + "/" + id2, json={"username": username},
                           headers={"Authorization": "Bearer " + app.TOKEN})

    # 查请求
    def get(self, session,id1):
        return session.get(self.emp_url + "/" + id1,
                           headers={"Authorization": "Bearer " + app.TOKEN})

    # 删-请求
    def delete(self,session,id1):
        return session.delete(self.emp_url + "/" + id1,
                           headers={"Authorization": "Bearer " + app.TOKEN})
