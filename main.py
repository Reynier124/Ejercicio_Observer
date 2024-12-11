from chat_box import ChatBox
from user import User
from admin import Admin

facultad = ChatBox()

alumno1 = User("Rodrigo")
alumno2 = User("Carlita")
admin = Admin("Marta")

facultad.add_observer(alumno1)
facultad.add_observer(alumno2)
facultad.add_observer(admin)

facultad.notify_all(admin, "Este grupo es para cosas relacionadas a la facultad")

facultad.remove_observer(alumno2)

facultad.notify_all(alumno1, "Ok")