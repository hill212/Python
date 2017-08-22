#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-07-17 17:32:40
# @Author  : zhangbs


import requests
import json
import unittest
from src.test.common import myunit, function
from src.test.page.loginPage import login


class cduanapi_test(myunit.MyTest):
    '''alianC端api接口测试类'''

    def setUp(self):
        print("start test")
        pass

    def test_cduanapi_1login(self):
        '''登录'''
        postdata = {'phone': '13810134875', 'appKey': 'Android',
                    'pwd': 'e10adc3949ba59abbe56e057f20f883e', 'sig': 'sig'}
        url = 'http://118.178.193.118:83/login/pwd'
        r = requests.post(url, data=postdata)
        jsontext = r.text
        self.assertEqual(r.status_code, 200)
        json_to_python = json.loads(jsontext)
        msg = (json_to_python['msg'])
        data = (json_to_python['data'])
        token = data['token']
        self.assertEqual(msg, 'sucess')
        # print(token)
        # print(json_to_python)
        return token

    def test_cduanapi_2propertyget(self):
        '''获取个人资料,token需要传递之前登录接口返回的数值'''
        token1 = cduanapi_test.test_cduanapi_1login(self)
        # print(token1)
        url = 'http://118.178.193.118:83/property/get?id=28&token=' + \
            token1 + '&sig=sig&appKey=Android'
        # print (url)
        r = requests.get(url)
        jsontext = r.text
        self.assertEqual(r.status_code, 200)
        json_to_python = json.loads(jsontext)
        msg = (json_to_python['msg'])
        self.assertEqual(msg, 'sucess')
        print(url)
        print(json_to_python)

    def test_cduanapi_3gethotlist(self):
        '''获取热门企业,token需要传递之前登录接口返回的数值'''
        token1 = cduanapi_test.test_cduanapi_1login(self)
        # print(token1)
        url = 'http://118.178.193.118:83/enterprise/gethotlist?id=7' + \
            '&beginIndex=0&pageSize=30&token=' + token1 + '&sig=sig&appKey=Android'
        # print (url)
        r = requests.get(url)
        jsontext = r.text
        self.assertEqual(r.status_code, 200)
        json_to_python = json.loads(jsontext)
        msg = (json_to_python['msg'])
        self.assertEqual(msg, 'success')
        print(url)

    def test_cduanapi_4getkeeplist(self):
        '''获取收藏企业,token需要传递之前登录接口返回的数值'''
        token1 = cduanapi_test.test_cduanapi_1login(self)
        # print(token1)
        url = 'http://118.178.193.118:83/enterprise/getkeeplist?id=7' + \
            '&beginIndex=0&pageSize=30&token=' + token1 + '&sig=sig&appKey=Android'
        # print (url)
        r = requests.get(url)
        jsontext = r.text
        self.assertEqual(r.status_code, 200)
        json_to_python = json.loads(jsontext)
        msg = (json_to_python['msg'])
        self.assertEqual(msg, 'success')
        print(url)

    def test_cduanapi_5getquestionlist(self):
        '''获取菜单'''
        # token1 = mytest.test_cduanapi_1login(self)
        # print(token1)
        url = 'http://118.178.193.118/api/getquestionlist?cpyid=30092591'
        # print (url)
        r = requests.get(url)
        jsontext = r.text
        self.assertEqual(r.status_code, 200)
        json_to_python = json.loads(jsontext)
        msg = (json_to_python['msg'])
        self.assertEqual(msg, 'success')
        print(url)

    def test_cduanapi_6gethistorylist(self):
        '''获取最近通讯历史列表'''
        token1 = cduanapi_test.test_cduanapi_1login(self)
        # print(token1)
        url = 'http://118.178.193.118:83/call/gethistorylist?id=14&beginIndex=0&' + \
            'pageSize=30&token=' + token1 + '&sig=sig&appKey=Android'
        # print (url)
        r = requests.get(url)
        jsontext = r.text
        self.assertEqual(r.status_code, 200)
        json_to_python = json.loads(jsontext)
        msg = (json_to_python['msg'])
        self.assertEqual(msg, 'success')
        print(url)

    def tearDown(self):  # 与setUp()相对
        print("end test")
        pass


if __name__ == '__main__':
    unittest.main()
