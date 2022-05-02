# 1. Pergunte ao usuário em qual cidade e o estado em que ele(a) mora
cidade = input("Você mora em qual cidade? ")
estado = input("Você mora em qual estado? ")

# 2. Imprima uma mensagem diga a cidade em que o usuário mora.
#    O nome da cidade deve estar todo em letras maiúsculas.
cidade_maiscula = cidade.upper()
print("Você mora em", cidade_maiscula)

# 3. Imprima uma mensagem diga o estado em que o usuário mora.
#    O nome do estado deve estar todo em letras maiúsculas.
#    Utilize uma forma de formatação de string diferente da que foi usada no item 2.
estado_maiusculo = estado.upper()
print(f'Você mora na {estado_maiusculo}')
