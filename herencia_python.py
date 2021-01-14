class Person:
  #creamos una clase general de persona e inicializamos sus atributos
	def __init__(self, firstName, lastName, idNumber):
		self.firstName = firstName
		self.lastName = lastName
		self.idNumber = idNumber
  #definimos un metodo que pueda permitirnos visualizar de forma mas amigable los parametros pasados al constructor cuando se instancie el objeto  
	def printPerson(self):
		print("Name:", self.lastName + ",", self.firstName)
		print("ID:", self.idNumber)


#creamos una clase estudiante y aplicamos el concepto de herencia para tomar los atributos que venian de la clase Person y los inicializamos y tambien agregamos el atributo nuevo (scores) que seran las calificaciones del estudiante(arreglo de enteros)
class Student(Person):
  #constructor que hereda atributos de Person
    def __init__(self, firstName, lastName, idNumber,scores):
        Person.__init__(self,  firstName, lastName, idNumber)
        #inicializamos el nuevo atributo scores(califiaciones)
        self.scores = scores
        
#metodo que permite calcular el promedio de calificaciones del estudiante y determina que letra de calificacion le corresponde
    def calculate(self):  
        promedio = sum(self.scores)/len(self.scores)
        if  90<=promedio<= 100:
          return "O"
        if  80<=promedio<= 90:
          return "E"
        if  70<=promedio<= 80:
          return "A"
        if  55<=promedio<= 70:
          return "P"
        if  40<=promedio<= 55:
          return "D"
        if  promedio<40:
          return "T"


line = input().split()
firstName = line[0]
lastName = line[1]
idNum = line[2]
numScores = int(input())
#mapeamos las entradas de calificaciones a una lista de enteros
scores = list( map(int, input().split()) )

#creamos una instancia de la clase Student con sus respectivos parametros
s = Student(firstName, lastName, idNum, scores)

#hacemos el llamado a los dos metodos necesarios para el desarrollo del problema y mostramos la salida en consola
s.printPerson()
print("Grade:", s.calculate())