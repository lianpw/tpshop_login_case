from selenium.webdriver.common.by import By

# 页面url地址信息
url = 'http://localhost'

# 以下为登录页面元素配置信息
login_link = By.PARTIAL_LINK_TEXT, '登录'

login_username = By.CSS_SELECTOR, '#username'

login_pwd = By.CSS_SELECTOR, '#password'

login_verify_code = By.CSS_SELECTOR, '#verify_code'

login_btn = By.CSS_SELECTOR, '.J-login-submit'

login_err_text = By.CSS_SELECTOR, '.layui-layer-content'

login_err_tooltip_confirm = By.CSS_SELECTOR, '.layui-layer-btn0'

login_logout = By.PARTIAL_LINK_TEXT, '安全退出'
