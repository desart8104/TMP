class Strategy:
    def execute(self, num1, num2):
        pass

class AddStrategy(Strategy):
    def execute(self, num1, num2):
        return num1 + num2

class SubtractStrategy(Strategy):
    def execute(self, num1, num2):
        return num1 - num2

class Context:
    def __init__(self, strategy):
        self.strategy = strategy

    def execute_strategy(self, num1, num2):
        return self.strategy.execute(num1, num2)

# Пример использования
num1 = 10
num2 = 5

add_strategy = AddStrategy()
sub_strategy = SubtractStrategy()

context = Context(add_strategy)
result = context.execute_strategy(num1, num2)
print(f"Результат сложения: {result}")

context.strategy = sub_strategy
result = context.execute_strategy(num1, num2)
print(f"Результат вычитания: {result}")
