from Optimizacion.Optimizacion import Optimizacion
from Optimizacion.TipoCodigo import TipoBloque, TipoInstruccion


class Optimizar():
    def __init__(self, bloques, reglas):
        self.bloques = bloques
        self.reglas = reglas
        self.iteracion = 1

    def Ejecutar(self):
        self.Regla1()
        self.Regla2()
        self.Regla3()
        self.Regla4()
        self.Regla5()
        self.Regla6()
        self.Regla7()
        self.Regla8()

    def IncrementarIteracion(self):
        self.iteracion = self.iteracion +1 

    def Regla1(self):
        '''
        t2 = b | t2 = b
        b = t2 |
        '''
        for bloque in self.bloques:
            if bloque.getTipo() == TipoBloque.VOID or bloque.getTipo() == TipoBloque.MAIN:
                i = 0
                while i<len(bloque.getInstrucciones()):
                    #DEBO BUSCAR ASIGNACIONES SIMPLES
                    if bloque.getInstrucciones()[i].getTipo() == TipoInstruccion.ASIGNACIONSIMPLE:
                        #ENCUENTRA UNA ASI QUE NECESITO IR A i ++
                        #TENGO QUE ITERAR HASTA QUE ENCUENTRE UNA ETIQUETA
                        nuevoinicio = i + 1
                        etiqueta = False
                        hayCambio = False
                        temporal = bloque.getInstrucciones()[i].getTemporal()
                        operador = bloque.getInstrucciones()[i].getOperador1()
                        #SI ES UN NUMERO NO CUENTA
                        if not self.IsNumber(operador):
                            j = nuevoinicio
                            while j < len(bloque.getInstrucciones()):
                                if bloque.getInstrucciones()[j].getTipo() == TipoInstruccion.ETIQUETA:
                                    etiqueta = True
                                if etiqueta:
                                    break;
                                #VER SI ES UN TIPO DE ASIGNACION
                                if bloque.getInstrucciones()[j].getTipo() == TipoInstruccion.ASIGNACIONSIMPLE or bloque.getInstrucciones()[j].getTipo() == TipoInstruccion.ASIGNACIONOPERACION:
                                    temporal2 = bloque.getInstrucciones()[j].getTemporal()
                                    operador2 = bloque.getInstrucciones()[j].getOperador1()
                                    linea = bloque.getInstrucciones()[j].getFila()
                                    codigo = bloque.getInstrucciones()[j].getCodigoAnterior()

                                    if temporal2 == operador:#SI ES VERDADERO QUIERE DECIR QUE SI PUDO HABER CAMBIADO
                                        if operador2 == temporal:#PERO PUEDE SER QUE HALLA LLEGADO AL FIN DE LA REGLA TAMBIEN
                                            #SI ES ASÍ TENGO QUE VER QUE NO HALLA CAMBIO
                                            if not hayCambio:
                                                bloque.getInstrucciones().pop(j)
                                                self.reglas.append(Optimizacion("Mirilla", "Regla 1", "Se eliminó variable redundante", codigo, " - ", linea))
                                                j += -1
                                                i += -1
                                        else:
                                            hayCambio = True
                                if bloque.getInstrucciones()[j].getTipo() == TipoInstruccion.ASIGNACIONARREGLO:
                                    temporal2 = bloque.getInstrucciones()[j].getTemporal()
                                    if temporal2 == operador:
                                        hayCambio = True
                                j += 1
                    i += 1

    def Regla2(self):
        '''
        goto L1         | L1:
        <instrucciones> |
        L1:             |
        '''
        for bloque in self.bloques:
            linea = ""
            if bloque.getTipo() == TipoBloque.VOID or bloque.getTipo() == TipoBloque.MAIN:
                i = 0
                while i<len(bloque.getInstrucciones()):
                    if bloque.getInstrucciones()[i].getTipo() == TipoInstruccion.GOTO:
                        etiqueta = bloque.getInstrucciones()[i].getEtiqueta()
                        codigo = bloque.getInstrucciones()[i].getC3D() + "..instrucciones.. "+etiqueta+":"
                        linea = bloque.getInstrucciones()[i].getFila()
                        j = i+1
                        encontrado = False
                        k = 0
                        l = i+1
                        while j < len(bloque.getInstrucciones()):
                            if bloque.getInstrucciones()[j].getTipo() == TipoInstruccion.ETIQUETA:
                                if bloque.getInstrucciones()[j].getEtiqueta() == etiqueta:
                                    encontrado = True
                                    k = j-1
                                    break

                            j += 1
                        #ver si encontró la etiqueta (obvio la encuentra)
                        if encontrado:
                            hayEtiquetas = False
                            t = l
                            while l < k:
                                if bloque.getInstrucciones()[l].getTipo() == TipoInstruccion.ETIQUETA:
                                    hayEtiquetas = True
                                l += 1
                            
                            if not hayEtiquetas:
                                while t<k:
                                    bloque.getInstrucciones().pop(t)
                                    t+=1
                                self.reglas.append(Optimizacion("Mirilla", "Regla 2", "Se encontró codigo inalcanzable", codigo, bloque.getInstrucciones()[i].getC3D(), linea))
                    i += 1
                            
    def Regla3(self):
        '''
        f a == 10 {goto L1} |if a != 10 {goto L2}
        goto L2             |<instrucciones1>
        L1:                 |L2:
        <instrucciones1>    |
        L2:                 |
        '''
        for bloque in self.bloques:
            linea = ""
            if bloque.getTipo() == TipoBloque.VOID or bloque.getTipo() == TipoBloque.MAIN:
                i=0
                while i<len(bloque.getInstrucciones()):
                    if bloque.getInstrucciones()[i].getTipo() == TipoInstruccion.IF and bloque.getInstrucciones()[i+1].getTipo() == TipoInstruccion.GOTO:
                        codigoant = bloque.getInstrucciones()[i].getCodigoAnterior() + " "+bloque.getInstrucciones()[i+1].getC3D()
                        negacion = bloque.getInstrucciones()[i+1].getEtiqueta()
                        aceptacion = bloque.getInstrucciones()[i].getGoto()
                        linea = bloque.getInstrucciones()[i].getFila()
                        cambio = self.CambiarCondicion(bloque.getInstrucciones()[i].getOperador())
                        bloque.getInstrucciones()[i].setOperador(cambio)
                        bloque.getInstrucciones()[i].setGoto(negacion)
                        bloque.getInstrucciones().pop(i+1)
                        #TENGO QUE ELIMINAR LA ETIQUETA ACEPTACION
                        j = i
                        while j <len(bloque.getInstrucciones()):
                            if bloque.getInstrucciones()[j].getTipo() == TipoInstruccion.ETIQUETA:
                                etiquetatmp = bloque.getInstrucciones()[j].getEtiqueta()
                                if etiquetatmp == aceptacion:
                                    bloque.getInstrucciones().pop(j)
                                    i+=1
                                break
                            j+=1
                        self.reglas.append(Optimizacion("Mirilla", "Regla 3", "Se encontró if", codigoant, bloque.getInstrucciones()[i].getC3D(), linea))
                    i+=1

    def Regla4(self):
        '''
        goto L1         |goto L2
        <instrucciones> |<instrucciones>
        L1:             |L1:
        goto L2         |goto L2
        '''
        for bloque in self.bloques:
            if bloque.getTipo() == TipoBloque.VOID or bloque.getTipo() == TipoBloque.MAIN:
                i=0
                posprimergoto=0
                segundogoto=""
                secumple=False
                while i<len(bloque.getInstrucciones()):
                    if bloque.getInstrucciones()[i].getTipo()== TipoInstruccion.GOTO:
                        #DEBEMOS BUSCAR LA ETIQUETA
                        etiqueta = bloque.getInstrucciones()[i].getEtiqueta()
                        j = i+1
                        while j<len(bloque.getInstrucciones()):
                            #DEBEMOS VER SI ES ETIQUETA
                            if bloque.getInstrucciones()[j].getTipo() == TipoInstruccion.ETIQUETA:
                                #SI ENCUENTRA LA ETIQUETA... PREGUNTA SI SON IGUALES
                                if bloque.getInstrucciones()[j].getEtiqueta() == etiqueta:
                                    posterior = j + 1
                                    #DEBEMOS VER SI BAJO ESA ETIQUETA HAY UN GOTO CON OTRA ETIQUETA
                                    if posterior < len(bloque.getInstrucciones()):
                                        if bloque.getInstrucciones()[posterior].getTipo()== TipoInstruccion.GOTO:
                                            segundogoto = bloque.getInstrucciones()[posterior].getEtiqueta()
                                            #ELIMINO LA ETIQUETA PARA QUE NO HALLA CLAVO CON GOLANG
                                            bloque.getInstrucciones().pop(j)
                                            secumple = True
                                            break
                                    else:
                                        secumple = False
                                        break
                            j+=1
                        if secumple:
                            bloque.getInstrucciones()[posprimergoto].setEtiqueta(segundogoto)
                            linea = bloque.getInstrucciones()[posprimergoto].getFila()
                            self.reglas.append(Optimizacion("Mirilla", "Regla 4", "Se encontro una Etiqueta redundante", bloque.getInstrucciones()[posprimergoto].getCodigoAnterior(), bloque.getInstrucciones()[posprimergoto].getC3D(), linea))
                    i+=1

    def Regla5(self):
        '''
        if a < b {goto L1}  |if a < b {goto L2}
        <instrucciones>     |<instrucciones>
        L1:                 |L1:
        goto L2             |goto L2
        '''
        for bloque in self.bloques:
            linea = ""
            if bloque.getTipo() == TipoBloque.VOID or bloque.getTipo() == TipoBloque.MAIN:
                i=0
                posprimergoto=0
                while i<len(bloque.getInstrucciones()):
                    if bloque.getInstrucciones()[i].getTipo()== TipoInstruccion.IF:
                        #DEBEMOS BUSCAR LA ETIQUETA
                        etiqueta = bloque.getInstrucciones()[i].getGoto()
                        posprimergoto = i
                        segundogoto = ""
                        secumple = False
                        j = i+1
                        while j<len(bloque.getInstrucciones()):
                            if bloque.getInstrucciones()[j].getTipo() == TipoInstruccion.ETIQUETA:
                                #SI ENCUENTRA LA ETIQUETA... PREGUNTA SI SON IGUALES
                                if bloque.getInstrucciones()[j].getEtiqueta() == etiqueta:
                                    posterior = j +1
                                    if bloque.getInstrucciones()[posterior].getTipo()== TipoInstruccion.GOTO:
                                        segundogoto = bloque.getInstrucciones()[posterior].getEtiqueta()
                                        secumple = True
                                        #ELIMINO LA ETIQUETA PARA QUE NO HALLA CLAVO CON GOLANG
                                        bloque.getInstrucciones().pop(j)
                                        break
                            j+=1
                        if secumple:
                            bloque.getInstrucciones()[posprimergoto].setGoto(segundogoto)
                            linea = bloque.getInstrucciones()[posprimergoto].getFila()
                            self.reglas.append(Optimizacion("Mirilla", "Regla 5", "Se encontro una If con Etiqueta redundante", bloque.getInstrucciones()[posprimergoto].getCodigoAnterior(), bloque.getInstrucciones()[posprimergoto].getC3D(), linea))
                    i+=1

    def Regla6(self):
        '''
        x = x + 0   |SE ELIMINAN
        x = x - 0   |
        x = x * 1   |
        x = x / 1   |
        '''
        for bloque in self.bloques:
            if bloque.getTipo() == TipoBloque.VOID or bloque.getTipo() == TipoBloque.MAIN:
                    i=0
                    while i<len(bloque.getInstrucciones()):
                        if bloque.getInstrucciones()[i].getTipo() == TipoInstruccion.ASIGNACIONOPERACION:
                            if bloque.getInstrucciones()[i].getOperador1() == bloque.getInstrucciones()[i].getTemporal():
                                #SI ES SUMA HAY QUE VER QUE SEA 0
                                print("OPERADOR: ", bloque.getInstrucciones()[i].getOperador())
                                if bloque.getInstrucciones()[i].getOperador()=="+" or bloque.getInstrucciones()[i].getOperador()=="-":
                                    if bloque.getInstrucciones()[i].getOperador2() == 0:
                                        anterior = bloque.getInstrucciones()[i].getCodigoAnterior()
                                        linea = bloque.getInstrucciones()[i].getFila()
                                        self.reglas.append(Optimizacion("Mirilla", "Regla 6", "Se encontró suma/resta con cero", anterior, "Se elimina", linea))
                                        bloque.getInstrucciones().pop(i)
                                        i = i - 1;
                                elif bloque.getInstrucciones()[i].getOperador()=="*" or bloque.getInstrucciones()[i].getOperador()=="/":
                                    if bloque.getInstrucciones()[i].getOperador2() == 1:
                                        anterior = bloque.getInstrucciones()[i].getCodigoAnterior()
                                        linea = bloque.getInstrucciones()[i].getFila()
                                        self.reglas.append(Optimizacion("Mirilla", "Regla 6", "Se encontró mult/div con cero", anterior, "Se elimina", linea))
                                        bloque.getInstrucciones().pop(i)
                                        i = i - 1;
                        i+=1

    def Regla7(self):
        '''
        x = y + 0   | X = Y
        x = y - 0   |
        x = y * 1   |
        x = y / 1   |
        '''
        for bloque in self.bloques:
            if bloque.getTipo() == TipoBloque.VOID or bloque.getTipo() == TipoBloque.MAIN:
                    i=0
                    while i<len(bloque.getInstrucciones()):
                        if bloque.getInstrucciones()[i].getTipo() == TipoInstruccion.ASIGNACIONOPERACION:
                            if bloque.getInstrucciones()[i].getOperador1() != bloque.getInstrucciones()[i].getTemporal():
                                #SI ES SUMA HAY QUE VER QUE SEA 0
                                if bloque.getInstrucciones()[i].getOperador()=="+" or bloque.getInstrucciones()[i].getOperador()=="-":
                                    if bloque.getInstrucciones()[i].getOperador2() == 0:
                                        anterior = bloque.getInstrucciones()[i].getCodigoAnterior()
                                        linea = bloque.getInstrucciones()[i].getFila()
                                        bloque.getInstrucciones()[i].setOperador2("")
                                        bloque.getInstrucciones()[i].setOperador("")
                                        bloque.getInstrucciones()[i].setTipo(TipoInstruccion.ASIGNACIONSIMPLE)
                                        nuevo = bloque.getInstrucciones()[i].getC3D()
                                        self.reglas.append(Optimizacion("Mirilla", "Regla 7", "Se encontró suma/resta con cero", anterior, nuevo, linea))
                                elif bloque.getInstrucciones()[i].getOperador()=="*" or bloque.getInstrucciones()[i].getOperador()=="/":
                                    if bloque.getInstrucciones()[i].getOperador2() == 1:
                                        anterior = bloque.getInstrucciones()[i].getCodigoAnterior()
                                        linea = bloque.getInstrucciones()[i].getFila()
                                        bloque.getInstrucciones()[i].setOperador2("")
                                        bloque.getInstrucciones()[i].setOperador("")
                                        bloque.getInstrucciones()[i].setTipo(TipoInstruccion.ASIGNACIONSIMPLE)
                                        nuevo = bloque.getInstrucciones()[i].getC3D()
                                        self.reglas.append(Optimizacion("Mirilla", "Regla 7", "Se encontró mult/div con cero", anterior, nuevo, linea))
                        i+=1

    def Regla8(self):
        '''
        x = y * 2   | x = y + y
        x = y * 0   | x = 0
        x = 0 / y   | x = 0
        '''
        for bloque in self.bloques:
            if bloque.getTipo() == TipoBloque.VOID or bloque.getTipo() == TipoBloque.MAIN:
                    i=0
                    while i<len(bloque.getInstrucciones()):
                        print("ENTRO ALV")
                        if bloque.getInstrucciones()[i].getTipo() == TipoInstruccion.ASIGNACIONOPERACION:
                            if bloque.getInstrucciones()[i].getOperador1() != bloque.getInstrucciones()[i].getTemporal():
                                #SI ES SUMA HAY QUE VER QUE SEA 0
                                if bloque.getInstrucciones()[i].getOperador()=="*":
                                    if bloque.getInstrucciones()[i].getOperador2() == 2:
                                        anterior = bloque.getInstrucciones()[i].getCodigoAnterior()
                                        linea = bloque.getInstrucciones()[i].getFila()
                                        bloque.getInstrucciones()[i].setOperador2(bloque.getInstrucciones()[i].getOperador1())
                                        bloque.getInstrucciones()[i].setOperador("+")
                                        bloque.getInstrucciones()[i].setTipo(TipoInstruccion.ASIGNACIONSIMPLE)
                                        nuevo = bloque.getInstrucciones()[i].getC3D()
                                        self.reglas.append(Optimizacion("Mirilla", "Regla 8", "Se encontró multiplicacion de dos", anterior, nuevo, linea))
                                    if bloque.getInstrucciones()[i].getOperador2() == 0:
                                        anterior = bloque.getInstrucciones()[i].getCodigoAnterior()
                                        linea = bloque.getInstrucciones()[i].getFila()
                                        bloque.getInstrucciones()[i].setOperador1(0)
                                        bloque.getInstrucciones()[i].setOperador2("")
                                        bloque.getInstrucciones()[i].setOperador("")
                                        bloque.getInstrucciones()[i].setTipo(TipoInstruccion.ASIGNACIONSIMPLE)
                                        nuevo = bloque.getInstrucciones()[i].getC3D()
                                        self.reglas.append(Optimizacion("Mirilla", "Regla 8", "Se encontró multiplicacion de cero", anterior, nuevo, linea))
                                elif bloque.getInstrucciones()[i].getOperador()=="/":
                                    if bloque.getInstrucciones()[i].getOperador1() == 0:
                                        anterior = bloque.getInstrucciones()[i].getCodigoAnterior()
                                        linea = bloque.getInstrucciones()[i].getFila()
                                        bloque.getInstrucciones()[i].setOperador1(0)
                                        bloque.getInstrucciones()[i].setOperador2("")
                                        bloque.getInstrucciones()[i].setOperador("")
                                        bloque.getInstrucciones()[i].setTipo(TipoInstruccion.ASIGNACIONSIMPLE)
                                        nuevo = bloque.getInstrucciones()[i].getC3D()
                                        self.reglas.append(Optimizacion("Mirilla", "Regla 8", "Se encontró division con cero", anterior, nuevo, linea))
                        i+=1

    def CambiarCondicion(self, condicion):
        print("CONDICION: ", condicion)
        if condicion == "==":
            return "!="
        if condicion == "!=":
            return "=="
        if condicion == "<=":
            return ">="
        if condicion == ">=":
            return "<="
        if condicion == "<":
            return ">"
        if condicion == ">":
            return "<"

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