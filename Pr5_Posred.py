class Mediator:
    def create_partnership(self, partner1, partner2):
        pass


class Partner:
    def __init__(self, name, mediator):
        self.name = name
        self.mediator = mediator

    def request_partnership(self, partner):
        self.mediator.create_partnership(self, partner)


class ConcreteMediator(Mediator):
    def create_partnership(self, partner1, partner2):
        print(f"{partner1.name} and are now partners")

if __name__ == "__main__":
    mediator = ConcreteMediator()

    partner1 = Partner("Alice", mediator)
    partner2 = Partner("Bob", mediator)

    partner1.request_partnership(partner2)
