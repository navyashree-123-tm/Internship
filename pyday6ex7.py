class Engine:
    def start(self):
        print("Engine started")

class Car:
    def __init__(self):
        self.engine = Engine()

    def start_engine(self):
        self.engine.start()
my_car=Car()
my_car.start_engine()
