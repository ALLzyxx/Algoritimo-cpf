import re
import sys
while True:
    entrada = input('Digite o seu cpf(apenas numeros): ')
    cpf = re.sub(r'[^0-9]', '', entrada)
    entrada_sequencial = entrada == entrada[0] * len(entrada)
    if entrada_sequencial:
        print('Voce enviou dados sequenciais.')
        sys.exit()
    nove_digitos_1 = cpf[:9]
    contador_regressivo_1 = 10
    resultado_1 = 0
    for digito in nove_digitos_1:
        resultado_1 += int(digito) * contador_regressivo_1
        contador_regressivo_1 -= 1
    digito_1 = ((resultado_1 * 10) % 11)
    digito_1 = digito_1 if digito_1 <= 9 else 0

    nove_digitos_2 = cpf[:10]
    contador_regressivo_2 = 11
    resultado_2 = 0
    for digito in nove_digitos_2:
        resultado_2 += int(digito) * contador_regressivo_2
        contador_regressivo_2 -= 1
    digito_2 = ((resultado_2 * 10) % 11)
    digito_2 = digito_2 if digito_2 <= 9 else 0
    print(f'os digitos do seu cpf sao {digito_1}{digito_2}')

    novo_cpf = f'{nove_digitos_1}{digito_1}{digito_2}'
    if cpf == novo_cpf:
        print(f'{novo_cpf} e valido')
    else:
        print('cpf invalido')
