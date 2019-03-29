# PythonDraw.py实例2
import turtle
turtle.setup(650, 350, 200, 200)
turtle.penup()
turtle.fd(-250)
turtle.pendown()
turtle.pensize(25)
turtle.pencolor("purple")
turtle.seth(-40)
for i in range(4):
    turtle.circle(40, 80)
    turtle.circle(-40, 80)
turtle.circle(40, 80 / 2)
turtle.fd(40)
turtle.circle(16, 180)
turtle.fd(40 * 2 / 3)
turtle.done()

"""
import 保留字，导入库
库名.函数（函数参数）
import库名as别名
turtle 绘图库，海归库
turtle库的使用：
1、turtle库基本介绍：
最小单位为像素
turtle.setup(with,height,startx,starty)宽度、高度、横坐标、纵坐标
2、turtle空间坐标体系：绝对坐标
turtle.goto(x,y)直线走向
海归坐标
turtle.fd()前进方向
turtle.bk()后退方向
3、角度坐标体系
turtle.seth(angle)改变绘图方向
海归角度：
turtle.left(angle)
turtle.right(angle)
4、RGB色彩模式
turtle.colormode()
"""