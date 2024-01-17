 #! class method & static method

class myClass:
    clsVar = ' 0 ' # class / static variable
    def __init__(self):
        self.InsVar = ' x ' # Instance variable

    def function(self, num):
        self.InsVar += num
        self.clsVar += num
        print('Normal Function Invoked', self.InsVar)

    @classmethod
    def classFunction(self, num):
        self.clsVar += num
        # can access class variable but not instance varaiable
        print('Class Function Invoked', self.clsVar)

    @staticmethod
    def staticFunction(num):
        # can't access outside variables, as self is not passed
        print('Static Function Invoked', num)

    # @(at) is called decorator

obj = myClass()
obj.function(' 1 ')
# if a medhod is used without object, self argument is required

myClass.classFunction(' 2 ')
# class & static methods can be used without object & self argument
myClass.staticFunction(' 3 ')

# class & static methods can be called with object, but not prefered
obj.classFunction(' 8 ')
obj.staticFunction(' 5 ')
print()


 #! Getter & Setter:

class decorate:
    def __init__(self, value) -> None:
        self.__value = value
    
    def showValue(self):
        print('Value is', self.__value)
    
    @property # marks the following method as getter
    def accessValue(self):
        print('= Got', self.__value)
    # getter without setter is read-only & can't have parameters

    @accessValue.setter # makes a method setter
    def accessValue(self, val): # name must be same as its getter
        if val < 0: print('Invalid setting attempt')
        else:
            self.__value += val
            print('+ Set', val)
    # setter format: @'getter-name'.setter [above target method]
            
test = decorate(1)
test.showValue()

# test.accessValue() # will throw error
test.accessValue # getter method is invoked like a variable
test.accessValue = 10 # wouldn't work without setter
# setter doesn't take parameter like a normal method
test.showValue()
print()


 #! Nested Methods:

def outer():
    print('Outer method invoked')
    def inner(): # method within method
        print('Inner method invoked')
    return inner

print(outer()) # calling the outer method only
outer()() # calling the inner method aswell
print()


 #! Parameter Method:

def method_taker(fun):
    print('Main method opened')
    fun()
    print('Main method closed')

def method_send():
    print('Parameter method invoked')

method_taker(method_send) # sending method as parameter
print()


 #! Decorated nested Methods: (Kinda Complex)

def outer_fun(para_fun):
    # parameter of the parameter method goes to inner method
    def inner_fun(*args):
        print('Inner method started')
        para_fun(*args)
        print('Inner method ended')
    return inner_fun

@outer_fun # making following method parameter or this method
def aFunction(arg):
    print('Decorated', arg)

aFunction(101) # now calls the method its parameter of