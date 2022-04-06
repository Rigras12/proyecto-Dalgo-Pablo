"""
4,3
portales={
            4: {3:(1,3),1:(3,2),2:(2,1)},
            3:  {1:(1,2)}
}
energia={1:2,2:1,3:3,4:0}
"""
"""
5,3
portales={
    3:{3:(1,3)},
    5:{2:(3,1),1:(3,2)}

}
energia={1:5,2:17,3:8,4:1,5:4}
"""
"""
6,3
portales={
    3:{3:(1,3)},
    5:{2:(3,1),1:(3,2)}
}
energia={
    1:5,2:17,3:8,4:1,5:4,6:2
}
"""


portales={  5:{4:[(2,2)],2:[(4,4),(3,3)]},
            4:{2:[(3,5),(1,2)]}
}
energia={1:3,2:2,3:3,4:7,5:5}

def maximo_energia(energia):
    maximo=-1
    for i in energia:
        if energia[i]>maximo:
            maximo=energia[i]
    return maximo+1
def torres(i:int,j:int ,portales:dict ,energia:dict,maximo:int)->int:
    minimo=maximo
    eficiencia=0
    if i==1: 
        eficiencia_base=abs(j-1)*energia[i]
        return eficiencia_base
    elif i not in portales:
        return maximo
    else: 
        for j_portal in portales[i]:
            for portales_cuarto in portales[i][j_portal]:
                coordenadas=portales_cuarto
                eficiencia=abs(j-j_portal)*energia[i]
                valor=torres(coordenadas[0],coordenadas[1],portales,energia,maximo)
                if valor==maximo:
                    eficiencia=maximo
                else:
                    eficiencia+=valor

                if eficiencia<minimo:
                    minimo=eficiencia
            
        return minimo



            
        
maximo=maximo_energia(energia)*5*5
xd=torres(5,5,portales,energia,maximo)   
if maximo==xd:
    print("No existe")
else:
    print(xd)