""""
题目3：
定义一个函数，实现两个变量的值交换。
"""


def set_wakeup_fd(a,b):
    temp = a
    a = b
    b = temp
    print(f"a = {a},b = {b}")
    
def swap(a,b):
    a,b = b,a # 使用解包方式，更加方便快捷
    print(f"a = {a},b = {b}")

def swap_really(a,b):
    temp = a
    a = b
    b = temp
    return a,b

if __name__ == '__main__':
    a = 1
    b = 2
    set_wakeup_fd(a,b)
    swap(a,b)
    a,b = swap_really(a,b)
    print(f"a = {a},b = {b}")