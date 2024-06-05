class Visitor:
    def visit(self, element):
        pass

class ElementA:
    def accept(self, visitor):
        visitor.visit(self)

class ElementB:
    def accept(self, visitor):
        visitor.visit(self)

class ConcreteVisitorA(Visitor):
    def visit(self, element):
        print("ConcreteVisitorA visited", element.__class__.__name__)

class ConcreteVisitorB(Visitor):
    def visit(self, element):
        print("ConcreteVisitorB visited", element.__class__.__name__)

# Пример использования
element_a = ElementA()
element_b = ElementB()

visitor_a = ConcreteVisitorA()
visitor_b = ConcreteVisitorB()

element_a.accept(visitor_a)
element_b.accept(visitor_b)
