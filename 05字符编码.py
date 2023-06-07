# https://www.liaoxuefeng.com/wiki/1016959663602400/1017075323632896
# 对于单个字符的编码，Python提供了ord()函数获取字符的整数表示，chr()函数把编码转换为对应的字符：
print(ord('A'))
print(ord('中'))
print(chr(66))
print(chr(25991))
print('\u4e2d\u6587')

# 由于Python的字符串类型是str，在内存中以Unicode表示，一个字符对应若干个字节。如果要在网络上传输，或者保存到磁盘上，就需要把str变为以字节为单位的bytes。

# Python对bytes类型的数据用带b前缀的单引号或双引号表示：
x = b'ABC'
print(x)

print('ABC'.encode('ascii'))
print('中文'.encode('utf-8'))
# print('中文'.encode('ascii'))
# 纯英文的str可以用ASCII编码为bytes，内容是一样的，含有中文的str可以用UTF-8编码为bytes。含有中文的str无法用ASCII编码，因为中文编码的范围超过了ASCII编码的范围，Python会报错。

#!/usr/bin/env python3 
# -*- coding: utf-8 -*-

print(b'ABC'.decode('ascii'))
print(b'\xe4\xb8\xad\xe6\x96\x87'.decode('utf-8'))

# bytes中只有一小部分无效的字节，可以传入errors='ignore'忽略错误的字节：
print(b'\xe4\xb8\xad\xff'.decode('utf-8', errors='ignore'))

# 计算str包含多少个字符，可以用len()函数：
print(len('我说python'))

# len()函数计算的是str的字符数，如果换成bytes，len()函数就计算字节数：
print(len(b'ABC'))
print(len(b'\xe4\xb8\xad\xe6\x96\x87'))

# 格式化
print('Hello, %s' % 'world')
print('Hi, %s, you have $%d.' % ('Michael', 1000000))

# 占位符	替换内容
# %d	整数
# %f	浮点数
# %s	字符串
# %x	十六进制整数

print('%2d-%02d' % (3, 1))
print('%.2f' % 3.1415926)
# 字符串里面的%是一个普通字符怎么办？这个时候就需要转义，用%%来表示一个%：
print('growth rate: %d %%' % 7)

# format()
print('Hello, {0}, 成绩提升了 {1:.1f}%'.format('小明', 17.125))

# f-string
r = 2.5
print(r)
s = 3.14 * r ** 2
print(f'The area of a circle with radius {r} is {s:.2f}')


# operation
# 小明的成绩从去年的72分提升到了今年的85分，请计算小明成绩提升的百分点，并用字符串格式化显示出'xx.x%'，只保留小数点后1位：
s1= 72
s2=85
r=(s2-s1)/s1*100

print(f'小明的成绩提升了 {r:.2f}%')
print('{0}成绩提升了{1:.1f}%'.format('小明',r))
print('小明成绩提升了%.1f%%' % r)

