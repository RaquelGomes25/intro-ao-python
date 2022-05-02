from datetime import date, datetime, timedelta

# Peça para o usuário digitar a data de seu próximo aniversário no formato brasileiro
proximo_aniversario = input(
    "Qual a data do seu próximo aniversário? (dd/mm/aa): ")
data_prxaniversario = datetime.strptime(proximo_aniversario, '%d%m%y').date()
# Imprima uma mensagem dizendo quantos dias faltam para o aniversário dele

# Pergunte ao usuário se ele(a) gosta de aniversário e salve a resposta

# Pergunte ao usuário se ele(a) vai fazer festa e salve a resposta

# Imprima uma mensagem dizendo se o usuário vai ganhar presente ou não

# A regra é: o usuário só pode ganhar presente se gostar de aniversário e for fazer festa.
