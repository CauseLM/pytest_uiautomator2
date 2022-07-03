# _*_ coding：utf-8 _*_

from appium import webdriver
import yaml
from Config.root_config import CONFIG_PATH


class BaseDriver(object):
    """获取driver"""

    def __init__(self, device_info):
        with open(CONFIG_PATH, 'r') as f:
            self.data = yaml.load(f, Loader=yaml.FullLoader)
        self.device_info = device_info

    def get_base_driver(self):
        desired_caps = {
            'platformName': self.data['platformName'],
            'platformVerion': self.data['platformVersion'],
            'udid': self.device_info[1],
            "deviceName": self.device_info[1],
            'noReset': self.data['noReset'],
            'appPackage': self.data['appPackage'],
            'appActivity': self.data['appActivity'],
            "unicodeKeyboard": True,
            'automationName': 'UiAutomator2'
        }
        print(desired_caps)
        url = f"http://{self.data['ip']}:{self.device_info[0]}/wd/hub"
        print(url)
        driver = webdriver.Remote(url, desired_caps)
        return driver


if __name__ == '__main__':
    pass
