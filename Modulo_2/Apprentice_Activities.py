def activity01(num1):
 '''Determine if an input number is Even or Odd'''

 num_input = int(raw_input("Insira um numero: "))

 if (num_input % 2 == 0):
	print "O numero inserido eh par"
 else:
	print "O numero inserido eh impar"

 return
	
def activity02(iv_one, iv_two):
	'''Return the sum of two input values'''
	num1 = int(raw_input("Insira o primeiro numero: "))
	num2 = int(raw_input("Insira o segundo numero: "))

	soma = num1 + num2

	print "A soma dos numeros sao: %d" % (soma)
	
	return

def activity03(num_list):
	'''Given a list of integers, count how many are even'''
	par = 0
	impar = 0
	continuar = str("S")

	while continuar == "S":
		num1 = int(raw_input("Insira o primeiro numero: "))
		num2 = int(raw_input("Insira o segundo numero: "))
		num3 = int(raw_input("Insira o terceiro numero: "))
		num4 = int(raw_input("Insira o quarto numero: "))
		num5 = int(raw_input("Insira o quinto numero: "))
		
		list1 = [num1, num2, num3, num4, num5]

		print list1

		for num in list1:
			if ( num % 2 == 0):
				par = par + 1
			else:
				impar = impar + 1
 
		print "Existem %d numeros pares e %d numeros impares." % (par,impar)

		par = 0
		impar = 0
	
		continuar = str(raw_input("Se deseja continuar, digite S, senao, digite N: "))
	
	return
	
def activity04(input_string):
	'''Return the input string, backward'''
	
	contrario = ""

	word1 = str(raw_input("Insira uma palavra: "))
 
	contador = len(word1)

	while contador != 0:
		contrario += word1 [contador-1]
		contador -= 1

	print "A palavra inserida ao contrario fica: "

	print contrario
	
	return
