# import sys
# sys.path.insert(0, '/home/jx/Documents/hardware e software/git_projects/tools_py')
from time import sleep
from item_biggest_size import bsidict

menu = '''
-----------------------------------------------------------------
			[d]epósito
			[s]aque
			[e]xtrato
			criar conta [u]ser
			[c]riar conta corrente
			
			sai[r]
-----------------------------------------------------------------
'''
# Variáveis default
# x = True
deposito = []
saque = []
extrato = {'deposito': [], 'saque': []}
saldo_total = 1000
LIMITE_DIARIO = 3
contas_users = [0,]
contas_correntes = []
agencia = '0001'
num_conta = 1
cpfs_cadastrados_contas = []

# test output
# print(f'Deposito:{deposito}, Saque: {saque}, Extrato: {extrato}, Saldo Total: {saldo_total}, Limite Diário {LIMITE_DIARIO}\n')


def func_deposito(quant_depo, /):
	global deposito, extrato, saldo_total

	if quant_deposito < 0:
		print("Valor de depósito é inválido! Por favor, ao tentar novamente insira um valor positivo!\n")
	
	else:
		deposito.append(quant_deposito)
		extrato['deposito'].append(quant_deposito)
		saldo_total += quant_deposito

		# test output
		# print(f'Deposito:{deposito}, Saque: {saque}, Extrato: {extrato}, Saldo Total: {saldo_total}, Limite Diário {LIMITE_DIARIO}\n')




def func_saque(*, quant_saq):
	global saque, extrato, saldo_total, LIMITE_DIARIO
		
	if quant_saque <= saldo_total and LIMITE_DIARIO > 0:
		if quant_saque > 0:
			saque.append(quant_saque)
			extrato['saque'].append(quant_saque)
			saldo_total -= quant_saque
			LIMITE_DIARIO -= 1
			
			# test output
			# print(f'\nDeposito:{deposito}, Saque: {saque}, Extrato: {extrato}, Saldo Total: {saldo_total}, Limite Diário {LIMITE_DIARIO}\n')

	else:
		print('\nValor de saque é inválido! Por favor, ao tentar novamente insira um valor positivo!')

	if LIMITE_DIARIO <= 0:
		print("\nATENÇÃO! LIMITE DIÁRIO DE SAQUES EXCEDIDO!")
		
	if quant_saque > saldo_total:
		print("\nATENÇÃO! NÃO HÁ SALDO SUFICIENTE NA CONTA!")
	



def func_extrato(sald='', /, *, extrat=''):
	global extrato, saldo_total

	if bsidict(extrato) == 0:
		min_to_run = 1
	
	else:
		min_to_run = bsidict(extrato)
	
	for i in range(min_to_run):
		deposito_info = extrato['deposito'][i] if i < len(extrato['deposito']) else '/----------/'
		saque_info = extrato['saque'][i] if i < len(extrato['saque']) else '/----------/'
		print('\n--------------------------- EXTRATO -------------------------------')
		print(f"depósito: {deposito_info} | saque: {saque_info}")
		print(f'\nSaldo Total: R${saldo_total}')
		print('---------------------------------------------------------------------')

		# test output
		# print(f'\nDeposito:{deposito}, Saque: {saque}, Extrato: {extrato}, Saldo Total: {saldo_total}, Limite Diário {LIMITE_DIARIO}\n')





def criar_conta_user():
	global contas_users

	print('\n----Para criação de uma nova conta, por favor, insira os dados a seguir----')
	nome = input('Nome: ')
	data_nascimento = input('Data de nascimento: ')
	while True:
		n_cpf = input('Insira somente os números do seu CPF: ')
		if len(n_cpf) == 11:
			break
		else:
			print('___Atenção! Insira SOMENTE os números do seu CPF, nada além disso____')
	
	print('Insira seu endereço a seguir:')
	endereco = {'Endereço':{'logradouro': input('Logradouro: '), 
	     			'numero': input('Número: '), 
	     			'bairro': input('Bairro: '), 'cidade': input('Cidade: '), 
					'estado': input('Estado(Ex.: SP, RJ, ES.): ')}}
	# endereco_id = f'Endereço: {endereco}'
	
	user = [nome, data_nascimento, int(n_cpf), endereco]
	contas_users.append(user)
	print(contas_users)
	# criar_conta_corrente()





def criar_conta_corrente():
	global contas_users, contas_correntes, num_conta, agencia, cpfs_cadastrados_contas

	print('\n----Para criação de uma nova conta corrente, por favor, insira os dados a seguir----')
	cpf_id = int(input('Por favor insira seu CPF:'))
	if cpf_id in cpfs_cadastrados_contas:
		print('O seu CPF já tem cadastro em nosso sistema!')
	else:
		for user in contas_users:
			# if contas_users[i[2]] == cpf_id:
			if cpf_id == user[2]:
				contas_correntes.append([agencia, num_conta, contas_users[num_conta]])
				cpfs_cadastrados_contas.append(cpf_id)
	
	print(contas_correntes)
	
	print('...Criando conta corrente...')
	print(contas_correntes)
	print('\n---------------------conta criada com sucesso!---------------------')



	
	









while True:
	question = input('para consultar o menu digite "m".')
	if question == 'm':
		print(menu)
	
	if question == 'd':
		quant_deposito = float(input('Quanto deseja depositar?: R$ '))
		func_deposito(quant_deposito)

	if question == 's':
		quant_saque = float(input('Quanto deseja saque?: R$ '))
		func_saque(quant_saq=quant_saque)
	
	if question == 'e':
		func_extrato()

	if question == 'u':
		criar_conta_user()
	
	if question == 'c':
		criar_conta_corrente()
					
	elif question == 'i':
		print("saindo...")
		break
	
	else:
		print("\nPor favor escolha uma opção...\n")
