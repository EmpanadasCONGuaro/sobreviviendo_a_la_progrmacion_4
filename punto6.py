def CalcularContagios(C:float, D:float) -> float:
  NumeroDeContagios=(C*(2**D))
  return NumeroDeContagios

if __name__ == "__main__":
 C: float = float(input("Ingrese el número de contagios actuales:"))
 D: float = float(input("Ingrese el número de dias:"))
 NumeroDeContagios = CalcularContagios(C,D)
 print("el número de contadios después de "  + str(D) +  " dia(s) es de " + str(NumeroDeContagios))
