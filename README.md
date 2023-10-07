# sobreviviendo_a_la_progrmacion_4


# 1.Dado la figura de la imagen, desarrolle:

![image](https://github.com/EmpanadasCONGuaro/sobreviviendo_a_la_progrmacion_4/assets/142174506/e8528ef1-3b1a-4b6d-8b76-876eabe24ec1)
 - Una función matemática para calcular el volumen y el área superficial.
 - Cree dos funciones en python para calcular los valores antes establecidos, al ingresar por teclado r1, r2 y h
 - Revise como utilizar el valor de pi usando import math y math.pi



```pseudocode
import math
p = math.pi #defini la variable pi, importante para todos los calculos

def CalcularVolumen(r1:float, r2:float, h:float) -> float:
  volumen=((4/3*p*(r1**3))+(1/3*p*h*(r2**2)))    
  return volumen

def CalcularAreaSuperficial(r1:float, r2:float, h:float) ->float:
  AreaSuperficial=((4*p*(r1**2))+(p*r2*(r2+g)))       
  return AreaSuperficial
                                                      

if __name__ == "__main__":
 
 r1: float = float(input("ingrese el valor de r1:"))
 r2: float = float(input("ingrese el valor de r2:"))
 h: float = float(input("ingrese el valor de h:"))
 g= ((r2**2)+(h**2))**0.5 #defini la variable g para poder hallar el area del cono, basicamente es la hipotenusa
 volumen=CalcularVolumen(r1,r2,h)
 print("el volumen es "+str(volumen)+" unidades cubicas")

 AreaSuperficial=CalcularAreaSuperficial(r1,r2,h)
 print("el area superficial es: "+str(AreaSuperficial)+" unidades cuadradas")
```


# 2. Dado la figura de la imagen, desarrolle:

![image](https://github.com/EmpanadasCONGuaro/sobreviviendo_a_la_progrmacion_4/assets/142174506/3402dd47-5f10-4841-b056-03e000102525)

 - Una función matemática para calcular el área y el perimetro.
 - Cree dos funciones en python para calcular los valores antes establecidos, al ingresar por teclado r, a y b.
 - Revise como utilizar el valor de pi usando import math y math.pi

```pseudocode
import math
p = math.pi #defini la variable pi, importante para todos los calculos

def CalcularArea(r:float, a:float, b:float) -> float:
  area=((a*b)+(2*(p*(r**2))))   
  return area

def CalcularPerimetro(r:float, a:float, b:float) ->float:
  perimetro=((2*(a+b))+(2*(2*p*r)))  
  return perimetro
                                                      

if __name__ == "__main__":
                                    
 r: float = float(input("ingrese el valor de r:"))        
 a: float = float(input("ingrese el valor de a:"))
 b: float = float(input("ingrese el valor de b:"))
 area=CalcularArea(r,a,b)
 print("el area es "+str(area)+" unidades cuadras")

 perimetro=CalcularPerimetro(r,a,b)
 print("el perimetro es: "+str(perimetro)+" unidades ")
```



# 3. Diseñe una función que calcule la cantidad de carne de aves en kilos si se tienen N gallinas, M gallos y K pollitos cada uno pesando 6 kilos, 7 kilos y 1 kilo respectivamente.

```pseudocode
def CalcularCantidadDeCarne(N:float, M:float, K:float) -> float:
  CantidadDeCarne=((N*6)+(M*7)+(K))  #defini la fumción para calcular la cantidad de carne
  return CantidadDeCarne

if __name__ == "__main__":
 N: float = float(input("ingrese el numero de gallinas:"))
 M: float = float(input("ingrese el numero gallos:"))
 K: float = float(input("ingrese el numero de pollitos:"))
 CantidadDeCarne=CalcularCantidadDeCarne(N,M,K)
 print("La cantidad de carne es "+str(CantidadDeCarne)+" kilogrmos")
```



# 4. Mi mamá me manda a comprar P panes a 300 cada uno, M bolsas de leche a 3300 cada una y H huevos a 350 cada uno. Hacer un programa que me diga las vueltas (o lo que quedo debiendo) cuando me da un billete de B pesos.

```pseudocode
def Vueltas(P:float, M:float, H:float, B:float) -> float:
  ValorDeVueltas=((B)-((P*300)+(M*3300)+(H*350))) #defini la fumción para calcular las vueltas
  return ValorDeVueltas


if __name__ == "__main__":
 B: float = float(input("ingrese el valor del billete:"))
 P: float = float(input("ingrese el numero de panes:"))
 M: float = float(input("ingrese el numero de bolsas de leche:"))
 H= float = float(input("ingrese el numero de huevos:"))
 ValorDeVueltas=Vueltas(P,M,H,B)

ValorDeVueltas2= (ValorDeVueltas*(-1))

if ValorDeVueltas == 0:
 print("sus vueltas son 0, por lo tanto estamos a paz y salvo")
elif ValorDeVueltas < 0:
 print("quedas debiendo "+str(ValorDeVueltas2))
elif ValorDeVueltas > 0:
 print("sus vueltas son" +str(ValorDeVueltas))

```



# 5. Haga un programa que utilice una función para calcular el valor de un préstamo C usando interés compuesto del i por n meses.

```pseudocode
def CalcularPrestamos(c:float, i:float, n:float) -> float:
  valortotaldelprestamo= (c*((1+i/100)**n))
  return valortotaldelprestamo

if __name__ == "__main__":
 c: float = float(input("Ingrese el valor del prestamo:"))
 i: float = float(input("Ingrese la tasa de intereses:"))
 n: float = float(input("Ingrese el tiempo es meses:"))
 valortotaldelprestamos= CalcularPrestamos(c,i,n)
 print("el valor final del prestamos es "+str(valortotaldelprestamos))
```



# 6. El número de contagiados de Covid-19 en el país de NuncaLandia se duplica cada día. Hacer un programa que diga el número total de personas que se han contagiado cuando pasen D días a partir de hoy, si el número de contagiados actuales es C.

```pseudocode
def CalcularContagios(C:float, D:float) -> float:
  NumeroDeContagios=(C*(2**D))
  return NumeroDeContagios

if __name__ == "__main__":
 C: float = float(input("Ingrese el número de contagios actuales:"))
 D: float = float(input("Ingrese el número de dias:"))
 NumeroDeContagios = CalcularContagios(C,D)
 print("el número de contadios después de "  + str(D) +  " dia(s) es de " + str(NumeroDeContagios))
```



# 7. Escriba un programa que pida 5 números reales y calcule las siguientes operaciones usando una función para cada una:
 - El promedio
 - La mediana
 - El promedio multiplicativo (multilplica todos y luego calcula la raíz de la cantidad de operandos)
 - Ordenar los números de forma ascendente
 - Ordenar los números de forma descendente
 - La potencia del mayor número elevado al menor número
 - La raíz cúbica del menor número


```pseudocode
def CalcularPromedio(A:float, B:float, C:float, D:float, E:float) -> float:
  Promedio = (A+B+C+D+E)/5
  return Promedio

def CalcularMediana(A:float, B:float, C:float, D:float, E:float) -> float:
  lista = [A, B, C, D, E]
  mediana_2= sorted(lista) 
  mediana_1= len(lista)
  mediana= mediana_2[mediana_1 // 2]
  return mediana

def CalcularPromedioMultiplicativo(A:float, B:float, C:float, D:float, E:float) -> float:
  PromedioMultiplicativo=((A*B*C*D*E)**1/5)
  return PromedioMultiplicativo

def OrdenarDeFormaAscendente(A:float, B:float, C:float, D:float, E:float) -> float:
  lista = [A, B, C, D, E]
  Ascendente= sorted(lista)
  return Ascendente

def OrdenarDeFormaDescendente(A:float, B:float, C:float, D:float, E:float) -> float:
  lista = [A, B, C, D, E]
  Descendente = sorted(lista, reverse = True)
  return Descendente

def PotenciaDelMayorAlMenor(A:float, B:float, C:float, D:float, E:float) -> float:
  lista = [A, B, C, D, E]
  mayornumero= max(lista)
  menornumero= min(lista)
  PotenciaDelMayorAlMenor= (mayornumero**menornumero)
  return PotenciaDelMayorAlMenor

def CalcularRaizCubiaDelMenor(A:float, B:float, C:float, D:float, E:float) -> float:
  lista = [A, B, C, D, E]
  menornumero= min(lista)
  RaizCubicaDelMenor= (menornumero**1/3)
  return RaizCubicaDelMenor

if __name__ == "__main__":
  A: float = float(input("Ingrese el primer numero:"))
  B: float = float(input("Ingrese el segundo numero:"))
  C: float = float(input("Ingrese el tercer numero:"))
  D: float = float(input("Ingrese el cuarto numero:"))
  E: float = float(input("Ingrese el quinto numero:"))
  Promedio = CalcularPromedio(A,B,C,D,E)
  mediana = CalcularMediana(A,B,C,D,E)
  promedio_multiplicativo= CalcularPromedioMultiplicativo(A,B,C,D,E)
  Ascendente= OrdenarDeFormaAscendente(A,B,C,D,E)
  Descendente=OrdenarDeFormaDescendente(A,B,C,D,E)
  PotenciaDelMayorAlMenor_1= PotenciaDelMayorAlMenor(A,B,C,D,E)
  RaizCubicaDelMenor_1= CalcularRaizCubiaDelMenor(A,B,C,D,E)
  print("el número de contadios después de "  + str(Promedio))
  print("la mediana es " + str(mediana))
  print("el promedio multicplicativo es " + str(promedio_multiplicativo))
  print("orden ascendente: " + str(Ascendente))
  print("orden descendente: " + str(Descendente))
  print("la protencia del mayor número elvado al menor es: " + str(PotenciaDelMayorAlMenor_1))
  print("la raiz cubica del menor es: " + str(RaizCubicaDelMenor_1))

```



# 8. Para el punto anterior incluir las funciones en un archivo independiente e importarlas para su uso.

```pseudocode
from reto6punto7 import CalcularPromedio
from reto6punto7 import CalcularMediana
from reto6punto7 import CalcularPromedioMultiplicativo
from reto6punto7 import OrdenarDeFormaAscendente
from reto6punto7 import OrdenarDeFormaDescendente
from reto6punto7 import PotenciaDelMayorAlMenor
from reto6punto7 import CalcularRaizCubiaDelMenor

if __name__ == "__main__":
  A: float = float(input("Ingrese el primer numero:"))
  B: float = float(input("Ingrese el segundo numero:"))
  C: float = float(input("Ingrese el tercer numero:"))
  D: float = float(input("Ingrese el cuarto numero:"))
  E: float = float(input("Ingrese el quinto numero:"))
  Promedio = CalcularPromedio(A,B,C,D,E)
  mediana = CalcularMediana(A,B,C,D,E)
  promedio_multiplicativo= CalcularPromedioMultiplicativo(A,B,C,D,E)
  Ascendente= OrdenarDeFormaAscendente(A,B,C,D,E)
  Descendente=OrdenarDeFormaDescendente(A,B,C,D,E)
  PotenciaDelMayorAlMenor_1= PotenciaDelMayorAlMenor(A,B,C,D,E)
  RaizCubicaDelMenor_1= CalcularRaizCubiaDelMenor(A,B,C,D,E)
  print("el número de contadios después de "  + str(Promedio))
  print("la mediana es " + str(mediana))
  print("el promedio multicplicativo es " + str(promedio_multiplicativo))
  print("orden ascendente: " + str(Ascendente))
  print("orden descendente: " + str(Descendente))
  print("la protencia del mayor número elvado al menor es: " + str(PotenciaDelMayorAlMenor_1))
  print("la raiz cubica del menor es: " + str(RaizCubicaDelMenor_1))
```



# 9. Consultar qué es y cómo funciona pip en python.


pip es una herramienta en Python que se utiliza para administrar paquetes de software. Su nombre es un acrónimo de "Pip Installs Packages" (Pip Instala Paquetes) en español. Con pip, se puede instalar, actualizar y desinstalar paquetes de Python de manera fácil y eficiente desde varios repositorios. Los paquetes son conjuntos de código que pueden contener módulos, funciones y recursos que puedes usar en tus proyectos de Python.



# 10. Hacer un listado de módulos populares para python que se puedan instalar com pip y consultar cómo instalarlos.

 - Requests: Para realizar solicitudes HTTP de manera sencilla.

Instalación: pip install requests



 - Pandas: Para el análisis y manipulación de datos tabulares.

Instalación: pip install pandas


 - NumPy: Biblioteca fundamental para la computación numérica en Python.

Instalación: pip install numpy


 - Matplotlib: Para la creación de gráficos y visualización de datos.

Instalación: pip install matplotlib


 - Beautiful Soup: Para analizar y extraer datos de documentos HTML y XML.

Instalación: pip install beautifulsoup4


 - Django: Framework web de alto nivel para desarrollo rápido y robusto.

Instalación: pip install Django


 - Flask: Framework web minimalista y ligero.

Instalación: pip install Flask


 - Scikit-Learn: Para aprendizaje automático y análisis de datos.

Instalación: pip install scikit-learn


 - SQLAlchemy: Para interactuar con bases de datos SQL de manera eficiente.

Instalación: pip install SQLAlchemy


 - TensorFlow: Framework de aprendizaje automático desarrollado por Google.

Instalación: pip install tensorflow





		
		
		
		
		
		
		
		
		
		







