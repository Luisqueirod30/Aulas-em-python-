# Ler as entradas dos sensores
temp1 = float(input("Primeiro sensor: "))
temp2 = float(input("Segundo sensor: "))

# Calcular a média das temperaturas
media_temp = (temp1 + temp2) / 2

if media_temp <= 4:
    print("Um pouco frio")
elif media_temp <= 6:
    print("Um pouco quente")
elif media_temp <= 8:
    print("Muito quente")
else:
    print("Muito quente ou muito frio")

# Imprimir a média das temperaturas
print(f"Média das temperaturas: {media_temp}")

# Mensagem final
print("Fim")
