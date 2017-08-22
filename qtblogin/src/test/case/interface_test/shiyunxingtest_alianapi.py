#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-07-17 17:32:40
# @Author  : zhangbs


import requests
import json
import unittest
from src.test.common import myunit, function
from src.test.page.loginPage import login


class alianapi_test(myunit.MyTest):
    '''alianA端api接口测试类'''

    def setUp(self):
        print("start test")
        pass

    def test_alianapi_alogin(self):
        '''登录接口'''
        url = 'http://118.178.193.118:82/login/pwd?agentno=zhangbs@infobird.cn&password=123456'
        r = requests.get(url)
        jsontext = r.text
        self.assertEqual(r.status_code, 200)
        json_to_python = json.loads(jsontext)
        msg = (json_to_python['msg'])
        self.assertEqual(msg, '登录成功')
        # print(jsontext)
        print(url)
        print(json_to_python)

    def test_alianapi_getdepartment(self):
        '''获取部门接口'''
        url = 'http://118.178.193.118:82/employee/getdept?corpid=2&token='
        r = requests.get(url)
        jsontext = r.text
        self.assertEqual(r.status_code, 200)
        json_to_python = json.loads(jsontext)
        msg = (json_to_python['msg'])
        self.assertEqual(msg, '获取部门成功')
        print(url)

    def test_alianapi_customerlist(self):
        '''获取客户列表接口'''
        url = 'http://118.178.193.118:82/customer/list?corpid=2&agentno=zhangbs@infobird.cn&size=100&beginIndex=0&token='
        r = requests.get(url)
        jsontext = r.text
        self.assertEqual(r.status_code, 200)
        json_to_python = json.loads(jsontext)
        msg = (json_to_python['msg'])
        self.assertEqual(msg, '获取客户列表成功')
        print(url)

    def test_alianapi_employeelist(self):
        '''获取员工通讯录列表接口'''
        url = 'http://118.178.193.118:82/employee/list?corpid=2&size=100&beginIndex=0&token='
        r = requests.get(url)
        jsontext = r.text
        self.assertEqual(r.status_code, 200)
        json_to_python = json.loads(jsontext)
        msg = (json_to_python['msg'])
        self.assertEqual(msg, '获取数据成功')
        print(url)

    def test_alianapi_historycallin(self):
        '''获取通讯历史-呼入'''
        url = 'http://118.178.193.118:82/history/list?managerid=30092591&agentno=zhangbs@infobird.cn&beginDate=2017-07-07&beginTime=12&endDate=2017-07-14&endTime=12&size=100&beginIndex=0&token=&type=callin'
        r = requests.get(url)
        jsontext = r.text
        self.assertEqual(r.status_code, 200)
        json_to_python = json.loads(jsontext)
        msg = (json_to_python['msg'])
        self.assertEqual(msg, '获取通讯历史成功')
        print(url)

    def test_alianapi_historycallout(self):
        '''获取通讯历史-呼出'''
        url = 'http://118.178.193.118:82/history/list?managerid=30092591&agentno=zhangbs@infobird.cn&beginDate=2017-07-07&beginTime=12&endDate=2017-07-14&endTime=12&size=100&beginIndex=0&token=&type=callout'
        r = requests.get(url)
        jsontext = r.text
        self.assertEqual(r.status_code, 200)
        json_to_python = json.loads(jsontext)
        msg = (json_to_python['msg'])
        self.assertEqual(msg, '获取通讯历史成功')
        print(url)

    def test_alianapi_historyunanswer(self):
        '''获取通讯历史-呼入未接'''
        url = 'http://118.178.193.118:82/history/list?managerid=30092591&agentno=zhangbs@infobird.cn&beginDate=2017-07-07&beginTime=12&endDate=2017-07-14&endTime=12&size=100&beginIndex=0&token=&type=unanswer'
        r = requests.get(url)
        jsontext = r.text
        self.assertEqual(r.status_code, 200)
        json_to_python = json.loads(jsontext)
        msg = (json_to_python['msg'])
        self.assertEqual(msg, '获取通讯历史成功')
        print(url)

    def test_alianapi_historycalloutunanswer(self):
        '''获取通讯历史-呼出未接'''
        url = 'http://118.178.193.118:82/history/list?managerid=30092591&agentno=zhangbs@infobird.cn&beginDate=2017-07-07&beginTime=12&endDate=2017-07-14&endTime=12&size=100&beginIndex=0&token=&type=calloutunanswer'
        r = requests.get(url)
        jsontext = r.text
        self.assertEqual(r.status_code, 200)
        json_to_python = json.loads(jsontext)
        msg = (json_to_python['msg'])
        self.assertEqual(msg, '获取通讯历史成功')
        print(url)

    def test_alianapi_historyagtoag(self):
        '''获取通讯历史-席间'''
        url = 'http://118.178.193.118:82/history/list?managerid=30092591&agentno=zhangbs@infobird.cn&beginDate=2017-07-07&beginTime=12&endDate=2017-07-14&endTime=12&size=100&beginIndex=0&token=&type=agtoag'
        r = requests.get(url)
        jsontext = r.text
        self.assertEqual(r.status_code, 200)
        json_to_python = json.loads(jsontext)
        msg = (json_to_python['msg'])
        self.assertEqual(msg, '获取通讯历史成功')
        print(url)

    def tearDown(self):  # 与setUp()相对
        print("end test")
        pass


if __name__ == '__main__':
    unittest.main()
