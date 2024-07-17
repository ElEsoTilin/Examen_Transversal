
import random
import csv

empleados = ["Juan Pérez", "María García", "Carlos López", "Ana Martínez", "Pedro Rodríguez", 
                 "Laura Hernández", "Miguel Sánchez", "Isabel Gómez", "Francisco Díaz", "Elena Fernández"]
    
def generar():
    sueldos = {}  
    for empleado in empleados:
        sueldo = random.randint(300000, 2500000)  
        sueldos[empleado] = sueldo  
    return sueldos

def contar_menores_1000000(sueldos_empleados):
    total_menores_1000000 = sum(1 for sueldo in sueldos_empleados.values() if sueldo < 1000000)
    return total_menores_1000000
def contar_mayores_2000000(sueldos_empleados):
    total_mayores_2000000 = sum(1 for sueldo in sueldos_empleados.values() if sueldo > 2000000)
    return total_mayores_2000000
def contar_entre_1000000_2000000(sueldos_empleados):
    total_entre_1000000_2000000 = sum(1 for sueldo in sueldos_empleados.values() if 1000000 < sueldo < 2000000)
    return total_entre_1000000_2000000

def ordendelossueldos(sueldos_empleados):
    menores_1000000 = []
    entre_1000000_2000000=[]
    mayores_2000000 = []
    for empleado, sueldo in sueldos_empleados.items():
        if sueldo < 1000000:
            menores_1000000.append((empleado, sueldo))
        elif 1000000 <= sueldo <= 2000000:
            entre_1000000_2000000.append((empleado, sueldo))
        elif sueldo > 2000000:
            mayores_2000000.append((empleado, sueldo))
    menuClasificar='''
    1. Sueldos menores a 1.000.000 (1 millon)
    2. Sueldos entre 1.000.000 y 2.000.000 (Entre 1 millon y 2 millones)
    3. Sueldos Mayores a 2.000.000 (Mas de 2 millones)
    4. Salir
    '''
    while True:
        print(menuClasificar)
        op1=int(input('Ingrese opción: '))
        while(op1<1 or op1>4):
            op1=int(input('Ingrese opción del 1 al 3: '))
        if(op1==1):
            total_menores_1000000 = contar_menores_1000000(sueldos_empleados)
            print("\n\nEmpleados con Sueldos Menores a 1.000.000: \nTOTAL: {}\n".format(total_menores_1000000))
            for empleado, sueldo in menores_1000000:
                print(f"{empleado}: {sueldo}")
            continue
        if(op1==2):
            total_entre_1000000_2000000 = contar_entre_1000000_2000000(sueldos_empleados)
            print("\n\nempleados con Sueldos Entre 1.000.000 y 2.000.000: \nTOTAL: {}\n".format(total_entre_1000000_2000000))
            for empleado, sueldo in entre_1000000_2000000:
                print(f"{empleado}: {sueldo}")
            continue
        if(op1==3):
            total_mayores_2000000 = contar_mayores_2000000(sueldos_empleados)
            print("\n\nEmpleados con Sueldos Mayores a 2.000.000: \nTOTAL: {}\n".format(total_mayores_2000000))
            for empleado, sueldo in mayores_2000000:
                print(f"{empleado}: {sueldo}")
            continue
        if(op1==4):
            break
        
def max_sueldo(diccionario_sueldos):
    empleado_mayor_sueldo = max(diccionario_sueldos, key=diccionario_sueldos.get)
    return empleado_mayor_sueldo, diccionario_sueldos[empleado_mayor_sueldo]

def min_sueldo(diccionario_sueldos):
    empleado_mayor_sueldo = min(diccionario_sueldos, key=diccionario_sueldos.get)
    return empleado_mayor_sueldo, diccionario_sueldos[empleado_mayor_sueldo]

def promedio_sueldo(diccionario_sueldos):
    total_sueldos = sum(diccionario_sueldos.values())  
    cantidad_empleados = len(diccionario_sueldos)  
    promedio = total_sueldos / cantidad_empleados  
    return promedio


def media_sueldo(diccionario_sueldos):
    
    sueldos = list(diccionario_sueldos.values())
    
    if not sueldos:
        raise ValueError("El diccionario de sueldos está vacío")
    producto = 1
    for sueldo in sueldos:
        producto *= sueldo
    media_geometrica = round(producto ** (1 / len(sueldos)))
    return media_geometrica


    
def estadisticasdelossueldos():
    menu=''''
    1. Sueldo mas alto
    2. Sueldo mas bajo
    3. Promedio de sueldos
    4. Media Geometrica
    5. Salir
    '''
    while True:
        print(menu)
        op2=int(input('Ingrese opcion: '))
        while(op2<1 or op2>5):
            op2=int(input('Ingrese opcion del 1 al 5: '))
        if(op2==1):
           
            sueldos_empleados = generar()
            
            empleado_max, sueldo_max = max_sueldo(sueldos_empleados)
            print("\nEl empleado con mayor sueldo es {}, con un sueldo de ${} Pesos".format(empleado_max, sueldo_max))

        if(op2==2):
           
            sueldos_empleados = generar()
            
            empleado_min, sueldo_min = min_sueldo(sueldos_empleados)
            print("\nEl empleado con menor sueldo es {}, con un sueldo de ${} Pesos".format(empleado_min, sueldo_min))
        if(op2==3):
             
            sueldos_empleados = generar()
            sueldo_promedio = promedio_sueldo(sueldos_empleados)
            print(f"\nEl sueldo promedio es de ${sueldo_promedio:.2f} Pesos")
        if(op2==4):
            sueldos_empleados = generar()
            try:
                media_geo = media_sueldo(sueldos_empleados)
                print("La media geométrica de los sueldos es {}".format(media_geo))
            except ValueError as e:
                print(f"Error: {e}")
            continue
        if(op2==5):
            break
        

import csv

def reportedelossueldos(sueldos_empleados):
    tasa_afp = 0.1 
    tasa_salud = 0.05   
    
    reporte_datos = [] # Lista para almacenar los datos del reporte
    
    print("\n\nReporte de Sueldos con Deducciones de AFP y Salud:\n")
    for empleado, sueldo in sueldos_empleados.items():
        descuento_afp = sueldo * tasa_afp
        descuento_salud = sueldo * tasa_salud
        sueldo_neto = sueldo - descuento_afp - descuento_salud
        
        sueldo_redondeado = round(sueldo, 2)
        descuento_afp_redondeado = round(descuento_afp, 2)
        descuento_salud_redondeado = round(descuento_salud, 2)
        sueldo_neto_redondeado = round(sueldo_neto, 2)
        
        reporte_datos.append([empleado, round(sueldo_redondeado), round(descuento_afp_redondeado), round(descuento_salud_redondeado), round(sueldo_neto_redondeado)])
        
        print("Empleado: {}".format(empleado))
        print("Sueldo Bruto: {}".format(sueldo_redondeado))
        print(f"Deducción AFP ({tasa_afp * 100}%): {descuento_afp_redondeado}")
        print(f"Deducción Salud ({tasa_salud * 100}%): {descuento_salud_redondeado}")
        print(f"Sueldo Neto: {sueldo_neto_redondeado}\n")
    
    guardar_reporte_en_csv(reporte_datos)

def guardar_reporte_en_csv(reporte_datos):
    confirmacion = input("¿Desea guardar el reporte en un archivo CSV? (s/n): ")
    
    if confirmacion.lower() == 's':
        with open('reporte_sueldos.csv', 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['Empleado', 'Sueldo Bruto', 'Deducción AFP', 'Deducción Salud', 'Sueldo Neto'])
            writer.writerows(reporte_datos)
        print("El reporte se ha guardado exitosamente en el archivo 'reporte_sueldos.csv'.")
    else:
        print("Operación cancelada. El reporte no ha sido guardado.")

        
def menu():
    menu='''
    1. Asignar sueldos aleatorios
    2. Clasificar sueldos
    3. Ver estadísticas
    4. Reporte de sueldos
    5. Salir del programa
    '''
    print(menu)



while True:    
    menu()
    try:
        op=int(input('Ingrese opcion del 1 al 5: '))
    except ValueError:
        print('\nOpción no valida\nIngrese nuevamente la opcion: ')
        continue
    while(op<1 or op>5):
        op=int(input('\nDebe ser un numero entre 1 y 5\nIngrese opcion: '))
    if(op==1):
        sueldos_empleados = generar()
        print(sueldos_empleados)
        continue
    if(op==2):
        try:
            ordendelossueldos(sueldos_empleados)
        except NameError:
         print("\nNo se han generado sueldos aún.\nPor favor, genere los sueldos con la opción 1.")
        continue
    if(op==3):
        estadisticasdelossueldos()
    if(op==4):
        sueldos_empleados = generar()
        reportedelossueldos(sueldos_empleados)
    if(op==5):
        print("\nFinalizando programa....")
        print("Desarrollado por Matías Cerda")
        print("RUT 21.988.108-8")
        break  



    

