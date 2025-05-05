'''look! this is my No.1 python file.'''
#Chinese: 这是一条注释！以上也是一条注释。
import random #导入random库
a=1 #变量
b=[1,2,3,4,5,6,7,8] #列表
for i in b: #第一种for循环：在列表、元组等内循环
  print("Hello,world!I'm GC-1-1(Ha Ha!)\n\t",a,b) #打印"Hello,world!"，用户名与a,b。
  for i in range(5): #嵌套循环和第二种for循环：range()函数循环
    print("随机数：",random.random(),random.choice(range(0,10)),random.randint(0,100),random.shuffle((0,1,2,3,4,5,6,7,8,9,10),(10,11,12,13,14,15,16,17,18,19,20)))
    if(a): #绝对会执行的if语句
      print("a==1!")
