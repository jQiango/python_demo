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
print('中文'.encode('ascii'))
# 纯英文的str可以用ASCII编码为bytes，内容是一样的，含有中文的str可以用UTF-8编码为bytes。含有中文的str无法用ASCII编码，因为中文编码的范围超过了ASCII编码的范围，Python会报错。