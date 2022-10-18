# Programação Orientada a Objetos
# AC01 POO-EaD - Números especiais
#
# Email Impacta: kawan.messias@aluno.faculdadeimpacta.com.br



def eh_primo(n):
	
	qtd_divisores = 0
	i = 1	#Variavel contadora
	
	while i <= n:
		if n % i == 0:	# Testa se n é divisor de i
			qtd_divisores += 1
		i += 1	# Incrementa valor de i
  
	if qtd_divisores == 2:
		return True

	else:
		return False
	
	pass


def lista_primos(n):
 
	lista = []
	for i in range(2, n): # i varia de 2 até n -1
		if eh_primo(i):
			lista.append(i)
	return lista

	pass


def conta_primos(s):
	"""Função que conta a quantidade de primos em uma sequência

	Recebe uma sequência de números naturais s e retorna
	um dicionário com a contagem de ocorrências de cada número
	primo da sequência. Números não primos devem ser ignorados.
	Os números da sequência serão sempre maiores ou iguais a 2.

	Exemplos
	--------
	Caso s = [11, 2, 3, 4, 11, 2, 5, 2]
		O retorno deverá ser: {11: 2, 2: 3, 3: 1, 5: 1}
	Caso s = [1, 4, 8, 10]
		O retorno deverá ser: {}
	Caso s = (111, 191, 202, 306, 239, 579)
		O retorno deverá ser: {191: 1, 239: 1}

	Parâmetros
	----------
	s : list | tuple
		itens : int
		descrição : Uma sequência arbitrária de números naturais.

	Retorno
	-------
	dict
		chave : int
		valor : int
		descrição : a chave é o número primo e o valor
			o total de ocorrências do número primo na
			sequência s.
	"""
	primos = []
	qnt = []
	for i in list(dict.fromkeys(s)):
		if eh_primo (i) is True:
			primos.append(i)
			qnt.append(s.count(i))
	resul = dict(
    	zip(primos, qnt)
     )
	return resul
	pass




def eh_armstrong(n):
	"""Função que verifica se um número é de Armstrong

	Recebe um número natural n, com n >= 0, e retorna
	verdadeiro se n é um número de Armstrong e falso
	caso contrário.

	Exemplos
	--------
	Um número é dito número de Armstrong se a soma de seus digitos
	elevados ao número total de digitos é igual a ele próprio.
	153 é número de Armstrong:
		1**3 + 5**3 + 3**3 = 1 + 125 + 27 = 153
	4 é número de Armstrong:
		4 ** 1 = 4

	Parâmetros
	----------
	n : int
		Número natural a ser testado.

	Retorno
	-------
	bool
		True se n for um número de Armstrong e False caso contrário.
	"""
	qualquer = str(n)
	numero = 0
	for i in qualquer:
		numero += int(i) ** len(qualquer)
	if numero == n:
		return True
	else:
		return False
	pass


def eh_quase_armstrong(n):
	"""Função que verifica se um número é quase de Armstrong

	Recebe um número natural n, com n >= 0, e retorna
	verdadeiro se n atende aos seguintes critérios:

	1) não ser um número de Armstrong;
	2) o resultado da soma de seus digitos elevados ao número total
	   de digitos é igual a ele próprio somado ou subtraído de 1.

	Exemplos
	--------
	35 é quase um número de Armstrong:
		3**2 + 5**2 = 9 + 25 = 34
	75 é quase um número de Armstrong:
		7**2 + 5**2 = 49 + 25 = 74

	Parâmetros
	----------
	n : int
		Número natural a ser testado.

	Retorno
	-------
	bool
		True se n for um número quase de Armstrong e False caso contrário.
	"""
	if eh_armstrong(n) is not True:
			valor = str(n)
			ams = 0
			for i in valor:
				ams += int(i) ** len(valor)
			if ams == n + 1:
				return True
			elif ams == n - 1:
				return True
			else:
				return False
	else:
		return False
	pass


def lista_armstrong(n):
	"""Função que lista os números e Armstrong até n

	Recebe um número natural n e retorna uma lista com todos o
	números de Armstrong estritamente menores que n, em ordem crescente.

	Parâmetros
	----------
	n : int
		Número natural que define o limite superior da lista.

	Retorno
	-------
	list
		itens : int
		descrição : Uma lista contendo todos os números de Armstrong
			menores que n, em ordem crescente.
	"""
	listAms = []
	for i in range(0, n):
		if eh_armstrong(i) is True:
			listAms.append(i)
	return listAms
	pass


def eh_perfeito(n):
	"""Função que verifica se um número é dito perfeito

	Recebe um número natural n, com n >= 2, e retorna verdadeiro se
	n é dito um número perfeito e falso caso contrário

	Exemplos
	--------
	Um número é dito perfeito se a soma de todos os divisores próprios é
	igual a ele mesmo.
	6 é um número perfeito:
		divisores próprios de 6: 1, 2, 3
		1 + 2 + 3 = 6
	12 NÃO é um número perfeito:
		divisores próprios de 12: 1, 2, 3, 4, 6
		1 + 2 + 3 + 4 + 6 = 16

	Parâmetros
	----------
	n : int
		Número natural a ser testado.

	Retorno
	-------
	bool
		True se n for um número perfeito e False caso contrário.
	"""
	pft = 1
	for i in range(2,n):
		if n % i == 0:
			pft += i
	if pft == n:
		return True
	else:
		return False
	pass


def lista_perfeitos(n):
	"""Função que lista os números ditos perfeitos até n

	Recebe um número natural n, com n >= 2, e retorna uma lista
	com todos os números perfeitos estritamente menores que n,
	em ordem crescente.

	Parâmetros
	----------
	n : int
		Número natural que define o limite superior da lista.

	Retorno
	-------
	list
		itens : int
		descrição : Uma lista contendo todos os números perfeitos
			menores que n em ordem crescente.
	"""
	listaPerfeita = []
	for i in range(2, n):
		if eh_perfeito(i) is True:
			listaPerfeita.append(i)
	return listaPerfeita
	pass
