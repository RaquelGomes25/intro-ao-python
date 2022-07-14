import sys
import requests
import json

# Crie uma aplicação que permita ao usuário obter informações sobre um determinado feitiço.
# O usuário deve digitar o nome de um feitiço como entrada para a nossa aplicação através da
# linha de comando. Por exemplo:
# python 07_desafio_14.py Vanishing Spell
# Você deverá obeter os dados sobre o feitiço diretamente do JSON disponível em
# https://construdelas.blob.core.windows.net/intro-ao-python/feiticos.json
# Utilize a biblioteca requests para ler o JSON.
# Ao final do programa, imprima os dados sobre o feitiço que ele solicitou.
# Se o feitiço não foi encontrado, lance uma exceção.


def solicitar_feitico():
    feitico = input('Digite o nome do feitiço: ')
    feitico = feitico.lower()
    return feitico


def arquivo_json():
    URL = "https://construdelas.blob.core.windows.net/intro-ao-python/feiticos.json"
    resposta = requests.get(URL)
    dicionario = json.loads(resposta.content.lower())
    print('Código da resposta:', resposta.status_code)
    print('Tipo da resposta:', resposta.headers['Content-Type'])
    print()
    return dicionario


def consulta_feitico():
    feitico = solicitar_feitico()
    dicionario = arquivo_json()

    try:
        if dicionario[feitico]:
            print('Feitiço encontrado!!!\n')
            print(f'Feitiço: ', feitico.upper())
            for chave, valor in dicionario[feitico].items():
                resultado = (f'{chave}: {valor}')
                print(resultado.title())
            print('\n')

    except KeyError:
        print('\n')
        print(" ---  FEITIÇO NÃO ENCONTRADO!  ---")
        print('\n')


consulta_feitico()
