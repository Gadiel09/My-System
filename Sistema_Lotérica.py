import random
import time
import sys
from prettytable import *

print("					    [ LOTERIA ] \n")


#__________________________________________CRIAÇÃO_DA_TABELA_________________________________________#
tabela= PrettyTable( [ "Número","Preço"])
preco_jog = [ 
	4.50, 31.50, 126, 378,
	945.0, 2079, 4158, 7772,
	13513.00, 22522.50
]

primeiro_numero = 5
for item in range(len(preco_jog)):
	primeiro_numero += 1
	tabela.add_row( [
	f"{primeiro_numero:^45}",
	f"{preco_jog[item]:^45.2f}"
])
print(f"""

   ● Prêmio R$: 50.000
		
{tabela} """)



#__________________________________________CRIAÇÃO_DA_TABELA_________________________________________#









#________________________________________CRIAÇÃO_DAS_ENTRADAS______________________________________#
total_jogos = [ ]
print("___"*34, "\n\n")
qtd_numeros = int(input("   •  Quantos números deseja jogar (6 a 15) : "))
print()
if qtd_numeros < 6:
	print("   •  Escolha inválida...")
	sys.exit()
if qtd_numeros > 15:
	print("   •  Escolha inválida...")
	sys.exit()
for c in range(1):
	if qtd_numeros < 6:
		print(" --> Erro de entrada! Quantidade de números insuficiente...")
		sys.exit()
	elif qtd_numeros > 15:
		print(" --> Erro de entrada! Quantidade de números excedida do padrão....")
		sys.exit()
	elif qtd_numeros == 6:
		total_jogos  += [
		random.randint(0,60), random.randint(0,60),random.randint(0,60),
		random.randint(0,60),random.randint(0,60), random.randint(0,60)
		]
		time.sleep(0.8)
		print(f"\033[1;m   •  SEUS NÚMEROS :\033[m \033[1;33m {total_jogos}\n \033[m")
	elif qtd_numeros == 7:
		total_jogos  += [
		random.randint(0,60), random.randint(0,60),random.randint(0,60),
		random.randint(0,60), random.randint(0,60),random.randint(0,60), 
		random.randint(0,60)
		]
		time.sleep(0.8)
		print(f"\033[1;m   •  SEUS NÚMEROS :\033[m \033[1;33m {total_jogos}\n \033[m")
	elif qtd_numeros == 8:
		total_jogos  += [
		random.randint(0,60), random.randint(0,60),random.randint(0,60),
		random.randint(0,60), random.randint(0,60),random.randint(0,60), 
		random.randint(0,60),random.randint(0,60)
		]
		time.sleep(0.8)
		print(f"\033[1;m   •  SEUS NÚMEROS :\033[m \033[1;33m {total_jogos}\n \033[m")
	elif qtd_numeros == 9:
		total_jogos  += [
		random.randint(0,60), random.randint(0,60),random.randint(0,60),
		random.randint(0,60), random.randint(0,60),random.randint(0,60), 
		random.randint(0,60),random.randint(0,60),random.randint(0,60)
		]
		time.sleep(0.8)
		print(f"\033[1;m   •  SEUS NÚMEROS :\033[m \033[1;33m {total_jogos}\n \033[m")
	elif qtd_numeros == 10:
		total_jogos  += [
		random.randint(0,60), random.randint(0,60),random.randint(0,60),
		random.randint(0,60), random.randint(0,60),random.randint(0,60), 
		random.randint(0,60),random.randint(0,60),random.randint(0,60),
		random.randint(0,60)
		]
		time.sleep(0.8)
		print(f"\033[1;m   •  SEUS NÚMEROS :\033[m \033[1;33m {total_jogos}\n \033[m")
	elif qtd_numeros == 11:
		total_jogos  += [
		random.randint(0,60), random.randint(0,60),random.randint(0,60),
		random.randint(0,60), random.randint(0,60),random.randint(0,60), 
		random.randint(0,60),random.randint(0,60),random.randint(0,60),
		random.randint(0,60),random.randint(0,60)
		]
		time.sleep(0.8)
		print(f"\033[1;m   •  SEUS NÚMEROS :\033[m \033[1;33m {total_jogos}\n \033[m")
	elif qtd_numeros == 12:
		total_jogos  += [
		random.randint(0,60), random.randint(0,60),random.randint(0,60),
		random.randint(0,60), random.randint(0,60),random.randint(0,60), 
		random.randint(0,60),random.randint(0,60),random.randint(0,60),
		random.randint(0,60),random.randint(0,60),random.randint(0,60)
		]
		time.sleep(0.8)
		print(f"\033[1;m   •  SEUS NÚMEROS :\033[m \033[1;33m {total_jogos}\n \033[m")
	elif qtd_numeros == 13:
		total_jogos  += [
		random.randint(0,60), random.randint(0,60),random.randint(0,60),
		random.randint(0,60), random.randint(0,60),random.randint(0,60), 
		random.randint(0,60),random.randint(0,60),random.randint(0,60),
		random.randint(0,60),random.randint(0,60),random.randint(0,60),
		random.randint(0,60)
		]
		time.sleep(0.8)
		print(f"\033[1;m   •  SEUS NÚMEROS :\033[m \033[1;33m {total_jogos}\n \033[m")
	elif qtd_numeros == 14:
		total_jogos += [
		random.randint(0,60), random.randint(0,60),random.randint(0,60),
		random.randint(0,60), random.randint(0,60),random.randint(0,60), 
		random.randint(0,60),random.randint(0,60),random.randint(0,60),
		random.randint(0,60),random.randint(0,60),random.randint(0,60),
		random.randint(0,60),random.randint(0,60)
		]
		time.sleep(0.8)
		print(f"\033[1;m   •  SEUS NÚMEROS :\033[m \033[1;33m {total_jogos}\n \033[m")
	elif qtd_numeros == 15:
		total_jogos  += [
		random.randint(0,60), random.randint(0,60),random.randint(0,60),
		random.randint(0,60), random.randint(0,60),random.randint(0,60), 
		random.randint(0,60),random.randint(0,60),random.randint(0,60),
		random.randint(0,60),random.randint(0,60),random.randint(0,60),
		random.randint(0,60),random.randint(0,60),random.randint(0,60)
		]
		time.sleep(0.8)
		print(f"\033[1;m   •  SEUS NÚMEROS :\033[m \033[1;33m {total_jogos}\n \033[m")	#________________________________________CRIAÇÃO_DAS_ENTRADAS_______________________________________#
		
		
		
		
		




#________________________________________CRIAÇÃO_DO_BOLÃO____________________________________________#
numeros_sistema = [ ]
for c in range(1,60 +1):
	numeros_sistema.append(random.randint(1,60))
	
	
print("..."*33,"\n\n")
print(f"   •  Números da MegaSena : {numeros_sistema}")
print("\n", "..."*33,"\n\n")
tr = list(set(total_jogos) & set(numeros_sistema))
tr_2 = tr[: 15]
#________________________________________CRIAÇÃO_DO_BOLÃO____________________________________________#









#______________________________________________SAÍDAS_____________________________________________________#
if len(tr_2) > 6 and len(tr_2) <= 15:
	print(f"  ◇ PARABÉNS VOCÊ FEZ {len(tr_2)} PONTOS :  \033[1;32m{tr_2}\033[m")
elif len(tr_2) < 6  and len(tr_2) > 4: 
	print(f"  ◇ PARABÉNS VOCÊ FEZ UMA QUINA  : \033[1;32m{tr_2}\033[m")
elif len(tr_2) < 5 and len(tr_2) > 3: 
	print(f"  ◇ PARABÉNS VOCÊ FEZ UMA QUADRA :  \033[1;32m{tr_2}\033[m")
elif len(tr_2) < 4:
	print(f"  ◇ VOCÊ FEZ {len(tr_2)} PONTOS :  \033[1;32m{tr_2}\033[m")
else:
	print(f"  ◇ Infelizmente nenhum número foi sorteado.")
#______________________________________________SAÍDAS_____________________________________________________#
