for i in range(1, 11):
    a = 2
    print(i)
print(i) #虽然规范说for循环中的变量不能再使用，但是实际上，在Python中，for循环中的变量可以继续使用,只是并不推荐
print(a) #变量a在for循环外面，但是在for循环中使用了，所以可以正常输出。

# 规范使用：预先在for循环外面定义变量，然后在for循环中使用。
# 实际使用：在for循环中使用变量，并不影响外部变量的使用。
a = 1
for a in range(1, 11):
    print(a)
    
print(a) # 变量a在for循环中使用，但是并不影响外部变量的使用。

# for循环嵌套
# 使用嵌套 for 循环打印二维矩阵的坐标
rows = 3  # 矩阵的行数
cols = 4  # 矩阵的列数

for i in range(rows):
    for j in range(cols):
        print(f"坐标 ({i}, {j})")

print(type(range(10))) # <class 'range'>


