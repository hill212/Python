# __author__ = 'penny'
# -*-coding:utf-8-*-

from pyvirtualdisplay import Display
from selenium import webdriver

# 启动浏览器驱动
def browser():
    #打开Xvfb
    display = Display(visible=0, size=(800, 600))
    display.start()

    driver = webdriver.Firefox()
    return driver

if __name__ == '__main__':
    dr = browser()
    dr.get("http://www.baidu.com")
    dr.quit()

