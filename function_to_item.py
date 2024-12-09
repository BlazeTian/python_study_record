# 使用函数作为参数进行传递
def fuc(function):
    result = function(10)
    print(f"参数的类型为{type(function)}") # 参数的类型为<class 'function'>
    print(result)

def add(x):
    return x + 5

fuc(add)