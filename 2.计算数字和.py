""""
题目2：
计算两个数字的和，并打印结果
"""

def count1(x,y):
    result = x + y
    print(result)
    
def count2(x):
    sum = 0
    for i in x:
        sum += int(i)
    print("该列表中所有数字和为%3d"%(sum))
    
    
    
    
if __name__ == '__main__':
    count1(1,2)
    count2([1,2,3,4,5])
    count2("12345")
