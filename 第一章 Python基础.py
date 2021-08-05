# 1.5 Python的输入与输出
# print('嗨！Python我来了！') #输出
# name=input('请输入你的姓名') #输入     注：变量名可以是数字、字母、下划线，不能以数字开始
# print(name)

# 1.7 学Python，不愁没对象
# print(id('孙敬然')) #查询对象内存地址
# print(type(99)) #查询对象类型 int整数
# print(type('99')) #查询对象类型 str字符串
# print(type(99.99)) #查询对象类型 float浮点数
# print(type(99+0j)) #查询对象类型 complex复数

# 1.8 Python中的数字与字符串
# print('孙\n敬然') #换行符
# print('孙\r敬然') #回车符
# print('孙\t敬然') #制表符
# print('孙\\n敬然') #转普通字符
# print(r'孙\n敬然') #转普通字符
# num=99.99
# print(int(num)) #转换整数
# print(str(num)) #转换字符
# print('num')      #转换字符
# print("num")      #转换字符
# print(float(num)) #转换浮点数
# print(complex(num)) #转换复数

# 1.9 算术运算符
# print(1+1)
# print('孙'+'100分')
# print(3-1)
# print(2*3)
# print('孙！'*3)
# # print(3**3) #幂
# print(10/3)
# print(10//3)   #取整
# print(int(10/3))   #取整
# print(10%3)    #取模（余数）

# 1.10 比较运算符(True False)
# print(1==1)
# print(1==2)
# print(1!=2)
# print(1!=1)
# print(2>1)
# print(1>2)
# print(1<2)
# print(2<1)
# print(2>=2)
# print(2>=3)
# print(2<=3)
# print(2<=1)

# 1.11 赋值运算符
# n=0
# print(id(n))
# n=n+1           # n+=1
# print(id(n))
# n=n+2           # n+=2
# print(id(n))
# n=n+3           # n+=3
# print(id(n))
# print(n)
#
# a=100
# print(type(a))
# print(id(a))
# a=str(a)
# print(id(a))
# print(type(a))

# 1.12 逻辑运算符(True False)
# print(3>2 and 4>3)  #都成立
# print(2>3 and 3>2)
# print(2>3 or 3>2)   #有一个成立
# print(1>2 or 2>3)
# print(not 2>3)
# print(not 3>1)

# 1.13 成员运算符
# print('1' in '123')   #只针对字符串
# print('1' not in '123')

# 1.14 格式化字符串
# %[(name)][flags][width].[precision]typecode
# [(name)]可选，用于指定的key
# [flags]可选
#     右对齐:+，默认即是右对齐，（输出的正负数前会显示符号）
#     右对齐:空格（输出的正数前加空格，负数前加负号）
#     右对齐:0(输出正数前无符号，负数前加负号，用0填充空白处)
#     左对齐:-(输出正数前无符号，负数前加负号)
# [width]可选，占有宽度
# .[precision]可选，小数点后保留位数
# typecode必选
#    s，字符串
#    d，整数
#    f，浮点数
# a=10.123456789
# print('%+10.2s'%a)
# print('|% 10.2d|%010.3f|%-10.4f|'%(a,a*2,a*3))

# 1.15 完美看清代码运行过程
# num=input('输入：')
# num=float(num)
# num/=2
# print('结果：%.2f分'%num)