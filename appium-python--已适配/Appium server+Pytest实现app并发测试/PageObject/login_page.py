# _*_ coding：utf-8 _*_
import time
import allure
from Common.base.base_page import Base
from Locators import home_loc, my_loc, login_loc, setting_loc, account_setting_loc


class LoginPage(Base):

    # 点击首页
    @allure.step("点击首页")
    def click_home(self):
        doc = '点击首页'
        self.base_click(home_loc.nen_home, doc=doc)

    # 点击我的
    @allure.step("点击我的")
    def click_my(self):
        doc = '点击我的'
        self.base_click(home_loc.nen_wo, doc=doc)

    # 点击登录页面
    @allure.step("点击登录页面")
    def click_login(self):
        doc = '点击登录页面'
        self.base_click(my_loc.nen_登录, doc=doc)

    # 输入账号
    @allure.step("输入账号")
    def input_username(self, text):
        doc = '输入账号'
        self.base_input_text(login_loc.nen_username, text, doc=doc)

    # 输入密码
    @allure.step("输入密码")
    def input_password(self, text):
        doc = '输入密码'
        self.base_input_text(login_loc.nen_password, text, doc=doc)

    # 点击登录按钮
    @allure.step("点击登录按钮")
    def click_login_btn(self):
        doc = '点击登录按钮'
        self.base_click(login_loc.nen_登录按钮, doc=doc)

    # 点击协议
    @allure.step("点击同意协议")
    def click_agree(self):
        doc = '点击同意协议'
        self.base_click(login_loc.nen_协议, doc=doc)

    # 点击设置
    @allure.step("点击设置")
    def click_set(self):
        doc = '点击设置'
        self.base_click(my_loc.nen_设置, doc=doc)

    # 点击个人设置
    @allure.step("点击个人设置")
    def click_person_set(self):
        doc = '点击个人设置'
        self.base_click(setting_loc.nen_账号设置, doc=doc)

    # 点击登出
    @allure.step("点击登出")
    def click_logout(self):
        doc = '点击等出'
        self.base_click(account_setting_loc.nen_登出, doc=doc)

    # 点击取消退出
    @allure.step("点击取消退出登录")
    def click_cancel(self):
        doc = '点击取消退出登录'
        self.base_click(account_setting_loc.nen_取消退出, doc=doc)

    # 点击确定退出
    @allure.step("点击确定退出登录")
    def click_confirm(self):
        doc = '点击确定退出'
        self.base_click(account_setting_loc.nen_确认退出, doc=doc)

    def long_touch(self, times):
        doc = '长按登录按钮'
        self.base_long_touch(login_loc.nen_登录按钮, times, doc=doc)

    # 判断是否已登录
    @allure.step("判断是否已登录")
    def if_already_login(self):
        doc = '判断是否已登录'
        return not self.base_element_is_exist(my_loc.nen_登录, doc=doc)

    @allure.step("获取错误提示信息")
    def get_error_text(self):
        doc = '获取错误提示信息'
        return self.base_get_text(login_loc.nen_pwd_hint, doc=doc)

    @allure.step("获取toast信息")
    def get_toast_text(self):
        doc = '获取toast信息'
        self.base_get_toast("勾选同意", doc=doc)

    # 退出登录操作
    def do_logout(self):
        # doc = '退出登录操作'
        self.click_my()
        if self.if_already_login() is True:
            self.click_set()
            self.click_person_set()
            self.click_logout()
            self.click_confirm()
            self.sys_keys(4)
            # self.sys_keys(4)

    def app_login(self, user, pwd, agree, success, except_result):
        self.click_login()

        self.input_username(user)
        self.base_click(login_loc.nen_password)
        self.input_password(pwd)
        time.sleep(0.5)
        # get_attribute('checked') 得到 checkbox是否已选中， 未选中为 "false"  注意是字符串
        is_agree = self.base_find_element(login_loc.nen_协议).get_attribute('checked')
        time.sleep(0.5)
        if agree:
            if is_agree == 'false':
                self.click_agree()
            page = self.driver.page_source      # 获取当前页面信息
            self.click_login_btn()
            time.sleep(0.5)
            if page != self.driver.page_source:
                if not success:
                    try:
                        assert except_result in self.get_error_text()
                    except:
                        self.base_get_img_as_png()
                    self.sys_keys(4)
            else:
                try:
                    assert page == self.driver.page_source
                    print("未输入账号或密码")
                except:
                    self.base_get_img_as_png()
                self.sys_keys(4)
        else:
            if is_agree != 'false':
                self.click_agree()
            self.click_login_btn()
            time.sleep(1.5)
            try:
                assert except_result in self.base_get_toast("勾选同意")
            except:
                self.base_get_img_as_png()
                pass
            self.sys_keys(4)

    def app_home(self):
        self.base_swipe_find(home_loc.nen_sort, home_loc.nen_keji)