from abc import ABC, abstractmethod
from datetime import datetime

class SantiagoBNotificador(ABC):
    """Clase abstracta para todos los tipos de notificaciones"""

    def __init__(self, SantiagoTit):
        self.santiagoTit = SantiagoTit
        self.santiagoFEnvio = None

    @abstractmethod
    def SantiagoEnviar(self, SantiagoDestinatario, SantiagoMensaje):
        """Cada tipo de notificador debe implementar cómo enviar"""
        pass

    @abstractmethod
    def SantiagoValidarDest(self, SantiagoDestinatario):
        """Cada tipo debe validar su formato de destinatario"""
        pass

    def SantiagoRegisEnv(self):
        """Método concreto - usado por todos"""
        self.santiagoFEnvio = datetime.now()
        return f"Registrado envío: {self.santiagoFEnvio}"


class SantiagoNotificadorEmail(SantiagoBNotificador):
    def __init__(self):
        super().__init__("Notificador por Email")

    def SantiagoValidarDest(self, SantiagoDestinatario):
        return "@" in SantiagoDestinatario and "." in SantiagoDestinatario

    def SantiagoEnviar(self, SantiagoDestinatario, SantiagoMensaje):
        if not self.SantiagoValidarDest(SantiagoDestinatario):
            return f"Destinatario inválido: {SantiagoDestinatario}"
        self.SantiagoRegisEnv()
        return f"Email enviado a {SantiagoDestinatario} con mensaje: '{SantiagoMensaje}'"


class SantiagoNotificadorSMS(SantiagoBNotificador):
    def __init__(self):
        super().__init__("Notificador por SMS")

    def SantiagoValidarDest(self, SantiagoDestinatario):
        return SantiagoDestinatario.isdigit() and len(SantiagoDestinatario) == 10

    def SantiagoEnviar(self, SantiagoDestinatario, SantiagoMensaje):
        if not self.SantiagoValidarDest(SantiagoDestinatario):
            return f"Destinatario inválido: {SantiagoDestinatario}"
        self.SantiagoRegisEnv()
        return f"SMS enviado a {SantiagoDestinatario} con mensaje: '{SantiagoMensaje}'"


SantiagoEmail = SantiagoNotificadorEmail()
SantiagoSMS = SantiagoNotificadorSMS()

print(SantiagoEmail.SantiagoEnviar("david@correo.com", "¡Hola desde Santiago!"))
print(SantiagoEmail.SantiagoEnviar("santiago-correo.com", "Esto fallará"))

print(SantiagoSMS.SantiagoEnviar("1234567890", "Mensaje SMS"))
print(SantiagoSMS.SantiagoEnviar("12345abc", "SMS inválido"))
