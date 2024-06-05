class SquareIterator:
    def __init__(self, limit):
        self.limit = limit
        self.current = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.current < self.limit:
            result = self.current ** 2
            self.current += 1
            return result
        else:
            raise StopIteration

# Пример использования
iterator = SquareIterator(5)
for i in iterator:
    print(i)
