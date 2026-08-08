import base64

with open("cancion.mp3", "rb") as f:
    datos = base64.b64encode(f.read()).decode("utf-8")

with open("data1.txt", "w") as f:
    f.write(datos)

print("Listo. Se generó data.txt")
