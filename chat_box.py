
class ChatBox:
    def __init__(self):
        self.observers = []
    
    def add_observer(self, observer):
        self.observers.append(observer)
    
    def remove_observer(self, observer):
        self.observers.remove(observer)
    
    def notify_all(self, user, message):
        for observer in self.observers:
            if observer != user:
                observer.notify()
        print(message)