# 使用 set() 函数创建空集合
empty_set = set()

# 创建包含元素的集合
my_set = {1, 2, 3, 4}
print(my_set)  # 输出：{1, 2, 3, 4, [1, 2, 3, 4]}

# 通过 set() 转换其他可迭代对象为集合
list_set = set([1, 2, 3, 3, 4])  # 重复的 3 会被去掉
print(list_set)  # 输出：{1, 2, 3, 4}

# 创建空集合
empty_set = set()



my_set = {1, 2, 3}
my_set.update([4, 5], {6, 7},"hsujh")#支持多参数
print(my_set)  # 输出：{1, 2, 3, 4, 5, 6, 7}


set1 = {1, 2, 3}
set2 = {3, 4, 5}
union_set = set1.union(set2)  # 或者 set1 | set2
print(union_set)  # 输出：{1, 2, 3, 4, 5}

set1 = {1, 2, 3}
set2 = {3, 4, 5}
difference_set = set1.difference(set2)  # 或者 set1 - set2
print(difference_set)  # 输出：{1, 2}

set1 = {1, 2, 3}
set2 = {3, 4, 5}
set1.difference_update(set2)  # 或者 set1 - set2
print(set1)  # 输出：{1, 2}

list1 = [x**2 for x in range(1, 6) if x%2==0]  # 列表推导式生成的集合
print(list1)  # 输出：[1, 4, 9, 16, 25]

for i in range(6):
    print(i)