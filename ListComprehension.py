#_LIST COMPREHENTION IN PYTHON

'''fruits=["apples","mango","banana","kiwi","Oranges"]
newFruits=[]
for x in fruits:
    if "n" in x:
        newFruits.append(x)
print(newFruits)
'''

#list comprehension bellow

"""fruits=["apples","mango","banana","kiwi","Oranges"]
newFruits=[x for x in fruits if "a" in x]
print(newFruits)
"""
fruit=["mango","banana","kiwi","apples","Oranges"]
newFruits=[x for x in fruit if "banana" is != x]
print(newFruits)

