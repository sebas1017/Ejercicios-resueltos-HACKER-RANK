import copy
import itertools
superior  =list()
inferior = list()
relojes=[]
valores_finales=[]

#aqui tomamos cada fila de la matriz como una lista y la iteramos de 3 en 3 para obtener las tripletas superiores e inferiores  de los 16 relojes de arena que resultan de la matriz 6*6 que indica el problema 
def trios_superior(lista,lista2):
  for k in range(len(lista)-2):
    superior.append( lista[k:k+3])
    inferior.append( lista2[k:k+3])  


#aqui tomamos las filas necesarias para obtener los valores medios de cada reloj de arena y eliminamos los elementos innecesarios
def filtrado_valores_medios(arreglo):
  for k in range(len(arreglo)):
    arreglo[k].pop(0)
    arreglo[k].pop(-1)


#aqui leemos la matriz por consola
matriz = []
for _ in range(6):
    matriz.append(list(map(int, input().rstrip().split())))

#aqui tomaos las filas necesarias de donde se tomaran los valores superiores
valores_superiores = matriz[:4]

#aqui tomamos las filas necesarias de donde se tomaran los valores inferiores
valores_inferiores = matriz[2:]


#aqui tomamos las filas necesarias de donde se tomaran los valores medios
valores_medios =copy.deepcopy(matriz[1:5])

#aqui llamamos la funcion para hacer el filtrado de los valores medios 
filtrado_valores_medios(valores_medios)

#aqui armamos los trios de valores superiores e inferiores de cada fila  que conformaran nuestros 16 relojes de arena de nuestra matriz 6*6
for k in range(len(valores_superiores)):
  trios_superior(valores_superiores[k],valores_inferiores[k])



list2d = valores_medios

#aqui comprimimos los valores de cada reloj (valores inferiores,superiores) en una sublista que hara parte  de merged donde cada sublista(16 en total) sera el reloj de arena para un total de 16 relojes
merged = list(itertools.chain(*list2d))  
for valor in range(len(superior)):
  superior[valor].append(inferior[valor])
  relojes.append(superior[valor][:3])
  for k in range(len(superior[valor][3])):
    element = superior[valor][3]
    relojes[valor].append(element[k])
  relojes[valor].append(merged[valor])  
  
#una vez teniendo una lista de listas donde cada lista es un reloj de arena con sus valores superiores medios e inferiores se procede a recorrer cada sublista sumando sus elementos y agregando esta sumatoria en una nueva lista para luego obtener el maximo valor y poder dar la salida de el valor de la maxima sumatoria de uno de los 16 relojes  
for h in range(len(relojes)):
  valores_finales.append(sum(relojes[h]))
print(max(valores_finales))







  
  



      
    
        


    
    

  
    
    
    

