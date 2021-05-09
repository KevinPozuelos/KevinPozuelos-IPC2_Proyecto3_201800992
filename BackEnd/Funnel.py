from Estadistica import Estadistica

Salida= Estadistica()

class Funnling:
    
    def FunellingData(self, datafunnel):
        
        date=[]
        dateDif= []
        dataF= []   
        auxdate= ""
        pos= 1
        sig= 1
        arrayDate=[]    
        DateArray=[]

        
        for parsedate in datafunnel: 
            auxE=False


            if arrayDate != []:
                for DateF in arrayDate:
                    if auxdate == DateF:
                        auxE=True
                        break

            
            if auxE == False:
                for i in datafunnel:
                    if pos == len(datafunnel):
                        break

                        #pos. fecha de un dato
                    elif datafunnel[pos][1] == auxdate:
                        date.append(datafunnel[pos])

                    pos+=1
                
                if date == []:
                    dateDif.append(parsedate) 
                
                else:
                    date.insert(0,parsedate)
                    dataF.append(date)
                    date=[]
                    arrayDate.append(auxdate)

            sig+=1
            pos=sig
            
        print("---------OUT-CONSOLE---------")
        print("---------Salida: Fechas---------")
        print("----Fechas Iguales----")
        for datadate in dataF:
            print("Fecha: "+ str(datadate[0][1]))
            for line in datadate:
                print(line)

        print("\n----------------------------------------------------")
        print("----Fechas distintas----")
        for line in dateDif:
            print(line)
            print("<<<><<><<<<<<>>>>>><>><>>>")


        


        
        print("---------------------------------")
        print("-----TEST FUNNEL------")
        registroReportes=[]     
        contReportes=0
        Nreg=[]
        implicados=[]     
        FunnelDate=[]
        auxReportE=""
        auxCode=""

        
        

        
        for arrayDate2 in dataF:
            for arrayData in arrayDate2:
                auxrepo=False
                auxcode2=False
                auxReportE= arrayData[2]
                auxCode= arrayData[4]

                if registroReportes != []:
                    verificador=0
                    for i in registroReportes:
                        if verificador == len(registroReportes):
                            break
                        if auxReportE == registroReportes[verificador]:
                            ReportadorRegistrado[verificador+1]=registroReportes[verificador+1]+1
                            auxrepo=True
                            contReportes+=1
                            break

                        verificador+=2
                
                if Nreg != []:
                    verificador=0
                    for i in Nreg:
                        if verificador == len(Nreg):
                            break
                        if auxCode == Nreg[verificador]:
                            Nreg[verificador+1]=Nreg[verificador+1]+1
                            auxcode2=True
                            break

                        verificador+=2
            
                if auxrepo == False:
                    registroReportes.append(auxReportE)
                    registroReportes.append(1)
                    contReportes+=1

                if auxcode2 == False:
                    Nreg.append(auxCode)
                    Nreg.append(1)

                implicados.append(arrayData[3]) 
            
            FunnelDate.append(arrayData[1])   
            FunnelDate.append(contReportes)   
            FunnelDate.append(registroReportes) 
            FunnelDate.append(Nreg)         
            FunnelDate.append(implicados)   
            

            
            print("------------------------")
            print(arrayData[1])
            print(contReportes)
            print(registroReportes)
            print(Nreg)
            print("--afectados--")
            for d in implicados:
                print(d)

            
            registroReportes=[]
            Nreg=[]
            implicados=[]
            contReportes=0
        
        
        print("------------------------")
        print("--DISTINTA FECHA----")
        for dato in dateDif:
            print(dato[1])
            print(1)
            print(dato[2])
            print(dato[4])
            print("--afectados--")
            print(dato[3])
            print("-----------------")

        print(">>>>>>>>>>>FINALIZO FILTRACION<<<<<<<<<<")
        Salida.Parsear(FunnelDate,dateDif)
        DateArray.append(FunnelDate)
        DateArray.append(dateDif)
        return DateArray