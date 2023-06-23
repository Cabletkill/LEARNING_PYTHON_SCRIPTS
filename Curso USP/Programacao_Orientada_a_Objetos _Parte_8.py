def entrada_de_dados():
       ligar = input("Ligar")
       desligar = input('Desligar')
       info = input("Info")
       Saida_de_Dados(ligar, desligar, info)


# marca, memoria ram, placa de video
class Computador:
      def __init__( self, marca, memoria_ram, placa_de_video):
          self.marca = marca
          self.memoria_ram = memoria_ram
          self.placa_de_video   = placa_de_video

      def Ligar(self):#metodo para ligar o computador
          print("Executanto Ligar")

      def Desligar(self): #Metodo
          print("Executando Desligar")

      def Exibir_inf_Comp(self):Metodo
          print(self.marca, self.memoria_ram, self.placa_de_video)

def Saida_de_Dados(ligar,desligar,info):
    computador1 = Computador('marca', 'memoria_ram', 'placa_de_video')
    computador1.Ligar()
    computador1.Desligar()
    computador1.Exibir_inf_Comp()

entrada_de_dados()




