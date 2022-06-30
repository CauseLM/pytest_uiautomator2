# test_phone.py
class TestPhone:

    def setup(self):
        # 实例化封闭的页面类
        self.home = Home()

    def test_create_contact(self):
        """
        1.桌面点击phone
        2.点击contacts
        3.点击创建联系人
        4.输入联系人信息
        5.保存
        :return:
        """
        creat_page = self.home.goto_phone_recents() \
            .goto_phone_contacts() \
            .goto_create_contact()
        creat_page.input_mesg('test', 'contact', '10086')
        creat_page.save()


class Home(BasePage):
    """
    手机主页面
    """

    # 封装进入通话记录界面的方法，这样就可以在测试用例中实例化后
    # 直接调用此方法就可以完成操作，无需传值，后续维护也只需要维护这个方法
    # 无需要改动测试用例
    def goto_phone_recents(self):
        """
        主页面点击电话图标，进入电话应用界面
        :return: 电话通话记录界面
        """
        with allure.step('桌面点击电话图标'):
            self._driver.press('home')
            self.click(self._config['Home']['phone_bt'])
        return PhoneRecents(self._driver)

    # 另一种方式
    @allure.step(str)
    def test():
        pass

    def test_create_contact(self):
        # 测试用例的文档描述就是allure里的Description
        """
        #这里就是显示在allure里的Description
        1.桌面点击phone
        2.点击contacts
        3.点击创建联系人
        4.输入联系人信息
        5.保存
        :return:
        """

