from Optimizacion.Optimizacion import Optimizacion
from Optimizacion.TipoCodigo import TipoBloque, TipoInstruccion


class Optimizar():
    def __init__(self, bloques, reglas):
        self.bloques = bloques
        self.reglas = reglas
        self.iteracion = 1

    def Ejecutar(self):
        self.Regla1()

    def IncrementarIteracion(self):
        self.iteracion = self.iteracion +1 

    def Regla1(self):
        # t2 = b | t2 = b
        # b = t2 |
        for bloque in self.bloques:
            if bloque.getTipo() == TipoBloque.VOID or bloque.getTipo() == TipoBloque.MAIN:
                for i in range(0, len(bloque.getInstrucciones())):
                    #DEBO BUSCAR ASIGNACIONES SIMPLES
                    print("INIDICE I : ", i, " TOPE DE LA MATRIZ: ", len(bloque.getInstrucciones()))
                    if i >= len(bloque.getInstrucciones()):
                        return
                    if bloque.getInstrucciones()[i].getTipo() == TipoInstruccion.ASIGNACIONSIMPLE:
                        #ENCUENTRA UNA ASI QUE NECESITO IR A i ++
                        #TENGO QUE ITERAR HASTA QUE ENCUENTRE UNA ETIQUETA
                        nuevoinicio = i + 1
                        etiqueta = False
                        hayCambio = False
                        temporal = bloque.getInstrucciones()[i].getTemporal()
                        operador = bloque.getInstrucciones()[i].getOperador1()#Tengo que ver que este no cambie
                        
                        if not self.IsNumber(operador):#Para ver si es un numero no cuenta 
                            for j in range(nuevoinicio, len(bloque.getInstrucciones())):
                                if bloque.getInstrucciones()[j].getTipo() == TipoInstruccion.ETIQUETA:
                                    etiqueta = True
                                if etiqueta:
                                    break;
                                #VER SI ES UN TIPO DE ASIGNACION
                                if bloque.getInstrucciones()[j].getTipo() == TipoInstruccion.ASIGNACIONARREGLO or bloque.getInstrucciones()[j].getTipo() == TipoInstruccion.ASIGNACIONSIMPLE or bloque.getInstrucciones()[j].getTipo() == TipoInstruccion.ASIGNACIONOPERACION:
                                    temporal2 = bloque.getInstrucciones()[j].getTemporal()
                                    if bloque.getInstrucciones()[j]!=TipoInstruccion.ASIGNACIONARREGLO:
                                        operador2 = bloque.getInstrucciones()[j].getOperador1()
                                        linea = bloque.getInstrucciones()[j].getFila()
                                        codigo = bloque.getInstrucciones()[j].getCodigoOriginal()

                                        if temporal2 == operador:#SI ES VERDADERO QUIERE DECIR QUE SI PUDO HABER CAMBIADO
                                            if operador2 == temporal:#PERO PUEDE SER QUE HALLA LLEGADO AL FIN DE LA REGLA TAMBIEN
                                                #SI ES ASÍ TENGO QUE VER QUE NO HALLA CAMBIO
                                                if not hayCambio:
                                                    bloque.getInstrucciones().pop(j)
                                                    self.reglas.append(Optimizacion("Mirilla", "Regla 1", "Se eliminó original", codigo, " - ", linea))
                                                    j += -1
                                                    i += -1
                                            else:
                                                hayCambio = True

    def IsNumber(self, operador):
        if type(operador) is int:
            return True

        if type(operador) is float:
            return True
    
        return False

    def ReporteOptimizacion(self, lista):
        cadena = ""
        cadena +="<table class=\"table\">"
        cadena +="<tr>"
        cadena +="<th scope=\"col\">Tipo</th>"
        cadena +="<th scope=\"col\">Regla</th>"
        cadena +="<th scope=\"col\">Descripción</th>"
        cadena +="<th scope=\"col\">Original</th>"
        cadena +="<th scope=\"col\">Optimizado</th>"
        cadena +="<th scope=\"col\">Fila</th>"
        cadena +="<th scope=\"col\">Iteración</th>"
        cadena +="</tr>"
        for item in lista:
            cadena += "<tr>"
            cadena += "<td>"
            cadena += str(item.getTipo())
            cadena += "</td>"
            cadena += "<td>"
            cadena += str(item.getRegla())
            cadena += "</td>"
            cadena += "<td>"
            cadena += str(item.getDescripcion())
            cadena += "</td>"
            cadena += "<td>"
            cadena += str(item.getOriginal())
            cadena += "</td>"
            cadena += "<td>"
            cadena += str(item.getOptimizado())
            cadena += "</td>"
            cadena += "<td>"
            cadena += str(item.getFila())
            cadena += "</td>"
            cadena += "<td>"
            cadena += str(self.iteracion)
            cadena += "</td>"
            cadena += "</tr>"
        cadena +="</table>"
        return cadena   