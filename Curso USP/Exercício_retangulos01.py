x=int(input("Digite a Largura:"))
y=int(input("Digite a Altura:"))
repetelinha = 0
repetecoluna = 0
while repetecoluna<y:
      repetecoluna=repetecoluna+1
      leg='#'
      while repetelinha<x:
            repetelinha=repetelinha+1
      if repetecoluna%2==0:
         if x==y:
            print(leg * repetelinha)
         else:
            print(leg,' ' * (x-4),leg)
      else:
         print(leg * repetelinha)
