class Dictclass(object):
    def __init__(self,dict):
        self.dict = dict
    
    def del_dict(self,key):
        if key in self.dict.keys():
            del self.dict[key]
            return self.dict
        else:
            return 'no result'

    def get_dict(self,key):
        if key in self.dict.keys():
            retuen self.dict[key]
        else:
            return 'not found'

    def update_dict(self,dict2):
        self.dict.update(dict2)
        return self.dict

    dict={
        'name':'ZJL',
        'grade':120,
        'age':20
    }
    a=Dictclass(dict1)
    key1=str(input('请输入要查找的内容'))
    print (a.get_dict(key1))
    key2=str(input('请输入你想要删除的内容'))
    print (a.del_dict(key2))
    print (a.update_dict({'gender':4}))