from enum import Enum

class lista_organos(Enum):
    corazon=1
    higado=2
    pancreas=3
    huesos=4
    rinon=5
    pulmones=6
    intestino=7
    piel=8
    corneas=9
    
class organos(lista_organos): 
    def __init__(self, organo:lista_organos, ablacion, hora_inicio): 
        self.organo=organo
        self.fecha_ablacion=ablacion  ##fecha de organo disponible
        self.hora_inicio=hora_inicio ##hora inicio de organo disponible
        
              
    