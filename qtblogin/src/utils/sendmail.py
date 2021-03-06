#__author__ = 'penny'
#coding=utf-8

import os,time
import smtplib
from email.mime.text import MIMEText
from config import globalparam
from src.utils.log import Log

#测试报告路径
reportPath = globalparam.report_path
logger = Log()
# 配置收发件人
rec_address = ['hanrn@infobird.com','zhangbs@infobird.com']
# 发件人163的用户名和密码
sender_name = '853382055@qq.com'
sender_pswd = 'testBJ123!@#'

class SendMail():
    '''定义发送邮件'''

    def __init__(self, receiver=None):
        """接收邮件的人：list or tuple"""
        if receiver is None:
            self.sendTo = rec_address
        else:
            self.sendTo = receiver

    def __get_report(self):
        '''获得最新测试报告'''
        #获取目录下的所有文件
        lists = os.listdir(reportPath)
        lists.sort()
        new_report_name = lists[-1]
        print('The new report name: {0}'.format(new_report_name))
        return new_report_name

    def __messages(self):
        '''生成邮件内容'''
        # 定义正文
        new_report = self.__get_report()
        f = open(os.path.join(reportPath,new_report), 'rb')
        mail_body = f.read()
        f.close()
        self.msg = MIMEText(mail_body, _subtype='html', _charset='utf-8')
        # 定义标题
        self.msg['Subject'] = u"工单系统测试报告"
        # 定义发送时间
        self.msg['date'] = time.strftime('%a, %d %b %Y%H:%M:%S %z')


    def send_mail(self):
        '''
        sub:主题
        content:内容
        send_mail("aaa@126.com","sub","content")
        '''
        self.__messages()
        self.msg['mail_from'] = sender_name
        try:
            smtp = smtplib.SMTP()
            smtp.connect('smtp.exmail.qq.com')
            smtp.login(sender_name,sender_pswd)
            smtp.sendmail( self.msg['mail_from'], self.sendTo, self.msg.as_string())
            smtp.quit()
            logger.info("邮件发送成功")
        except Exception:
            logger.error("邮件发送失败")
            raise

if __name__ == '__main__':
    sendMail = SendMail()
    sendMail.send_mail()






