#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-07-20 11:02:03
# @Author  : zhangbs

from src.utils import sendmailatt
import unittest
import time
import HTMLTestRunner
#from config import globalparam
from src.test.common.function import project_path

case_dir = project_path() + './src/test/case/interface_test/'
#case_dir = globalparam.prj_path + './src/test/case/'
#discover = unittest.defaultTestLoader.discover(case_dir,pattern='start_*.py',top_level_dir=None)
discover = unittest.defaultTestLoader.discover(
    case_dir, pattern='test*.py', top_level_dir=None)


if __name__ == '__main__':
    now = time.strftime("%Y-%m-%d %H_%M_%S")
    filename = project_path() + './report/testreport/' + now + 'tesult.html'
    fp = open(filename, 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp,
                                           title=u'alianapi&cduanapi接口测试报告',
                                           description='')
    runner.run(discover)
    fp.close()
    time.sleep(5)
    mail = sendmailatt.SendMail()
    mail.send_mail()
