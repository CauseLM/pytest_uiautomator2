# depend.py


def read_yaml(file):
    """
    读取数据文件
    :param file:文件绝对路径
    :return:
    """
    with open(file, 'r', encoding='utf8') as f:
        return yaml.safe_load(f.read())

def get_all_adb_devices():
    """
    返回当前系统所有已连接的adb设备列表
    :return:list
    """
    devices = list()
    devices_str = run_cmd("adb devices").split('\n')
    for i in range(1, len(devices_str) - 2):
        devices.append(devices_str[i].split('\t')[0])
    assert len(devices) != 0, "devices is None,Plese connect device"
    return devices

def get_logger(sn):
    """
    供外部调用的log接口
    :param sn: 设备号，也是显示在log里面的用户名
    :return:
    """
    return _get_device_log(sn)


def _get_device_log(sn):
    """
    设置全局logger
    :param sn: 设备号，也是显示在log里面的用户名
    :return: logger
    """
    logger = logging.getLogger(sn)
    #设置logger显示的级别
    logger.setLevel(logging.DEBUG)

    fmat = logging.Formatter("%(asctime)s,%(name)s,%(levelname)s : %(message)s")
    consore = logging.StreamHandler()
    consore.setFormatter(fmat)
    consore.setLevel(logging.INFO)
	# logfile是自己创建的函数，返回以sn_time.txt的绝对路径
    file = logging.FileHandler(log_file(sn), 'w+')
    file.setLevel(logging.DEBUG)
    file.setFormatter(fmat)
	# 输出至控制台
    logger.addHandler(consore)
    # 输出至文件
    logger.addHandler(file)
    return logger
