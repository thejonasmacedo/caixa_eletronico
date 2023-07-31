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
na_conta = 0
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
		na_conta += quant_deposito
		extrato['deposito'].append(quant_deposito)

		saldo_total += quant_deposito

	elif question == 's':
		quant_saque = float(input('Quanto deseja saque?: R$'))
		
		if quant_saque <= saldo_total:
			saque.append(quant_saque)
			na_conta += quant_saque
			extrato['saque'].append(quant_deposito)
			saldo_total -= quant_saque
		else:
			print("ATENÇÃO! NÃO HÁ SALDO SUFICIENTE NA CONTA!")

	
	elif question == 'e':
		# for i in range(bsidict(extrato)):
			# try:
			# 	print(f"depósito: {extrato['deposito'][i]} | saque: {extrato['saque'][i]}")
			# except:
			# 	try:
			# 		print(f"depósito: ---------- | saque: {extrato['saque'][i]}")
			# 	except:
			# 		print(f"depósito: {extrato['deposito'][i]} | saque: ----------")
		
		for i in range(bsidict(extrato)):
			if not extrato['deposito'][i] and not extrato['saque'] == 0:
				print ('depósito: ---------- | saque: ---------- ')
			
			elif not extrato['deposito'][i] == 0:
				print (f"depósito: ---------- | saque: {extrato['saque'][i]} ")
			
			elif not extrato['saque'][i]:
				print(f"depósito: {extrato['saque'][i]} | saque: ---------- ")

			else:
				print(f"depósito: {extrato['saque'][i]} | saque: {extrato['saque'][i]} ")
			
				
					

	elif question == 'a':
		print(f'Seu saldo total é igual à R${saldo_total}')

	elif question == 'i':
		print("saindo")
		break
	
	else:
		print("Por favor escolha uma opção...")
