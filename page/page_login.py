from base.base import Base
import page


class PageLogin(Base):
    # 点击登录链接
    def page_login_link(self):
        self.base_click(page.login_link)

    def page_input_username(self, username):
        self.base_input(page.login_username, username)

    def page_input_pwd(self, pwd):
        self.base_input(page.login_pwd, pwd)

    def page_input_code(self, code):
        self.base_input(page.login_verify_code, code)

    def page_login_btn(self):
        self.base_click(page.login_btn)

    def page_err_text(self):
        return self.base_get_text(page.login_err_text)

    def page_err_tooltip_confirm(self):
        self.base_click(page.login_err_tooltip_confirm)

    def page_printscreen(self):
        self.base_printscreen()

    # 点击安全退出 退出使用
    def page_click_logout(self):
        self.base_click(page.login_logout)

    # 判断是否登录成功
    def page_login_success(self):
        return self.base_element_is_exist(page.login_logout)

    # 判断退出登录是否成功
    def page_logout_success(self):
        return self.base_element_is_exist(page.login_link)

    # 组合业务方法
    def page_login(self, username, pwd, code):
        self.page_input_username(username)
        self.page_input_pwd(pwd)
        self.page_input_code(code)
        self.page_login_btn()