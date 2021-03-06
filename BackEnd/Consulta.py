import os
class Consulta:

    def ConsultaCodigo(self, DateArray, busqueda):
        auxLista = DateArray
        Codigo = busqueda
        datos = []
        contenido=''
        DatoA = auxLista[0]
        DatosB = auxLista[1]
        sig = 0
        derecha = 3

        for i in range(len(DatoA)):
            if derecha >= len(DatoA):
                break
            codeSig = 0
            CodigoL = DatoA[derecha]
            for i  in range(len(CodigoL)):
                if codeSig == len(CodigoL):
                    break
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
                break
            auxdatos = DatosB[derecha]
            if auxdatos[4]==Codigo:
                datos.append(auxdatos[sig])
                datos.append("1")
            derecha +=1     
        if datos != []:
            grafico= open("graph.html","w")
            grafico.write("""<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Gráfico de barras"""+Codigo+"""</title>
 
    <style>
    .chart-wrap {
        --chart-width:420px;
        --grid-color:#aaa;
        --bar-color:#F16335;
        --bar-thickness:40px;
        --bar-rounded: 3px;
        --bar-spacing:10px;
 
        font-family:sans-serif;
        width:var(--chart-width);
    }
 
    .chart-wrap .title{
        font-weight:bold;
        padding:1.8em 0;
        text-align:center;
        white-space:nowrap;
    }
 
    /* cuando definimos el gráfico en horizontal, lo giramos 90 grados */
    .chart-wrap.horizontal .grid{
        transform:rotate(-90deg);
    }
 
    .chart-wrap.horizontal .bar::after{
        /* giramos las letras para horizontal*/
        transform: rotate(45deg);
        padding-top:0px;
        display: block;
    }
 
    .chart-wrap .grid{
        margin-left:50px;
        position:relative;
        padding:5px 0 5px 0;
        height:100%;
        width:100%;
        border-left:2px solid var(--grid-color);
    }
 
    /* posicionamos el % del gráfico*/
    .chart-wrap .grid::before{
        font-size:0.8em;
        font-weight:bold;
        content:'0%';
        position:absolute;
        left:-0.5em;
        top:-1.5em;
    }
    .chart-wrap .grid::after{
        font-size:0.8em;
        font-weight:bold;
        content:'100%';
        position:absolute;
        right:-1.5em;
        top:-1.5em;
    }
 
    /* giramos las valores de 0% y 100% para horizontal */
    .chart-wrap.horizontal .grid::before, .chart-wrap.horizontal .grid::after {
        transform: rotate(90deg);
    }
 
    .chart-wrap .bar {
        width: var(--bar-value);
        height:var(--bar-thickness);
        margin:var(--bar-spacing) 0;
        background-color:var(--bar-color);
        border-radius:0 var(--bar-rounded) var(--bar-rounded) 0;
    }
 
    .chart-wrap .bar:hover{
        opacity:0.7;
    }
 
    .chart-wrap .bar::after{
        content:attr(data-name);
        margin-left:100%;
        padding:10px;
        display:inline-block;
        white-space:nowrap;
    }
 
    </style>
</head>
<body>
 
<div class="chart-wrap horizontal"> <!-- quitar el estilo "horizontal" para visualizar verticalmente -->
  <div class="title">ESTADISTICA</div>
 
  <div class="grid">""")
            
            siguiente=0
            for i in datos:
                if siguiente == len(datos):
                    break
                contenido+=("""<div class="bar" style="--bar-value:"""+ str((int(datos[siguiente+1])) ) +"%"+ """;" data-name="""+ datos[siguiente] + """ title="""+datos[siguiente]+ str((int(datos[siguiente+1])) )+"%"+"""></div>""")
                
                siguiente+=2
            grafico.write(contenido)
            grafico.write("""</div>
</div>
 
</body>
</html> """)
            os.startfile("graph.html")
            repuesta = "COMPLETADO"
            return repuesta
        else:
            repuesta="!! Codigo no existente !!"
            return repuesta
        