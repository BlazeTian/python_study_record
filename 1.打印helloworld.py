""""
题目一：
使用python打印“hello world!”
"""
def test1():
    print("hello world!")

def test2():
    a = ['h','e','l','l','o',' ','w','o','r','l','d','!']
    # for i in a:
    #     print(i,end="")
    print("".join(a))
    
    

if __name__ == '__main__':
    #test1()
    test2()