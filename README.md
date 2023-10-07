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
  volumen=((4/3*p*(r1**3))+(1/3*p*h*(r2**2)))    #defini la fumción para calcular le volumen
  return volumen

def CalcularAreaSuperficial(r1:float, r2:float, h:float) ->float:
  AreaSuperficial=((4*p*(r1**2))+(p*r2*(r2+g)))       #defini la función para calcular el area superficial
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
  area=((a*b)+(2*(p*(r**2))))   #defini la fumción para calcular le area
  return area

def CalcularPerimetro(r:float, a:float, b:float) ->float:
  perimetro=((2*(a+b))+(2*(2*p*r)))  #defini la función para calcular el perimetro
  return perimetro
                                                      

if __name__ == "__main__":
                                    
 r: float = float(input("ingrese el valor de r:"))        #pedir al usuario que ingrese los datos
 a: float = float(input("ingrese el valor de a:"))
 b: float = float(input("ingrese el valor de b:"))
 area=CalcularArea(r,a,b)
 print("el area es "+str(area)+" unidades cuadras")

 perimetro=CalcularPerimetro(r,a,b)
 print("el perimetro es: "+str(perimetro)+" unidades ")
```



