from Pacientes import Pacientes
from enum import Enum

class lista_prioridad(Enum):
    #es el primer coparativo para designar bien el orden, si coincide usamos las fechas de ingreso a la losta de espera
    #1-5 es prioridad 
    corazon=1
    pulmon=2
    higado=3
    riñon=4
    intestino=5
    ##6-9 no es tan urgente
    pancreas=6
    piel=7
    corneas=8
    huesos=9
    

class receptor(Pacientes, lista_prioridad): 
    def __init__(self, nombre, DNI, fecha_nac, sexo, telefono, tipo_de_sangre, hospital,fecha_ingreso, patologia,prioridad:lista_prioridad, estado): 
        super().__init__(nombre, DNI, fecha_nac, sexo, telefono, tipo_de_sangre, hospital)
        self.fecha_ingreso=fecha_ingreso#fecha de ingreso a la lista de espera
        self.__patologia=patologia
        self.prioridad=prioridad
        self. estado=estado
        
        
        

    
        
    