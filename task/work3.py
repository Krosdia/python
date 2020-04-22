list1 = ['张三', '李四', '王五', '老二']

list2 = ['张三', '李四', '老二', '王七']

a = [x for x in list1 if x in list2] 
print('两个列表表都存在',a)