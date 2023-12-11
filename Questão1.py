#Variavel N1 solicitando um número qualquer
N1 = float(input("Digite o valor da sua média atual"))
# Verificar a faixa de valores e calcular o imposto
if N1 <= 2000:
   # Se a média for até 2000, isento de imposto
    print("Isento")
elif N1 == 2000.01 or N1 <= 3000.00:
   # Para médias entre 2000.01 e 3000.00, aplica-se um imposto de 8%
   imposto = N1 + N1 * 0.08 
   print("imposto de 8%")
   print(f"{imposto:.2f}")
elif N1 == 3000.01 or N1 <= 4500.00:
    # Para médias entre 3000.01 e 4500.00, aplica-se um imposto de 18%
    print("imposto de 18%")
    imposto = N1 + N1 * 0.18
    print(f"{imposto:.2f}")
else:
    # Para médias acima de 4500.00, aplica-se um imposto de 28%
    print("imposto de 28%")
    imposto = N1 + N1 * 0.28
    print(f"{imposto:.2f}")