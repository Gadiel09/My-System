import os
import sys
import time
from prettytable import *

tot = [ ]
clientes = {}
barbeiros = {}

class ManagerBarbearia:
	def CadastrarUser(self):
		clientes.clear()
		name = str(input("  ◇  Nome: ")).capitalize()
		clientes["Nome"] = name
		tipo = int(input(""" 
	
		QUAL O  SEU TIPO DE CABELO ? 
	
	[ 1 ] - LISO
	[ 2 ] - ONDULADO
	[ 3 ] - CACHEADO
	[ 4 ] - CRESPO
	
	•  RESPOSTA : """))
		if tipo == 1:
			servicos = int(input(""" 
		
	● Serviços ofertados
	
	[ 1 ] - CABELO LISO COM TEXTURA + RISCA DE NAVALHA ( 20,00)
	[ 2 ] - POMPADOUR COMB OVER ( 18,00)
	[ 3 ] - CORTE CAASER + BARBA  (25,00)
	[ 4 ] - CORTE FADE COM LISTRA NA FRENTE (22,00)
	[ 5 ] - TOPETE + DEGRADÊ (20,00)
	[ 6 ] - HIGH FADE + DEGRADÊ( 20,00)
	[ 7 ] - MID FADE + LISTRAS ATRÁS ( 22,00)
	
	◇ Opção : """))
			if servicos == 1:
				corte = " LISO COM TEXTURA + RISCA DE NAVALHA"
				preco = 20
				clientes["Corte"] = corte
				clientes["Preço"] = preco
			elif servicos == 2:
				corte = " POMPADOUR COMB OVER "
				preco = 18
				clientes["Corte"] = corte
				clientes["Preço"] = preco
			elif servicos == 3:
				corte = " CORTE CAASER + BARBA"
				preco = 25
				clientes["Corte"] = corte
				clientes["Preço"] = preco
			elif servicos == 4:
				corte = " CORTE FADE COM LISTRA NA FRENTE"
				preco = 22
				clientes["Corte"] = corte
				clientes["Preço"] = preco
			elif servicos == 5:
				corte = " TOPETE + DEGRADÊ"
				preco = 20
				clientes["Corte"] = corte
				clientes["Preço"] = preco
			elif servicos == 6:
				corte = " HIGH FADE + DEGRADÊ"
				preco = 20
				clientes["Corte"] = corte
				clientes["Preço"] = preco
			elif servicos == 7:
				corte = " MID FADE + LISTRAS ATRÁS "
				preco = 22
				clientes["Corte"] = corte
				clientes["Preço"] = preco
			else:
				if servicos < 1 or servicos > 7:
					print("  • Escolha inválida... agendamento cancelado. ")
					sys.exit()
					
					
					
					
		elif tipo == 2:
			servicos = int(input(""" 
		
	● Serviços ofertados
	
	[ 1 ] - CABELO ONDULADO COM TEXTURA VOLUMOSA ( 28,00)
	[ 2 ] - POMPADOUR COMB OVER  COM TEXTURA MÉDIA ( 25,00)
	[ 3 ] - ONDULADO COM BARBA E RISCO NA SOBRANCELHA (30,00)
	[ 4 ] - ONDULADO COM VOLUME MÉDIO (25,00)
	[ 5 ] - TOPETE + ONDULADO MÉDIO (28,00)
	[ 6 ] - DEGRADÊ + ONDULADO + LISTRA ( 32,00)
	[ 7 ] - FADE + ONDULADO CURTO + BARBA ( 32,00)
	
	◇ Opção: """))
			if servicos == 1:
				corte = " CABELO ONDULADO COM TEXTURA VOLUMOSA"
				preco = 28
				clientes["Corte"] = corte
				clientes["Preço"] = preco
			elif servicos == 2:
				corte = " POMPADOUR COMB OVER  COM TEXTURA MÉDIA "
				preco = 25
				clientes["Corte"] = corte
				clientes["Preço"] = preco
			elif servicos == 3:
				corte = " ONDULADO COM BARBA E RISCO NA SOBRANCELHA"
				preco = 30
				clientes["Corte"] = corte
				clientes["Preço"] = preco
			elif servicos == 4:
				corte = " ONDULADO COM VOLUME MÉDIO "
				preco = 25
				clientes["Corte"] = corte
				clientes["Preço"] = preco
			elif servicos == 5:
				corte = " TOPETE + ONDULADO MÉDIO"
				preco = 28
				clientes["Corte"] = corte
				clientes["Preço"] = preco
			elif servicos == 6:
				corte = " DEGRADÊ + ONDULADO + LISTRA "
				preco = 32
				clientes["Corte"] = corte
				clientes["Preço"] = preco
			elif servicos == 7:
				corte = " FADE + ONDULADO CURTO + BARBA "
				preco = 32
				clientes["Corte"] = corte
				clientes["Preço"] = preco
			else:
				if servicos < 1 or servicos > 7:
					print("  • Escolha inválida... agendamento cancelado. ")
					sys.exit()
					
					
					
		elif tipo == 3:
			servicos = int(input(""" 
		
	● Serviços ofertados
		
	[ 1 ] - CACHEADO PARTIDO + BARBA ( 30,00)
	[ 2 ] - MOICANO CURTO CACHEADO ( 35,00)
	[ 3 ] - CACHEADO CURTO + BARBA  (25,00)
	[ 4 ] - CACHEADO CURTO + DEGRADÊ (32,00)
	[ 5 ] - FRANJA + DEGRADÊ (25,00)
	[ 6 ] - CACHEADO COM FRANJA( 40,00)
	[ 7 ] - TOPETE CURTO  FADED (28,00)
		
	◇ Opção: """))
			if servicos == 1:
				corte = " CACHEADO PARTIDO + BARBA "
				preco = 30
				clientes["Corte"] = corte
				clientes["Preço"] = preco
			elif servicos == 2:
				corte = " MOICANO CURTO CACHEADO"
				preco = 35
				clientes["Corte"] = corte
				clientes["Preço"] = preco
			elif servicos == 3:
				corte = " CACHEADO CURTO + BARBA  "
				preco = 25
				clientes["Corte"] = corte
				clientes["Preço"] = preco
			elif servicos == 4:
				corte = " CACHEADO CURTO + DEGRADÊ "
				preco = 32
				clientes["Corte"] = corte
				clientes["Preço"] = preco
			elif servicos == 5:
				corte = " FRANJA + DEGRADÊ"
				preco = 25
				clientes["Corte"] = corte
				clientes["Preço"] = preco
			elif servicos == 6:
				corte = " CACHEADO COM FRANJA"
				preco = 40
				clientes["Corte"] = corte
				clientes["Preço"] = preco
			elif servicos == 7:
				corte = " TOPETE CURTO  FADED"
				preco = 28
				clientes["Corte"] = corte
				clientes["Preço"] = preco
			else:
				if servicos < 1 or servicos > 7:
					print("  • Escolha inválida... agendamento cancelado. ")
					sys.exit()
					
					
		elif tipo == 4:
			servicos = int(input(""" 
		
	● Serviços ofertados
		
	[ 1 ] - DEGRADÊ  (25,00)
	[ 2 ] - LOW FADE ( 20,00)
	[ 3 ] - MID FADE  (25,00)
	[ 4 ] - HIGH FADE  (30,00)
	[ 5 ] - COQUE ALTO (20,00)
	[ 6 ] - BLACK POWER( 28,00)
	[ 7 ] - DEGRADÊ + FADED + BARBA (35,00)
		
	◇ Opção : """))
			if servicos == 1:
				corte = " DEGRADÊ"
				preco = 25
				clientes["Corte"] = corte
				clientes["Preço"] = preco
			elif servicos == 2:
				corte = " LOW FADE"
				preco = 20
				clientes["Corte"] = corte
				clientes["Preço"] = preco
			elif servicos == 3:
				corte = " MID FADE "
				preco = 25
				clientes["Corte"] = corte
				clientes["Preço"] = preco
			elif servicos == 4:
				corte = " HIGH FADE "
				preco = 30
				clientes["Corte"] = corte
				clientes["Preço"] = preco
			elif servicos == 5:
				corte = " COQUE ALTO  "
				preco = 20
				clientes["Corte"] = corte
				clientes["Preço"] = preco
			elif servicos == 6:
				corte = " BLACK POWER"
				preco = 28
				clientes["Corte"] = corte
				clientes["Preço"] = preco
			elif servicos == 7:
				corte = " DEGRADÊ + FADED + BARBA"
				preco = 35
				clientes["Corte"] = corte
				clientes["Preço"] = preco
			else:
				if servicos < 1 or servicos > 7:
					print("  • Escolha inválida... agendamento cancelado. ")
					sys.exit()
		else:
			if tipo < 1 or tipo > 4:
				print("  • Escolha inválida... agendamento cancelado. ")
				sys.exit()
		
		
		
		horario = int(input(f""" 
			
	● Olá  {name} agende seu horário
	
	[ 1 ] - Manhã
	[ 2 ] - Tarde
	[ 3 ] - Noite
			
	• Reserver seu Horário : """))
		if horario == 1:
			clientes["Barbeiro"] = "Renan"
			hora = int(input(""" 
	[ 1 ] : 8h00
	[ 2 ] : 8h30
	[ 3 ] : 9h00
	[ 4 ] : 9h30
	[ 5 ] : 10h00
	[ 6 ] : 10h30
	[ 7 ] : 11h00
	[ 8 ] : 11h30
	[ 9 ] : 12h00
	
Escolha uma das opções disponíveis: """))
			if hora == 1:
				clientes["Horário"] = "8h00"
			elif hora == 2:
				clientes["Horário"] = "8h30"
				
			elif hora == 3:
				clientes["Horário"] = "9h00"
				
			elif hora == 4:
				clientes["Horário"] = "9h30"
				
			elif hora == 5:
				clientes["Horário"] = "10h00"
				
			elif hora == 6:
				clientes["Horário"] = "10h30"
				
			elif hora == 7:
				clientes["Horário"] = "11h00"
				
			elif hora == 8:
				clientes["Horário"] = "11h30"
				
			elif hora == 9:
				clientes["Horário"] = "12h00"
				
			elif hora > 9 or hora < 1:
				print("  ●  Escolha inválida.")
				
				
				
		elif horario == 2:
			clientes["Barbeiro"] = "Lyan"
			hora = int(input(""" 
	[ 1 ] : 13h00
	[ 2 ] : 13h30
	[ 3 ] : 14h00
	[ 4 ] : 14h30
	[ 5 ] : 15h00
	[ 6 ] : 15h30
	[ 7 ] : 16h00
	[ 8 ] : 16h30
	[ 9 ] : 17h00
	
Escolha uma das opções disponíveis: """))
			if hora == 1:
				clientes["Horário"] = "13h00"
			elif hora == 2:
				clientes["Horário"] = "13h30"
				
			elif hora == 3:
				clientes["Horário"] = "14h00"
				
			elif hora == 4:
				clientes["Horário"] = "14h30"
				
			elif hora == 5:
				clientes["Horário"] = "15h00"
				
			elif hora == 6:
				clientes["Horário"] = "15h30"
				
			elif hora == 7:
				clientes["Horário"] = "16h00"
				
			elif hora == 8:
				clientes["Horário"] = "16h30"
				
			elif hora == 9:
				clientes["Horário"] = "17h00"
				
			elif hora > 9 or hora < 1:
				print("  ●  Escolha inválida.")
				
				
		elif horario == 3:
			clientes["Barbeiro"] = "Juan Paulo"
			hora = int(input(""" 
	[ 1 ] : 18h00
	[ 2 ] : 18h30
	[ 3 ] : 19h00
	[ 4 ] : 19h30
	[ 5 ] : 20h00
	[ 6 ] : 20h30
	[ 7 ] : 21h00
	[ 8 ] : 21h30
	[ 9 ] : 22h00
	
Escolha uma das opções disponíveis: """))
			if hora == 1:
				clientes["Horário"] = "18h00"
				
			elif hora == 2:
				clientes["Horário"] = "18h30"
				
			elif hora == 3:
				clientes["Horário"] = "19h00"
				
			elif hora == 4:
				clientes["Horário"] = "19h30"
				
			elif hora == 5:
				clientes["Horário"] = "20h00"
				
			elif hora == 6:
				clientes["Horário"] = "20h30"
				
			elif hora == 7:
				clientes["Horário"] = "21h00"
				
			elif hora == 8:
				clientes["Horário"] = "21h30"
				
			elif hora == 9:
				clientes["Horário"] = "22h00"
				
			elif hora > 9 or hora < 1:
				print("  ●  Escolha inválida.")
		else:
			print(f" •  O cliente : {name} não está cadastrado no sistema .")
		all_clientes = clientes.copy()
		tot.append(all_clientes)
		return tot
		
	
	
	
	
	def Menu(self):
		return print(""" 
				BEM VINDO AO BARBER SHOP
				
			[ 1 ] - Criar Agendamento
			[ 2 ] - Carregar Agendamentos
			[ 3 ] - Sair
	""")
	
	
	
	def Agendamentos(self):
		tabela= PrettyTable( ["Barbeiro","Nome","Corte","Preço" ,"Horário"])
		print("  •  Carregando agendamentos...")
		time.sleep(0.8)
		os.system("clear")
		print("  •  Registros Carregados !")
		print("\n")
		for c in range(1):
			for y in tot:
				tabela.add_row( [
					f'{y["Barbeiro"]:^8}', 
					f'{y["Nome"]:^8}', 
					f'{y["Corte"]:^25}', 
					f'R${y["Preço"]:^8.2f}', 
					f'{y["Horário"]:^8}', 
				])
		print(tabela)
		print("\n", "_____" *18)
		cont = 0
		while True:
			p = " "
			while p not in "S" and len(p) > 0:
				cont += 1
				p = str(input("  • Deseja Sair (S) ?")).strip().upper()
				print("..."* 24, "\n")
				if len(p) == 0 and cont > 2:
					os.system("clear")
					print(tabela)
					cont = 0
				if cont > 2 and p not in "S":
					os.system("clear")
					print(tabela)
					cont = 0
			if len(p) > 0 and p  in "S":
				print(" Ok...")
				time.sleep(0.8)
				os.system("clear")
				break
					









MyBarber = ManagerBarbearia()

menu = " "
print("\n", "___"*33,"\n")
cont = 0
while menu != 4 :
	cont += 1
	MyBarber.Menu()
	menu = int(input("   •  Escolha : "))
	os.system("clear")
	print("\n")
	if menu == 1:
		MyBarber.CadastrarUser()
		time.sleep(0.8)
		os.system("clear")

		
	elif menu == 2:
		MyBarber.Agendamentos()
		
	elif menu== 3:
		print("  •  Encerrando Sistema...")
		time.sleep(0.8)
		sys.exit()
	else:
		if menu > 3 or menu < 1:
			print("  ▪︎  Escolha inválida")
			print("  ▪︎  Encerrando Sistema...")
			time.sleep(0.8)
			sys.exit()
