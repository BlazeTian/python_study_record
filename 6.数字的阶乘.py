""""
题目6：
计算数字的阶乘
"""


def factorial(n):
    if n < 0:
        print("输入的数字必须大于等于0")
    elif n==0:
        return 0
    elif n==1:
        return 1
    return n*factorial(n-1)

if __name__ == '__main__':
    print(factorial(3))