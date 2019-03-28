# 创建与展示列表
bicycles = ['trek', 'cannondale', 'realine', 'specialized']
print(bicycles)
# 访问列表元素
print(bicycles[0])
print(bicycles[0].title())
# 使用列表中的各个值
message = "My first bicycle was a " + bicycles[0].title() + '.'
print(message)

# 修改添加删除列表元素
motocycles = ['honda', 'yamada', 'suzuki']
print(motocycles)
motocycles[0] = 'ducati'
print(motocycles)

motocycles = ['honda', 'yamada', 'suzuki']
motocycles.append('ducati')
print(motocycles)

motocycles = []
print(motocycles)
motocycles.append('honda')
motocycles.append('yamda')
motocycles.append('suzuki')
print(motocycles)

# 插入元素
motocycles = ['honda', 'yamada', 'suzuki']
motocycles.insert(0, 'ducati')
print(motocycles)
motocycles.insert(1, 'hha')
print(motocycles)

# 删除元素
motocycles = ['honda', 'yamada', 'suzuki']
del motocycles[2]
print(motocycles)

# 组织列表
cars = ['bmw', 'audi', 'toyato', 'subaru']
cars.sort()
print(cars)

# 反向排序
cars = ['bmw', 'audi', 'toyato', 'subaru']
cars.sort(reverse=True)
print(cars)

# 使用函数sorted()对列表进行临时排序
cars = ['bmw', 'audi', 'toyato', 'subaru']
print("Here is the original list:")
print(cars)
print("\nHere is the sorted list:")
print(sorted(cars))
print("\nHere is the original list again:")
print(cars)

# 倒序打印列表
cars = ['bmw', 'audi', 'toyato', 'subaru']
print(cars)
cars.reverse()
print(cars)

# 确定列表的长度
cars = ['bmw', 'audi', 'toyato', 'subaru']
length = len(cars)
print(length)
