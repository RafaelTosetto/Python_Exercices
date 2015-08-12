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
