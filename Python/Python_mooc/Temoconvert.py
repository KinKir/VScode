# Tempconvert.py用于温度转换
TempStr = input('请输入带有符号位的温度：')
if TempStr[-1] in ['F', 'f']:
    C = (eval(TempStr[0:-1]) - 32) / 1.8
    print('转换后的温度为:{:.2f}C'.format(C))
elif TempStr[-1] in ['C', 'c']:
    F = 1.8 * (eval(TempStr[0:-1]) + 32)
    print("转换后的温度为:{:.2f}F".format(F))
else:
    print("输入格式有误，请重新输入！")
30
# 笔记：1、.2F表示取值位数；2、format函数的使用2
