# __author__ = ‘penny‘
# -*-coding:utf-8-*-

import os
#截图函数
def insert_img(driver, file_name):
    base_dir = os.path.dirname(os.path.dirname(__file__))
    base_dir = str(base_dir)
    base_dir = base_dir.replace('\\','/')
    base = base_dir.split('src')[0]
    file_path = base + "report/image/" + file_name
    driver.get_screenshot_as_file(file_path)

#获得项目路径函数
def project_path():
    base_dir = os.path.dirname(__file__)
    base_dir = str(base_dir)
    base_dir = base_dir.replace('\\','/')
    base = base_dir.split('src')[0]
    return base

#获取登录后的cookie
def cookie(driver):
    # 删除cookie里的内容
    driver.delete_all_cookies()
    #初始化cookie

    new_cookies = [
        {'name': 'count', 'httpOnly': False, 'domain': '118.178.112.3', 'value': '1', 'expiry': 1485827985.934692,
         'secure': False, 'path': '/'},
        {'name': 'PHPSESSID', 'domain': '118.178.112.3', 'value': 'fehab7ea7fbs416s4v8s1qqfv4', 'httpOnly': False,
         'secure': False, 'path': '/'},
        {'name': 'remember', 'httpOnly': False, 'domain': '118.178.112.3', 'value': '0', 'expiry': 1485827985.934689,
         'secure': False, 'path': '/'},
        {'name': 'username', 'httpOnly': False, 'domain': '118.178.112.3', 'value': 'test1%40zj.com',
         'expiry': 1485827985.93469, 'secure': False, 'path': '/'}]

    # 添加登录信息的cookie
    for cookie in new_cookies:
        driver.add_cookie(cookie)


#时间区间比较函数,日期大小比较函数
import time
# 这里比较l_time 是否在时间区间[start_t, end_t]中
def compare_time(l_time, start_t, end_t):
    #"2011-11-10 14:56:58"  定义格式串时应该为: "%Y-%m-%d %H:%M:%S"
    s_time = time.mktime(time.strptime(start_t, '%Y%m%d%H%M'))  # get the seconds for specify date
    e_time = time.mktime(time.strptime(end_t, '%Y%m%d%H%M'))
    log_time = time.mktime(time.strptime(l_time, '%Y-%m-%d %H:%M:%S'))
    if (float(log_time) >= float(s_time)) and (float(log_time) <= float(e_time)):
        return True
    return False
