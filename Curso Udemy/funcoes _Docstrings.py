'''''
Domumentação de funçoes con Docstrings
Podemos ter acesso á documentação de uma função em python utilizadom __doc__
'''

def diz_oi():
    '''Uma função que retorn oi'''
    return 'oi'

def entrada (a,b):
    """
    :param a:recebe a
    :param b: recebe b
    :return: retorna a+b
    """
    return a+b

import docstrings from entrada
print(entrada(10,01))