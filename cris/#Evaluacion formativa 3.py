#Evaluacion formativa 3    

import funciones as fn
trabajadores =[]



#Principal



while True:
    try:
        print('Menú')
        print('')
        print('1. Registrar trabajador')
        print('2. Listar los trabajadores')
        print('3. imprimir planilla de sueldos')
        print('4. Salir')

        opcion = int(input('Ingrese opcion: '))

        if opcion == 1:
            print("Entraste a registrar trabajador")
            fn.registrar_trabajador(trabajadores)


        elif opcion == 2:
            print("Ingresaste a la opcion listar trabajadores")
            fn.listar_trabajadores(trabajadores)

        elif opcion == 3:
            print("Ingresaste a la opcion imprimir planilla de sueldos")
            fn.imprimir_planilla(trabajadores)
        elif opcion == 4:
            print("Hasta luego")
            break





    except:
        print('Lo siento algo no salio como se esperaba. Volveras al menú')    





