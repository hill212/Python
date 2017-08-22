# __author__ = ‘penny‘
# -*-coding:utf-8-*-
from src.test.page.basePage import Page
import time

class login(Page):
    '''启通宝登录页'''

    url = '/login'

    def login_username(self,username):
        '''登录用户名'''
        self.driver.find_element_by_id("name").clear()
        self.driver.find_element_by_id("name").send_keys(username)

    def login_password(self,password):
        '''登录用户名'''
        self.driver.find_element_by_id("cipher").clear()
        self.driver.find_element_by_id("cipher").send_keys(password)

    def login_button(self):
        '''登录按钮'''
        self.driver.find_element_by_name("button").click()

    def user_login(self,username,password):
        '''统一登录入口'''
        self.openPage()
        self.login_username(username)
        self.login_password(password)
        self.login_button()
        time.sleep(2)

    def user_login_again(self,username,password):
        '''重新登录入口'''
        self.login_username(username)
        self.login_password(password)
        self.login_button()
        time.sleep(2)

    def pawd_error_hint(self):
        '''密码错误提示'''
        return self.driver.find_element_by_xpath("//*[@id='commentform']/div/span").text

    def user_login_success(self):
        '''用户名登录成功'''
        return self.driver.find_element_by_id('shouye')
