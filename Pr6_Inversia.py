class Observer:
    def update(self, data):
        pass


class Subject:
    def __init__(self):
        self._observers = []

    def attach(self, observer):
        self._observers.append(observer)

    def detach(self, observer):
        self._observers.remove(observer)

    def notify(self, data):
        for observer in self._observers:
            observer.update(data)


class DataSource(Subject):
    def set_data(self, data):
        self.notify(data)


class DataObserver(Observer):
    def __init__(self, name):
        self.name = name

    def update(self, data):
        print(f"{self.name} received data: {data}")


if __name__ == "__main__":
    data_source = DataSource()

    observer1 = DataObserver("Observer1")
    observer2 = DataObserver("Observer2")

    data_source.attach(observer1)
    data_source.attach(observer2)

    data_source.set_data("Hello, this is the data")
