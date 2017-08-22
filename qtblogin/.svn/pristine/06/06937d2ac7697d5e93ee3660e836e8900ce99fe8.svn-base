# __author__ = ‘penny‘
# -*-coding:utf-8-*-

import unittest
from src.test.common import myunit,function
from src.test.page.loginPage import login

class loginTest(myunit.MyTest):
    '''测试用户登录'''

    def user_login_verify(self,username = '',password= ''):
        login(self.driver).user_login(username,password)

    def test_login1(self):
        '''用户名、密码为空登录'''
        self.user_login_verify()
        self.assertEqual(self.driver.current_url,'http://118.178.112.3:8006/login/login')
        function.insert_img(self.driver,'user_pawd_empty.jpg')

    def test_login2 (self):
        '''用户名正确、密码为空'''
        self.user_login_verify(username='test1@zj.com')
        self.assertEqual(login(self.driver).pawd_error_hint(),'密码错误！')
        function.insert_img(self.driver, 'pawd_empty.jpg')

    def test_login3(self):
        '''用户名为空、密码正确'''
        self.user_login_verify(password='test1@zj.com')
        self.assertEqual(self.driver.current_url, 'http://118.178.112.3:8006/login/login')
        function.insert_img(self.driver, 'user_empty.jpg')

    def test_login4(self):
        '''用户名与密码不匹配'''
        self.user_login_verify(username='test1@zj.com',password='123456')
        self.assertEqual(login(self.driver).pawd_error_hint(), '密码错误！')
        function.insert_img(self.driver, 'user_pawd_error.jpg')

    def test_login5(self):
        '''用户名与密码匹配'''
        self.user_login_verify(username='test1@zj.com',password='test1@zj.com')
        self.assertTrue(login(self.driver).user_login_success())
        function.insert_img(self.driver, 'user_pawd_true.jpg')

if __name__ == '__main__':
    unittest.main()