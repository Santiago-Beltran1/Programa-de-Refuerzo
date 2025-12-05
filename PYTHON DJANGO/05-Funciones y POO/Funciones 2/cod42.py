import pygame as SantiagoPygame

def SantiagoRepAud(SantiagoArch):
    SantiagoPygame.mixer.init()
    SantiagoPygame.mixer.music.load(SantiagoArch)
    SantiagoPygame.mixer.music.play()
    while SantiagoPygame.mixer.music.get_busy():
        pass

# SantiagoRepAud("SantiagoCancion.mp3")
