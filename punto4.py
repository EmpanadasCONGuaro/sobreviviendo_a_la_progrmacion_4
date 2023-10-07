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
