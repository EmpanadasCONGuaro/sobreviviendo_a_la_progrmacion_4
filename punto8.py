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
