from abc import ABC, abstractmethod

# Компоновщик
class Component(ABC):
    @abstractmethod
    def operation(self):
        pass

# Лист
class Leaf(Component):
    def operation(self):
        print("Лист выполняет операцию")

# Контейнер
class Composite(Component):
    def __init__(self):
        self.children = []

    def add(self, component):
        self.children.append(component)

    def remove(self, component):
        self.children.remove(component)

    def operation(self):
        print("Контейнер выполняет операцию:")
        for component in self.children:
            component.operation()

# Использование
leaf1 = Leaf()
leaf2 = Leaf()

composite = Composite()
composite.add(leaf1)
composite.add(leaf2)

composite.operation()
