# Váriaveis QP e SP
QP = 0
SP = 0
# Loop pra ler 6 números
for i in range(6):
    # Solicitar para o usuário que digite um número qualquer
    valor = float(input(f"Digite o {i + 1} número:"))
    # Verificar se o valor digitado é positivo
    if valor > 0:
        QP += 1
        SP += valor
# Calcular a média dos valores positivos (evitando a divisão por 0)
MP = SP / QP if QP > 0 else 0
# Exibe a quantidade de números positivos
print(f"Quantidade de números positivos: {QP}")
# Exibe a média dos números positivos com um dígito após o decimal
print(f"Média dos números positivos: {MP:.1f}")