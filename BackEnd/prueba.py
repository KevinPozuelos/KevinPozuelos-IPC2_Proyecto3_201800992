ArchivoXML=open("EJEMPLO.xml","w")
ArchivoXML.write("<ESTADISTICAS>\n")

nombre="samuel"
fecha="22/10/1997"
for i in range(3):
    ArchivoXML.write("\t<ESTADISTICA>\n")
    ArchivoXML.write("\t\t<FECHA>"+fecha+"</FECHA>\n")
    ArchivoXML.write("\t\t<REPORTADO_POR>"+nombre+"</REPORTADO_POR>\n")
    ArchivoXML.write("\t</ESTADISTICA>\n")

ArchivoXML.write("</ESTADISTICAS>")
ArchivoXML.close()