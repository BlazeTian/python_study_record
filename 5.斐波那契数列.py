""""
题目5：
打印斐波那契数列的前n个数
"""

# 默认打印数超过2，即n >= 2
def fibonacci(n):
    a = 0
    b = 1
    # 第二项：c = a + b
    for i in range(n):
        print(a, end=" ")
        a, b = b, a + b
        

def main():
    n = int(input("请输入一个正整数："))
    fibonacci(n)


if __name__ == '__main__':
    main()