'''
Escopo de Variáveis
/ espaço delimitado de informçõa/variáveis /

1º Variáveis Globais:
   Abrange todo o programa
2ºVariáveis locais:
  Limitado ao bloco onde foi declarada.

Para declarar varável em Python
nome da variavel = valor da variavel

Python tem a tipagem dinâmica.
'''

numero=42
print (numero)
print(type(numero))

numero='Geek'
print (numero)
print(type(numero))

nao_existe=34
print(nao_existe)

numero = 9

if numero > 10:
   novo=numero+10
   print(novo)
elif numero < 10:
     novo=numero-10
     print(novo)
