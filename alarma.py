from time import localtime
from pygame import mixer

H = input("Ingrese la hora: ")
M = input("Ingrese el minuto: ")

while True:
    if localtime().tm_hour == int(H) and localtime().tm_min == int(M):
        print("Sonando alarma")
        mixer.init()
        mixer.music.load("alarma.mp3")
        mixer.music.play()
        break
    