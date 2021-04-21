import math
import random as rnd
import numpy as npm
import matplotlib.pyplot as plt

# ----------------------------------------------------------------------------------------------------
class Cromosoma(object):
    
    IDCromosoma=1
    #Atributos
    def __init__(self):         
        self.funcFitness=0
        self.funcObjetivo=0
        self.valorDecimal=0
        self.arrGenes=[]
    
    def calculoDatosCromosoma(self):
        """Se calcula el valor de cada cromosoma"""     
        cadena = "".join([ str(gen) for gen in self.arrGenes])  #Hace la conversion del arreglo a una cadena por ejemplo[1,0,1] a '101'
        self.valorDecimal = int(cadena, 2) #Se transofrma la cadena de genes en un valor en decimal
        self.funcObjetivo = round( ((self.valorDecimal / Dominio)**2) , 5) #Dominio se define en el cuerpo principal      

    def calculoFitness(self,sumaPoblacion): 
        """Dependiendo de la suma de la poblacion, se calcula el fitness de cada cromosoma"""
        self.funcFitness = self.funcObjetivo / sumaPoblacion

    def mutoGen(self):
        numRandom=rnd.randint(0,tCromo-1)
        if(self.arrGenes[numRandom]==0):
            self.arrGenes[numRandom]=1
        else:
            self.arrGenes[numRandom]=0

    def instancioGenes(self):
        for x in range(0,tCromo):
            self.arrGenes.append(rnd.randint(0, 1))
    
    def insertoGen(self,gen):
        """Se envia el gen a insertar en el arreglo del cromosoma"""
        self.arrGenes.append(gen)

    def datosCromosoma(self):
        cadena = "".join([ str(gen) for gen in self.arrGenes])
        print(f"Func Fitness: {self.funcFitness}, Valor decimal: {self.valorDecimal}, Func Objetivo: {self.funcObjetivo}, Genes {cadena}")
 # -----------------------------------------------------------------------------------------------------------     

class Poblacion(object):

    """Poblacion genetica del algoritmo"""
    IDPoblacion = 1
    
    #Metodo de clase
    def reseteoIDPoblacion():
        Poblacion.IDPoblacion=1

    #Metodos de instancia
    def __init__(self):
        if(Poblacion.IDPoblacion > cantCorridas):
            Poblacion.IDPoblacion = 1
            self.ID = Poblacion.IDPoblacion
            Poblacion.IDPoblacion +=1  
        else:
            self.ID = Poblacion.IDPoblacion
            Poblacion.IDPoblacion +=1       
        self.arrCromosomas=[]
        self.sumaPoblacion=0
        self.mediaPoblacionFO=0   
        
    def instancioCromosomas(self):
        for x in range(0,tPobla):
            cromosoma = Cromosoma() 
            cromosoma.instancioGenes()   
            self.arrCromosomas.append(cromosoma)

    def calculoSumaPobla(self):
        """Se calcula la suma de la poblacion a partir del valor de cada cromosoma"""
        for cromosoma in self.arrCromosomas:
            self.sumaPoblacion += cromosoma.funcObjetivo

    def calculoMediaFO(self):
        """Se calcula la media poblacional""" 
        self.mediaPoblacionFO = round( self.sumaPoblacion / len(self.arrCromosomas) ,5)

    def buscoMenorYMayorCromosoma(self):
        self.maxCromosoma=self.arrCromosomas[0] #Para poder tener como base el primer cromosoma y comparar el resto
        self.minCromosoma=self.arrCromosomas[0]
        for cromosoma in self.arrCromosomas:
            if (self.maxCromosoma.valorDecimal < cromosoma.valorDecimal):
                self.maxCromosoma = cromosoma
            if (self.minCromosoma.valorDecimal > cromosoma.valorDecimal):
                self.minCromosoma = cromosoma               

    def calculoDatosPoblacion(self):
        for cromosoma in self.arrCromosomas:
            cromosoma.calculoDatosCromosoma()
        self.calculoSumaPobla()
        for cromosoma in self.arrCromosomas:        
            cromosoma.calculoFitness(self.sumaPoblacion)
        self.calculoMediaFO()
        self.buscoMenorYMayorCromosoma()
    
    def datosPoblacion(self):      
        print(f"Poblacion ID: {self.ID}, media de la FO fue: {self.mediaPoblacionFO}")        
        """
        print("-------------------------------------------------")      
        for cromosoma in self.arrCromosomas:            
            cromosoma.datosCromosoma()
        print("-------------------------------------------------") 
        """           
        cadena1="".join([ str(gen) for gen in self.maxCromosoma.arrGenes])  #Hace el casteo de un arreglo de enteros a una cadena de los genes
        cadena2="".join([ str(gen) for gen in self.minCromosoma.arrGenes])
        print(f"El cromosoma {cadena1} fue el mas grande y su fitnnes es {self.maxCromosoma.funcFitness}")
        print(f"El cromosoma {cadena2} fue el mas chico y su fitnnes es {self.minCromosoma.funcFitness}")
        print("-----------------------------------------------------")
        
    def creoNuevaPoblacion(self,poblacionAnterior):
        paresPadres=self.aplicoSeleccionRuleta(poblacionAnterior)     #Devuevle los cromosomas seleccionados en la ruleta      
        self.aplicoOperadorCrossover(paresPadres) #A los cromosomas seleccionados se les aplica crossover
        #self.aplicoOperadorMutacion()  #Una vez aplicado el crossover, se les aplica la mutacion    

    def aplicoSeleccionRuleta(self,poblacionAnterior):
        ruleta=[0]
        valor=0     
        paresPadres=[]         
        for cromosoma in poblacionAnterior.arrCromosomas:       
            valor+=cromosoma.funcFitness
            ruleta.append(valor)                                        
        for i in range(int(tPobla/2)): #Se debe armar 5 pares de longitud 2, tengo que castearlo a entero pro que tira error
            pares=[]
            while ( len(pares) < 2 ): #Se debe armar el par, esto garantiza que siempre se forme
                numAleatorio = rnd.random()     
                for j in range(tPobla-1):  #Esto es ya que se debe recorrer toda la ruleta hasta encontrar el intervalo
                    if (numAleatorio >= ruleta[j] and numAleatorio <= ruleta[j+1]):
                        pares.append(poblacionAnterior.arrCromosomas[j])
            paresPadres.append(pares)  
        return paresPadres

    def aplicoOperadorCrossover(self,padres):      
        for i in range(0,int(tPobla/2)):
            padre=padres[i][0] #Padres viene de a pares
            madre=padres[i][1]
            if(rnd.random() <= probCrossover):     #Se aplica crossover si el numero generado es mayor a la prob.  
                hijo1=Cromosoma()
                hijo2=Cromosoma()
                posicionCorte=rnd.randint(0,tCromo)
                #Se instnacia los primeros N genes de cada padre hasta la posicion de corte en cada hijo
                for j in range(0,posicionCorte):
                    hijo1.insertoGen(padre.arrGenes[j])
                    hijo2.insertoGen(madre.arrGenes[j])
                #Posteriormente se intercambian los genes de cada padre en los hijos, luego de la posicion del corte
                for k in range(posicionCorte,tCromo):
                    hijo1.insertoGen(madre.arrGenes[k])
                    hijo2.insertoGen(padre.arrGenes[k])  
                #Luego una vez de aplicars el crossover se aplica la mutacion a los hijos             
                self.aplicoOperadorMutacion(hijo1)
                self.aplicoOperadorMutacion(hijo2)
                #Se guarda cada cromosoma en la nueva poblacion
                self.arrCromosomas.append(hijo1)
                self.arrCromosomas.append(hijo2)          
            else: #Si no se aplica, los padres vuelven a ser los hijos
                #Se aplica mutacion a los padres
                self.aplicoOperadorMutacion(padre)
                self.aplicoOperadorMutacion(madre)
                #Se guarda cada cromosoma en la nueva poblacion
                self.arrCromosomas.append(padre)
                self.arrCromosomas.append(madre)
            
    def aplicoOperadorMutacion(self,cromosoma):
        if(rnd.random()<= probMutacion):   
            cromosoma.mutoGen()
# -----------------------------------------------------------------------------------------       

class Generacion(object):
    
    #Atributos de instancia
    def __init__(self):    
        self.arrPoblaciones=[]

    #Metodos
    def creoGeneracion(self):
        """Si se ejecuta por primera vez, generara una poblacion, si no, a la ultima existente se le aplicara algun operador genetico"""
        poblacion=Poblacion()
        if(len(self.arrPoblaciones) == 0 ): #Por si es la poblacion inicial
            poblacion.instancioCromosomas()
            poblacion.calculoDatosPoblacion()           
        else:
            poblacion.creoNuevaPoblacion(self.arrPoblaciones[-1])   #Se crea la nueva poblacion a partir de la anterior       
            poblacion.calculoDatosPoblacion()
        self.arrPoblaciones.append(poblacion)

    def dibujoGrafica(self):
        arrPromedios = []
        arrMaximos = []
        arrMinimos = []

        for cro in self.arrPoblaciones:
            arrPromedios.append(cro.mediaPoblacionFO)
            arrMaximos.append(cro.maxCromosoma.funcObjetivo)
            arrMinimos.append(cro.minCromosoma.funcObjetivo)

        plt.plot( arrPromedios, color='r', label='Medias')
        plt.plot( arrMaximos, color='g', label='Maximos')
        plt.plot( arrMinimos, color='b', label='Minimos')
        
        # Se pone nombre a los ejes X e Y 
        cantPoblacion=len(self.arrPoblaciones)
        plt.title(f"Grafico con {cantPoblacion} corridas")
        plt.xlabel("Numero de población")
        plt.ylabel("Valor")
        plt.ylim(0, 1.25)
        # Se agrega la leyenda para poder diferenciar cada color
        plt.legend()

        plt.show()
        

    def datosGeneracion(self):
        for poblacion in self.arrPoblaciones:
            poblacion.datosPoblacion()             
# -----------------------------------------------------------------------------------------        

#Main
#cantCorridas=int(input("Ingrese la cantidad de corridas"))    
#tPobla=int(input("Ingrese el tamaño de la poblacion"))
#tCromo=int(input("Ingrese el tamaño del cromosoma"))
#Dominio=((2**tCromo) - 1)  #Dominio es una variable global
tCromo=30
tPobla=10
Corridas=[20,100,200]
probCrossover=0.75
probMutacion=0.05 
Dominio=((2**tCromo)-1)
generaciones=[]

for x in Corridas:
    global cantCorridas
    cantCorridas=x
    generacion=Generacion()
    for i in range(cantCorridas):        
        generacion.creoGeneracion()
    Poblacion.reseteoIDPoblacion() #Metodo de clase que vuelve el ID a 1
    generaciones.append(generacion)

#for generacion in generaciones:
#    generacion.datosGeneracion()

for generacion in generaciones:
    generacion.dibujoGrafica()
