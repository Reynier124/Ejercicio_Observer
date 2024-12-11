from observer import Observer

class User(Observer):
    def __init__(self, name):
        self._name = name

    def notify(self):
        print(f"El usuario {self._name} ha recibido la notificación")