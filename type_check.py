# 定义一个函数，用于判断变量类型并输出相应结果
def check_type(var):
    #if type(var) == int or type(var) == float:  
    # 使用 type() 判断是否为整型或浮点型
    if type(var) in (int, float):
        print("数字")
    elif type(var) == str:  # 使用 type() 判断是否为字符串类型
        print("字符串")
    else:
        print("其他类型")  # 如果是其他类型，输出“其他类型”

# 测试
check_type(42)          # 输出：数字
check_type(3.14)        # 输出：数字
check_type("Hello")     # 输出：字符串
check_type([1, 2, 3])   # 输出：其他类型
print(type(int))              # 输出：<class 'type'>   


# 定义一个函数，用于判断变量类型并输出相应结果
def check_type(var):
    if isinstance(var, (int, float)):  # 检查是否为整型或浮点型
        print("数字")
    elif isinstance(var, str):  # 检查是否为字符串类型
        print("字符串")
    else:
        print("其他类型")  # 如果是其他类型，输出“其他类型”

# 测试
check_type(42)          # 输出：数字
check_type(3.14)        # 输出：数字
check_type("Hello")     # 输出：字符串
check_type([1, 2, 3])   # 输出：其他类型
