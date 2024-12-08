# # 字典的定义
# dict1 = {'name': 'Alice', 'age': 25, 'city': 'Beijing'}
# dict2 = dict(name='Bob', age=30, city='Shanghai')

# # 空字典
# dict3 = {}
# dict4 = dict() # 输出为{}，为什么不是dict()，集合中空集合为set()，并未占用{}

# # 字典的访问
# print(dict1)
# print(dict2)
# print(dict3)
# print(dict4)

# # 字典的添加、修改、删除
# dict1['gender'] = 'female'
# dict2['gender'] ='male'
# print(dict1)
# print(dict2)

# del dict1['age']
# print(dict1)

# # 字典的遍历
# for key in dict1:
#     print(key, dict1[key])

# # 字典的合并
# dict3.update(dict1)
# dict3.update(dict2)
# print(dict3)

my_dict = {'name': 'Alice', 'age': 25, 'city': 'Beijing',(1,2,3):'test'}
print(my_dict)
for key in my_dict.keys():
    print(key)

# from collections import defaultdict
# my_dict = defaultdict(int)
# my_dict["a"] += 1  # 如果 "a" 不存在，默认值为 0，之后值为 1
# print(my_dict)  # 输出: defaultdict(<class 'int'>, {'a': 1})
