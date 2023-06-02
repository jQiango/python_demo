print("Hello, World!")
# 第一个注释
import keyword;

print(keyword.kwlist)
# 第二个注释
'''
第三注释
第四注释
'''
"""
第五注释
第六注释
"""
str2 = 'a'
if str2 == 'a':
    print("im true")
else:
    print("im false")

# 数字
a = 3
b = True
c = 1.23
d = 1 + 2j

print(a, b, c, d)

# 字符串
word = '字符串'
sentence = "这是一个句子。"
paragraph = """这是一个段落，
可以由多行组成"""
print(paragraph)

str2 = 'dasjldalksjds'

print(str2)  # 输出字符串
print(str2[0:-1])  # 输出第一个到倒数第二个的所有字符
print(str2[0])  # 输出字符串第一个字符
print(str2[2:5])  # 输出从第三个开始到第六个的字符（不包含）
print(str2[2:])  # 输出从第三个开始后的所有字符
print(str2[1:5:2])  # 输出从第二个开始到第五个且每隔一个的字符（步长为2）
print(str2 * 2)  # 输出字符串两次
print(str2 + '你好')  # 连接字符串

print('------------------------------')

print('hello\nrunoob')  # 使用反斜杠(\)+n转义特殊字符
print(r'hello\nrunoob')  # 在字符串前面添加一个 r，表示原始字符串，不会发生转义

# input("\n\n按下 enter 键后退出。")


import sys;

x = 'runoob';
sys.stdout.write(x + '\n')
