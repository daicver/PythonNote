# 字符串拆分

# 使用list切分为字母列表
str= "hello"
list_str = list(str)
print(list_str)
# ['h', 'e', 'l', 'l', 'o']

str= "hello,,world"
# 使用split按字符切分（默认为按空格切分）
list_str = str.split(',')
print(list_str)
# ['hello', '', 'world']

# https://www.python100.com/html/59572.html
# 判断元素是否在列表中
my_list = ['apple', 'banana', 'orange']
if 'apple' in my_list: 
    print('apple in my_list')

# 统计元素在列表中出现的次数
my_list = ['apple', 'banana', 'apple', 'orange', 'apple']
cnt = my_list.count('apple')
print(cnt)

# 遍历列表
my_list = ['apple', 'banana', 'orange']
for index, item in enumerate(my_list):
    if item == 'banana':
        print('banana在列表中的位置是：', index)

# 使用集合判断元素是否在列表中
my_list = ['apple', 'banana', 'orange']
my_set = set(my_list)
if 'apple' in my_set:
    print('apple in myset')
