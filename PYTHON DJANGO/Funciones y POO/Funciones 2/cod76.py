import requests as SantiagoRequests

def SantiagoVerif(SantiagoURL):
    try:
        SantiagoR = SantiagoRequests.get(SantiagoURL)
        if SantiagoR.status_code == 200:
            print(f"URL válida: {SantiagoURL}")
        else:
            print(f"URL inaccesible ({SantiagoR.status_code}): {SantiagoURL}")
    except:
        print(f"URL inválida o error de conexión: {SantiagoURL}")

SantiagoVerif("https://www.google.com")
SantiagoVerif("https://www.santiagonoseexiste.com")
