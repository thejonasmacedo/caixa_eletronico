# import sys
# sys.path.insert(0, '/home/jx/Documents/hardware e software/git_projects/tools_py')
from item_biggest_size import bsidict

def deposito():
	quant_deposito = float(input('Quanto deseja depositar?: R$ '))

	if quant_deposito < 0:
		print("Valor de depósito é inválido! Por favor, ao tentar novamente insira um valor positivo!\n")
	else:
		deposito.append(quant_deposito)
		extrato['deposito'].append(quant_deposito)
		
		saldo_total += quant_deposito

def saque():
	quant_saque = float(input('Quanto deseja saque?: R$ '))
		
	if quant_saque <= saldo_total and LIMITE_DIARIO > 0:
		if quant_saque > 0:
			saque.append(quant_saque)
			extrato['saque'].append(quant_saque)
			saldo_total -= quant_saque
			LIMITE_DIARIO -= 1
		else:
			print('\nValor de saque é inválido! Por favor, ao tentar novamente insira um valor positivo!')

		if LIMITE_DIARIO <= 0:
			print("\nATENÇÃO! LIMITE DIÁRIO DE SAQUES EXCEDIDO!")
		
		if quant_saque > saldo_total:
			print("\nATENÇÃO! NÃO HÁ SALDO SUFICIENTE NA CONTA!")
	

def extrato():
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

	

def criar_conta_cliente():
	...

def criar_conta_corrente():
	...

def sair():
	...





menu = '''
--------------------------------
		[d]epósito
		[s]aque
		[e]xtrato
		sai[r]
--------------------------------
'''
x = True
deposito = []
saque = []
extrato = {'deposito': [], 'saque': []}
saldo_total = 0
LIMITE_DIARIO = 3


while x:
	question = input('para consultar o menu digite "m".')
	if question == 'm':
		print(menu)
					
	elif question == 'i':
		print("saindo...")
		break
	
	else:
		print("\nPor favor escolha uma opção...\n")
