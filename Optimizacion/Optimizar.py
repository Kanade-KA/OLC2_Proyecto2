from Optimizacion.Optimizacion import Optimizacion
from Optimizacion.TipoCodigo import TipoBloque, TipoInstruccion


class Optimizar():
    def __init__(self, bloques, reglas, iteracion):
        self.bloques = bloques
        self.reglas = reglas
        self.iteracion = iteracion

    def Ejecutar(self):
        self.Regla1()
        self.Regla2()
        self.Regla3()
        self.Regla4()

        self.Regla5()
        self.Regla6()
        self.Regla7()
        self.Regla8()

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
                                                self.reglas.append(Optimizacion("Mirilla", "Regla 1", "Se eliminó variable redundante", codigo, " - ", linea, self.iteracion))
                                                j += -1
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
                                self.reglas.append(Optimizacion("Mirilla", "Regla 2", "Se encontró codigo inalcanzable", codigo, bloque.getInstrucciones()[i].getC3D(), linea, self.iteracion))
                    i += 1
                            
    def Regla3(self):
        '''
        if a == 10 {goto L1}|if a != 10 {goto L2}
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
                    #VER QUE SEA UN IF CON GOTO PRIMERO
                    if bloque.getInstrucciones()[i].getTipo() == TipoInstruccion.IF and bloque.getInstrucciones()[i+1].getTipo() == TipoInstruccion.GOTO:
                        aceptacion = bloque.getInstrucciones()[i].getGoto()
                        #TENGO QUE VER SI DESPUES DEL GOTO VIENE LA ETIQUETA DE ACEPTACION
                        if bloque.getInstrucciones()[i+2].getTipo() == TipoInstruccion.ETIQUETA:
                            if bloque.getInstrucciones()[i+2].getEtiqueta() == aceptacion:
                                codigoant = bloque.getInstrucciones()[i].getCodigoAnterior() + " "+bloque.getInstrucciones()[i+1].getC3D()+" "+bloque.getInstrucciones()[i+2].getC3D()
                                negacion = bloque.getInstrucciones()[i+1].getEtiqueta()
                                linea = bloque.getInstrucciones()[i].getFila()
                                cambio = self.CambiarCondicion(bloque.getInstrucciones()[i].getOperador())
                                bloque.getInstrucciones()[i].setOperador(cambio)
                                bloque.getInstrucciones()[i].setGoto(negacion)
                                #TENGO QUE VER SI ESA ETIQUETA ES UTILIZADA EN OTRO LADO...
                                k = 0
                                tope = i+1
                                siseusa = False
                                while k < tope:
                                    if bloque.getInstrucciones()[k].getTipo() == TipoInstruccion.IF:
                                        if bloque.getInstrucciones()[k].getGoto() == aceptacion:
                                            siseusa = True
                                    if bloque.getInstrucciones()[k].getTipo() == TipoInstruccion.GOTO:
                                        if bloque.getInstrucciones()[k].getEtiqueta() == aceptacion:
                                            siseusa = True
                                    k+=1
                                
                                if not siseusa:
                                    bloque.getInstrucciones().pop(i+1)#PARA ELIMINAR EL DE GOTO
                                    bloque.getInstrucciones().pop(i+1)#PARA ELIMINAR LA ETIQUETA DEL GOTO
                                    self.reglas.append(Optimizacion("Mirilla", "Regla 3", "Se encontró if", codigoant, bloque.getInstrucciones()[i].getC3D(), linea, self.iteracion))
                                
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
                posicionGoto1 = 0
                posicionObsoleta = 0
                etiquetaGoto1 = ""#Sera la obsoleta 
                etiquetaGoto2 = ""#Sera la que reemplaza al goto 1
                secumple = False
                while i<len(bloque.getInstrucciones()):
                    #BUSCAMOS UN GOTO...
                    if bloque.getInstrucciones()[i].getTipo()== TipoInstruccion.GOTO:
                        posicionGoto1 = i
                        etiquetaGoto1 = bloque.getInstrucciones()[i].getEtiqueta()
                        j = i+1
                        #BUSCAMOS LA ETIQUETA CON ESE NOMBRE
                        while j<len(bloque.getInstrucciones()):
                            if bloque.getInstrucciones()[j].getTipo() == TipoInstruccion.ETIQUETA:
                                #SI ENCUENTRA LA ETIQUETA... PREGUNTA SI SON IGUALES
                                if bloque.getInstrucciones()[j].getEtiqueta() == etiquetaGoto1:
                                    #DEBEMOS VER SI BAJO ESA ETIQUETA HAY UN GOTO CON OTRA ETIQUETA
                                    posicionObsoleta = j
                                    if j+1 < len(bloque.getInstrucciones()):#ESTO PARA VER SI NO LLEGÓ A UN TOPE
                                        if bloque.getInstrucciones()[j+1].getTipo()== TipoInstruccion.GOTO:
                                            etiquetaGoto2 = bloque.getInstrucciones()[j+1].getEtiqueta()
                                            secumple = True
                                            break
                                    else:
                                        secumple = False
                                        break
                            j+=1
                        if secumple:
                            #ANTES DE ELIMINAR ESA ETIQUETA DEBEMOS VER QUE NO ESTÉ LLAMADA POR OTRO LADO
                            k = 0
                            while k < posicionObsoleta:
                                if bloque.getInstrucciones()[k].getTipo() == TipoInstruccion.IF:
                                    if bloque.getInstrucciones()[k].getGoto() == etiquetaGoto1:
                                        siseusa = True
                                if bloque.getInstrucciones()[k].getTipo() == TipoInstruccion.GOTO:
                                    if bloque.getInstrucciones()[k].getEtiqueta() == etiquetaGoto1:
                                        siseusa = True
                                k+=1

                            #SI NO SE USA DEBO ELIMINAR ESA ETIQUETA OBSOLETA Y CAMBIAR EL GOTO
                            if not siseusa:
                                linea = bloque.getInstrucciones()[i].getFila()
                                antes = bloque.getInstrucciones()[i].getCodigoAnterior()
                                actual = bloque.getInstrucciones()[i].getC3D()
                                #CAMBIAMOS LA ETIQUETA
                                bloque.getInstrucciones()[posicionGoto1].setEtiqueta(etiquetaGoto2)
                                bloque.getInstrucciones().pop(posicionObsoleta)#PARA ELIMINAR LA ETIQUETA OBSOLETA
                                self.reglas.append(Optimizacion("Mirilla", "Regla 4", "Se encontro una Etiqueta redundante", antes, actual, linea, self.iteracion))
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
                                    if posterior < len(bloque.getInstrucciones()):
                                        if bloque.getInstrucciones()[posterior].getTipo()== TipoInstruccion.GOTO:
                                            segundogoto = bloque.getInstrucciones()[posterior].getEtiqueta()
                                            secumple = True
                                            #ELIMINO LA ETIQUETA PARA QUE NO HALLA CLAVO CON GOLANG
                                            bloque.getInstrucciones().pop(j)
                                            j+= -1
                                            break
                            j+=1
                        if secumple:
                            bloque.getInstrucciones()[posprimergoto].setGoto(segundogoto)
                            linea = bloque.getInstrucciones()[posprimergoto].getFila()
                            self.reglas.append(Optimizacion("Mirilla", "Regla 5", "Se encontro una If con Etiqueta redundante", bloque.getInstrucciones()[posprimergoto].getCodigoAnterior(), bloque.getInstrucciones()[posprimergoto].getC3D(), linea, self.iteracion))
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
                                if bloque.getInstrucciones()[i].getOperador()=="+" or bloque.getInstrucciones()[i].getOperador()=="-":
                                    if bloque.getInstrucciones()[i].getOperador2() == 0:
                                        anterior = bloque.getInstrucciones()[i].getCodigoAnterior()
                                        linea = bloque.getInstrucciones()[i].getFila()
                                        self.reglas.append(Optimizacion("Mirilla", "Regla 6", "Se encontró suma/resta con cero", anterior, "Se elimina", linea, self.iteracion))
                                        bloque.getInstrucciones().pop(i)
                                        i = i - 1;
                                elif bloque.getInstrucciones()[i].getOperador()=="*" or bloque.getInstrucciones()[i].getOperador()=="/":
                                    if bloque.getInstrucciones()[i].getOperador2() == 1:
                                        anterior = bloque.getInstrucciones()[i].getCodigoAnterior()
                                        linea = bloque.getInstrucciones()[i].getFila()
                                        self.reglas.append(Optimizacion("Mirilla", "Regla 6", "Se encontró mult/div con cero", anterior, "Se elimina", linea, self.iteracion))
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
                                        self.reglas.append(Optimizacion("Mirilla", "Regla 7", "Se encontró suma/resta con cero", anterior, nuevo, linea, self.iteracion))
                                elif bloque.getInstrucciones()[i].getOperador()=="*" or bloque.getInstrucciones()[i].getOperador()=="/":
                                    if bloque.getInstrucciones()[i].getOperador2() == 1:
                                        anterior = bloque.getInstrucciones()[i].getCodigoAnterior()
                                        linea = bloque.getInstrucciones()[i].getFila()
                                        bloque.getInstrucciones()[i].setOperador2("")
                                        bloque.getInstrucciones()[i].setOperador("")
                                        bloque.getInstrucciones()[i].setTipo(TipoInstruccion.ASIGNACIONSIMPLE)
                                        nuevo = bloque.getInstrucciones()[i].getC3D()
                                        self.reglas.append(Optimizacion("Mirilla", "Regla 7", "Se encontró mult/div con cero", anterior, nuevo, linea, self.iteracion))
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
                                        self.reglas.append(Optimizacion("Mirilla", "Regla 8", "Se encontró multiplicacion de dos", anterior, nuevo, linea, self.iteracion))
                                    if bloque.getInstrucciones()[i].getOperador2() == 0:
                                        anterior = bloque.getInstrucciones()[i].getCodigoAnterior()
                                        linea = bloque.getInstrucciones()[i].getFila()
                                        bloque.getInstrucciones()[i].setOperador1(0)
                                        bloque.getInstrucciones()[i].setOperador2("")
                                        bloque.getInstrucciones()[i].setOperador("")
                                        bloque.getInstrucciones()[i].setTipo(TipoInstruccion.ASIGNACIONSIMPLE)
                                        nuevo = bloque.getInstrucciones()[i].getC3D()
                                        self.reglas.append(Optimizacion("Mirilla", "Regla 8", "Se encontró multiplicacion de cero", anterior, nuevo, linea, self.iteracion))
                                elif bloque.getInstrucciones()[i].getOperador()=="/":
                                    if bloque.getInstrucciones()[i].getOperador1() == 0:
                                        anterior = bloque.getInstrucciones()[i].getCodigoAnterior()
                                        linea = bloque.getInstrucciones()[i].getFila()
                                        bloque.getInstrucciones()[i].setOperador1(0)
                                        bloque.getInstrucciones()[i].setOperador2("")
                                        bloque.getInstrucciones()[i].setOperador("")
                                        bloque.getInstrucciones()[i].setTipo(TipoInstruccion.ASIGNACIONSIMPLE)
                                        nuevo = bloque.getInstrucciones()[i].getC3D()
                                        self.reglas.append(Optimizacion("Mirilla", "Regla 8", "Se encontró division con cero", anterior, nuevo, linea, self.iteracion))
                        i+=1

    def CambiarCondicion(self, condicion):
        if condicion == "==":
            return "!="
        if condicion == "!=":
            return "=="
        if condicion == "<=":
            return ">"
        if condicion == ">=":
            return "<"
        if condicion == "<":
            return ">="
        if condicion == ">":
            return "<="

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
            cadena += str(item.getIteracion())
            cadena += "</td>"
            cadena += "</tr>"
        cadena +="</table>"
        return cadena   