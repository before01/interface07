"""
    封装类:
        请求函数
"""
import app


class Login:

    # 封装 url
    def __init__(self):
        self.login_url = app.BASE_URL + "/api/sys/login"

    def login(self, session, mobile, password):
        my_login = {"mobile": mobile,
                    "password": password}
        return session.post(self.login_url, json=my_login)


