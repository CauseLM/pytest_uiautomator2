# test_phone.py
class TestPhone:

    def setup(self):
        # ʵ������յ�ҳ����
        self.home = Home()

    def test_create_contact(self):
        """
        1.������phone
        2.���contacts
        3.���������ϵ��
        4.������ϵ����Ϣ
        5.����
        :return:
        """
        creat_page = self.home.goto_phone_recents() \
            .goto_phone_contacts() \
            .goto_create_contact()
        creat_page.input_mesg('test', 'contact', '10086')
        creat_page.save()


class Home(BasePage):
    """
    �ֻ���ҳ��
    """

    # ��װ����ͨ����¼����ķ����������Ϳ����ڲ���������ʵ������
    # ֱ�ӵ��ô˷����Ϳ�����ɲ��������贫ֵ������ά��Ҳֻ��Ҫά���������
    # ����Ҫ�Ķ���������
    def goto_phone_recents(self):
        """
        ��ҳ�����绰ͼ�꣬����绰Ӧ�ý���
        :return: �绰ͨ����¼����
        """
        with allure.step('�������绰ͼ��'):
            self._driver.press('home')
            self.click(self._config['Home']['phone_bt'])
        return PhoneRecents(self._driver)

    # ��һ�ַ�ʽ
    @allure.step(str)
    def test():
        pass

    def test_create_contact(self):
        # �����������ĵ���������allure���Description
        """
        #���������ʾ��allure���Description
        1.������phone
        2.���contacts
        3.���������ϵ��
        4.������ϵ����Ϣ
        5.����
        :return:
        """

