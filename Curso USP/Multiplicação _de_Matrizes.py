"""
def main():
    a = [[1, 2, 3], [4, 5, 6]]
    b = [[1, 2], [3, 4], [5, 6]]
    mat_mul(a,b)

def mat_mul(a,b):
    num_linhas_a, num_colunas_a = len(a),len(a[0])
    num_linhas_b, num_colunas_b = len(b), len(b[0])
    assert num_colunas_a == num_colunas_b

    c = []
    for linha in range(num_linhas_a):
       #comecando uma nova linha
       c.append([])
       for coluna in range(num_colunas_b):
           # adicionando uma nova coluna na linha
           c[linha].append(0)
           for k in range(num_colunas_a):
               c[linha][coluna] += a[linha][k] * b[k][coluna]
    print(c)
main()
"""""
'''
if __name__ == '__main__':
    a = [[1,2,3],[4,5,6]]
    b = [[1,2],[3,4],[5,6]]
    print(mat_mul(a,b)
    )
'''
a = [[1, 2, 3], [4, 5, 6]]
b = [[1, 2], [3, 4], [5, 6]]
nova = []
soma = 0
for i in range(len(a)):
    for j in range(len(a[i])):
        soma = a[i][j] * b[j][i]
        nova.append(soma)

print(nova)        