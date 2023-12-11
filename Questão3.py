#Guardar o valor da senha na variável S
S = 2002

#Pedir a entrada, um número inteiro
T= int(input("Digite a senha: "))

#Verificar se a senha colocada pelo usuário é a senha correta, caso não, pedir a senha novamente
while T != S:
    print("Senha Invalida")
    T = int(input("Digite a senha: "))

#Caso a senha colocada pelo usuário for a senha correta acaba o processo
print("Acesso permitido")