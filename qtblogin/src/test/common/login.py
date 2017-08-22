# __author__ = ‘penny‘
# -*-coding:utf-8-*-


def login(self,username,password):
    '''登录模块'''
    self.driver = self.driver
    #用户名
    self.driver.find_element_by_id("name").clear()
    self.driver.find_element_by_id("name").send_keys(username)
    #密码
    self.driver.find_element_by_id("cipher").clear()
    self.driver.find_element_by_id("cipher").send_keys(password)
    #登录按钮
    self.driver.find_element_by_name("button").click()
