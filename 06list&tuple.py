
# list 数组
classmates = ['Michael', 'Bob', 'Tracy']
print(classmates)
print(len(classmates))
print(classmates[0],classmates[1],classmates[2])
# 要取最后一个元素，除了计算索引位置外，还可以用-1做索引，直接获取最后一个元素：
print(classmates[-1])

# list是一个可变的有序表，所以，可以往list中追加元素到末尾
classmates.append('Adam')
print(classmates)

# 把元素插入到指定的位置，比如索引号为1的位置
classmates.insert(1, 'Jack')
print(classmates)

# 要删除list末尾的元素，用pop()方法
classmates.pop()
print(classmates)

# 删除指定位置的元素，用pop(i)方法，其中i是索引位置
classmates.pop(1)
print(classmates)

# 把某个元素替换成别的元素，可以直接赋值给对应的索引位置
classmates[1] = 'Sarah'
print(classmates)

# list里面的元素的数据类型也可以不同 这里就和java不一样了，不受泛型约束
L = ['Apple', 123, True]

# list里面增加另一个list
s = ['python', 'java', ['asp', 'php'], 'scheme']

p = ['asp', 'php']
s = ['python', 'java', p, 'scheme']

# 获取php的值两种方式
print(p[1])
# 因此s可以看成是一个二维数组，类似的还有三维、四维……数组，不过很少用到
print(s[2][1])






# tuple 元组 tuple和list非常类似，但是tuple一旦初始化就不能修改， 
# tuple 语法 ()
# list []
# 不可变的tuple有什么意义？因为tuple不可变，所以代码更安全。如果可能，能用tuple代替list就尽量用tuple。

tuples = ('Michael', 'Bob', 'Tracy')
print(tuples)
t = (1, 2)
print(t)
# 如果要定义一个空的tuple，可以写成()：
# 注意：！！定义的不是tuple，是1这个数！这是因为括号()既可以表示tuple，又可以表示数学公式中的小括号，这就产生了歧义，因此，Python规定，这种情况下，按小括号进行计算，计算结果自然是1。
t = (1)
print(t)
t = (1,)
print(t)
# “可变的”tuple：“指向不变”
t = ('a', 'b', ['A', 'B'])
t[2][0] = 'X'
t[2][1] = 'Y'
print(t)

# 练习
# 请用索引取出下面list的指定元素：
L = [
    ['Apple', 'Google', 'Microsoft'],
    ['Java', 'Python', 'Ruby', 'PHP'],
    ['Adam', 'Bart', 'Lisa']
]
# 打印Apple:
print(L[0][0])
# 打印Python:
print(L[1][1])
# 打印Lisa:
print(L[2][2])
