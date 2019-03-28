# title函数以首字母大写的方式显示所有字符
name = 'ada lovelace'
print(name.title())
# upper()以所有字符的大写方式输出
print(name.upper())
# lower()以所有字符的小写方式输出
print(name.lower())
# 合并字符串:通过+号连接两个字符串
fisrt_name = 'ada'
last_name = 'lovelace'
full_name = fisrt_name + ' ' + last_name
print(full_name)
# 使用制表符\t
print("Python")
print("\tPython")
# 使用换行符实现换行\n
print("Language:\nPython\nC\nC++\nJavaScript")
# 叠加使用
print("Language:\n\tPython\n\tC\n\tC++\n\tJavasript")
# 删除空白
favorite_language = 'Python '
favorite_language
favorite_language.rstrip()
favorite_language
# 永久删除空白,#删除末尾空白
# favorite_language = favorite_language.rstrip()
# 删除开头空白
# favorite_language = favorite_language.lstrip()
# 删除两端空白
# favorite_language = favorite_language.strip()
# 正确使用双引号与单引号
message = "One of Python's strengths is its diverse comunity"
# 数字运算 整数/浮点数
a = 3+5*6
# 使用str()函数避免类型错误
age = 23
# message_flase = 'Happy'+age+'birthday'
message = 'Happy'+str(age)+'rd birthday'
print(message)
