#!/bin/python3
import itertools
numeros=[]
#aqui convertimos de decimal a binario y agregamos este numero en la lista numeros
def binario(n):
  if n == 1:
    numeros.append(n)
    return n
  else:
    residuo = n%2
    cociente = int(n/2)
    if cociente ==1:
      numeros.append(residuo)
      numeros.append(cociente)
      return True
    if  cociente>1:
      numeros.append(residuo)
      binario(cociente)
    else:
      return True



if __name__ == '__main__':
    numero = int(input())
    binario(numero)
    #luego de tener la lista numeros con el numero convertido a binario invertimos el orden ya que en la division de conversion empezamos desde el ultimo cociente , y tomando los residuos de las divisiones de forma ascendente
    numeros.reverse()
    #utilizamos agrupacion para saber cual es la maxima frecuencia de repeticion de secucencia de numeros sucesivos en este caso ( 0 o 1 )

    z = [(x[0], len(list(x[1]))) for x in itertools.groupby(numeros)]
    nueva = []
    #esta agrupacion nos retorna una lista de tuplas con las repeticiones de secuencias de los valores 0 o 1 en una lista de tuplas pero no necesitamos las frecuencias del valor 0 ya que el problema solo nos pide la mayor frecuencia consecutiva de valor 1 por lo que la descartamos
    for j in range(len(z)):
      if 0 in z[j]:
        pass
      else:
        nueva.append(z[j])

    #aqui calculamos la maxima frecuencia de valores 1 repetidos en orden consecutivo y damos la salida     

    print(max(nueva, key=lambda x:x[1])[1])      
        
      
    






  
  



      
    
        


    
    

  
    
    
    

