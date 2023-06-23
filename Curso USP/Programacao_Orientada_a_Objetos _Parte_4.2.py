class Triangulo:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def tipo_lado(self):
        if self.a != self.b and self.b != self.c and self.a != self.c :
            return 'escaleno'
            #print('escaleno')
        elif self.a == self.b and self.b == self.c:
             return 'equilátero'
             #print('equilátero')
        else:
            return 'isósceles'
            #print('isósceles')




t = Triangulo(5,8,5)
t.tipo_lado()











