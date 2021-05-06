class Estadistica(object):
    ####################Clase destinada a la escritura del archivo de salida de estadisticas en formato XML####################
    def XMLsalida(self, DatoF, DatoDif):
        nFechas = 0 
        sig = 0 
        for i in range(len(DatoF)):
            if sig == len(DatoFa):
                break
            nFechas += 1
            sig+= 5
        salida = open("Estadisticas.xml", "w")
        salida.write("<ESTADISTICAS>\n")

        posF = 0
        for r in range(nFechas):
            salida.write("\t<ESTADISTICA>\n")
            salida.write("\t\t<FECHA>" + DatoF[posF] + "</FECHA>\n")
            salida.write("\t\t<TOTAL_MENSAJES>" + str(DatoF[posF+1])) + "</TOTAL_MENSAJES>\n")
            salida.write("\t\t\t<REPORTADO_POR>\n")
            auxreport = DatoF[posF+2]
            posR
            for j in range(len(auxreport)):
                if posR == len(auxreport):
                    break
                salida.write("\t\t\t\t<USUARIO>\n")
                salida.write("\t\t\t\t\t<MENSAJES_REPORTADOS>" + str(auxreport[posR+1]) + "</MENSAJES_REPORTADOS>\n")
                posR+= 2
            salida.write("\t\t\t</REPORTADO_POR>\n")
            salida.write("\t\t\t<AFECTADOS>\n")
            
            auxA = DatoF[posF+4]

            for a in auxA:
                for element in a:
                    if len(element) == 1:
                        salida.write("\t\t\t\t<AFECTADO>" + a + "</AFECTADO>\n")
                        break
                    else:
                        salida.write("\t\t\t\t<AFECTADO>" + element + "</AFECTADO>\n")
            salida.write("\t\t\t</AFECTADOS>\n")
            salida.write("\t\t\t<ERRORES>\n")

            auxE = DatoF[posF+3]
            posE
            for dato in auxR:
                if posE == len(auxR):
                    break
                salida.write("\t\t\t\t<ERROR>\n")
                salida.write("\t\t\t\t\t<CODIGO>" + str(auxR[PosE]) + "</CODIGO>\n")
                salida.write("\t\t\t\t\t<MENSAJES_GENERADOS>"+str(auxE[posE+1])+"</MENSAJES_GENERADOS>\n")
                posE+= 2
                salida.write("\t\t\t\t</ERRROR>\n")
            salida.write("\t\t\t</ERRORES>\n")
            salida.write("\t</ESTADISTICA>\n")
            posF+= 5
        
        for fechaDif in DatoDif:
            salida.write("\t<ESTADISTICA>\n")
            salida.write("\t\t<FECHA>"+fechaDif[1]+"</FECHA>\n")
            salida.write("\t\t<TOTAL_MENSAJES>1</TOTAL_MENSAJES>\n")
            salida.write("\t\t\t<REPORTADO_POR>\n")
            salida.write("\t\t\t\t<USUARIO>\n")
            salida.write("\t\t\t\t\t<EMAIL>"+fechaDif[2]+"</EMAIL>\n")
            salida.write("\t\t\t\t\t<MENSAJES_REPORTADOS>1</MENSAJES_REPORTADOS>\n")
            salida.write("\t\t\t\t</USUARIO>\n")
            salida.write("\t\t\t</REPORTADO_POR>\n")
            salida.write("\t\t\t<AFECTADOS>\n")
            tempA = fechaDif[3]
            for afectado in tempA:
                for element in afectado:
                    if len(elemento) == 1:
                        salida.write("\t\t\t\t<AFECTADO>" + afectado + "</AFECTADO>\n")
                        break
                    else:
                        salida.write("\t\t\t\t<AFECTADO>" + elemento + "</AFECTADO>\n")
            salida.write("\t\t\t</AFECTADOS>\n")
            salida.write("\t\t\t<ERRORES>\n")
            salida.write("\t\t\t\t<ERROR>\n")
            salida.write("\t\t\t\t\t<CODIGO>" + fechaDif[4] + "</CODIGO>\n")
            salida.write("\t\t\t\t\t<MENSAJES_GENERADOS>1</MENSAJES_GENERADOS>\n")
            salida.write("\t\t\t\t</ERROR>\n")
            salida.write("\t\t\t</ERRORES>\n")
            salida.write("\t</ESTADISTICA>\n")  
        salida.write("</ESTADISTICAS>")
        salida.close
        print("\narchivo Estadistica.XML creado<---------")