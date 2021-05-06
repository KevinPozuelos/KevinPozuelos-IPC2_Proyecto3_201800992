from Funnel import funneling
import re

funnel = funneling()

class ParserXML(object):

    def eDatos(self, lDatos):
        Dato=[]
        Evento=[] 
        Indice=1
        MensajeE=""
        lineas= lDatos
        cont=1
    try:    
        for linea in lineas:
            if "<EVENTO>" in linea:
                Evento.append(str(Indice))
                Indice+= 1
                cont= 1
            elif "<EVENTOS>" not in linea and "</EVENTOS>" not in linea:
                linea= re.sub("\t","",linea) 
                linea= re.sub("<","",linea)
                linea= re.sub(">","",linea)
                linea= re.sub('"',"",linea)
                
                if cont == 1:
                    fecha = re.search(r'[0-9|/]+', linea) #expresion regular para las fechas
                    if fecha != None:
                        Evento.append(fecha.group())
                    else:
                        print("FECHA INVALIDA")

                elif cont == 2:
                    report = re.search(r'([\w\.]+)@([\w\.]+)(\.[\w\.]+)', linea) #Expresion regular para los Correos que notifican error
                    if report != None:
                        Evento.append(report.group())
                    else:
                        print("FORMATO DE CORREO INVALIDO")
                
                elif cont == 3:
                    afectado = re.findall(r'([\w\.]+@[\w\.]+\.[\w\.]+)', linea) #Expresion regular para los correos que presentan el problema
                    if afectado != None:
                        Evento.append(afectado)
                        else:
                            print("NO SE AGREGO CORREO DE AFECTADO")

                elif cont == 4:
                    CodigoE = re.search(r'([0-9]{5,5})', linea) #Expresion regular para el codigo del error
                    mError = re.search(r'(-.+(\w)+)', linea)#Expresion regular para la descripcion del error
                    if CodigoE != None:
                        Evento.append(CodigoE.group())
                    else:
                        print("NO SE AGREGO CODIGO")
                    if mError != None:
                        MensajeE += mError.group()
                    else:
                        print("No agrega descripcion del error")

                elif cont > 4:
                    mError2 = re.search(r'(\w.+)+', linea)#Expresion regular de las lineas de la descripcion de errores
                    if mError2 != None:
                        MensajeE += mError2.group()
                    else:
                        print("no agrega descripcion erroor")
                
                cont+=1
            elif "</EVENTO>" in linea:
                Evento.append(MensajeE)
                Dato.append(Evento)
                MensajeE = ''
                Evento = []
        funnel.Ordenar(Dato)
    except FileNotFoundError:
        print("NO SE ENCONTRO ARCHIVO")

                        