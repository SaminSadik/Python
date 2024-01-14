class Base:
    def __init__(self, property1, property2) -> None:
        self.common1 = property1
        self.common2 = property2
    def __repr__(self) -> str:
        return (f"[{self.common1} ; {self.common2}]")

class Derived(Base): # format: child-class(parent-class)
    def __init__(self, property1, property2, property3, property4): 
        self.uncommon1 = property3
        self.uncommon2 = property4
        super().__init__(property1, property2)
        # using super() to pass arguments to parent class
    def __repr__(self) -> str:
        print(self.common1) # directly accessing parent's property
        return f"{super().__repr__()} ; [{self.uncommon1} ; {self.uncommon2}]"
        # using super() to access properties of parent class

child = Derived('A', 'B', 'a', 'b')
print(child.common1, child.uncommon1, end=" ")
print(child)


 #! Types of Inheritance:

class Grandparent:
    def __init__(self):
        print("At grandparent's")

class parent_A(Grandparent): # Simple inheritance
    def __init__(self):
        print("At A-parent's", end=" -> ")
        super().__init__() # constructing / going to Baseclass

class parent_B(Grandparent): # Hierarchical inheritance
    def __init__(self):
        print("At B-parent's", end=" -> ")
        super().__init__()
    
class child_A(parent_A): # Multi-level inheritance
    def __init__(self):
        print("At A-child's", end=" -> ")
    # instead of super(), a parent class can be specified to go
        Grandparent.__init__(self)
    # in such case, self must be give among the required arguments
    
class child_B(parent_A, parent_B): # Multiple inheritance
    def __init__(self):
        print("At B-child's", end=" -> ")
        super().__init__()
        # parent_A.__init__(self)
    
# This combind "family tree"/inheritance is Hybrid inheritance

print()  
fam1 = child_A()
fam2 = child_B() #? why pB after pA instead of grand ?#
print()

 #! Compositions:
# Interitance -> "is a" relation
# Composition -> "has a" relation
class Strength:
    def start(self):
        print('Muscles Ready')

class Wisdom:
    def __init__(self) -> None:
        self.start = 'Brain is ON'

class Human:
    def __init__(self) -> None:
        self.body = Strength()
        self.mind = Wisdom()
    # composition is similar to inheritance
    
    def start(self):
        self.body.start()
        print(self.mind.start)

person = Human()
person.start()