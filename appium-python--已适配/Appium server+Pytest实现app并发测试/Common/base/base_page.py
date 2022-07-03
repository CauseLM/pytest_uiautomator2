# _*_ coding：utf-8 _*_
import datetime
import time
import allure
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from Config.root_config import IMAGE_DIR


class Base(object):

    def __init__(self, common_driver):
        self.driver = common_driver[0]
        self.log = common_driver[1]

    # 查找单个元素
    def base_find_element(self, location, doc='', timeout=20, poll=0.5):
        """

        :param location: 要查找元素的位置信息
        :param doc:描述该日志信息
        :param timeout: 显示等待的超时时间
        :param poll: 未找到元素时的查找频率
        :return: 返回找到的元素信息
        """
        try:
            # start = datetime.datetime.now()
            # 初始化显示等待信息
            wait = WebDriverWait(self.driver, timeout=timeout, poll_frequency=poll)
            element = wait.until(lambda x: x.find_element(*location))
            # end = datetime.datetime.now()
            # wait_time = (end - start).seconds
            # self.Output.info('{0},查找页面元素：{2}，共耗时{1}S'.format(doc, wait_time, location))
            return element
        except TimeoutError:
            self.log.info(f'{doc}：查找页面元素：{location} 失败！！！')
            raise

    # 查找多个元素
    def base_find_elements(self, location, doc='', timeout=20, poll=0.5):
        try:
            # start = datetime.datetime.now()
            # 初始化显示等待信息
            wait = WebDriverWait(self.driver, timeout=timeout, poll_frequency=poll)
            element = wait.until(lambda x: x.find_elements(*location))
            # end = datetime.datetime.now()
            # wait_time = (end - start).seconds
            # self.Output.info('{0},查找页面元素：{1}，共耗时i{2}S'.format(doc, location, wait_time))
            return element
        except TimeoutError:
            self.log.info(f'{doc}：查找页面元素：{location} 失败！！！')
            raise

    # 点击指定元素
    def base_click(self, location, doc=''):
        self.base_find_element(location).click()
        self.log.info(f"{doc}：点击页面元素：{location}")

    # 在指定元素输入文本
    def base_input_text(self, location, text, doc='', clear=True):
        ele = self.base_find_element(location)
        if clear is True:
            ele.clear()
            self.log.info('清空内容')
        ele.send_keys(text)
        self.log.info(f"{doc}：给元素：{location} 输入：{text}")

    # 获取指定元素文本
    def base_get_text(self, location, doc=''):
        text = self.base_find_element(location).text
        self.log.info(f"{doc}：获取元素：{location} 文本内容：{text}")
        return text

    # 截图
    def base_get_img_as_png(self, doc=''):
        self.driver.get_screenshot_as_file(IMAGE_DIR + f"img_{time.strftime('%Y_%m_%d-%H%M%S')}.png")
        self.log.info(f"{doc}：截图成功")

    # 判断元素是否存在
    def base_element_is_exist(self, location, doc=''):
        try:
            self.base_find_element(location, timeout=2)
            self.log.info(f"{doc}：页面元素：{location} 存在")
            # 如果2S内找到该元素，则返回True
            return True
        except Exception:
            self.log.info(f"{doc}：页面元素：{location} 不存在")
            return False

    # 判断按钮是否可用
    def base_btn_is_enabled(self, location, doc=''):
        flag = self.base_find_element(location).is_enabled
        self.log.info(f"{doc}：页面元素：{location} is enabled")
        return flag

    # 判断元素是否已选中
    def base_is_selected(self, location, doc=''):
        flag = self.base_find_element(location).is_selected()
        self.log.info(f"{doc}：页面元素：{location} 已选中")
        return flag

    # 判断元素是否显示
    def base_is_displayed(self, location, doc=''):
        flag = self.base_find_element(location).is_displayed()
        self.log.info(f"{doc}：页面元素：{location} 可以显示在页面中")
        return flag

    # 获取元素属性值
    def base_get_element_attribute(self, location, name, doc=''):
        txt = self.base_find_element(location).get_attribute(name=name)
        self.log.info(f"{doc}：页面元素：{location} 的{name}属性是：{txt}")
        return txt

    # 获取当前窗口句柄
    def base_get_now_window(self, doc=''):
        handle = self.driver.current_window_handle
        self.log.info(f"{doc}：当前窗口句柄：{handle}")
        return handle

    # 获取所有窗口句柄
    def base_get_all_window(self, doc=''):
        handles = self.driver.window_handles
        self.log.info(f"{doc}：当前窗口句柄：{handles}")
        return handles

    # 切换到指定窗口
    def base_switch_window(self, handle, doc=''):
        self.driver.switch_to.window(handle)
        self.log.info(f"{doc}：切换到的窗口句柄是：{handle}")

    # 切换浏览器窗口
    @allure.step(title="切换浏览器窗口")
    def base_switch_new_window(self, n, doc=''):
        handles = self.base_get_all_window()
        self.base_switch_window(handles[n])

    # 切换Frame
    def base_goto_frame(self, iframe, doc=''):
        self.driver.switch_to.frame(iframe)
        self.log.info(f"{doc}：切换到的iframe是：{iframe}")

    # 回到主frame
    def base_go_home_frame(self, doc=''):
        self.driver.switch_to.default_content()
        self.log.info(f"{doc}：回到主frame")

    # App特有
    # 定义以swipe方法的滑屏操作
    def base_execute_swipe(self, direction, count=1):
        """
        :param direction: 选择滑动方向  (top, down, left, right)
        :param count: 滑动次数
        :return:
        """
        # 获取屏幕分辨率
        dpi = self.driver.get_window_size()
        self.log.info(f"获取手机屏幕分辨率：{dpi}")
        w = dpi["width"]
        h = dpi["height"]
        # 判断滑屏方向
        if direction == "top":  # 往上滑
            scope = (w / 2, h * 0.8, w / 2, h * 0.1)
            self.log.info("准备向上滑动屏幕")
        elif direction == "down":  # 往下滑
            scope = (w / 2, h * 0.2, w / 2, h * 0.9)
            self.log.info("准备向下滑动屏幕")
        elif direction == "left":  # 往左滑
            scope = (w * 0.8, h / 2, w * 0.1, h / 2)
            self.log.info("准备向左滑动屏幕")
        elif direction == "right":  # 往右滑
            scope = (w * 0.2, h / 2, w * 0.9, h / 2)
            self.log.info("准备向右滑动屏幕")
        else:
            print("参数错误，请选择（top, down, left, right）中的一个")
            return False
        # 循环执行滑屏次数
        for i in range(count):
            self.driver.swipe(*scope, duration=1200)
            self.log.info(f"第{i}次向{scope}滑屏")
            time.sleep(1)

    # 封装一个边查找边点击的方法
    def base_swipe_find(self, scope_info, find_info):
        # 获取要滑屏区域的大小
        scope = self.base_find_element(scope_info)
        scope_size = scope.size
        self.log.info(f"要滑屏区域的大小：{scope_size}")
        width = scope_size["width"]
        height = scope_size["height"]
        # 获取要滑屏区域左上角的坐标
        scope_position = scope.location
        self.log.info(f"要滑屏区域左上角的坐标：{scope_position}")
        x = scope_position["x"]
        y = scope_position["y"]
        # 指定滑屏路线  注意路线过大时容易错漏
        start_x = x + width * 0.9
        y = y + height / 2
        end_x = x + width * 0.1
        while True:
            # 记录查找前的页面，通过对比页面资源来退出死循环
            page = self.driver.page_source
            self.log.info(f"当前页面信息：{page}")
            try:
                self.base_find_element(find_info, timeout=1).click()
                self.log.info(f"已找到元素：{find_info}")
                # 找到对应元素则返回
                return True
            except Exception:
                self.log.info("本次未找到指定元素，并准备再次尝试")
                # driver.get_screenshot_as_file("./image/img{}.png".format(time.strftime("%Y%m%d-%H%M%S")))
            # 未找到元素时，进行滑屏操作，重新查找
            self.driver.swipe(start_x, y, end_x, y, duration=1500)
            self.log.info("再次滑动屏幕")
            time.sleep(1)
            if page == self.driver.page_source:
                self.log.info("滑屏操作完成后仍未找到该元素")
                return False

    # 轻敲操作
    def base_touch_action(self, location, count=1):
        """
        :param location: 定位元素信息
        :param count: 轻敲次数 默认为1
        :return:
        """
        TouchAction(self.driver).tap(self.base_find_element(location), count).perform()
        self.log.info(f"轻敲元素：{location} {count}次")

    # 长按操作 --> 按下一定时间后抬起 时间单位为ms
    def base_long_touch(self, location, times, doc):
        ele = self.base_find_element(location)
        TouchAction(self.driver).long_press(ele, duration=times).perform()
        self.log.info(f"{doc},正在长按元素{location}")

    # 定义获取toast消息的方法
    def base_get_toast(self, message, doc=None, timeout=3):
        xpath = By.XPATH, "//*[contains(@text,'{}')]".format(message)
        element = self.base_find_element(xpath, timeout=timeout)
        self.log.info(f"{doc},toast信息:{element.text}")
        return element.text

    # 系统按键 3-home   4-返回    66-确定
    def sys_keys(self, number):
        self.driver.keyevent(number)


if __name__ == '__main__':
    pass
