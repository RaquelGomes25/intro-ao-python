import time

# Crie um decorator que calcule o tempo de execução de uma determinada função


def calcular_duracao(funcao):
    def wrapper():
        tempo_inicial = time.time()
        funcao()
        tempo_final = time.time()

        print("Tempo total de execução da função: {tempo_total}".format(
            funcao=funcao._name_,
            tempo_total=str(tempo_final - tempo_inicial))
        )

    return wrapper


# Aplique seu decorator na função abaixo e veja quanto tempo a busca de um mesmo valor em um set e uma lista demoram para serem executadas

def buscar_item(container, item):
    return item in container


@calcular_duracao
def main():
    tamanho = 1000000
    set_g = set(range(tamanho))
    lista_g = list(range(tamanho))
    item = 500399
    buscar_item(set_g, item)
    buscar_item(lista_g, item)


if _name_ == '_main_':
    main()
