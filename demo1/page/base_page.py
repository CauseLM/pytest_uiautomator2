# base_page.py
# 设备号，通过conftest.py文件读取来自命令行的参数
SN = None


class _Driver:
    """
    单独将drvier建立一个类，
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
            # 获取设备属性，如果是灭屏状态，则亮屏解锁
            if not self._driver.info['screenOn']:
                # 解锁
                self._driver.unlock()
                self._log.info('device is unlock')
            else:
                self._log.info('device is screen on')
            self._isinit = True

    def get_driver_and_log(self):
        # 返回此类的driver和log实例
        return self._driver, self._log

    def __new__(cls, *args, **kwargs):
        if cls._instancn is None:
            cls._instancn = super().__new__(cls, *args, **kwargs)
        return cls._instancn


class BasePage:
    # 设备
    _driver: u2.Device = None
    # 配置文件
    _config = read_yaml(os.path.join(os.getcwd(), 'data', 'test_data.yaml'))
    # log
    _log: logging = None

    def __init__(self, driver=None):
        """
        初始化driver,运行时进入homepage，当实例化时未传入driver
        则会新建一个driver，否则就使用传入的driver
        """
        if driver is None:
            # 初始化log，这里在第二次调用时，会实例不到
            self._driver, self._log = _Driver().get_driver_and_log()
            self._log = get_logger(SN)
            self._driver = u2.connect(SN)
            self._log.info('connect done')
            # self._log.info("device info:", *self._driver.info)

            # 获取设备属性，如果是灭屏状态，则亮屏解锁
            if not self._driver.info['screenOn']:
                # 解锁
                self._driver.unlock()
                self._log.info('device is unlock')
            else:
                self._log.info('device is screen on')

            self._driver.press('home')
        else:
            self._driver = driver

    def __find_ele(self, locator: str):
        """
        查找元素，自动判断元素属性，调用driver查找， 不供子类调用
        返回查找到的对象，这里由于uiautomator2不管是否有找到元素都会返回一个对象
        需要通过判断对象长度才能决断是否找到元素
        :param locator:
        :return:
        """

        ele = []
        # 查找元素前等待，使页面加载完成，防止执行太快而定位不到元素或者过早的定位到元素
        time.sleep(3)
        # 查找元素，返回找到的对象
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
        返回一个元素，有弹框处理机制，供子类及外部类调用
        :param locator:
        :param index:
        :return:
        """
        try:
            # 返回指定的元素
            # 找到后设置异常处理次数为默认0
            ele = self.__find_ele(locator)
            if len(ele) == 0:
                # 抛出异常
                raise ValueError('not find ele')
            else:
                self._error_count = 0
                # 这里是因为在xpath中不会有下标，只会返回一个元素
                # 不判断会造成错误
                if len(ele) > 1:
                    return ele[index]
                return ele
        except Exception as e:
            self._log.debug('find ele error,try black list')
            # 判断异常处理次数是否达到最大值,达到则报错
            self._log.info(f'erorr count is {self._error_count}')
            if self._error_count > self._error_max_count:
                raise e
            self._error_count += 1
            # 到弹框处理的列表中查找，能找到就点击
            for black in self._black_list:
                # 遍历列表中的弹框
                self._log.info(f'try find {black}')
                # 查找黑名单元素
                ele = self.__find_ele(black)
                if len(ele) > 0:
                    ele.click()
                    self._log.debug('raise done')
                    # 处理完弹框后，调用自身，继续查找目标元素
                    # 这里一定要写在if里面，不然会造成
                    return self.find(locator, index)
            self._log.info('no black text in this page')
            # 如果列表中也没找到，则报错,并截图
            self.screenshot()
            raise e

    def click(self, name, index=0):
        """
        封装点击
        :param name: 定位的字符串
        :param index: 定位下标，当有多个相同元素时使用
        :return:
        """
        self.find(name, index).click()

    def sendkey(self, name, mesg, index=0):
        """
        封装输入字符
        :param name: 定位的字符串
        :param mesg: 需要输入的文本
        :param index: 定位下标，当有多个相同元素时使用
        :return:
        """
        self.find(name, index).send_keys(mesg)

    def screenshot(self):
        """
        截图并附加到测试报告中
        :return:
        """
        picture_file = os.path.join(os.getcwd(), 'tmp_picture.png')
        try:
            # 截图
            self._driver.screenshot(picture_file)
            # 将生成的截图附加到测试报告中，这里一定文件读取方式一定要为 rb
            # 否则会造成测试报告中图片无法打开的错误
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
    # 通话记录界面

    pass


class PhoneContact(BasePage):
    # 联系人列表界面
    def goto_create_contact(self):
        """
        点击创建联系人
        :return: 创建联系人界面
        """
        # 元素操作封装到页面类中
        self.click(元素定位)
        # 返回页面类，传入当前的driver,避免实例多个driver，后面会有driver初始化的代码
        return PhoneCreateContact(self._driver)

    pass


class PhoneCreateContact(BasePage):
    # 创建联系人界面
    pass


# home_page.py
class Home(BasePage):
    """
    手机主页面
    """

    def goto_phone_recents(self):
        """
        主页面点击电话图标，进入电话应用界面
        :return: 电话通话记录界面
        """
        self._driver.press('home')
        self.click(self._config['Home']['phone_bt'])
        return PhoneRecents(self._driver)
