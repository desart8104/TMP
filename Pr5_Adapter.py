# Адаптируемый класс
class Adaptee:
    def specific_request(self):
        return "Specific request"

# Целевой интерфейс
class Target:
    def request(self):
        return "Default request"

# Адаптер
class Adapter(Target):
    def __init__(self, adaptee):
        self.adaptee = adaptee

    def request(self):
        return f"Adapter: {self.adaptee.specific_request()}"

# Клиентский код
def client_code(target):
    print(target.request())

if __name__ == "__main__":
    adaptee = Adaptee()
    adapter = Adapter(adaptee)

    print("Adaptee interface is incompatible with the Target interface.")
    print("But with adapter it's compatible.")
    client_code(adapter)
