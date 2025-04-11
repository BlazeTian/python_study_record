""""
题目4：
进行质数、偶数、奇数的判断
"""

def is_prime(n):
    if n <= 1:
        print("不是质数")
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            print("不是质数")
            return 0
    print("是质数")
    
def is_even(n):
    if n % 2 == 0:
        print("是偶数")
    else:
        print("不是偶数")

def is_odd(n):
    if n % 2 == 1:
        print("是奇数")
    else:
        print("不是奇数")

def main():
    n = int(input("请输入一个整数："))
    is_prime(n)
    is_even(n)
    is_odd(n)

if __name__ == "__main__":
    main()