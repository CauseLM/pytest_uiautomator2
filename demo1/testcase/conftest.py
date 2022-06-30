#  conftest.py
# ����hook������pytest�涨ֻ��ʹ�ô�����д
def pytest_addoption(parser):
    """
    ��pytest����������Զ������
    :param parser:
    :return:
    """
    parser.addoption("--sn",
                     help='test device')

# ������Ҫ��autouse��ֱ���ڻỰ��ʼʱ���ã������Ͳ����ڲ��������м�fixture��
@pytest.fixture(scope='session', autouse=True)
def get_cmd_device(request):
    """
    ��������ȡ�ò���
    :param request:
    :return:
    """
    # ��ȡ�����в���
    base_page.SN = request.config.getoption('--sn')
    deivces = get_all_adb_devices()
    # ���豸�ж�
    if base_page.SN is None and len(deivces) > 1:
        raise RuntimeError('more than one device/emulator, '
                           'please specify the serial number by --sn=device')
    elif base_page.SN is None and len(deivces) == 1:
        base_page.SN = deivces[0]
    # SNΪbase_page��ȫ�ֱ��������ղ��Ե��豸��
    return base_page.SN
