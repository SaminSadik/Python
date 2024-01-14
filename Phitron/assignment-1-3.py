 #* args example:
def func(*args):
    for arguments in args:
        print(arguments, end = " ")
    print(args)
func('arg-1', 'arg-2', '...', 'arg-N')
# Output:
# arg-1 arg-2 ... arg-N ('arg-1', 'arg-2', '...', 'arg-N')

 #* kwargs example:
def func(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")
    print(kwargs)
func(item1='name', item2=10, item3=True)
# Output:
# item1: name
# item2: 10
# item3: True
# {'item1': 'name', 'item2': 10, 'item3': True}