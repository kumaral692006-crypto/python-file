from abc import ABC, abstractmethod

class Notification(ABC):
    @abstractmethod
    def send(self):
        pass

class Email(Notification):
    def send(self):
        print("Sending Email Notification")

class SMS(Notification):
    def send(self):
        print("Sending SMS Notification")

class Push(Notification):
    def send(self):
        print("Sending Push Notification")


# objects
e = Email()
e.send()

s = SMS()
s.send()

p = Push()
p.send()
