'''
CRUD

AÇAI









'''


print('\n === Sistema de Açaiteria === \n')

print('1. Cadastro no Aplicativo')
print('2. Número de Telefone')
print('3. Agendar Pedido')
print('4. Promoções e Ofertas')
print('5. Cancelamento')
print('6. Constatar o suporte')
print('7. Feedbecks')
print('8. Avaliações do Aplicativo')
print('0. Sair')


while True:

 escolha_menu = input("\n Cadastro no Aplicativo")
if escolha_menu == '1':
    print('Agendamento do Cliente...')
    nome_do_cliente = ipunt("Digite o Nome do Cliente")
    telefone_cliente = inpunt('Digite o Telefone do Cliente')
    # Código para agendar cliente 

elif escolha_menu == '0':
    

    print("Saindo do Sistema. Até logo!")
    

else:
   print('Opção Invalida. Por Favor, Tente Novamente.')