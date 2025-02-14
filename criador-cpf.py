import random
for _ in range(10):
    cpf = ''
    for i in range(9):
        cpf += str(random.randint(0, 9))

    nove_digitos = cpf[:9]
    contador_regressivo_1 = 10
    resultado_1 = 0
    for digito in nove_digitos:
        resultado_1 += int(digito) * contador_regressivo_1
        contador_regressivo_1 -= 1
    digito_1 = ((resultado_1 * 10) % 11)
    digito_1 = digito_1 if digito_1 <= 9 else 0

    dez_digitos = nove_digitos + str(digito_1)
    contador_regressivo_2 = 11
    resultado_2 = 0
    for digito in dez_digitos:
        resultado_2 += int(digito) * contador_regressivo_2
        contador_regressivo_2 -= 1
    digito_2 = ((resultado_2 * 10) % 11)
    digito_2 = digito_2 if digito_2 <= 9 else 0
    print(f'os digitos do seu cpf sao {digito_1}{digito_2}')

    novo_cpf = f'{nove_digitos}{digito_1}{digito_2}'
    print(novo_cpf)
