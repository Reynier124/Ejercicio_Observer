from observer import Observer

class Admin(Observer):
    def __init__(self, name):
        self._name = name
    
    def notify(self):
        print(f"El administrador {self._name} ha recibido la notificación")