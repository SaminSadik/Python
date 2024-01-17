# Poly(many/multiple) + Morph(shape/form)

class Human:
    def __init__(self, name) -> None:
        self.name = name
        print(f"{name} just spawned")
    def introduce(self):
        print(f"{self.name}: I'm definitely a Human")

class mail(Human):
    def __init__(self, name) -> None:
        super().__init__(name)
    def introduce(self):
        print(f"{self.name}: I am a boii")
# polymorphism of this introduce method for different classes

class femail(Human):
    def __init__(self, name) -> None:
        super().__init__(name)
    def introduce(self):
        print(f"{self.name}: I am a gaal")
# method overriden, so won't inherit this method from base class

class gmail(Human):
    def __init__(self, name) -> None:
        super().__init__(name)
# no introduce method here, so it will inherit from base class

boy = mail('Saad')
girl = femail('Meem')
Ai = gmail('ChatGPT')

boy.introduce()
girl.introduce()
Ai.introduce()
# same introduce() have multiple forms in different classes


class Human:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gen = gender

    def overriden(self):
        print("I'm overriden, so my child won't get me")
    
    def unOverriden(self):
        print("I wasn't overriden, so my child uses me")

class Programmer(Human):
    def __init__(self, name, age, gender, income):
        self.income = income
        super().__init__(name, age, gender)

    def overriden(self):
        print("I overriden my parent, so I won't inherit this")

    # operator overloading using dunder/magic methods
    def __add__(self, other): # + op overload
        return self.age + other.age
    
    # dunder method names starts & ends with double-underscore
    def __le__(self, other): # <= op overload
        return self.income <= other.income
    
    # similarly built-in function overloading
    def __len__(self): # len() function overload 
        return self.age * self.income

entity1 = Programmer('Samin', 21, 'male', 0)
entity1.overriden()
entity1.unOverriden()
entity2 = Programmer('Sadia', 99, 'female', 1000000000)

print("\nInteger Addition: 12 + 11 =", 12 + 11)
print("String Addition:'Samin' + 'Sadik' =", 'Samin'+'Sadik')
print("Lest Addition: [1,2,3] + [10,20,30] =", [1,2,3] + [10,20,30])

# these normally wouldn't work without overloading:
print("Addition Overloaded:", entity1 + entity2)
print("Male Income <= Female Income:", entity1 <= entity2)
print("Overloaded fun:",len(entity2))

# print(dir(int)) # checking other dunder methods