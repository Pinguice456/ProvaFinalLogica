# Inicio do contador de números pares
CP = 0
# Loop para ler 5 números
for i in range(5):
    # Pedir para o usuario colocar os números para o loop
    valor = int(input(f"Digite o {i + 1} número: "))
    # Verificar se o valor do número digitado é par
    if valor % 2 == 0:
        CP += 1
# Exibir a contagem de números pares
print(f"\nQuantidade de pares: {CP}")