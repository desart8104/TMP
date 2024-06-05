from abc import ABC, abstractmethod

# Абстрактные классы для создания продуктов
class AbstractProductA(ABC):
    @abstractmethod
    def do_something(self):
        pass

class AbstractProductB(ABC):
    @abstractmethod
    def do_another_thing(self):
        pass

# Конкретные классы продуктов
class ConcreteProductA1(AbstractProductA):
    def do_something(self):
        print("Product A1 doing something")

class ConcreteProductA2(AbstractProductA):
    def do_something(self):
        print("Product A2 doing something")

class ConcreteProductB1(AbstractProductB):
    def do_another_thing(self):
        print("Product B1 doing another thing")

class ConcreteProductB2(AbstractProductB):
    def do_another_thing(self):
        print("Product B2 doing another thing")

# Абстрактная фабрика
class AbstractFactory(ABC):
    @abstractmethod
    def create_product_A(self) -> AbstractProductA:
        pass

    @abstractmethod
    def create_product_B(self) -> AbstractProductB:
        pass

# Конкретные фабрики
class ConcreteFactory1(AbstractFactory):
    def create_product_A(self) -> AbstractProductA:
        return ConcreteProductA1()

    def create_product_B(self) -> AbstractProductB:
        return ConcreteProductB1()

class ConcreteFactory2(AbstractFactory):
    def create_product_A(self) -> AbstractProductA:
        return ConcreteProductA2()

    def create_product_B(self) -> AbstractProductB:
        return ConcreteProductB2()

# Создание продуктов с помощью фабрик
factory1 = ConcreteFactory1()
productA1 = factory1.create_product_A()
productA1.do_something()
productB1 = factory1.create_product_B()
productB1.do_another_thing()

factory2 = ConcreteFactory2()
productA2 = factory2.create_product_A()
productA2.do_something()
productB2 = factory2.create_product_B()
productB2.do_another_thing()
