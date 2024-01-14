 #! Public vs Private Access:
class locker:
    def __init__(self, name, amount) -> None:
        self.name = name # public
        self.__money = amount # private (starts with __)
    def add_money(self, amount):
        # can't be accessed outside its class with name
        self.__money += amount
        # but can be accessed & modified inside its class
    def show_money(self):
        return self.__money

# public data can be accessed/modified directly outside class 
person = locker("Samin", 1000)
print("Original Name:",person.name)
person.name = 'Sadik'
print("Changed Name:",person.name)
# private data can't be accessed/modified normally
""" 
print("Original Bal:",person.__money)
person.__money = 0
print("Changed Bal:",person.__money)
"""
# private data is generally accessed through class methods
person.add_money(1003)
print('Secured =',person.show_money(), 'tk')
# still can be accessed/modified differently (loophole?)
print("Hacked -",person._locker__money, 'tk')
person._locker__money = 0
print("New :",person._locker__money, 'tk')

# TODO: What is Encapsulation