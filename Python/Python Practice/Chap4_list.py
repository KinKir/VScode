# 遍历整个列表
magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(magician)

# 深入研究循环 for循环必须冒号 循环体必须tab
for magician in magicians:
    print(magician.title()+", that was a great trick!")

for magician in magicians:
    print(magician.title()+", that was a great trick!")
    print("I can't wait to see your next trick, " + magician.title()+".\n")
print("Thank you, every one. That was a great magic show!")

# 创建数值列表
# 使用函数 range() 函数会打印从1到给定值-1的所有数字
for value in range(1, 5):
    print(value)

# 列表解析
squares = [value**2 for value in range(1, 11)]
print(squares)

# 使用列表的一部分--切片
numbers = list(range(1, 5))
print(list)
even_numbers = list(range(1, 11, 2))

# 混合使用列表
squares = []
for value in range(1, 11):
    square = value**2
    squares.append(square)
    print(squares)

squares = []
for value in range(1, 11):
    squares.append(value**2)

# 遍历切片
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print("Here are the first therr players on my tem")
for player in players[:3]:
    print(player.title())

# 复制列表
my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]
print("My favorite foods are:")
print(my_foods)
print("\nMy friend's favorite foods are：")
print(friend_foods)

# 使用列表的一部分
players = ['charles', 'martine', 'michal', 'florence', 'eli']
print(players[0:3])

# 元组
dimensions = (200, 50)
print(dimensions[0])
print(dimensions[1])

# 修改元组数据，不能够修改元组数值
demesions = (200, 50)
# demesions[0] = 250

# 遍历元组中的所有值
dimensios = (200, 50)
for demension in demesions:
    print(demension)

# 修改元组变量
dimensions = (200, 50)
print("Original dimensions:")
for dimensios in dimensions:
    print(dimensions)

dimensions = (400, 100)
print("\nmodefied dimensions:")
for dimension in dimensions:
    print(dimension)

#  设置代码格式
# PE8是最古老的代码格式之一
# 缩进：采用4个空格
# 行长：不超过80字符
# 空行：将程序的不同部分分开，可使用空行
