name1 = 'Alice'
name2 = "Bob"
name3 = '''Charlie'''
name4 = """Dave"""

print(type(name1))
print(type(name2))
print(type(name3))
print(type(name4))

print(name1 + "和" + name2)
print("你好" + "我是" + "菜狗")
print("你好" + "我是" + "菜狗" + name1)

phone = 123456
#print("我的手机号码是" + phone) #报错，因为phone是整数，不能直接拼接字符串TypeError: can only concatenate str (not "int") to str
print("我的手机号码是" + str(phone))

print("我的手机号码是%s，我的姓名是%s" % (phone, name1)) # 我的手机号码是123456，我的姓名是Alice
num = 3.1415926
print("我的手机号码是%d，我的姓名是%s，我有一个浮点数%f" % (phone, name1, num)) # 我我的手机号码是123456，我的姓名是Alice，我有一个浮点数3.141593


num = 3.1415926
print("我的手机号码是%d，我的姓名是%s，我有一个浮点数%5.2f" % (phone, name1, num)) # 我的手机号码是123456，我的姓名是Alice，我有一个浮点数[空格]3.14


print("1*1的结果是%d，2*2的结果是%s" % (1*1, 2*2)) # 1*1的结果是1，2*2的结果是4
print(f'1*1的结果是{1*1}，2*2的结果是{2*2}')