# 位置传参
def fuc1(name,age,item):
    print(f"{age}岁的{name}，购买了{item}")

fuc1("张三",25,"手机")
# 关键字传参
def fuc2(name,age,item):
    print(f"{age}岁的{name}，购买了{item}")

fuc2(age=25,name="张三",item="手机")# 此处参数传递顺序不做要求
fuc2("小花",item="电脑",age=20)


# 缺省传参（默认参数）
def fuc3(name,age,item="电脑"):
    print(f"{age}岁的{name}，购买了{item}")

fuc3("小明",20) # 最后一个参数可以不传，默认使用电脑
fuc3("小红",25,"手机") # 最后一个参数可以传，使用手机


# 不定长参数（可变参数、关键字参数）
# 1. *args 代表可变参数，可以传入0个或多个参数，会以【元组】的形式返回
# 2. **kwargs 代表关键字参数，可以传入0个或多个参数，会以【字典】的形式返回
def fuc4(*args):
    print(f"参数的类型为{type(args)}，值为{args}")

fuc4(1,2,3,4,5) # (1, 2, 3, 4, 5)

def fuc5(**kwargs):
    print(f"参数的类型为{type(kwargs)}，值为{kwargs}")

fuc5(name="张三",age=25,item="手机") # {'name': '张三', 'age': 25, 'item': '手机'}