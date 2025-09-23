#Tipos de dados.
# linguagem de tipagem dinâmica, não precisa esclarecer qual tipo de dados.


#STR SSTRING
nome = 'Nicolas'

#INT INTEIRO
idade = 30

#FLOAT NUMERO COM PONTO FLUTUANTE/NUMEROS REAIS
altura = 1.81

#BOOL, BOOLEANO, 0 OU 1, VERSADEIRO OU FALSO.
dirige = True

#NUMEROS COMPLEXOS
rg = 4j
#j é a parte imaaginária

imaginarios = 1+2j #2j é a parte imaginária 1 paarte real

imaginarios2 = (4, -2) #4 - 2j 

#-----------------------------------------------------------------------------------


#ALTERAR VALORE DA VARIÁVEL

idade = 18

#Verificar o tipo de dado

type(nome) #função type, mostra o tipo de dado

#CONVERSÃO DE TIPOS DE DADOS


teste = '123' #str

print(type(teste)) #verificação

teste =int(teste) #para int

print(type(teste)) #verificação

teste = float(teste)
print(type(teste)) #verificação

#-----------------------------------------------------------------------------------

#CONVERTER TEXTO OU NUMERO PARA BOOL

#tudo que for diferente de 0 é veradeiro, o que for 0 é falso
testebool = 123  #declarar
testebool2 = 0

testebool = bool(testebool) #converter
testebool2 = bool(testebool2)

print(f'{testebool}  // {testebool2}')


#texto vazio é falso, texto com caracteres verdadeiro

testebool3 = 'true' #declarar
testebool4 = ''

testebool3 = bool(testebool3)
testebool4 = bool(testebool4)

print(f'{testebool3} // {testebool4}')


