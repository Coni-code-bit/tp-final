from Pacientes import Pacientes
class donante(Pacientes): 
    def __init__(self, nombre, DNI, fecha_nac, sexo, telefono, tipo_de_sangre, hospital, fecha_fallecimiento):
        super().__init__(nombre,DNI, fecha_nac,sexo, telefono,tipo_de_sangre,hospital) 
        self.__fecha_fallecimiento= fecha_fallecimiento
        
        
        