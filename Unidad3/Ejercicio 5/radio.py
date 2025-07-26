from claMedio import Medio

class Radio(Medio):
    __nombre: str
    __programacion: list 
    def __init__(self, nombre, frecuencia, audiencia):
        super().__init__(nombre, frecuencia, audiencia)
        
    
    