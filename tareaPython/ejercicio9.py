fecha_nacimiento = input("Introduce tu fecha de nacimiento en formato dd/mm/aaaa: ")

dia, mes, año = fecha_nacimiento.split('/')

dia = dia.zfill(2)

mes = mes.zfill(2)

print(f"Día: {dia}")
print(f"Mes: {mes}")
print(f"Año: {año}")
