# Registrar trabajador

CARGOS =['ceo','desarrollador','analista de datos']



def registrar_trabajador(trabajadores):
    print("Registro trabajador")
    nombre = input('Ingrese nombre y apellido del trabajador: ')
    cargo = input('Ingrese cargo del trabajador: (CEO/Desarrollador/Analista de Datos): ').lower()
    while cargo not in CARGOS:
        print('Cargo no existe intentelo nuevamente')
        cargo = input('Ingrese cargo del trabajador: (CEO/Desarrollador/Analista de Datos): ').lower()
    sueldoBruto = int(input('Ingrese sueldo bruto del trabajador: '))

    #Calcular descuentos
    descSalud = sueldoBruto * 0.07
    descAFP = sueldoBruto * 0.12
    liquidoPagar = sueldoBruto - descSalud - descAFP
    
    trabajadores.append({
        'Nombre': nombre,
        'Cargo': cargo,
        'SueldoBruto': sueldoBruto,
        'DescSalud': descSalud,
        'DescAFP': descAFP,
        'LiquidoPagar': liquidoPagar
    })

# Listar todos los trabajadores

def listar_trabajadores(trabajadores):
    print("lista de trabajadores")
    for trabajador in trabajadores:
        print(trabajador)






# Imprimir planilla de sueldos

def imprimir_planilla(trabajadores):
    print('planilla')
    cargoSeleccionado = input('Ingrese cargo para imprimir planilla o bien presione ENTER para seleccionar todos: ').lower()
    if cargoSeleccionado == "":
        trabajadores_a_imprimir = trabajadores
        nombreArchivo = 'planilla_todos.txt'
    elif cargoSeleccionado in CARGOS:
        trabajadores_a_imprimir = []
        for trabajador in trabajadores:
            if trabajador['Cargo'] == cargoSeleccionado:
                trabajadores_a_imprimir.append(trabajador)
        nombreArchivo = f'planilla_{cargoSeleccionado}.txt'
    else:
        print('Cargo no válido')
        return
    
    with open(nombreArchivo, 'w') as archivo:
        for trabajador in trabajadores_a_imprimir:
            archivo.write(f"Nombre y Apellido:  {trabajador['Nombre']} \n")
            archivo.write(f"Cargo:  {trabajador['Cargo']} \n")
            archivo.write(f"Sueldo Bruto:  {trabajador['SueldoBruto']} \n")
            archivo.write(f"Desc de Salud:  {trabajador['DescSalud']} \n")
            archivo.write(f"Desc de AFP:  {trabajador['DescAFP']} \n")
            archivo.write(f"Liquido a Pagar:  {trabajador['LiquidoPagar']} \n")






