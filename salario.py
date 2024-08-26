# Entradas do usuário
salario = float(input("Digite o valor do salário: "))
contas = int(input("Digite o número de contas a pagar: "))
conta_telefone = float(input("Digite o valor da conta telefone: "))
conta_de_agua = float(input("Digite o valor da conta de água: "))
conta_internet = float(input("Digite o valor da conta internet: "))
conta_de_luz = float(input("Digite o valor da conta de luz: "))

# Calculando o total das contas
total_contas = conta_telefone + conta_de_agua + conta_internet + conta_de_luz

# Calculando o salário restante
salario_restante = salario - total_contas

# Exibindo o resultado
print(f"Salário restante após pagar as contas: R${salario_restante:.2f}")
