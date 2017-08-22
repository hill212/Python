# __author__ = ‘penny‘
# -*-coding:utf-8-*-
'''
  创建页面基础类，通过__init__()方法初始化参数：浏览器驱动、URL地址、超时时长等
  定义基本方法：open()用于打开BBS地址
               find_element()和find_elements()分别用来定位单个与多个元素
               创建script()方法可以更简便地调用JavaScript代码
'''


class Page(object):
     ''''页面基础类，用于所有页面的继承'''

     qtb3_url = 'http://118.178.112.3:8006'

     def __init__(self,driver,base_url = qtb3_url,parent =None):
         self.driver = driver
         self.base_url = base_url
         self.timeout = 30
         self.parent = parent

     def _openPage(self, url):
        url = self.base_url + url
        self.driver.get(url)
        b=self.driver.current_url
        c=self.base_url + self.url
        assert self.onPage(), 'Did not land on %s' % url

     def openPage(self):
         '''动态绑定属性'''
         self._openPage(self.url)

     def onPage(self):
         return self.driver.current_url == self.base_url + self.url

