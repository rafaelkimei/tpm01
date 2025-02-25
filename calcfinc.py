# Trabalho Prático Módulo 1: Fundamentos de Programação para Ciência de Dados
# Objetivo: Criar um Script em Python de calculadora financeira de juros compostos interativa
# Inicio: Fevereiro/2025
# rafael.kimei@gmail.com

# TODO
# alterar a funcao fun_CalcularI para que aceite o pagamento mensal como parametro


import math



def fun_FormatarBR(x):
  """
  Formata um número para o padrão brasileiro, usando "." como separador de milhar e "," como separador decimal.

  Args:
    x: O número sem formatação

  Returns:
    O número formatado.
  """

  return "{:,.2f}".format(x).replace(',', 'X').replace('.', ',').replace('X', '.')



def fun_CalcularVF(CI: float, I: float, T: int, PGTO: float) :
  """
  Calcula e imprime o Valor Futuro.

  Args:
    CI: Capital Inicial.
    I: Taxa de Juros.
    T: Quantidade de períodos.
    PGTO: Pagamento mensal.

  Returns:
    O Valor Futuro.
  """

  #return CI*(1+I)**T
  fator = (1 + I) ** T
  VF = (CI * fator + PGTO *  (fator - 1) / I)

  print (f"O Valor Futuro é R$ {fun_FormatarBR(VF)}")



def fun_CalcularCI(VF: float, I: float, T: int, PGTO: float):
  """
  Calcula e imprime o Capital Inicial.

  Args:
    VF: Valor Futuro.
    I: Taxa de Juros.
    T: Quantidade de períodos.
    PGTO: Pagamento mensal.

  Returns:
    O Capital Inicial.
  """

  #return VF/(1+I)**T

  fator = (1 + I) ** T
  CI = (-PGTO  * (fator - 1) / (I* fator)) + (VF / fator)

  print (f"O capital Inicial é {fun_FormatarBR(CI)}")



def fun_CalcularT(VF: float, CI: float, I: float, PGTO: float):
  """
  Calcula e imprime a quantidade de períodos.

  Args:
    VF: Valor Futuro.
    CI: Capital Inicial.
    I: Taxa de Juros.
    PGTO: Pagamento mensal.

  Returns:
    A quantidade de períodos.
  """
  #T =  math.log(VF / CI) / math.log(1 + I)
  T =  - math.log((PGTO + I * CI) / (PGTO  + I * VF)) / math.log(1 + I)

  print (f"A quantidade de período(s) é {T:.2f}")



def fun_CalcularI(VF: float, CI: float, T: int):
  """
  Calcula e imprime a taxa de Juros.

  Args:
    VF: Valor Futuro.
    CI: Capital Inicial.
    T: Quantidade de períodos.

  Returns:
    A taxa de juros.
  """
  I = (((VF / CI)**(1/T)) - 1)*100

  print (f"A taxa de juros é {I:.2f} %")



def fun_CalcularPGTO(VF: float, CI: float, T: int, I: float):
  """
  Calcula e imprime o pagamento mensal.

  Args:
    VF: Valor Futuro
    CI: Capital Inicial.
    T: Quantidade de períodos.
    I: Taxa de Juros.

  Returns:
    O pagamento mensal.
  """

  fator = (1 + I) ** T
  PGTO = (VF - CI* fator) * I / (fator - 1)

  print (f"O pagamento mensal é de R$  {fun_FormatarBR(PGTO)} ")



def main():

  str_Ficar: String = "S"

  print("Bem-vindo à calculadora de Juros Compostos!")

  while str_Ficar == "S":
    str_Comando = input("\nO que você gostaria de calcular? (VF,CI,T,I,PGTO): ")

    if str_Comando != "VF":
      input_VF = float(input("Digite o valor do Valor Futuro(VF) em R$: "))

    if str_Comando != "CI":
      input_CI = float(input("Digite o valor do Capital Inicial(CI) em R$: "))

    if str_Comando != "T":
      input_T = int(input("Digite a quantidade de Periodos(T): "))

    if str_Comando != "I":
      input_I = float(input("Digite o valor da Taxa de juros(I) dividido por 100: "))

    if str_Comando != "PGTO":
      input_PGTO = float(input("Digite o valor do Pagamento Mensal em R$: "))

    match str_Comando:
      case "VF":
        fun_CalcularVF(input_CI,input_I,input_T,input_PGTO)
      case "CI":
        fun_CalcularCI(input_VF,input_I,input_T, input_PGTO)
      case "T":
        fun_CalcularT(input_VF,input_CI,input_I, input_PGTO)
      case "I":
        fun_CalcularI(input_VF,input_CI,input_T)
      case "PGTO":
        fun_CalcularPGTO(input_VF,input_CI,input_T, input_I)
      case _:
        print("Comando inválido.")

    str_Ficar = input("\nDeseja fazer mais algum cálculo?(S)")

if __name__ == "__main__":
  main()
