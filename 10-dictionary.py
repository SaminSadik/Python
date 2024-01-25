# Dictionary is similar to sets but with key,value pairs
dic = {'name':'Sadik', 'age':20, 'gender':'male'}
print(dic) # shows all pairs in dictionary format
print(dic.keys()) # shows all keys only
print(dic.values()) # shows all value only

print(dic['name']) # keys are like index in dictionary
dic['name'] = 'San' # mutable, so can update value
dic['income'] = 0 # can add new key value pair like this
print(dic)

dic = {
    'name': 'samin',
    'age': 20,
    'age': 21, # won't keep duplicate keys, last value prevails
    'income': '0 tk'
}
print(dic)
print("Size of this", type(dic), ":", len(dic)) # type & len works

# Using dict() constructor [it won't even take duplicate key]
dic = dict(name = 'Sadik', gender = 'male', income = 0)

print('Befor Deleting Income:',dic)
del dic['income'] # deletes the key & its value
print('After Deleting Income:',dic)

print("\nNormal Loop Only Iterates for Key:", end=" ")
for key in dic: print(key, end=' ')

print("\nSpecial looping for Dictionary:")
for (key, val) in dic.items(): print(key,'=',val)

 # TODO: How to search in a Dictionary