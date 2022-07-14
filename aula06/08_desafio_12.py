# Escreva um programa que leia o arquivo "exemplo2.csv", e converta
# os registros desse CSV para o formato JSON. Escreva um arquivo de saída
# que contenha o conteúdo em JSON.

leitura_csv = 'exemplo2.csv'
with open(leitura_csv, mode='r') as arquivo:
    # considera que a primeira linha é cabeçalho
    leitor = csv.DictReader(arquivo)
    conteudo = []
    for registro in leitor:  # convertendo para dicionário
        conteudo.append(registro)
print(conteudo)

conteudo_json = json.dumps(conteudo)
print(conteudo_json)

arquivo_json = 'exemplo2_saida.json'
with open(arquivo_json, 'w') as arquivo2:
    arquivo2.writelines(conteudo_json)
