import qrcode as SantiagoQRCode

def SantiagoQR(SantiagoURL, SantiagoArch="SantiagoQR.png"):
    SantiagoQR = SantiagoQRCode.QRCode(version=1, box_size=10, border=5)
    SantiagoQR.add_data(SantiagoURL)
    SantiagoQR.make(fit=True)
    SantiagoImg = SantiagoQR.make_image(fill="black", back_color="white")
    SantiagoImg.save(SantiagoArch)
    print(f"SantiagoQR generado para {SantiagoURL} y guardado en {SantiagoArch}")

SantiagoQR("https://www.santiago.com")
