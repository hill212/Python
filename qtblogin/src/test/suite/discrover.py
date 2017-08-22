# __author__ = ‘penny‘
# -*-coding:utf-8-*-
# discover更多测试用例

import unittest,time,HTMLTestRunner
#from config import globalparam
from src.test.common.function import project_path
#from common.function import project_path

case_dir = project_path() + './src/test/case/'
#case_dir = globalparam.prj_path + './src/test/case/'
#discover = unittest.defaultTestLoader.discover(case_dir,pattern='start_*.py',top_level_dir=None)
discover = unittest.defaultTestLoader.discover(case_dir,pattern='start*.py',top_level_dir=None)


if __name__ == '__main__':
    now = time.strftime("%Y-%m-%d %H_%M_%S")
    filename =project_path() + './report/' +  now +  'result.html'
    fp = open(filename, 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp,
                                           title=u'启通宝登录测试报告',
                                           description=u'环境：window7 浏览器：chrome')
    runner.run(discover)
