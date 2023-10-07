def CalcularCantidadDeCarne(N:float, M:float, K:float) -> float:
  CantidadDeCarne=((N*6)+(M*7)+(K))  #defini la fumción para calcular la cantidad de carne
  return CantidadDeCarne

if __name__ == "__main__":
 N: float = float(input("ingrese el numero de gallinas:"))
 M: float = float(input("ingrese el numero gallos:"))
 K: float = float(input("ingrese el numero de pollitos:"))
 CantidadDeCarne=CalcularCantidadDeCarne(N,M,K)
 print("La cantidad de carne es "+str(CantidadDeCarne)+" kilogrmos")
