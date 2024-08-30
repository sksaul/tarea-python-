precio = input("Introduce el precio del producto en euros (con dos decimales): ")

euros, centimos = precio.split('.')
print(f"Euros: {euros}")
print(f"Céntimos: {centimos}")
