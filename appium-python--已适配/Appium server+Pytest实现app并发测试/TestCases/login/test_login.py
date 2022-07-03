# _*_ coding：utf-8 _*_

import allure
import pytest
from TestDatas import login_datas


@allure.epic('项目名称：xxx项目')
@allure.feature('登录模块')
# @allure.severity('blocker')
@pytest.mark.usefixtures('page_driver')
@pytest.mark.run(order=100)
class TestGesture(object):

    @allure.severity('blocker')
    @allure.story('登录模块：未同意协议用例')
    @pytest.mark.run(order=101)
    @pytest.mark.parametrize("data", login_datas.error_not_agree_data)
    def test_error_not_agree(self, data, page_driver):
        with allure.step('退出登录'):
            page_driver.do_logout()
        with allure.step('登录操作'):
            page_driver.app_login(user=data['username'], pwd=data['password'], agree=data['agree'],
                                   success=data['success'], except_result=data['except'])

    # @allure.severity('blocker')
    # @allure.story('登录模块：账号异常用例')
    # @pytest.mark.run(order=102)
    # @pytest.mark.parametrize("data", login_datas.error_username_data)
    # def test_error_username(self, data, page_driver):
    #     with allure.step('退出登录'):
    #         page_driver.do_logout()
    #     with allure.step('登录操作'):
    #         page_driver.app_login(user=data['username'], pwd=data['password'], agree=data['agree'],
    #                               success=data['success'], except_result=data['except'])
