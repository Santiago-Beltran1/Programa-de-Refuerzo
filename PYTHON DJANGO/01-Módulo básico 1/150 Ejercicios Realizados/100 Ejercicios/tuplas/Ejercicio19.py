# Cifrado cambiando letras por números

santiagoCode = (("a", "4"), ("e", "3"), ("i", "1"), ("o", "0"), ("u", "7"))
santiagoText = input("Ingrese un texto: ")

for santiagoLet, santiagoNum in santiagoCode:
    santiagoText = santiagoText.replace(santiagoLet, santiagoNum)

print("Texto cifrado:", santiagoText)
