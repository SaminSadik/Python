# importing abstract base class module
from abc import ABC, abstractmethod

class Human(ABC):
    @abstractmethod
    #enforcing all derived class to have The following method
    def talk(self):
        print('I want to speak')

    # @abstractmethod
    def go(self, name):
        print(f"{name} is going...")
    # not enforcing this method without @abstractmethod
        
    # enforcing this method without using @abstractmethod
    def breath(self):
        raise NotImplementedError # Goriber abstraction
    # if it's not in derived class, this error will be raised

class Boy(Human):
    def __init__(self, name) -> None:
        super().__init__()
        self.name = name

    # must have this method, as enforced by @abstractmethod
    def talk(self):
        # super().talk()
        print(f"My name is {self.name}")

    # without it base-class function will force an error:
    def breath(self):
        print("Congrats, you survived")

person = Boy('Samin')
# accesses derived class's method, not base class's method:
person.talk()
# can access base class's method directly, if not abstracted:
person.go(person.name)

person.breath()

# TODO: Abstract vs Interface