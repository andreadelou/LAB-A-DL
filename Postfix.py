
class convertir:
    #constructor
    def __init__(self, t):
        self.top = -1
        self.tamano = t
        self.stack = []
        # precedencia setting
        self.precedencia = {'|': 1, '.': 1, '*': 2}
        # Aqui se almacena el resultado final
        self.output = []
        self.res = ""
