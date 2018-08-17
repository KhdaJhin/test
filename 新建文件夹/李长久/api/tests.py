from django.test import TestCase

# Create your tests here.
def register():
    while 1:
        username = input('>>>请输入要注册的用户名 : ')
        with open('user_info', encoding='utf8', mode='r+') as f:
            for line in f: # alex|alex3714
                # print(line)
                name,pwd = line.strip().split('|')
                if username == name:
                    pwd = input('>>>用户名已存在.请重新输入 ')
                    break

            else:
                    pwd = input('>>>请输入密码 : ')
                    f.write('%s|%s\n'%(username,pwd))
                    break
register()