import hashlib  

class SantiagoBPass:
    def __init__(self, SantiagoPass):
        # Almacena la contraseña de forma "encriptada" (hashed)
        self.SantiagoSetPassword(SantiagoPass)

    def _SantiagoHashPassword(self, SantiagoText):
        # Método privado para "encriptar" la contraseña
        if not isinstance(SantiagoText, str) or not SantiagoText:
            raise ValueError("La contraseña debe ser una cadena no vacía.")
        return hashlib.sha256(SantiagoText.encode('utf-8')).hexdigest()

    def SantiagoSetPassword(self, SantiagoNewPass):
        # Método público para establecer una nueva contraseña
        self.santiago_hashed_password = self._SantiagoHashPassword(SantiagoNewPass)
        print("Contraseña establecida correctamente.")

    def SantiagoCheckPassword(self, SantiagoProvided):
        # Verifica si la contraseña proporcionada coincide con la almacenada
        return self._SantiagoHashPassword(SantiagoProvided) == self.santiago_hashed_password

    @property
    def SantiagoCurrentHash(self):
        # Solo para depuración o prueba
        return self.santiago_hashed_password

    def __str__(self):
        return f"Objeto SantiagoPassword (hash: {self.santiago_hashed_password[:10]}...)"

try:
    santiago1 = SantiagoBPass("Santiago1234!")
    print(santiago1)

    print(f"Verificando 'Santiago1234$': {santiago1.SantiagoCheckPassword('Santiago1234!')}")
    print(f"Verificando 'Incorrecta!': {santiago1.SantiagoCheckPassword('Nosé1234')}")

    santiago1.SantiagoSetPassword("SantiagoNew!")
    print(santiago1)
    print(f"Verificando 'SantiagoNew!: {santiago1.SantiagoCheckPassword('SantiagoNew!')}")


except ValueError as e:
    print(f"Error de contraseña: {e}")
except Exception as e:
    print(f"Ocurrió un error inesperado: {e}")
