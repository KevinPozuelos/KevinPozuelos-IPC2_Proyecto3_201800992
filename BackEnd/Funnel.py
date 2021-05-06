from Estadistica import Estadistica
salida = Estadistica()
class funneling(object):

    def Ordenar(self, listaD):
        
        fecha= []
        DifFecha= []
        DatoFecha= []
        comparar = ""
        pos = 1
        sig = 1
        listaFecha= []

        Registro= []     
        tReporte= 0 
        cRegistro= []     
        afectado= []      
        DatoF=[]  
        rComparar= ""
        cComparar= ""

##################################################################
        for eFecha in listD:
            aux = False
            comparar = eFecha[1]

            if listaFecha != []:
                for fecha in listaFecha:
                    if comparar == fecha:
                        aux = True
                        break
                    
                    
            if aux == False:
                for i in listaD:
                    if pos == len(listaD):
                        break

                    elif listaD[pos][1] == comparar:
                        fecha.append(listaD[pos])
                    pos+= 1

                if fecha == []:
                    DifFecha.append(eFecha)
                else:
                    fecha.insert(0, eFecha)
                    DatoFecha.append(fecha)
                    fecha = []
                    listaFecha.append(comparar)
            sig+= 1
            pos = sig
####################################################################        
        for lFecha in DatoFecha:
            print("Fecha: "+str(lFecha[0][1]))
            for dato in lFecha:
                print(dato)
####################################################################
        for dato in DifFecha:
            print(dato)
####################################################################            
        for lFecha in DatoF:
            for lista in lFecha:
                bRep = False
                bCod = False
                rComparar= lista[2]
                cComparar= lista[4]

                if rComparar= ![]:
                    aux = 0
                    for i in rComparar:
                        if aux == len(cRegistro):
                            break
                        if cComparar == cRegistro[aux]:
                            cRegistro[aux+1] = cRegistro[aux+1]+1
                            bCod = True
                            break
                        aux+= 2
                
                if bRep == False:
                    Registro.append(rComparar)
                    Registro.append(1)
                    tReporte+= 1
                
                if bCod == False:
                    cRegistro.append(cComparar)
                    cRegistro.append(1)
                
                afectado.append(lista[3])

            DatoF.append(lista[1])
            DatoF.append(tReporte)
            DatoF.append(Registro)
            DatoF.append(cRegistro)  
            DatoF.append(afectado)  
 

        salida.XMLsalida(DatoF,DifFecha)
        
        