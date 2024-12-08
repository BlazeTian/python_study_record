my_string = "Hello World"
my_string_split = my_string[5:1:-1] #注意如果是反向取值，起始位置和结束位置的顺序要调换，即：my_string[5:1:-1] 而不是 my_string[1:5:-1]
print(my_string_split)


my_string = "Hello World"
my_string_reverse = my_string[::-1] # 取值范围为整个字符串，步长为-1，即反向取值
print(my_string_reverse)
