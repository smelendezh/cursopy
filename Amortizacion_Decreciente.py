def Amortizacion(capital_presatado, tasa_interes, plazo):
    amortizacion = capital_presatado / plazo
    intereses = capital_presatado * tasa_interes
    cuota_mensual = intereses + amortizacion
    total_pagado = cuota_mensual

    for i in range(plazo):
        print("Mes: ", i, "Capital: ", round(capital_presatado,2), "Intereses: ", round(intereses,2), "Amortización: ", round(amortizacion,2), "Cuota Mensual: ", round(cuota_mensual,2))
        capital_presatado = capital_presatado - amortizacion
        intereses = capital_presatado * tasa_interes
        cuota_mensual = intereses + amortizacion
        total_pagado = total_pagado + cuota_mensual

    print("Total pagado: ", total_pagado)


capital_presatado = float(input("Ingrese el capital a solicitar: "))
tasa_interes = float(input("Ingrese la tasa de interés: "))
intereses = 0.
plazo = int(input("Ingrese el número de meses de la amortización: "))

print(Amortizacion(capital_presatado, tasa_interes, plazo))
