import unittest
from time import sleep
from parameterized import parameterized
from page.page_login import PageLogin
from tools.read_json import read_json
from base.get_driver import GetDriver
from tools.reda_txt import read_txt


def get_data():
    # datas = read_json('login.json')
    # arrs = []
    # for data in datas.values():
    #     arrs.append((data.get('username'), data.get('password'), data.get('verify_code'), data.get('expect_result'),
    #                  data.get('success')))
    # return arrs

    datas = read_txt('login.txt')
    arrs = []
    for data in datas:
        arrs.append(tuple(data.strip().split(',')))
    return arrs


class TestLogin(unittest.TestCase):
    login = None

    @classmethod
    def setUpClass(cls):
        cls.login = PageLogin(GetDriver.get_driver())
        cls.login.page_login_link()

    @classmethod
    def tearDownClass(cls):
        sleep(2)
        GetDriver.quit_driver()

    @parameterized.expand(get_data())
    def test_login(self, username, pwd, code, expect, success):
        self.login.page_login(username, pwd, code)
        # 注意: 如果读取的是txt文件,那么结果是字符串True,读取的是json格式则是bool值True
        # if success:
        if success == 'True':
            sleep(2)
            try:
                # 判断安全退出是否存在
                print(self.login.page_login_success())
                self.assertTrue(self.login.page_login_success())
                sleep(3)
                # 点击退出
                self.login.page_click_logout()
                try:
                    self.assertTrue(self.login.page_logout_success())
                except:
                    # 截图
                    self.login.page_printscreen()
                # 点击登录按钮
                self.login.page_login_link()
            except:
                # 截图
                self.login.page_printscreen()
        else:
            msg = self.login.page_err_text()
            try:
                self.assertEqual(msg, expect)
            except AssertionError:
                self.login.page_printscreen()

            # sleep(2)

            self.login.page_err_tooltip_confirm()