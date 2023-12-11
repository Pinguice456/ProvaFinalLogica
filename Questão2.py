# Solicita ao usuário que digite seu salário
Salário_normal = float(input("Digite seu salário: "))
# Verificar a faixa de salário e calcular o reajuste e o novo salário correspondentes
if Salário_normal <= 400.00:
    S1 = Salário_normal + Salário_normal * 0.15
    S2 = Salário_normal * 0.15
    print (f"Reajuste ganho:{S2:.2f}")
    print ("Em percentual: 15%")
    print (f"Novo salario :{S1:.2f}")
elif Salário_normal <= 800.00:
    # Para salários entre 400.01 e 800.00, aplicar um reajuste de 12%
    S1 = Salário_normal + Salário_normal * 0.12
    S2 = Salário_normal * 0.12
    print ("Em percentual: 12%")
    print (f"Reajuste ganho:{S2:.2f}")
    print (f"Novo salario :{S1:.2f}")
elif Salário_normal <= 1200.00:
    # Para salários entre 800.01 e 1200.00, aplicar um reajuste de 10%
    S1 = Salário_normal + Salário_normal * 0.10
    S2 = Salário_normal * 0.10
    print (f"Reajuste ganho:{S2:.2f}")
    print ("Em percentual: 10%")
    print (f"Novo salário :{S1:.2f}")
elif Salário_normal >= 1200.01 and Salário_normal <= 2000.00:
    # Para salários entre 1200.01 e 2000.00, aplicar um reajuste de 7%
    S1 = Salário_normal + Salário_normal * 0.07
    S2 = Salário_normal * 0.07
    print (f"Reajuste ganho:{S2:.2f}")
    print ("Em percentual: 7%")
    print (f"Novo salario :{S1:.2f}")
elif Salário_normal >= 2000.01:
    # Para salários acima de 2000.00, aplicar um reajuste de 4%
    S1 = Salário_normal + Salário_normal * 0.04
    S2 = Salário_normal * 0.04
    print (f"Reajuste ganho:{S2:.2f}")
    print ("Em percentual: 4%")
    print (f"Novo salario :{S1:.2f}")