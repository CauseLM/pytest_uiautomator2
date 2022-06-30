# depend.py


def read_yaml(file):
    """
    ��ȡ�����ļ�
    :param file:�ļ�����·��
    :return:
    """
    with open(file, 'r', encoding='utf8') as f:
        return yaml.safe_load(f.read())

def get_all_adb_devices():
    """
    ���ص�ǰϵͳ���������ӵ�adb�豸�б�
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
    ���ⲿ���õ�log�ӿ�
    :param sn: �豸�ţ�Ҳ����ʾ��log������û���
    :return:
    """
    return _get_device_log(sn)


def _get_device_log(sn):
    """
    ����ȫ��logger
    :param sn: �豸�ţ�Ҳ����ʾ��log������û���
    :return: logger
    """
    logger = logging.getLogger(sn)
    #����logger��ʾ�ļ���
    logger.setLevel(logging.DEBUG)

    fmat = logging.Formatter("%(asctime)s,%(name)s,%(levelname)s : %(message)s")
    consore = logging.StreamHandler()
    consore.setFormatter(fmat)
    consore.setLevel(logging.INFO)
	# logfile���Լ������ĺ�����������sn_time.txt�ľ���·��
    file = logging.FileHandler(log_file(sn), 'w+')
    file.setLevel(logging.DEBUG)
    file.setFormatter(fmat)
	# ���������̨
    logger.addHandler(consore)
    # ������ļ�
    logger.addHandler(file)
    return logger
