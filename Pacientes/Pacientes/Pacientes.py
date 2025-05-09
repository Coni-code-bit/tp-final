from enum import Enum

class Pacientes(): 
    def __init__(self, nombre, DNI, fecha_nac, sexo, telefono, tipo_de_sangre, hospital): 
        self.nombre=nombre
        self.DNI=DNI
        self.__fecha_nac=fecha_nac
        self.__sexo=sexo
        self.__telefono=telefono 
        self.tipo_de_sangre=tipo_de_sangre
        self.hospital=hospital
        
class donante(Pacientes): 
    def __init__(self, nombre, DNI, fecha_nac, sexo, telefono, tipo_de_sangre, hospital, fecha_fallecimiento):
        super().__init__(nombre,DNI, fecha_nac,sexo, telefono,tipo_de_sangre,hospital) 
        self.__fecha_fallecimiento= fecha_fallecimiento
        
        

            
        
        
        
        
            
        
        
         
    
        
    
        
        
    
        
    