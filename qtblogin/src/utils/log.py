# __author__ = 'penny'
#coding=utf-8

import logging,os,time
from config import globalparam

log_path = globalparam.log_path
class Log:
    def __init__(self):
        self.logname = os.path.join(log_path,'{0}.log'.format(time.strftime("%Y-%m-%d")))

    def _print_console(self,level,message):
        # 创建一个logger
        logger = logging.getLogger()
        logger.setLevel(logging.DEBUG)
        #创建一个handler ,用于写入日志文件
        fh = logging.FileHandler(self.logname,'a',encoding='utf-8')
        fh.setLevel(logging.DEBUG)
        #创建一个handler，用于输出到控制台
        ch = logging.StreamHandler()
        ch.setLevel(logging.DEBUG)
        #定义handler的输出格式
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        fh.setFormatter(formatter)
        ch.setFormatter(formatter)
        #给logger添加handler
        logger.addHandler(fh)
        logger.addHandler(ch)
        #记录一条记录
        if level == 'info':
            logger.info(message)
        elif level == 'debug':
            logger.debug(message)
        elif level == 'warning':
            logger.warning(message)
        elif level == 'error':
            logger.error(message)
        logger.removeHandler(ch)
        logger.removeHandler(fh)
        #关闭打开的文件
        fh.close()

    def info(self,message):
        self._print_console('info',message)

    def debug(self,message):
        self._print_console('debug',message)

    def warning(self,message):
        self._print_console('warning',message)

    def error(self,message):
        self._print_console('error',message)
