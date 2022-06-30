#  conftest.py
# 这是hook函数，pytest规定只能使用此名重写
def pytest_addoption(parser):
    """
    向pytest命令行添加自定义参数
    :param parser:
    :return:
    """
    parser.addoption("--sn",
                     help='test device')

# 这里需要加autouse，直接在会话开始时调用，后续就不用在测试用例中加fixture了
@pytest.fixture(scope='session', autouse=True)
def get_cmd_device(request):
    """
    从命令行取得参数
    :param request:
    :return:
    """
    # 获取命令行参数
    base_page.SN = request.config.getoption('--sn')
    deivces = get_all_adb_devices()
    # 多设备判断
    if base_page.SN is None and len(deivces) > 1:
        raise RuntimeError('more than one device/emulator, '
                           'please specify the serial number by --sn=device')
    elif base_page.SN is None and len(deivces) == 1:
        base_page.SN = deivces[0]
    # SN为base_page的全局变量，接收测试的设备号
    return base_page.SN
