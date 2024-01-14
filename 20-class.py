 #! Class & Object declaration:
class myClass: # creating a class
    name = 'Samin'
    age = 21 # class attributes / static attribute
    gender = "male"

info = myClass() # creating an object of a class to use
print(info) # can't see the object data like this
print(info.name, info.age, info.gender) # accessing object data


 #! Constructors & Class Functions:
class cFunctions:
    id = 101
    def __init__(self) -> None: # default constructor
        pass
    # __init__ define the constructor
    # every class function must have a self argument
    # None is the return type (can be ommited if nothing returns)
    # pass indicates this constructor does nothing

    def myFunc(self):
        print("\nClass Functions", self.id)
    def retFun(self, sub):
        return (f"{sub} {self.id+1}\n")
    # specifying return type is not compulsory, except in constuctor
    
metho = cFunctions() # no parameter needed only for the self argument
metho.myFunc()
returned = metho.retFun('Consrtuctor is Class Function')
print(returned)


 #! Class variable Vs. Instance variable:
class verDiff:
    items = [] # class varibale (shared by all instances in the class)
    def __init__(self, name): 
        print("Object Constructed", name)
        self.name = name # storing the parameter for later use
        self.pvt_items = [] # instance variable
    def add_item(self, item):
        print(f"{item} added to {self.name}'s list")
        self.items.append(item)
        self.pvt_items.append(item)

his, her = verDiff('Mr'), verDiff('Ms')
hisList = his.add_item((1,2))
print("His List?", his.items) # using class variable
herList = her.add_item((3,4))
print("Her List?", her.items)

# using instance variable (items) which is not shared:
print("His Main List:", his.pvt_items)
print("Her Main List:", her.pvt_items)


 #! Class representation (__rept__):
print()
class Unrepresented:
    def __init__(self, name, ID, hp):
        self.Name = name
        self.hp = hp
        self.id = ID
personel = Unrepresented('Sadik', 21, 'male')
print(personel)

# same thing but with __repr__:
class Represented:
    def __init__(self, name, age, gender):
        self.Name = name
        self.gen = gender
        self.age = age
    # changing the default return(from object address)
    def __repr__(self) -> str: # str is the return type here
        return f'Name: {self.Name}, Age: {self.age}, Gender: {self.gen}'
personel = Represented('Sadik', 21, 'male')
print(personel)
# instead of an address, returns according to representation 
