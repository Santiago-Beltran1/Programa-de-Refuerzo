SantiagoM = 1000000
SantiagoSaldo = 0

while SantiagoSaldo < SantiagoM:
    SantiagoDep = float(input("Ingrese cantidad a depositar: "))
    SantiagoSaldo += SantiagoDep
    print("Saldo actual:", SantiagoSaldo)

print("Meta alcanzada:", SantiagoSaldo)
