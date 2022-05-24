from datetime import date, datetime, timedelta

# Peça para o usuário digitar a data de seu próximo aniversário no formato brasileiro

proximo_aniversario = input("Qual a data do seu próximo aniversário? (dd/mm/aaaa): ")
prx_aniversario = datetime.strptime(proximo_aniversario, '%d/%m/%Y').date()
print(type(prx_aniversario))
print('Próximo aniversário:'+ (prx_aniversario.strftime('%d/%m/%Y')))

#Imprima uma mensagem dizendo quantos dias faltam para o aniversário dele
hoje = datetime.now().date()
print('Data de hoje:'+ hoje.strftime('%d/%m/%Y'))
dias_faltantes = abs((prx_aniversario - hoje).days)
print('Faltam ' + str(dias_faltantes) + ' dias para o seu próximo aniversário.')

# Pergunte ao usuário se ele(a) gosta de aniversário e salve a resposta
gosta_de_festa =  input('Você gosta de festa de aniversário?(sim ou não) ')
# Pergunte ao usuário se ele(a) vai fazer festa e salve a resposta
fazer_festa =  input('Você vai fazer festa no seu aniversário?(sim ou não) ')
# Imprima uma mensagem dizendo se o usuário vai ganhar presente ou não
# A regra é: o usuário só pode ganhar presente se gostar de aniversário e for fazer festa.
if gosta_de_festa.lower() == 'sim' and fazer_festa.lower() == 'sim':
    print('Você vai ganhar presente!!!!!')
else :
    print('Nada de presente.')