# 字符串拆分

# 使用 list 切分为字母列表
str= "hello"
list_str = list(str)
print(list_str)
# ['h', 'e', 'l', 'l', 'o']

# 使用split按字符切分（默认为按空格切分）
str= "hello,,world"
list_str = str.split(',')
print(list_str)
# ['hello', '', 'world']

# https://www.python100.com/html/59572.html
# 判断元素是否在列表中
my_list = ['apple', 'banana', 'orange']
if 'apple' in my_list: 
    print('apple in my_list')

# 使用集合判断元素是否在列表中
my_list = ['apple', 'banana', 'orange']
my_set = set(my_list)
if 'apple' in my_set:
    print('apple in myset')


# 统计元素在列表中出现的次数
my_list = ['apple', 'banana', 'apple', 'orange', 'apple']
cnt = my_list.count('apple')
print('apple count', cnt)

# 遍历列表
my_list = ['apple', 'banana', 'orange']
for index, item in enumerate(my_list):
    if item == 'banana':
        print('banana在列表中的位置是：', index)

my_list = ['apple', 'banana', 'orange']
counts = [0] * 26
for str in my_list:
    for s_i in str:
        counts[ord(s_i)-ord('a')]+=1
for i in range(26):
    if counts[i]>0:
        print(chr(ord('a')+i),counts[i],sep=',')
        print(chr(ord('a')+i),counts[i])

print和sys.stdout.write的区别
输出方式：
    sys.stdout.write: 这是 sys.stdout 对象的方法，用于将字符串写入标准输出。它不会自动添加换行符，所以你需要在输出的字符串末尾显式地添加换行符 \n，如果你想要换行的话。
    print: 这是 Python 内置的函数，用于将一个或多个对象打印到标准输出。它会在每个对象之间自动添加空格，并在输出结束时默认添加换行符。你可以通过设置 end 参数来更改默认的结束字符，从而实现不换行或者使用其他字符。
使用的便利性：
    sys.stdout.write 需要显式地写入字符串，并在需要时添加换行符。这对于需要更精细控制输出格式的情况可能更有用，但可能需要更多的编码工作。
    print 更为方便，因为它可以一次性打印多个对象，它会自动处理空格和换行，更适合一般的输出需求。


isinstance 和 type 的区别在于：
    type()不会认为子类是一种父类类型。
    isinstance()会认为子类是一种父类类型。

Python3 中，bool 是 int 的子类，True 和 False 可以和数字相加， True==1、False==0 会返回 True，但可以通过 is 来判断类型

转意字符：\ 
禁止转意：r''
\ 可以作为续行符

字符串不能被赋值

连接列表： +
重复列表： *

tup1 = ()    # 空元组
tup2 = (20,) # 一个元素，需要在元素后添加逗号
虽然tuple的元素不可改变，但它可以包含可变的对象，比如list列表


创建一个空集合必须用 set() 而不是 { }，因为 { } 是用来创建一个空字典

sites = {'Google', 'Taobao', 'Runoob', 'Facebook', 'Zhihu', 'Baidu'}
print(sites)   # 输出集合，重复的元素被自动去掉

# set可以进行集合运算
a = set('abracadabra')
b = set('alacazam')
print(a)
print(a - b)     # a 和 b 的差集
print(a | b)     # a 和 b 的并集
print(a & b)     # a 和 b 的交集
print(a ^ b)     # a 和 b 中不同时存在的元素

字典是一种映射类型，字典用 { } 标识，它是一个无序的 键(key) : 值(value) 的集合
键(key)必须使用不可变类型。
在同一个字典中，键(key)必须是唯一的
tinydict = {'name': 'runoob','code':1, 'site': 'www.runoob.com'}
print (tinydict)          # 输出完整的字典
print (tinydict.keys())   # 输出所有键
print (tinydict.values()) # 输出所有值
构造字典
>>> dict([('Runoob', 1), ('Google', 2), ('Taobao', 3)])
{'Runoob': 1, 'Google': 2, 'Taobao': 3}
>>> {x: x**2 for x in (2, 4, 6)}
{2: 4, 4: 16, 6: 36}
>>> dict(Runoob=1, Google=2, Taobao=3)
{'Runoob': 1, 'Google': 2, 'Taobao': 3}


x = bytes("hello", encoding="utf-8")
x = b"hello"
y = x[1:3]  # 切片操作，得到 b"el"
z = x + b"world"  # 拼接操作，得到 b"helloworld"
需要注意的是，bytes 类型中的元素是整数值，因此在进行比较操作时需要使用相应的整数值
x = b"hello"
if x[0] == ord("h"):
    print("The first element is 'h'")

chr(x)
将一个整数转换为一个字符

ord(x)
将一个字符转换为它的整数值

hex(x)
将一个整数转换为一个十六进制字符串

oct(x)
将一个整数转换为一个八进制字符串


在Linux/Unix系统中，你可以在脚本顶部添加以下命令让Python脚本可以像SHELL脚本一样可直接执行：
#! /usr/bin/env python3
然后修改脚本权限，使其有执行权限，命令如下：
$ chmod +x hello.py
执行以下命令：
./hello.py

random
choice(seq)	从序列的元素中随机挑选一个元素，比如random.choice(range(10))，从0到9中随机挑选一个整数。
randrange ([start,] stop [,step])	从指定范围内，按指定基数递增的集合中获取一个随机数，基数默认值为 1
random()	随机生成下一个实数，它在[0,1)范围内。
seed([x])	改变随机数生成器的种子seed。如果你不了解其原理，你不必特别去设定seed，Python会帮你选择seed。
shuffle(lst)	将序列的所有元素随机排序
uniform(x, y)	随机生成下一个实数，它在[x,y]范围内。

f-string 格式化字符串以 f 开头，后面跟着字符串，字符串中的表达式用大括号 {} 包起来，它会将变量或表达式计算后的值替换进去
f'Hello {name}'  # 替换变量
'Hello Runoob'

del lists[2]
remove方法
lists.remove(lists[2])

列表比较
operator.eq(a,b)
在列表末尾添加新的对象
list.append(obj)
统计某个元素在列表中出现的次数
list.count(obj)
在列表末尾一次性追加另一个序列中的多个值（用新列表扩展原来的列表）
list.extend(seq)
从列表中找出某个值第一个匹配项的索引位置
list.index(obj)
将对象插入列表
list.insert(index, obj)
移除列表中的一个元素（默认最后一个元素），并且返回该元素的值
list.pop([index=-1])
移除列表中某个值的第一个匹配项
list.remove(obj)
反向列表中元素
list.reverse()
对原列表进行排序
list.sort( key=None, reverse=False)
清空列表
list.clear()
复制列表
list.copy()

列表推导式
[表达式 for 变量 in 列表] 
[out_exp_res for out_exp in input_list]
[表达式 for 变量 in 列表 if 条件]
[out_exp_res for out_exp in input_list if condition]

字典推导式
{ key_expr: value_expr for value in collection }
或
{ key_expr: value_expr for value in collection if condition }

集合推导式
{ expression for item in Sequence }
或
{ expression for item in Sequence if conditional }

元组推导式
(expression for item in Sequence )
或
(expression for item in Sequence if conditional )

迭代器
list=[1,2,3,4]
it = iter(list)    # 创建迭代器对象
print (next(it))   # 输出迭代器的下一个元素

list=[1,2,3,4]
it = iter(list)    # 创建迭代器对象
for x in it:
    print (x, end=" ")

可以看见在调用函数前后，形参和实参指向的是同一个对象（对象 id 相同），在函数内部修改形参后，形参指向的是不同的 id
可变对象在函数里修改了参数，那么在调用这个函数的函数里，原始的参数也被改变了

不定长参数
加了星号 * 的参数会以元组(tuple)的形式导入，存放所有未命名的变量参数
def printinfo( arg1, *vartuple ):

加了两个星号 ** 的参数会以字典的形式导入
def printinfo( arg1, **vardict ):
printinfo(1, a=2,b=3)

lambda [arg1 [,arg2,.....argn]]:expression
# 可写函数说明
sum = lambda arg1, arg2: arg1 + arg2
# 调用sum函数
print ("相加后的值为 : ", sum( 10, 20 ))
