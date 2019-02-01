from random import Random
import time
import hashlib

from django.core.mail import send_mail

from users.models import EmailVerifyCode
from binshop.settings import EMAIL_FROM


def send_email(email, type='register'):
    """
        发送邮件的方法
        register:   注册账号
        forget:     找回密码
        change:     修改邮箱
    """
    if type == 'register':
        subject = '彬彬商场注册激活链接'
        code_str = generate_random_str(16)
        message = '请点击下面的链接激活您的账号: http://127.0.0.1:8000/active/{0}'.format(code_str)

    elif type == 'forget':
        subject = '彬彬商场忘记密码连接'
        code_str = generate_random_str(8)
        timestamp = int(time.time())
        md5 = hashlib.md5()
        md5_str = md5.update((code_str + email + str(timestamp)).encode('utf8'))
        hash_str = md5.hexdigest()
        message = '请点击下面的链接修改你的密码: http://127.0.0.1:8000/reset?timestamp={0}&hash={1}&email={2}'.format(timestamp,
                                                                                                        hash_str, email)
    elif type == 'change':
        subject = '彬彬商场修改邮箱连接'
        code_str = generate_random_str(6)
        message = '你的邮箱验证码为: {0}'.format(code_str)
    else:
        return False

    status = send_mail(subject, message, EMAIL_FROM, [email])
    if status:  # 发送成功
        email_code = EmailVerifyCode()
        email_code.email = email
        email_code.code = code_str
        email_code.type = type
        email_code.save()
        return True
    else:
        return False


def generate_random_str(str_len=8):
    """ 生成长度为str_len的随机字符串 """
    str = ''
    chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789'
    random = Random()
    for i in range(str_len):
        str += chars[random.randint(0, len(chars) - 1)]
    return str
