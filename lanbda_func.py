# lambda表达式（匿名函数）本质上其实一般也需要以函数作为参数的形式进行使用（此时应该只能使用位置参数）
def func1(function):
    result = function(10,12)
    print(f"参数的类型为{type(function)}") # 参数的类型为<class 'function'>
    print(result)
    
# 定义一个匿名函数
add_ten = lambda x,y: x + y + 10

# 调用func1函数，传入add_ten匿名函数
func1(add_ten)
func1(lambda x,y: x+y+120)