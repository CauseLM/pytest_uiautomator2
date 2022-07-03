# _*_ coding：utf-8 _*_
from time import sleep

import pytest
from Common.base.check_port import release_port
from Common.base.get_log import GetLog
from Common.drivers.app_driver_auto_server import BaseDriver

base_driver = None


# 给命令行添加 --cmdopt参数
def pytest_addoption(parser):
    parser.addoption("--cmdopt", action="store", default="device_info", help=None)


# 获取命令行参数 -cmdopt 的数据
@pytest.fixture(scope="session")
def cmd_opt(request):
    return request.config.getoption("--cmdopt")

# @pytest.fixture(scope="session")
# def common_log(cmd_opt):
#     cmd_opt = eval(cmd_opt)
#     log_base = GetLog().get_log(cmd_opt[2])
#     yield log_base


@pytest.fixture(scope="session")
def common_driver(cmd_opt):
    cmd_opt = eval(cmd_opt)
    log = GetLog().get_log(cmd_opt[2])
    # log.info('===================== 开始执行 < xx项目 > 测试用例=====================')
    app_driver = BaseDriver(cmd_opt, log).get_base_driver()
    yield app_driver, log
    app_driver.quit()
    sleep(10)
    release_port(cmd_opt[0])    # 关闭appium server
    # log.info('===================== 结束执行 < xx项目 > 测试用例=====================')
