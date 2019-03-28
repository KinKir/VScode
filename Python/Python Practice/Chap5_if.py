# if语句用于测试检查，并决定采取什么措施
cars = ['audi', 'bmw', 'subaru', 'toyata']
for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())

# 条件测试--检查是否相等
car = 'bmw'
car == 'bmw'

# 检查是否相等时考虑大小写，可先进行转换再比较

# 检查是否不相等
request_topping = 'mushrooms'
if request_topping != 'anchoves':
    print("Hold the anchovies")

# 比较数字
age = 18
age == 18
answer = 17
if answer != 0:
    print("That is the correct answer.Please try again")
# 检查多个条件
# 1\使用and
age_0 = 22
age_1 = 18
age_0 >= 21 and age_1 >= 21
age_1 = 24
age_0 >= 21 and age_1 >= 21
# 使用or
age_0 = 22
age_1 = 23
age_0 >= 25 or age_1 >= 20
age_0 <= 25 or age_1 <= 20
# 检查特定值是否包含在列表中
requested_toppings = ['mushrooms', 'options', 'pineapple']
'mushrooms' in requested_toppings
'pepperoni' in requested_toppings
# 检查特定值是否不包含在列表中
banned_users = ['andrew', 'carlina', 'david']
user = 'marie'
if user not in banned_users:
    print(user.title() + ", you can post a response if you wish")
# 布尔表达式
game_active = True
can_edit = False
# if语句
# 简单的if语句
age = 19
if age >= 19:
    print("you are old enough to vote1")
# if...else...语句
age = 17
if age >= 18:
    print("You are old enough to vote")
    print("Have you registered to vote yet?")
else:
    print("Sorry, you are too young to vote.")
    print("Please register to vote as soon as you turn 18!")
# if...elif...if语句
age = 12
if age < 4:
    print("Your admission cost is $0")
elif age > 18:
    print("your admission cost is $10")
else:
    print("Your admission cost is $5")

age = 12
if age < 4:
    price = 0
elif age > 18:
    price = 10
else:
    price = 5
print("Your admission cost is " + "$" + str(price) + ".")
# 使用多个elif代码块
age = 17
if age < 4:
    price = 0
elif age < 18:
    price = 5
elif age < 65:
    price = 10
else:
    price = 5
print("Your admission cost is $" + str(price) + ".")

# 省略else代码块用elif替换
age = 17
if age < 4:
    price = 0
elif age < 18:
    price = 5
elif age < 65:
    price = 10
elif age >= 65:
    price = 5
print("Your admission cost is $" + str(price) + ".")
# 测试多个条件
requested_toppings = ['mushrooms', 'extra cheese']
if 'mushrooms' in requested_toppings:
    print("Adding mushrooms.")
if 'pepperoni' in requested_toppings:
    print("Adding pepperoni.")
if 'extra cheese' in requested_toppings:
    print("Adding extra cheese")
print("\nFinished making your pizza")
# if...elif...else结构

# 使用if语句处理列表

# 检查特殊元素

# 确定列表不是空的

# 使用多个列表

# 使用if语句处理列表

# 设置if语句的格式
