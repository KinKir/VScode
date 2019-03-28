# Chap7_用户输入和while循环

# 7.1函数input()的工作原理
message = input("Tell me something, and I will repeat it back to you")
print(message)

# 7.1.1编写清晰的程序
name = input("Please enter your name: ")
print("hello， " + name + "!")
"""有时候，提示可能超过一行，例如，你可能需要指出获取特定输入的原因。
在这种情况下，可将提示存储在一个变量中，再将该变量传递给函数input()。
这样，即便提示超过一行，input()语句也非常清楚"""

prompt = "if you tell me something, I will repeat back to you"
prompt += "\nWhat is your first name?"
name = input(prompt)
print("Hello, " + name + "!")

# 7.1.2使用int()获取数值输入
age = input("how old are you ?")
age = int(age)
age >= 18

# 7.1.3求模运算符
number = input("Enter a number, and I'll tell you if it's evem or odd: ")
nember = int(number)
if number % 2 == 0:
    print("\nThe number" + str(number) + "is  evwen.")
else:
    print("\nThe number " + str(number) + "is odd.")

# 7.1.4在python2.7中获取输入

# 7.2while循环
current_number = 1
while current_number <= 5:
    print(current_number)
    current_number += 1

# 7.2.1使用while循环
prompt = "\nTell me something, and I will repeat it back to you: "
prompt += "\nEnter 'quit' to end the program"
messge = " "
while message != 'quit':
    message = input(prompt)
    print(message)

# 7.2.2让用户选择何时推出

# 7.2.3使用标志

# 7.2.4使用break退出循环

# 7.2.5在循环中使用contiune

# 7.2.6避免无限循环

# 7.3使用while循环来处理列表和字典

# 7.3.1在列表之间移动元素

# 7.3.2删除包含特定值的所有列表元素

# 7.3.3使用字典输入来填充字典
