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
