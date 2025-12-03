class SantiagoCont:
    def __init__(self, nombre, telefono, email):
        self.nombre = nombre
        self.telefono = telefono
        self.email = email

class SantiagoAgenda:
    def __init__(self):
        self.contactos = []

    def agregar_contacto(self, contacto):
        self.contactos.append(contacto)

    def buscar_contacto(self, nombre):
        return [c for c in self.contactos if nombre.lower() in c.nombre.lower()]

agenda = SantiagoAgenda()
agenda.agregar_contacto(SantiagoCont("SantiagoB", "12345", "santiago@mail.com"))
agenda.agregar_contacto(SantiagoCont("DavidP", "67890", "DavidP@mail.com"))
print([c.nombre for c in agenda.buscar_contacto("Santiago")])
