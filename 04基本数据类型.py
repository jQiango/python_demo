# https://www.liaoxuefeng.com/wiki/1016959663602400/1017063826246112
# Python 中的变量不需要声明。每个变量在使用前都必须赋值，变量赋值以后该变量才会被创建。

# 在 Python 中，变量就是变量，它没有类型，我们所说的"类型"是变量所指的内存中对象的类型。

# 等号（=）用来给变量赋值。

# 等号（=）运算符左边是一个变量名,等号（=）运算符右边是存储在变量中的值。例如：

# 整数
print(10_000_000_000)
print(10000000000)
# 浮点数
print(10000000000)


# 字符串
# 转义字符\可以转义很多字符，比如\n表示换行，\t表示制表符，字符\本身也要转义，所以\\表示的字符就是\，可以在Python的交互式命令行用print()打印字符串
print('I\'m \"OK\"!')
print('I\'m learning\nPython.')
print(r'\\\t\\')
# 如果字符串内部有很多换行，用\n写在一行里不好阅读，为了简化，Python允许用'''...'''的格式表示多行内容
print('''line1
... line2
... line3''')

# 布尔值
True
False
print(3 > 2)
print(3 > 5)

# 布尔值可以用and、or和not运算。 and运算是与运算，只有所有都为True，and运算结果才是True：
print(True and True)
print(True and False)
print(False and False)
print(5 > 3 and 3 > 1)
# or运算是或运算，只要其中有一个为True，or运算结果就是True：
print(True or False)

# not运算是非运算，它是一个单目运算符，把True变成False，False变成True：
print(not True)
print(not False)

age=1
if age >= 18:
    print('adult')
else:
    print('teenager')

# 空值
# 空值是Python里一个特殊的值，用None表示。None不能理解为0，因为0是有意义的，而None是一个特殊的空值。
print(None)

# 变量
# 变量的概念基本上和初中代数的方程变量是一致的，只是在计算机程序中，变量不仅可以是数字，还可以是任意数据类型。

# 变量在程序中就是用一个变量名表示了，变量名必须是大小写英文、数字和_的组合，且不能用数字开头
a = 1
t_007 = 'T007'
Answer = True
print(a,t_007,Answer)
a = 123 # a是整数
print(a)
a = 'ABC' # a变为字符串
print(a)

# 最后，理解变量在计算机内存中的表示也非常重要。当我们写：
# a = 'ABC'
# 时，Python解释器干了两件事情：

# 在内存中创建了一个'ABC'的字符串；

# 在内存中创建了一个名为a的变量，并把它指向'ABC'。

# 也可以把一个变量a赋值给另一个变量b，这个操作实际上是把变量b指向变量a所指向的数据，例如下面的代码：

a = 'ABC'
b = a
a = 'XYZ'
print(b)

# 常量
# 常量就是不能变的变量，比如常用的数学常数π就是一个常量。在Python中，通常用全部大写的变量名表示常量：
PI = 3.14159265359
# 但事实上PI仍然是一个变量，Python根本没有任何机制保证PI不会被改变，所以，用全部大写的变量名表示常量只是一个习惯上的用法，如果你一定要改变变量PI的值，也没人能拦住你。
print(10 / 3)

print(10 // 3)
# Python还提供一个余数运算，可以得到两个整数相除的余数：
print(10 % 3)

n = 123
f = 456.789
s1 = 'Hello, world'
s2 = 'Hello, \'Adam\''
s3 = r'Hello, "Bart"'
s4 = r'''Hello,
Lisa!'''

print(n,f,s1,s2,s3,s4)
print('n=123')