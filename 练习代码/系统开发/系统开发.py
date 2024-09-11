

#生成随机数,随机数范围为1~10


import random
number = random.randint(1,10)

#打印生成的随机数
print(number)


#编写函数用来计算输入的整数的阶乘

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)
    
#num = int(input())
print("您所输入的数字的阶乘为：")
print(factorial(num))


    

#尝试截取字符串一部分与一段字符拼接
str = 'Hello World!'
print("拼接后的字符串：",str[0:6]+'tom')


#将字符串 a = “This is string example” 全部转成大写，字符串 b = “Welcome To My World” 全部转成小写
a = 'This is string example'
b = 'Welcome To My World'

print(a.upper())
print(b.lower())


#比较给出的列表是否相同

import operator
a = [1, 2, 3]
b = [2, 3, 4]


if operator.eq(a,b):
    print("两个列表相同")
else:
    print("两个列表不相同")
    
    

a = [3,0,8,5,7]
for i in range(len(a)):
    if a[i] > 5:
       a[i] = 1
    else:
       a[i] = 0
print(a)



#向字典 {‘Alice’: 20, ‘Beth’: 18, ‘Cecil’: 21} 中追加 ‘David’:19 键值对，更新Cecil的值为17
a = {'Alice':20,'Beth':18,'Cecil':21}
a['David'] = 19
a['Cecil'] = 17
print(a)


#以列表 [‘A’,‘B’,‘C’,‘D’,‘E’,‘F’,‘G’,‘H’] 中的每一个元素为键，默认值都是0，创建一个字典
a = ['A','B','C','D','E','F','G','H']
b = {}
for i in a:
    b[i] = 0
print(b)


#创建一个空集合，增加 {‘x’,‘y’,‘z’} 三个元素
a = set() #空集合只能用set()创建
b = {'x','y','z'}
a.update(b)
print(a)


