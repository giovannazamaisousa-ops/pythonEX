# 1-Peça um número para ousuário e diga se ele é par ou impar
num1 = int(input('Digite um número: '))
if num1 % 2 == 0:
    print('Par')
else:
    print('Ímpar')

# 2-Peça um número par para o usuário e diga se ele é positivo, negativo ou zero
num2 = float(input('Digite um número: '))
if num2 > 0:
    print('Positivo')
elif num2 < 0:
    print('Negativo')
else:
    print('Zero')

# 3-Peça um usuário a senha. Se o usuário for 'adimin' e a senha for '1234', mostre 'acesso liberado', senão mostre 'Acesso negadouser
user = input('Usuário: ')
senha = int(input('Senhas: '))
if user == 'adimin' and senha == 1234:
    print('Acesso liberado')
else:
    print('Acesso negado')

# 4-Peça uma idade e informe a categoria: criança (até 11), adolescente (12 a 17), adulto(18 a 59), idoso(60 ou mais)
idade = int(input('Digite sua idade: '))
if idade <= 11:
    print('Criança')
elif idade >= 12 and idade <= 17:
    print('Adolescente')
elif idade >= 18 and idade <= 59:
    print('Adulto')
else:
    print('Idoso')
    