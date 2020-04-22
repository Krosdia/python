from random import randint
def filter_l(data):
    print(data.items())
    # 把字典转换成dict_items，循环里面的key和value，满足if条件返回对应的key和value值
data = {x:randint(60,100) for x in range(1,20)}
# 过滤出分数高于80的同学
res = {k:v for k,v in data.items() if v >= 80}
print(res)