# base_page.py
# �豸�ţ�ͨ��conftest.py�ļ���ȡ���������еĲ���
SN = None


class _Driver:
    """
    ������drvier����һ���࣬
    """
    _log: logging = None
    _driver: u2.Device = None
    _instancn = None
    _isinit = False

    def __init__(self):
        if not self._isinit:
            self._log = get_logger(SN)
            self._driver = u2.connect(SN)
            self._log.info('connect done')
            self._log.info(f'devices info:{self._driver.device_info}\n{self._driver.info}')
            # ��ȡ�豸���ԣ����������״̬������������
            if not self._driver.info['screenOn']:
                # ����
                self._driver.unlock()
                self._log.info('device is unlock')
            else:
                self._log.info('device is screen on')
            self._isinit = True

    def get_driver_and_log(self):
        # ���ش����driver��logʵ��
        return self._driver, self._log

    def __new__(cls, *args, **kwargs):
        if cls._instancn is None:
            cls._instancn = super().__new__(cls, *args, **kwargs)
        return cls._instancn


class BasePage:
    # �豸
    _driver: u2.Device = None
    # �����ļ�
    _config = read_yaml(os.path.join(os.getcwd(), 'data', 'test_data.yaml'))
    # log
    _log: logging = None

    def __init__(self, driver=None):
        """
        ��ʼ��driver,����ʱ����homepage����ʵ����ʱδ����driver
        ����½�һ��driver�������ʹ�ô����driver
        """
        if driver is None:
            # ��ʼ��log�������ڵڶ��ε���ʱ����ʵ������
            self._driver, self._log = _Driver().get_driver_and_log()
            self._log = get_logger(SN)
            self._driver = u2.connect(SN)
            self._log.info('connect done')
            # self._log.info("device info:", *self._driver.info)

            # ��ȡ�豸���ԣ����������״̬������������
            if not self._driver.info['screenOn']:
                # ����
                self._driver.unlock()
                self._log.info('device is unlock')
            else:
                self._log.info('device is screen on')

            self._driver.press('home')
        else:
            self._driver = driver

    def __find_ele(self, locator: str):
        """
        ����Ԫ�أ��Զ��ж�Ԫ�����ԣ�����driver���ң� �����������
        ���ز��ҵ��Ķ�����������uiautomator2�����Ƿ����ҵ�Ԫ�ض��᷵��һ������
        ��Ҫͨ���ж϶��󳤶Ȳ��ܾ����Ƿ��ҵ�Ԫ��
        :param locator:
        :return:
        """

        ele = []
        # ����Ԫ��ǰ�ȴ���ʹҳ�������ɣ���ִֹ��̫�����λ����Ԫ�ػ��߹���Ķ�λ��Ԫ��
        time.sleep(3)
        # ����Ԫ�أ������ҵ��Ķ���
        self._log.debug('try find element %s' % locator)
        if locator.startswith('//') and len(self._driver.xpath(locator)) > 0:
            ele = self._driver.xpath(locator)
            self._log.debug('Found ele by XPath')
            return ele
        elif ':id/' in locator and len(self._driver(resourceId=locator)) > 0:
            ele = self._driver(resourceId=locator)
            self._log.debug('Found ele by resourceId')
        elif len(self._driver(text=locator)) > 0:
            ele = self._driver(text=locator)
            self._log.debug('Found ele by text')
        elif len(self._driver(description=locator)) > 0:
            ele = self._driver(description=locator)
            self._log.debug('Found ele by description')
        elif len(self._driver(className=locator)) > 0:
            ele = self._driver(className=locator)
            self._log.debug('Found ele by className')
        return ele

    def find(self, locator: str, index=0):
        """
        ����һ��Ԫ�أ��е�������ƣ������༰�ⲿ�����
        :param locator:
        :param index:
        :return:
        """
        try:
            # ����ָ����Ԫ��
            # �ҵ��������쳣�������ΪĬ��0
            ele = self.__find_ele(locator)
            if len(ele) == 0:
                # �׳��쳣
                raise ValueError('not find ele')
            else:
                self._error_count = 0
                # ��������Ϊ��xpath�в������±ֻ꣬�᷵��һ��Ԫ��
                # ���жϻ���ɴ���
                if len(ele) > 1:
                    return ele[index]
                return ele
        except Exception as e:
            self._log.debug('find ele error,try black list')
            # �ж��쳣��������Ƿ�ﵽ���ֵ,�ﵽ�򱨴�
            self._log.info(f'erorr count is {self._error_count}')
            if self._error_count > self._error_max_count:
                raise e
            self._error_count += 1
            # ����������б��в��ң����ҵ��͵��
            for black in self._black_list:
                # �����б��еĵ���
                self._log.info(f'try find {black}')
                # ���Һ�����Ԫ��
                ele = self.__find_ele(black)
                if len(ele) > 0:
                    ele.click()
                    self._log.debug('raise done')
                    # �����굯��󣬵���������������Ŀ��Ԫ��
                    # ����һ��Ҫд��if���棬��Ȼ�����
                    return self.find(locator, index)
            self._log.info('no black text in this page')
            # ����б���Ҳû�ҵ����򱨴�,����ͼ
            self.screenshot()
            raise e

    def click(self, name, index=0):
        """
        ��װ���
        :param name: ��λ���ַ���
        :param index: ��λ�±꣬���ж����ͬԪ��ʱʹ��
        :return:
        """
        self.find(name, index).click()

    def sendkey(self, name, mesg, index=0):
        """
        ��װ�����ַ�
        :param name: ��λ���ַ���
        :param mesg: ��Ҫ������ı�
        :param index: ��λ�±꣬���ж����ͬԪ��ʱʹ��
        :return:
        """
        self.find(name, index).send_keys(mesg)

    def screenshot(self):
        """
        ��ͼ�����ӵ����Ա�����
        :return:
        """
        picture_file = os.path.join(os.getcwd(), 'tmp_picture.png')
        try:
            # ��ͼ
            self._driver.screenshot(picture_file)
            # �����ɵĽ�ͼ���ӵ����Ա����У�����һ���ļ���ȡ��ʽһ��ҪΪ rb
            # �������ɲ��Ա�����ͼƬ�޷��򿪵Ĵ���
            allure.attach(open(picture_file, 'rb').read(),
                          'Fail Screenshot',
                          attachment_type=allure.attachment_type.PNG)
            self._log.info('screenshot success')
            os.remove(picture_file)
        except Exception as e:
            self._log.exception('screenshot fail')
            raise e



# all_phone_page.py
class PhoneRecents(BasePage):
    # ͨ����¼����

    pass


class PhoneContact(BasePage):
    # ��ϵ���б����
    def goto_create_contact(self):
        """
        ���������ϵ��
        :return: ������ϵ�˽���
        """
        # Ԫ�ز�����װ��ҳ������
        self.click(Ԫ�ض�λ)
        # ����ҳ���࣬���뵱ǰ��driver,����ʵ�����driver���������driver��ʼ���Ĵ���
        return PhoneCreateContact(self._driver)

    pass


class PhoneCreateContact(BasePage):
    # ������ϵ�˽���
    pass


# home_page.py
class Home(BasePage):
    """
    �ֻ���ҳ��
    """

    def goto_phone_recents(self):
        """
        ��ҳ�����绰ͼ�꣬����绰Ӧ�ý���
        :return: �绰ͨ����¼����
        """
        self._driver.press('home')
        self.click(self._config['Home']['phone_bt'])
        return PhoneRecents(self._driver)
