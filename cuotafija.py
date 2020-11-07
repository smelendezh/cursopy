def amortizacion_1(monto, periodo, t_interes):
    '''
    Geneate calculation of payments
    :params: monto monto a prestar. Ie, 1000000
    :params: periodo tiempo de plazos. Ie, 24
    :params: t_interes tasa de interes. Ie, 0.1
    '''

    mensaje = '''Vamos a calcular la amortizacion de {monto}
    a un plazo de {periodo} con una tasa de interes de {t_interes} %'''.format(
        monto=monto,
        periodo=periodo,
        t_interes=t_interes*100,
    )
    print(mensaje)

    deuda_inicial = monto
    cuota_mensual=monto*(((1+t_interes)**periodo)*t_interes)/(((1+t_interes)**periodo)-1)
    
    print('deuda_inicial', deuda_inicial)
    print('Cuota Fija Mensual', cuota_mensual)

    interes_generado = deuda_inicial * t_interes
    deuda_final = deuda_inicial + interes_generado - cuota_mensual

    print ('deuda_inicial, interes_generado, pago, deuda_final')
    while deuda_final > 0:
        print(round(deuda_inicial, 3), round(interes_generado,3), round(cuota_mensual,3), round(deuda_final,3))
        deuda_inicial = deuda_final
        interes_generado = deuda_inicial * t_interes
        amortizacion = cuota_mensual - interes_generado
        if (deuda_inicial + interes_generado - cuota_mensual) < 0:
            cuota_mensual = deuda_inicial + interes_generado

        deuda_final = deuda_inicial - amortizacion

    #print(round(deuda_inicial, 3), round(interes_generado,3), round(cuota_mensual,3), round(deuda_final,3))
    print('-esto se acabo!')

monto = 1000000
periodo = 12
t_interes = 0.1

amortizacion_1(monto, periodo, t_interes)