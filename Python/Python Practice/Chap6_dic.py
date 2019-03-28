# Chap6_字典

# 6.1一个简单的字典
alien_0 = {'color': 'green', 'points': 5}
print(alien_0['color'])
print(alien_0['points'])

# 6.2使用字典
alien_0 = {'color': 'green'}

# 6.2.1访问字典的值
alien_0 = {'color': 'green'}
print(alien_0['color'])
alien_0 = {'color': 'green', 'points': 5}
new_points = alien_0['points']
print("You just earned " + str(new_points) + " points!")

# 6.2.2添加键-值对
alien_0 = {'color': 'green', 'points': 5}
print(alien_0)
alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)

# 6.2.3创建一个空字典
alien_0 = {}
alien_0['color'] = 'green'
alien_0['points'] = 5
alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)

# 6.2.4修改字典的值
alien_0 = {'color': 'green'}
print("This alien is " + alien_0['color'] + ".")
alien_0['color'] = 'yellow'
print("This alien is " + alien_0['color'] + ".")

alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}
print("Original alien x_position: " + str(alien_0['x_position']))
# 向右移动外星人，据外星人当前速度决定将其移动多远
if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    x_increment = 3
alien_0['x_position'] = alien_0['x_position'] + x_increment
print("The new x_position: " + str(alien_0['x_position']))

# 6.2.5删除键-值对
alien_0 = {'color': 'green', 'points': 5}
print(alien_0)
del alien_0['points']
print(alien_0)

# 6.2.6由类似对象组成的字典
favorie_language = {
    'jen': 'C',
    'sraaj': 'python',
    'edward': 'ruby',
    'ptil': 'python'
}
print("sraaj favoite language is " + favorie_language['sraaj'].title() + ".")

# 6.3遍历字典

# 6.3.1遍历所有的键-值对
favorie_language = {
    'jen': 'C',
    'sraaj': 'python',
    'edward': 'ruby',
    'ptil': 'python'
    }
for name, language in favorie_language.items():
    print(name.title() + "favorite language is " + language.title() + ".")

# 6.3.2遍历字典中的所有键
favorie_language = {
    'jen': 'C',
    'sraaj': 'python',
    'edward': 'ruby',
    'ptil': 'python'
}
for name in favorie_language.keys():
    print(name.title())

# 6.3.3按顺序遍历字典中的所有键
favorie_language = {
    'jen': 'C',
    'sraaj': 'python',
    'edward': 'ruby',
    'ptil': 'python'
}
for name in sorted(favorie_language.keys()):
    print(name.title() + ", Thank you for taking the poll")

# 6.3.4 遍历字典中的所有值
favorie_language = {
    'jen': 'C',
    'sraaj': 'python',
    'edward': 'ruby',
    'ptil': 'python'
}

# 6.4嵌套
alien_0 = {'color': 'green', 'points': 5}
alien_1 = {'color': 'yellow', 'points': 10}
alien_2 = {'color': 'red', 'points': 15}
aliens = [alien_0, alien_1, alien_2]
for alien in aliens:
    print(alien)

# 6.4.1字典列表

# 6.4.2在字典中存储列表

# 6.4.3在字典中存储字典
