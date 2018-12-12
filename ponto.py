class Ponto:
    """ Cria um novo Ponto, com coordenadas x, y """
    def __init__(self, x=0, y=0):
        """ Inicializa em x, y o novo ponto criado pela classe """
        self.x = x
        self.y = y
    def distancia_da_origem(self):
        """ Calcula minha distânica da origem """
        return ((self.x ** 2) + (self.y ** 2)) ** 0.5    
    def ponto_medio(self, alvo):
        """ Retorna o ponto medio entre esse ponto e o alvo """
        mx = (self.x + alvo.x)/2
        my = (self.y + alvo.y)/2
        return Ponto(mx, my)
        
    def para_string(self):
        return "({0}, {1})".format(self.x, self.y)
    
    def distancia_entre_pontos(self, alvo):
        return (((self.x - alvo.x)**2 + (self.y - alvo.y)**2)**0.5)
    def reflexao_x(self):
        return (self.x , - self.y)
    def inclinacao_da_origem(self):
        return self.y/self.x
