SantiagoX = 10  # Variable global

def SantiagoB():
    SantiagoY = 5  # Variable local
    print(f"Variable local y: {SantiagoY}")
    print(f"Variable global x: {SantiagoX}")

SantiagoB()

print(f"Variable global x: {SantiagoX}")
# print(f"Variable local y: {y}")  # Esto generaría un error
