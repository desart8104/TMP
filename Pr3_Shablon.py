from abc import ABC, abstractmethod

class AbstractClass(ABC):
    @abstractmethod
    def operation1(self):
        pass

    @abstractmethod
    def operation2(self):
        pass

    def template_method(self):
        self.operation1()
        self.operation2()

class ConcreteClass(AbstractClass):
    def operation1(self):
        print("Operation 1 implementation")

    def operation2(self):
        print("Operation 2 implementation")

if __name__ == "__main__":
    concrete_object = ConcreteClass()
    concrete_object.template_method()
