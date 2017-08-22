#__author__ = 'zhangbs'
# coding=utf-8

import os
import time
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from config import globalparam
from src.utils.log import Log

# 测试报告路径
reportPath = globalparam.report_path
logger = Log()
# 配置收发件人,发送多人邮件使用逗号隔开
rec_address = ['jian_liu@infobird.com','zhangbs@infobird.com','chensw@infobird.com','maliang@infobird.com']

'''
# 发件人使用讯鸟公司邮箱的用户名和密码
mail_host = 'smtp.exmail.qq.com'
sender_name = '***@infobird.com'
sender_pswd = '***'
'''


# 发件人使用qq邮箱的用户名，密码使用qq邮箱申请的授权码
mail_host = 'smtp.qq.com'
sender_name = '853382055@qq.com'
sender_pswd = 'ywdyniylehjebbbi'


class SendMail():
    '''定义发送带附件邮件'''

    def __init__(self, receiver=None):
        """接收邮件的人：list or tuple"""
        if receiver is None:
            self.sendTo = rec_address
        else:
            self.sendTo = receiver

    def __get_report(self):
        '''获得最新测试报告'''
        # 获取目录下的所有文件
        lists = os.listdir(reportPath)
        lists.sort()
        new_report_name = lists[-1]
        print('The new report name: {0}'.format(new_report_name))
        return new_report_name

    def __messages(self):
        '''生成邮件内容,和html报告附件'''
        # 创建一个带附件的实例
        self.msg = MIMEMultipart()

        # 生成邮件内容
        # 定义标题
        self.msg['Subject'] = u"alianapi&cduanapi接口测试报告"
        # 定义发送时间，开启此定义后foxmail无法接收邮件提示invalid argument to time encode
        #self.msg['date'] = time.strftime('%a, %d %b %Y%H:%M:%S %z')
        # 定义正文
        new_report = self.__get_report()
        f = open(os.path.join(reportPath, new_report), 'rb')
        mail_body = f.read()
        f.close()
        html = MIMEText(mail_body, _subtype='html', _charset='utf-8')
        self.msg.attach(html)

        # 构造html附件
        att = MIMEText(mail_body, 'base64', 'utf-8')
        att["Content-Type"] = 'application/octet-stream'
        # 这里的filename可以任意写，写什么名字，邮件中显示什么名字
        att["Content-Disposition"] = 'attachment; filename= "TestReport.html"'
        self.msg.attach(att)

    def send_mail(self):
        '''
        sub:主题
        content:内容
        send_mail("aaa@126.com","sub","content")
        '''
        self.__messages()
        self.msg['mail_from'] = sender_name
        try:
            # 使用讯鸟邮箱发送邮件
            #smtp = smtplib.SMTP()
            # smtp.connect('smtp.exmail.qq.com')

            smtp = smtplib.SMTP_SSL(mail_host, 465)
            smtp.login(sender_name, sender_pswd)
            smtp.sendmail(self.msg['mail_from'],
                          self.sendTo, self.msg.as_string())
            smtp.quit()
            logger.info("邮件发送成功")
        except Exception:
            logger.error("邮件发送失败")
            raise

if __name__ == '__main__':
    sendMail = SendMail()
    sendMail.send_mail()
