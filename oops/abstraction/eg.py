from abc import ABC, abstractmethod

class vechical(ABC):

    @abstractmethod
    def start(self):
        pass

class car(vechical):
    def start(self):
        print("car start with key")
class bike(vechical):
    def start (self):
        print("bike start with key ")

c=car()
c.start()

b=bike()
b.bike()