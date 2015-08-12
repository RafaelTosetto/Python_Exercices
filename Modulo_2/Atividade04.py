'''Return the input string, backward'''

contrario = ""

word1 = str(raw_input("Insira uma palavra: "))


''' O tipo len eh igual a lengh, ou seja, comprimento. Logo a variavel
 contador recebe o tamanho da quantidade de letras da variavel word1'''
 
contador = len(word1)

while contador != 0:
	contrario += word1 [contador-1]
	contador -= 1

print "A palavra inserida ao contrario fica: "

print contrario

'''A sintaxe abaixo faz a mesma coisa de maneira encurtada

print word1[::-1]

'''
