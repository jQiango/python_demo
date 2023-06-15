# dict
# Python内置了字典：dict的支持，dict全称dictionary，在其他语言中也称为map，使用键-值（key-value）存储，具有极快的查找速度
#  约等于 java的Map?
# 为什么这么快？顾名思义，其实是key作为索引值
dicts = {'Michael': 95, 'Bob': 75, 'Tracy': 85}
print(dicts['Bob'])

# 添加值
dicts['张三']=999
print(dicts['张三'])

# 通过in判断key是否存在：
print('张三1' in dicts)
# 通过dict提供的get()方法，如果key不存在，可以返回None，或者自己指定的value
print(dicts.get('张三1'))
print(dicts.get('张三1','不存在'))

# 要删除一个key，用pop(key)方法

dicts.pop('张三')
print(dicts)


# ，dict内部存放的顺序和key放入的顺序是没有关系的
# list比较，dict有以下几个特点：
    # 查找和插入的速度极快，不会随着key的增加而变慢；
    # 需要占用大量的内存，内存浪费多。
# 而list相反
# 查找和插入的时间随着元素的增加而增加；
# 占用空间小，浪费内存很少。



# set和dict类似，也是一组key的集合，但不存储value。由于key不能重复，所以，在set中，没有重复的key
# 要创建一个set，需要提供一个list作为输入集合
sets = set([1, 2, 3,1,1,1,1,1])
print(sets)
# 添加值
sets.add(999)
print(sets)
# 删除值
sets.remove(999)
print(sets)
# set可以看成数学意义上的无序和无重复元素的集合，因此，两个set可以做数学意义上的交集、并集等操作：
s1 = set([1, 2, 3])
s2 = set([2, 3, 4])
# 交集
print(s1 & s2)
# 并集
print(s1 | s2)
# set和dict的唯一区别仅在于没有存储对应的value，但是，set的原理和dict一样，所以，同样不可以放入可变对象，因为无法判断两个可变对象是否相等，也就无法保证set内部“不会有重复元素
# sets.add(['Michael', 'Bob', 'Tracy'])


# 不可变对象
a = ['c', 'b', 'a']
a.sort()
print(a)

# tuple虽然是不变对象，但试试把(1, 2, 3)和(1, [2, 3])放入dict或set中，并解释结果。
tuples = (1, 2, 3)
tuples2 = (1, [2, 3])
dicts[tuples]=tuples
dicts[tuples2]=tuples2
print(dicts)