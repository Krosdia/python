
import string
print('请输入字符串')
str_c = input()

str_letter=string.ascii_letters

dict_letter={}

for letter in str_letter:

    dict_letter[letter]=[]

for i in str_c:

    dict_letter[i].append(i)

for count in str_letter:

    if len(dict_letter[count])!=0:

        print("%s的个数为%d"%(count,len(dict_letter[count])))
