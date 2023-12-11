# Solicitar ao usuário que digite o DDD da cidade em número inteiro
DDD = int(input("Digite o DDD da cidade: "))
# Verificar qual cidade corresponde ao DDD digitado e apresentar o nome da cidade
if DDD == 61:
    #Se o DDD for igual a 61, apresentar o nome Brasilia
    print ("Brasilia")
elif DDD == 71:
    #Se o DDD for igual a 71, apresentar o nome Salvador
    print ("Salvador")
elif DDD == 11:
    #Se o DDD for igual a 11, apresentar o nome São Paulo
    print ("São Paulo")
elif DDD == 21:
    #Se o DDD for igual a 21, apresentar o nome Rio de Janeiro
    print ("Rio de Janeiro")
elif DDD == 32:
    #Se o DDD for igual a 32, apresentar o nome Juiz de Fora
    print ("Juiz de Fora")
elif DDD == 19:
    #Se o DDD for igual a 19, apresentar o nome Campinas
    print ("Campinas")
elif DDD == 27:
    #Se o DDD for igual a 27, apresentar o nome Vitória
    print ("Vitória")
elif DDD == 31:
    #Se o DDD for igual a 31, apresentar o nome Belo Horizonte
    print ("Belo Horizonte")
else:
    # Se o DDD não corresponder a nenhuma cidade conhecida, apresentar "DDD inválido"
    print ("DDD inválido")