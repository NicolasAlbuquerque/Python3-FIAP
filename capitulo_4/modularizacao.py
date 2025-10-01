# 1. IMPORTAR O ARQUIVO
import calculos
# 2. IMPORTAR AS FUNÇÕES ESPECIFICAS
from calculos import somar,subtrair, dividir, multiplicar
# 3. IMPORTAR TODAS AS FUNÇÕES DE UAM VEZ SÓ
from  calculos import *

# 1. CHAMANDO FUNÇÕES DO OUTRO ARQUIVO
print(f'A Soma dos valores é : {calculos.somar(1,2)}')
# 2. CHAMANDO FUNÇÕES IMPORTADAS
print(f'importando a função dividir: {dividir(float(input('Digite o primeiro valor: ')),float(input('Digite o segundo valor: ')))}')
