runnin = True

while(runnin):
  lado1 = int(input("Digite o valor do primeiro lado (EM CENTIMETROS): "))
  lado2 = int(input("Digite o valor do segundo lado (EM CENTIMETROS): "))

  total = ((lado1 * 2) + (lado2 * 2)) / 30
  print("VALOR TOTAL: ", str(total))
  fin = input("aperte N para finalizar")

  if lower(fin) == 'n':
    runnin = false
