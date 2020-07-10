import time
from selenium.webdriver.support.wait import WebDriverWait


class Base:
    def __init__(self, driver):
        self.driver = driver

    def base_find_element(self, loc, timeout=30, poll=0.5):
        """
        :param loc:
        :param timeout:
        :param poll:
        :return:
        """
        return WebDriverWait(self.driver, timeout=timeout, poll_frequency=poll).until(lambda x: x.find_element(*loc))

    # 点击方法
    def base_click(self, loc):
        self.base_find_element(loc).click()

    # 输入方法
    def base_input(self, loc, value):
        el = self.base_find_element(loc)
        el.clear()
        el.send_keys(value)

    # 获取文本方法
    def base_get_text(self, loc):
        return self.base_find_element(loc).text

    # 截图方法
    def base_printscreen(self):
        self.driver.get_screenshot_as_file('../img/{}.png'.format(time.strftime('%Y-%m-%d %H-%M-%S')))

    # 封装判断元素是否存在
    def base_element_is_exist(self, loc):
        try:
            self.base_find_element(loc, timeout=2)
            # 找到元素
            return True
        except:
            # 没有找到元素
            return False