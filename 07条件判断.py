# if
age = 20
if age >= 18:
    print('your age is', age)
    print('adult')

# if else
age = 3
if age >= 18:
    print('your age is', age)
    print('adult')
else:
    print('your age is', age)
    print('teenager')

#elif    elif是else if的缩写，完全可以有多个elif
# if <条件判断1>:
#     <执行1>
# elif <条件判断2>:
#     <执行2>
# elif <条件判断3>:
#     <执行3>
# else:
#     <执行4>
# if语句执行有个特点，它是从上往下判断，如果在某个判断上是True，把该判断对应的语句执行后，就忽略掉剩下的elif和else
age = 3
if age >= 18:
    print('adult')
elif age >= 6:
    print('teenager')
else:
    print('kid') 
# 判断条件还可以简写 只要x是非零数值、非空字符串、非空list等，就判断为True，否则为False。
x=True
if x:
    print('True')
# ！！！类型转换 str->int
# s = input('birth: ')
# birth = int(s)
# if birth < 2000:
#     print('00前')
# else:
#     print('00后')


# 练习
# 小明身高1.75，体重80.5kg。请根据BMI公式（体重除以身高的平方）帮小明计算他的BMI指数，并根据BMI指数
# 低于18.5：过轻
# 18.5-25：正常
# 25-28：过重
# 28-32：肥胖
# 高于32：严重肥胖
height = 1.75
weight = 80.5
bmi = weight/(height ** 2)
print(bmi)
if bmi>32:
    print('高于32：严重肥胖')
elif bmi >28:
    print('28-32：肥胖')
elif bmi >25:
    print('25-28：过重')
elif bmi>18.5:
    print('18.5-25：正常')
else:
    print('低于18.5：过轻')