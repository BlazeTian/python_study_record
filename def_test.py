# def name():
#     print("hello world")
#     #return None
    
# print(name()) # 输出 hello world，并返回 None
# print(name) # 输出 <function name at 0x000001>
# print(type(name)) # 输出 <class 'function'>
# print(type(name())) # 先执行 name()，输出 hello world，再执行 type(name())，输出 <class 'NoneType'>


# def add(num_1,num_2):
#     """_summary_

#     Args:
#         num_1 (_type_): _description_
#         num_2 (_type_): _description_

#     Returns:
#         _type_: _description_
#     """
#     result = num_1 + num_2
#     return result

# def fuc():
#     age = 18
#     print(age)
#     def name2():
#         print("hello world")
#     name2()
#     return None
# fuc()
# name2()
# print(age) # 输出 NameError: name 'age' is not defined，因为 age 未定义

# def outer_function(x):
#     # 外部函数
#     def inner_function(y):
#         # 内部函数
#         return y + 1
    
#     # 外部函数返回内嵌的函数结果
#     return inner_function(x)

# # 调用外部函数
# result = outer_function(10)
# print(result)  # 输出 11，因为 inner_function(10) 返回 11

num = 10

def change():
    # global num #若未加，则下面所示的num变量为局部变量，修改后不会影响全局变量
    num = 20
    print(num)

change()
print(num) # 输出 20，因为 change() 函数中使用了 global 关键字，将 num 变量声明为全局变量，并修改了它的值
    
a = []
print(a)