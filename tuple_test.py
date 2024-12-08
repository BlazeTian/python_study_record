t1 = (1, 2, 3)
t2 = tuple(t1)
print(t1)
print(t2)

t3 = ("j",) # 需要加上逗号，否则会被当作字符串处理，因为括号的特性
print(type(t3))

#元组当中嵌套列表
list1 = [1, 2, 3]
list2 = [4, 5, 6]
t4 = ('我是嵌套元组',list1, list2)
t4[1][0] = 100 # 修改元组中嵌套列表的值
print(t4)

