def CalcularPrestamos(c:float, i:float, n:float) -> float:
  valortotaldelprestamo= (c*((1+i/100)**n))
  return valortotaldelprestamo

if __name__ == "__main__":
 c: float = float(input("Ingrese el valor del prestamo:"))
 i: float = float(input("Ingrese la tasa de intereses:"))
 n: float = float(input("Ingrese el tiempo es meses:"))
 valortotaldelprestamos= CalcularPrestamos(c,i,n)
 print("el valor final del prestamos es "+str(valortotaldelprestamos))
