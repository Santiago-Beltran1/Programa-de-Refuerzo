from datetime import datetime as SantiagoDatetime

class SantiagoReg:
    def __init__(self):
        self.SantiagoAccesos = []

    def SantiagoAg(self, SantiagoUsuario):
        self.SantiagoAccesos.append({"usuario":SantiagoUsuario, "hora":SantiagoDatetime.now()})

SantiagoLog = SantiagoReg()
SantiagoLog.SantiagoAg("SantiagoB")
SantiagoLog.SantiagoAg("SantiagoP")
print(SantiagoLog.SantiagoAccesos)
