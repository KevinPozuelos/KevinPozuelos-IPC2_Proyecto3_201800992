
from bokeh.charts import Donut, show
import pandas as pd

class Consulta:
    def ConsultaCodigo(self, Lista, busqueda):
        auxLista = Lista
        Codigo = busqueda
        datos = []
        
        DatoA = auxLista[0]
        DatosB = auxLista[1]
        sig = 0
        derecha = 3

        for i in range(len(DatoA)):
            if derecha >= len(DatoA):
                return
            codeSig = 0
            CodigoL = DatoA[derecha]
            for i  in range(len(CodigoL)):
                if codeSig == len(CodigoL):
                    return
                if CodigoL[codeSig]==Codigo:
                    datos.append(DatoA[sig])
                    datos.append(str(CodigoL[codeSig+1]))
                codeSig +=2
            sig += 5
            derecha += 5
        sig = 1
        derecha = 1


        for j in range(len(DatosB)):
            if derecha ==len(DatosB):
                return
            auxdatos = DatosB[derecha]
            if auxdatos[4]==Codigo:
                datos.append(auxdatos[sig])
                datos.append("1")
            derecha +=1     
        

        if datos != []:
            siguiente = 0
            index = 1
            for i in datos:
                if siguiente == len(datos):
                    return
                graph = pd.Series(datos[i]), index = datos[i]
                pie_chart = Donut(graph)
            show(pie_chart)