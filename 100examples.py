#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author: Xu,Haijun time: 2020-02-22

# 三角形面积
import math
     # 可以不导入模块,像例子那样写 x**0.5
while True:
    print("请先输入三角形的三边长a,b,c")
    try:
        # 输入字符串会非法,提示重新输入
        a = float(input("请输入边长a:"))
        b = float(input("请输入变成b:"))
        c = float(input("请输入边长c:"))
    except ValueError:
        print("您输入的不是一个数字无法计算三角形面积,请重新输入正确的数字")
    else:
        # 判断三边的边长能否构成一个三角形
        if a+b > c and a+c > b and b+c > a:
            p = (a + b + c)/2
            s = math.sqrt(p*(p-a)*(p-b)*(p-c))
            print("三角形的面积为:{0:.3f}".format(s))
        else:
            print("输入的三边构不成三角形")

#a = float(input('输入三角形第一边长: '))
#b = float(input('输入三角形第二边长: '))
#c = float(input('输入三角形第三边长: '))
#
## 计算半周长
#s = (a + b + c) / 2
#
## 计算面积
#area = (s*(s-a)*(s-b)*(s-c)) ** 0.5
#print(f'三角形面积为{area:.2f}')
#

#import math
#def triangle_area_calculate():
#    judge = True
#    while judge:
#        a, b, c = sorted(eval(input('请输入三角形的三个边长（用逗号隔开）:'))) # sorted排序
#        if a > 0 and b > 0 and c > 0:
#            if c < a + b: #因为sorted的结果就是a<b<c, 所以只需要一个判断即可
#                p = (a + b + c)/2
#                S = math.sqrt(p*(p-a)*(p-b)*(p-c))
#                print(f'三角形的面积是{S:.3f}')
#                judge = False
#            else:
#                print('警告：三边不能构成三角形，请重新输入！！！')
#if __name__ == '__main__':
#    triangle_area_calculate()
#

### 平方根
#num = float(input('请输入一个数字：'))
#num_sqrt = num ** 0.5
#print('%0.3f 的平方根为 %0.3f'%(num, num_sqrt))
#print(f'{num:.3f} 的平方根为 {num_sqrt:.3f}')

import cmath
#num = int(input('请输入一个数字：'))
#num_sqrt = cmath.sqrt(num)
#print('{0} 的平方根为 {1:0.3f} + {2:0.3f}j'.format(num, num_sqrt.real, num_sqrt.imag))
#print(f'{num:.3f} 的平方根为 {num_sqrt:.3f}')
#
try:
    num = float(input('请输入一个数字：'))
except:
    print('输入的数字格式不正确，请重新输入！')
else:
    if num>=0:
        num_sqrt = num**0.5
        print(f'{num}的平方根是{num_sqrt:.3f}')
    else:
        num_sqrt = cmath.sqrt(num)
        #print(f'{num:.3f} 的平方根为 {num_sqrt:.3f}')
        print(f'{num:.3f} 的平方根为 {num_sqrt.real:.3f}+{num_sqrt.imag:.3f}j')

# 二次方程
import cmath

a = float(input('input a: '))
b = float(input('input b: '))
c = float(input('input c: '))

d = (b**2) - (4*a*c)

sol1 = (-b-cmath.sqrt(d))/(2*a)
sol2 = (-b+cmath.sqrt(d))/(2*a)

print('结果为 {0} 和 {1}'.format(sol1,sol2))
#print(f'结果为{sol1:.3f}和{sol2:.3f}')

# 二次方程式 ax**2 + bx + c = 0
# a、b、c 用户提供，为实数，a ≠ 0

import cmath

def get_para(para):
    """获取参数a, b, c的函数"""
    while True:
        try:
            number = float(input('请输入{}:'.format(para)))
            if para == 'a' and number == 0:
                print('a不能等于0!\n')
                continue
        except ValueError:
            print('请输入一个实数!\n')
            continue
        else:
            break
    return number

def solve(a, b, c):
    """解方程的函数"""
    d = b*b - 4*a*c
    if d < 0: # 复数解
        sol_1 = (-b + cmath.sqrt(d)) / (2*a)
        sol_2 = (-b - cmath.sqrt(d)) / (2*a)
    else: # 实数解
        sol_1 = (-b + d**0.5) / (2*a)
        sol_2 = (-b - d**0.5) / (2*a)
    print('方程的两个解为:\n{}\n{}'.format(sol_1, sol_2))

print('-'*60)
print('求解二次方程式 ax**2 + bx + c = 0 '.center(50))
print('-'*60)
print('请提供a, b, c的值(a, b, c为实数，a ≠ 0)'.center(50))
print('-'*60)

while True:
    a = get_para('a')
    b = get_para('b')
    c = get_para('c')
    solve(a, b, c)
    active = input('\n是否继续？(y/n): ')
    if active == 'n':
        break

#import math
#import unicodedata
#
#def is_number(s):
#    try:
#        float(s)
#        return True
#    except ValueError:
#        pass
#    try:
#        unicodedata.digit(s)
#        return True
#    except (TypeError, ValueError):
#        pass
#    return False
#
#a = input('输入 a: ')
#b = input('输入 b: ')
#c = input('输入 c: ')
#
#if is_number(a) and is_number(b) and is_number(c):
#    a = float(a)
#    b = float(b)
#    c = float(c)
#    if a == 0 and b == 0:
#        print('不是方程， 不需要解！')
#    elif a == 0 and b != 0:
#        x = -c / b
#        print(f'为一次方程式，结果为{x:.2f}')
#    elif a != 0 and b == 0:
#        d = -c / a
#        if d >= 0:
#            x = math.sqrt(d)
#            print(f'x的结果为{x:.2f}')
#        else:
#            print('警告：该方程无解！！！')
#    elif a != 0 and b != 0:
#        d = (b**2) - (4*a*c)
#        if d >= 0:
#            x1 = (-b - math.sqrt(d)) / (2 * a)
#            x2 = (-b + math.sqrt(d)) / (2 * a)
#            print(f'方程的结果为：x1={x1:.2f}, x2={x2:.2f}')
#        else:
#            print('警告：该方程无解！！！')
#    else:
#        print('错误！！！')
#else:
#    print('请输入数字类型！！！')

# 交换变量
x = input('输入 x 值：')
y = input('输入 y 值：')

temp = x
x = y
y = temp

print('交换后的x值为：{}'.format(x))
print('交换后的y值为：{}'.format(y))

x = input('输入 x 值: ')
y = input('输入 y 值: ')

# 不使用临时变量
x, y = y, x

print('交换后 x 的值为: {}'.format(x))
print('交换后 y 的值为: {}'.format(y))

# 任意数字比大小
N = int(input('输入需要对比大小数字的个数: '))
print('请输入需要对比的数字: ')
num = []

for i in range(1, N+1):
    temp = int(input('输入第%d个数字'%i))
    num.append(temp)

print('你输入的数字为: ', num)
print('最大值为: ', max(num))

# 任意数字比大小_MOD
num = []

print('输入Q/q来结束输入数字！')
while True:
    temp = input('请输入数字：')
    if temp != 'q' and temp != 'Q':
        try:
            i = int(temp)
            num.append(i)
        except ValueError:
            print('输入的不是数字！')
    else:
        break

print('你输入的数字为: ', num)
print('最大的数字是：', max(num))

# 判断闰年
year = int(input("请输入年份："))

print('闰年' if (year%4==0 and year%100!=0) or year%400==0 else '平年')

import calendar
print(calendar.isleap(2020))
print(calendar.isleap(2001))

# 圆面积
import math

pi = math.pi

def circle_area():

    r = input('请输入圆的半径: ')

    while r.isdigit() == False or float(r) <= 0:
        print("请输入大于0的数字！")
        r = input('请输入圆的半径: ')
    else:
        r = float(r)
        area = r * r * pi
        print('圆的面积为 %d' %area)

circle_area()

#import math
#while True:
#    try:
#        r = float(input('请输入圆的半径r:'))
#    except ValueError:
#        print('请输入正确的数字!')
#    else:
#        if r >= 0:
#            p = math.pi
#            square = p*r**2
#            print(f'圆的面积是：{square:.4f}')
#        else:
#            print()
#        active = input('\n是否继续?(y/n):')
#        if active == 'n':
#            break

# 奇偶数
num = int(input("输入一个数字: "))
if (num % 2) == 0:
   print("{0} 是偶数".format(num))
else:
   print("{0} 是奇数".format(num))

num = eval(input('Number:\n'))
print('{} is '.format(num) + ('even number.' if num % 2 == 0 else 'odd number.'))

# 数字判断
def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        pass

    try:
        import unicodedata
        unicodedata.numeric(s)
        return True
    except (TypeError, ValueError):
        pass

    return False

# 测试字符串和数字
print(is_number('foo'))  # False
print(is_number('1'))  # True
print(is_number('1.3'))  # True
print(is_number('-1.37'))  # True
print(is_number('1e3'))  # True

str = "123456";
print (str.isdigit())

str = "Runoob example...";
print (str.isdigit())

# 数字求和
num1 = input('input number 1: ')
num2 = input('input number 2: ')

sum = float(num1) + float(num2)

print('summary of number {0} and number {1} is: {2}'.format(num1, num2, sum))

print('两数之和为 %.1f' %(float(input('输入第一个数字：'))+float(input('输入第二个数字：'))))
#print(f'数字{num1}和数字{num2}相加结果为：{sum}')

# while 1:
#     num1 = input('输入第一个数字：')
#     num2 = input('输入第二个数字：')
#     try:
#         sum = float(num1) + float(num2)
#     except:
#         print('输入的数字格式不正确，请重新输入！')
#         continue
#     else:
#         print(f'俩个数字之和为: {sum:.0f}')
#         break

# 文件IO
with open("test.txt", "wt") as out_file:
    out_file.write("该文本会写入到文件中\n看到我了吧！")

# Read a file
with open("test.txt", "rt") as in_file:
    text = in_file.read()

print(text)

###w, r, wt, rt 都是 python 里面文件操作的模式。
###w 是写模式，r 是读模式。
###t 是 windows 平台特有的所谓 text mode(文本模式）,区别在于会自动识别 windows 平台的换行符。
###类 Unix 平台的换行符是 \n，而 windows 平台用的是 \r\n 两个 ASCII 字符来表示换行，python 内部采用的是 \n 来表示换行符。
###rt 模式下，python 在读取文本时会自动把 \r\n 转换成 \n。
###wt 模式下，Python 写文件时会用 \r\n 来表示换行。

# 条件语句
num = float(input("输入一个数字: "))
if num > 0:
   print("正数")
elif num == 0:
   print("零")
else:
   print("负数")

num = float(input("输入一个数字: "))
if num >= 0:
   if num == 0:
      print("零")
   else:
      print("正数")
else:
   print("负数")

# 温度转换
#celsius = float(input('输入摄氏温度: '))
#
#fahrenheit = (celsius * 1.8) + 32
#print('%0.1f 摄氏温度转为华氏温度为 %0.1f ' %(celsius,fahrenheit))

a = int(input('摄氏度转换为华氏温度请按1\n华氏温度转化为摄氏度请按2\n'))
while a != 1 and a != 2:
    a = int(input('你选择不正确，请重新输入。\n摄氏度转换为华氏温度请按1\n华氏温度转换为摄氏度请按2\n'))
if a == 1:
    celsius = float(input('输入摄氏度:'))
    fahrenheit = (celsius*1.8)+32 #计算华氏温度
    print('%.1f摄氏度转为华氏温度为%.1f' %(celsius,fahrenheit))
else:
    fahrenheit = float(input('输入华氏度:'))
    celsius = (fahrenheit-32)/1.8 #计算摄氏度
    print('%.1f华氏度转为摄氏度为%.1f' %(fahrenheit,celsius))

# 获取最大值函数
a = []
while True:
    #输入q来结束输入数字
    c = input('请输入数字：')
    if c != 'q':
        try:
            i = int(c)
            a.append(i)
        except ValueError:
            print('输入的不是数字！')
    else:
        break
print('最大数字是：', max(a))

# N = int(input('输入需要对比大小数字的个数：'))
# print("请输入需要对比的数字：")
# num = []
# for i in range(1,N+1):
#     temp = int(input('输入第 %d 个数字' % i))
#     num.append (temp)
#
# print('您输入的数字为：',num)
# print('最大值为：',max(num))

# 随机数
import random
i = 1
a = random.randint(0,100)
b = int(input('请输入0-100中的一个数字\n然后查看是否与电脑一样：'))
while a != b:
    if a > b:
        print('你第%d次输入的数字小于电脑随机数'%i)
        b = int(input('请再次输入数字：'))
    else:
        print('你第%d次输入的数字大于电脑随机数'%i)
        b = int(input('请再次输入数字：'))
    i+=1
else:
    print('恭喜你！你第%d次输入的数字与电脑的随机数字%d一样'%(i,b))

# 猜数字游戏
import random

rang1 = int(input("请设置本局游戏的最小值:"))
rang2 = int(input("请设置本局游戏的最大值:"))
num = random.randint(rang1, rang2)
guess = "guess"
print("数字猜谜游戏！")
i = 0
while guess != num:
    i += 1
    guess = int(input("请输入你猜的数字："))

    if guess == num:
        print("恭喜，你猜对了！")
    elif guess < num:
        print("你猜的数小了...")
    else:
        print("你猜的数大了...")

print("你总共猜了%d" % i + "次", end='')
print(",快和你朋友较量一下...")

# 随机数_MOD
import random
import re
from  sys import exit

def main():
    time = 3
    count = 1
    num = 0
    dict = {'0':5,'1':10,'2':20,'3':50,'4':100}

    print('猜数字')
    go = int(input('开始：1\n结束：0\n->'))

    while go != 1 and go != 0:
        print('Input 1 or 0.')
        go = int(input('开始：1\n结束：0\n->'))
    if go == 1:
        pass
    elif go == 0:
        exit()

    print('｛LV0.新手}｛LV1.简单｝｛LV2.一般｝｛LV3.困难｝｛LV4.噩梦｝｛LV5.地狱｝')
    r = input('Level:')
    r = re.sub('\D', '', r)

    if r.strip() == '':
        print('隐藏难度｛LV6.调戏｝')
        n = 1000
        time = 99
    else:
        n = dict.get(r, 500)

    secret = random.randint(1, n + 1)
    print('猜猜{1-%s}之间的数:' % n)

    while True:
        print('一定是：', end='')
        num = input()

        if num.isdigit():
            num = int(num)
            if num < 1:
                print('现在就放弃太可惜了')
            elif num > n:
                print('超出范围')
            elif num > secret:
                print('太大')
            elif num < secret:
                print('太小')
            else:
                if count == 1:
                    print('棒')
                elif count == 2:
                    print('赞')
                else:
                    print('好')
                break

            time -= 1
            count += 1

            if time == 0:
                print('正确答案：%s' % secret)
                break
            else:
                print('还有[%s]次机会:' % time)
        else:
            print('要崩溃了!!!')
    print('游戏结束!')

if __name__ == '__main__':
    main()

# 随机星星
import random
class computer(object):

    def __init__(self):
        pass

    g_num = 0
    def ger_num(start,end):
        return random.randint(start,end)

    def contrl(ctl_str):
        global g_num
        if ctl_str == 'l' or ctl_str == 'L':
            g_num -= 1
            if g_num < 0:
                g_num = 23
        elif ctl_str == 'r' or ctl_str == 'R':
            g_num += 1
            if g_num > 23:
                g_num = 0
        return g_num

    @staticmethod
    def print_space(space_num):
        print_content = ['-']*24
        print_content = ''.join(print_content)
        l_content = list(print_content)
        l_content[space_num] = '*'
        l_content = ''.join(l_content)
        print(l_content)

if __name__ == '__main__':
    #生成随机数，确定星号的位置
    g_num = computer.ger_num(0,24)
    computer.print_space(g_num)
    while True:
        ctrl_str = input("请输入移动星星的指令(L/l or R/r):")
        if ctrl_str == 'EXIT' or ctrl_str == 'exit':
            break
        g_num = computer.contrl(ctrl_str)
        computer.print_space(g_num)
