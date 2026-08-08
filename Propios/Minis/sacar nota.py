porcentaje = 0
total = 0
while porcentaje < 1:
    op = input("Nota (n) o finalizar (f): ")
    if op == "f":
        print("------")
        break
    nota = float(input("Nota: "))
    porce = float(input("Porcentaje: ")) / 100
    total += nota * porce
    porcentaje += porce
    print("------")
if porcentaje < 1:
    falta = 1 - porcentaje
    minimo = (3.5 - total) / falta
    print(
        f"Vas en {total:.2f}, falta un {(falta*100):.2f} y necesitas sacar un {minimo:.2f} minimo para el 3.5"
    )
elif porcentaje > 1:
    print(f"Como tienes un {(porcentaje*100):.2f} evaluado?")
else:
    print(f"Tu nota final es de {total:.2f}")
