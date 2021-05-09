import re
from Funnel import Funnling

funneldata=Funnling()

class RegexXML:

    def Parserxml(self, data):
        try:
            aidate=[]
            hashT= [] 
            index= 1
            msjE= ""
            archivo= data

            state= 1
            

            for part in archivo:
                if "<EVENTO>" in part:
                    hashT.append(str(index))
                    index+= 1
                    state= 1
                    auxVal= False
                elif "<EVENTOS>" not in part and "</EVENTO>" not in part  and "</EVENTOS>" not in part:
                    
                    part= re.sub("\t", "", part) 
                    part= re.sub("<" ,"", part)
                    part= re.sub(">", "", part)
                    part= re.sub('"', "", part)

                    if "Guatemala" in part:
                        scandate= re.search(r'[0-9|/]+', part)  #obtiene las fechas de (0-9)(0-9)/(0-9)(0-9)/(0-9)(0-9)
                        if scandate != None:
                            hashT.append(scandate.group())
                        else:
                            print("NO SE AGREGO FECHA")
                    

                    elif "Reportado por" in part:
                        scannreport=re.search(r'([\w\.]+)@([\w\.]+)(\.[\w\.]+)',part)   #Obtiene correo de quien reporta
                        if scannreport != None:
                            hashT.append(scannreport.group())
                        else:
                            print("NO SE AGREGO AL REPORTADOR")
                         
                        
                    elif "Usuarios afectados" in part:
                        scacafecct=re.findall(r'([\w\.]+@[\w\.]+\.[\w\.]+)', part)   #Obtiene Correos de los afectados
                        if scacafecct != None:
                            hashT.append(scacafecct)
                        else:
                            print("NO SE AGREGO AFECTADO")


                    elif "Error" in part:
                        scanerror= re.search(r'([0-9]{5,5})', part)   #Obtiene Numero de error
                        scanmsjerror= re.search(r'(-.+(\w)+)', part)   #Obtiene descripcion de error
                        if scanerror != None:
                            hashT.append(scanerror.group())
                        else:
                            print("NO HAY ERROR")

                        if scanmsjerror != None:
                            msjE+=scanmsjerror.group() + " "
                            auxVal = True
                            
                        else:
                            print("ERROR DESCONOCIDO NO SE AGREGA-")


                    elif auxVal==True:
                        scanmsjerror=re.search(r'(\w.+)+', part)   #Obtiene siguientes lineas de descripcion de error
                        if scanmsjerror != None:
                            msjE+=scanmsjerror.group()
                        else:
                            print("NO SE AGREGO ERROR DESCONOCIDO")
                    
                    auxVal=False

                elif "</EVENTO>" in part:
                    hashT.append(msjE)
                    aidate.append(hashT)
                    msjE=""
                    hashT=[]
                    

                    
                  
            return funneldata.FunellingData(aidate)

        except FileNotFoundError:
            print("\n--------NO SE ENCONTRO ARCHIVO----------\n")