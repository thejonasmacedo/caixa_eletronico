import sys
sys.path.insert(0, '/home/jx/Documents/hardware e software/git_projects/tools_py')
from item_biggest_size import bsidict

menu = '''
--------------------------------
		[d]epósito
		[s]aque
		[e]xtrato
		s[a]ldo
		sa[i]r
--------------------------------
'''
x = True
deposito = []
saque = []
extrato = {'deposito': [], 'saque': []}
saldo_total = 0


while x:
	question = input('para consultar o menu digite "m".')
	if question == 'm':
		print(menu)
	
	elif question == 'd':
		
		quant_deposito = float(input('Quanto deseja depositar?: R$ '))
		deposito.append(quant_deposito)
		extrato['deposito'].append(quant_deposito)

		saldo_total += quant_deposito

	elif question == 's':
		quant_saque = float(input('Quanto deseja saque?: R$'))
		
		if quant_saque <= saldo_total:
			saque.append(quant_saque)
			extrato['saque'].append(quant_saque)
			saldo_total -= quant_saque
		else:
			print("ATENÇÃO! NÃO HÁ SALDO SUFICIENTE NA CONTA!")

	
	elif question == 'e':

		if bsidict(extrato) == 0:
			min_to_run = 1
		
		else:
			min_to_run = bsidict(extrato)

		for i in range(min_to_run):
			deposito_info = extrato['deposito'][i] if i < len(extrato['deposito']) else '----------'
			saque_info = extrato['saque'][i] if i < len(extrato['saque']) else '----------'
			print(f"depósito: {deposito_info} | saque: {saque_info}")
			print(f'Seu saldo total é igual à R${saldo_total}')
	
					

	elif question == 'a':
		print(f'Seu saldo total é igual à R${saldo_total}')
		
	elif question == 'i':
		print("saindo")
		break
	
	else:
		print("Por favor escolha uma opção...")
