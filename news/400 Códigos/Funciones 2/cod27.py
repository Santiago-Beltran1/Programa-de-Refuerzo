import requests

def SantiagoDescImg(SantiagoURL, SantiagoNom):
    r = requests.get(SantiagoURL)
    with open(SantiagoNom, 'wb') as f:
        f.write(r.content)
    return f"{SantiagoNom} descargada"

print(SantiagoDescImg("https://via.placeholder.com/150", "balon.png"))
