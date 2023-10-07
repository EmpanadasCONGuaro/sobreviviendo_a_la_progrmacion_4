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
