from TablaSimbolo.NodoArbol import NodoArbol
from graphviz import Source
from graphviz import Graph
import pybase64 as base64
import os
os.environ ['PATH'] += os.pathsep + 'C:\Program Files\Graphviz\bin'

class GraficarNodos:
    
    def __init__(self):
        self.id_n = 1
        self.chart_data = Graph()
        
    def recorrerDot(self, nodo):
        if isinstance(nodo, str):
            return ""
        if isinstance(nodo.valor, NodoArbol):
            return ""
        concatena = ""
        if nodo.id == 0:
            nodo.id = self.id_n
            self.id_n = self.id_n + 1
        concatena += str(nodo.id) + ' [label="'+nodo.valor+'", fillcolor="LightBlue", style ="filled", shape="box"]; \n'
        for hijo in nodo.hijos:
            concatena += str(nodo.id) +'->'+ str(self.id_n) +";" + "\n";
            concatena += self.recorrerDot(hijo);
        return concatena;


    def recorrerDot2(self, nodo):
        if nodo.id == 0:
            nodo.id = self.id_n
            self.id_n = self.id_n + 1
        self.chart_data.node(str(nodo.id), str(nodo.valor))
        for hijo in nodo.hijos:
            self.chart_data.edge(str(nodo.id), str(self.id_n))
            self.recorrerDot2(hijo);
        return 

    def GenerarDot(self, nodo):
        self.recorrerDot2(nodo)
        chart_output = self.chart_data.pipe(format='png')
        chart_output = base64.b64encode(chart_output).decode('utf-8')   
        return chart_output

    def GenerarDotG(self, nodo):
        cadena = "digraph lista{ rankdir=TB;node[shape = box, style = filled, color = white]; \n"
        cadena += str(self.recorrerDot(nodo)) +"}"
        return cadena