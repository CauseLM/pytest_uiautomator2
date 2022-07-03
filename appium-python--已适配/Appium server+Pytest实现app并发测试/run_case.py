# _*_ coding：utf-8 _*_

import pytest
import os
from multiprocessing import Pool

# (appium_server 端口号，手机设备名称， 日志名称， allure存放文件， allure_report存放文件）
device_infos = [
    ('4723', 'emulator-5554', '一号测试机', 'allure0', 'allure0_report'),
    ('4725', 'emulator-5556', '二号测试机', 'allure1', 'allure1_report')
]


def main(device_info):
    pytest.main([f"--cmdopt={device_info}",
                 "--alluredir", f"./{device_info[3]}", "--clean-alluredir", "-vs"])
    os.system(f"allure generate {device_info[3]} -o {device_info[4]} --clean")


if __name__ == "__main__":
    with Pool(2) as pool:
        pool.map(main, device_infos)
        pool.close()
        pool.join()
