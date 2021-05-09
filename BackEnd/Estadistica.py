class Estadistica:
    def Parsear(self, ListaDato,ListaDif):
        
        CantFecha=0   
        sig=0
        for i in range(len(ListaDato)):
            if sig == len(ListaDato):
                break
            CantFecha+=1
            sig+=5

        salida=open("Estadistica.xml","w")    
        salida.write("<ESTADISTICAS>\n")

        PosF=0
        for xml in range(CantFecha):
            salida.write("\t<ESTADISTICA>\n")
            salida.write("\t\t<FECHA>" + ListaDato[PosF] + "</FECHA>\n")
            salida.write("\t\t<TOTAL_MENSAJES>" + str(ListaDato[PosF+1]) + "</TOTAL_MENSAJES>\n")
            salida.write("\t\t\t<REPORTADO_POR>\n")
            
            temp=ListaDato[PosF+2]
            PosR=0
            for j in range(len(temp)):
                if PosR == len(temp):
                    break
                salida.write("\t\t\t\t<USUARIO>\n")
                salida.write("\t\t\t\t\t<EMAIL>" + temp[PosR] + "</EMAIL>\n")
                salida.write("\t\t\t\t\t<MENSAJES_REPORTADOS>"+ str(temp[PosR+1]) + "</MENSAJES_REPORTADOS>\n")
                salida.write("\t\t\t\t</USUARIO>\n")
                PosR+=2
            salida.write("\t\t\t</REPORTADO_POR>\n")
            salida.write("\t\t\t<AFECTADOS>\n")
            
            aux2=ListaDato[PosF+4]
            
            for afectado in aux2:
                for objeto in afectado:
                    if len(objeto)==1:
                        salida.write("\t\t\t\t<AFECTADO>" + afectado +"</AFECTADO>\n")
                        break
                    else:
                        salida.write("\t\t\t\t<AFECTADO>" + objeto + "</AFECTADO>\n")
            salida.write("\t\t\t</AFECTADOS>\n")
            salida.write("\t\t\t<ERRORES>\n")
           
            auxE=ListaDato[PosF+3]
            PosD=0
            for dato in auxE:
                if PosD == len(auxE):
                    break
                salida.write("\t\t\t\t<ERROR>\n")
                salida.write("\t\t\t\t\t<CODIGO>" + str(auxE[PosD]) + "</CODIGO>\n")
                salida.write("\t\t\t\t\t<MENSAJES_GENERADOS>" + str(auxE[PosD+1]) + "</MENSAJES_GENERADOS>\n")
                PosD+=2
                salida.write("\t\t\t\t</ERRROR>\n")
            salida.write("\t\t\t</ERRORES>\n")
            salida.write("\t</ESTADISTICA>\n")
            PosF+=5


        for date in ListaDif: 
            salida.write("\t<ESTADISTICA>\n")
            salida.write("\t\t<FECHA>" + date[1] + "</FECHA>\n")        
            salida.write("\t\t<TOTAL_MENSAJES>1</TOTAL_MENSAJES>\n")
            salida.write("\t\t\t<REPORTADO_POR>\n")
            salida.write("\t\t\t\t<USUARIO>\n")
            salida.write("\t\t\t\t\t<EMAIL>" + date[2] + "</EMAIL>\n")
            salida.write("\t\t\t\t\t<MENSAJES_REPORTADOS>1</MENSAJES_REPORTADOS>\n")
            salida.write("\t\t\t\t</USUARIO>\n")
            salida.write("\t\t\t</REPORTADO_POR>\n")
            salida.write("\t\t\t<AFECTADOS>\n")
            aux2=date[3]
            for afectado in aux2:
                for objeto in afectado:
                    if len(objeto)==1:
                        salida.write("\t\t\t\t<AFECTADO>" + afectado + "</AFECTADO>\n")
                        break
                    else:
                        salida.write("\t\t\t\t<AFECTADO>" + objeto + "</AFECTADO>\n")
            salida.write("\t\t\t</AFECTADOS>\n")
            salida.write("\t\t\t<ERRORES>\n")
            salida.write("\t\t\t\t<ERROR>\n")
            salida.write("\t\t\t\t\t<CODIGO>" + date[4] + "</CODIGO>\n")
            salida.write("\t\t\t\t\t<MENSAJES_GENERADOS>1</MENSAJES_GENERADOS>\n")
            salida.write("\t\t\t\t</ERROR>\n")
            salida.write("\t\t\t</ERRORES>\n")
            salida.write("\t</ESTADISTICA>\n")

        salida.write("</ESTADISTICAS>")
        salida.close()
        print("\n>>>Estadistica.xml Creado<<<")