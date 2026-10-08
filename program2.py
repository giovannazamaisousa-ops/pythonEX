#----ADIVINHE EM 5 TENTATIVAS----#
import random

numero_secreto = random.randint(1, 20)

print('Pensei em um número entre 1 e 20. Você tem 5 tentativas!')

for tentativa in range(1, 6):
    palpite = int(input('Seu palpite'))

    if palpite < numero_secreto:
        print('Muito baixo! Tente um número maior.')
    elif palpite > numero_secreto:
        print('Muito alto! Tente um número menor.')
    else:
        print(f'Acertou em {tentativa} tentativa(s)!!')
        break
else:
    print(f'Acabaram as tentativas! O número secreto é {numero_secreto}!')