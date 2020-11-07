montoprestar=int(input("Ingrese el monto a solicitar: "))
tiempolimite=int(input("Ingrese el numero de meses: "))
tipocred=int(input("Ingrese el tipo de credito: \n 1->Hipotecario \n 2->Tarjeta de Credito \n 3->Compra Cartera \n 4->Libre Inversion \n"))
if tipocred==1:
  tasaint=0.4/100

elif tipocred==2:
  tasaint=2.16/100

elif tipocred==3:
  tasaint=0.8/100

else:
  tasaint=1.5/100
intcomp=0
amort=montoprestar/tiempolimite
montofinal=montoprestar
for i in range(tiempolimite):
  intcomp=montofinal*tasaint
  montofinal=montofinal-amort
  cuota=intcomp+amort
  print('Amortizacion $ = {3:.2f} Interes $ = {0:.2f} Cuota $ = {1:.2f} Saldo $ = {2:.2f}'.format(intcomp,cuota,montofinal,amort))