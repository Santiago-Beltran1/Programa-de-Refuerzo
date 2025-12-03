from plyer import notification as SantiagoNotification
import time as SantiagoTime

def SantiagoRDeskTop(SantiagoMens, SantiagoSeg):
    print(f"Recordatorio activado: '{SantiagoMens}' en {SantiagoSeg} segundos...")
    SantiagoTime.sleep(SantiagoSeg)
    SantiagoNotification.notify(title="SantiagoAlerta", message=SantiagoMens)
    print(f"Notificación enviada: {SantiagoMens}")

SantiagoRDeskTop("Revisar correo Santiago", 3)
