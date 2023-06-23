import Chama_Bhaskarah

class TestBhaskara:
    def testa_uma_raiz(self):
        b = Chama_Bhaskarah.Chama_Bhaskarah()
        assert b.calcularaizes(1, 0 , 0)==(1,0)