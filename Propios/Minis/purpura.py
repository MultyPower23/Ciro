vacio = int(input("Videos de Purpura: "))
adaptacion = float(input("% de adaptacion cada rueda: ")) / 100
ruedas = 0

while ruedas < 6:
    print(f"Giros: {ruedas}")
    if ruedas == 5:
        print("Purpura neutralizado")
        break
    print(f"Daño del purpura: {vacio:.0f} videos")

    vacio *= 1 - adaptacion
    ruedas += 1
