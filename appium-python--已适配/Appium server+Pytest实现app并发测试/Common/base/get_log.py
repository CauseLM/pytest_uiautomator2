# _*_ coding：utf-8 _*_

import logging.handlers
import os
import time

from Config.root_config import LOG_DIR


class GetLog:
    logger = None

    @classmethod
    def get_log(cls, filename):
        if cls.logger is None:
            # 创建一个logger
            cls.logger = logging.getLogger()
            cls.logger.setLevel(logging.INFO)
            # 创建一个handler， 用于写入日志文件
            log_name = os.path.join(LOG_DIR, f"{time.strftime('%Y-%m-%d')}-{filename}.log")
            th = logging.handlers.TimedRotatingFileHandler(filename=log_name,
                                                           when='midnight',
                                                           interval=1,
                                                           backupCount=30,
                                                           encoding='utf-8')
            # 创建一个handlers， 用于输出到控制台
            sh = logging.StreamHandler()
            # 设置日志的输出格式
            fmt = "%(asctime)s %(levelname)s [%(name)s] [%(filename)s (%(funcName)s:%(lineno)d] - %(message)s"
            fm = logging.Formatter(fmt)
            # 把格式添加到处理器---文件
            th.setFormatter(fm)
            # 把格式器添加到处理器---控制台
            sh.setFormatter(fm)
            # 把处理器 添加到日志器
            cls.logger.addHandler(th)
            return cls.logger


if __name__ == '__main__':
    log1 = GetLog().get_log("ABC")
    log2 = GetLog().get_log("123")
    log1.info('abc:{}'.format(log1))
    log2.info('123:{}'.format(log2))
