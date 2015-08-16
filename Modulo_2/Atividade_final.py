palavra = str(raw_input("Insira uma palavra: "))
lixo = str(raw_input("Selecione a letra a ser excluida: "))
lixo = lixo[0]
qtd = len(palavra)
location = 0

while (location < qtd):
	if palavra[location] == lixo:
		palavra = palavra[:location] + palavra[location+1::]
		qtd -=1
	location +=1

print "Resultado: %s" % palavra
