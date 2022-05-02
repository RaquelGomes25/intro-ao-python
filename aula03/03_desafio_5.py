# Crie uma lista com 60 números começando com o valor 1 e indo até o número 60 (ou seja, o número 60 deve estar na lista).
n = 61
print(f'For loop com range(1,{n}):')
for i in range(1, n):
    print(i, end=" ")
print()

# Imprima todos os itens da sua lista de índice par. Imprima o índice e o item.
minha_lista = list(range(2, 61, 2))
print("minha_lista: " + str(minha_lista))
print()
