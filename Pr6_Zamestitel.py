from abc import ABC, abstractmethod

# Заместитель
class Subject(ABC):
    @abstractmethod
    def request(self):
        pass

# Реальный объект
class RealSubject(Subject):
    def request(self):
        print("Реальный объект выполняет запрос")

# Заместитель
class Proxy(Subject):
    def __init__(self):
        self.real_subject = RealSubject()

    def request(self):
        if self.check_access():
            self.real_subject.request()
        else:
            print("Доступ запрещен")

    def check_access(self):
        # Здесь можно добавить логику проверки доступа
        return True

# Использование
proxy = Proxy()
proxy.request()
