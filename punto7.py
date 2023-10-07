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
