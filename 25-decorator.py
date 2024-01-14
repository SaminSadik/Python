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


 #! Getter & Setter: