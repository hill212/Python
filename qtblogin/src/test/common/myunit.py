# __author__ = ‘penny‘
# -*-coding:utf-8-*-

from selenium import webdriver
import unittest
from src.test.common.driver import browser
from src.utils.log import Log

class MyTest(unittest.TestCase):
    def setUp(self):
        self.logger = Log()
        self.logger.info('############################### START ###############################')
        #self.driver = webdriver.Chrome()
        self.driver = browser()
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()
        self.verificationErrors = []
        self.accept_next_alert = True

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([],self.verificationErrors)
        self.logger.info('################################ END ################################')

if __name__ == '__main__':
    unittest.main()