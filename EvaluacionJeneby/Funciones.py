###La automotora “Auto Seguro” necesita registrar todos los datos de los vehículos que en este periodo
#tienen a la venta. En el registro de vehículos que pertenece a la región metropolitana de Santiago de Chile, 
#requiere construir un programa con un menú quecontenga las siguientes opciones:Opción 1● Grabar: 
#Corresponde a guardar ciertos datos de un vehículo, entre ellos: Tipo, patente, marca y precio, multas (monto yfecha), 
#fecha de registro del vehículo y nombre del dueño.Además, debe verificar que la patente sea correcta,
##la marca considere entre 2 y 15 caracteres y el precio sea mayor a$5.000.000.
import random

l_tipoVeh = []
l_patenVeh = []
l_marcaVeh = []
l_precioVeh = []
l_fechreg = []
l_nomdueno = []
l_multas = []

#certificado = random.randit(valor)

def Buscador():
    global patente
    print("Ingrese la patente para buscar datos: ")
    patente = int(input())
    if patente == l_patenVeh:
        print(f"Los datos ingresados son: {l_tipoVeh,l_precioVeh,l_marcaVeh,l_patenVeh}")
    else:
        print("Ingrese patente válida en datos existentes.")








#Primera vista de menu usuario.
def menu():
    while True:
        try:
            print("Automotora Seguro")
            print("Repertorio de ventas de la región Metropolitana Santiago de Chile.")
            print("Bienvenido, elija su opción.")
            print("1.Grabar")
            print("2.Buscar")
            print("3.Certificados")
            print("4.Salir")
            op = int(input())
            if op == 1: #OOOOOOOOOO
                print("Elija los datos que quisiera almancenar.")
                print("----------------------------------------")
                print("1.Vehículo")
                print("2.Fecha registro Vehículo")
                print("3.Nombre dueño Vehículo")
                print("4.Multas")
                print("5.Salir.")
                eleccion = int(input())
                if eleccion == 1: #Opción Vehiculo ****
                    print("1.Tipo")
                    print("2.Patente")
                    print("3.marca")
                    print("4.Precio")
                    opVeh = int(input()) #Opción Vehículo = tipo Vehiculo
                    if opVeh == 1:
                        print("Añada su tipo de Vehículo: ")
                        tipVeh = str(input())
                        l_tipoVeh.append(tipVeh) #Añado de datos TIPO a la lista
                        print("Los datos ingresados son: ",l_tipoVeh)
                        print(""""
                        ¿Quisiera volver al menú principal?
                        1.Si
                        2.No
                        """)
                        salida = int(input())
                        if salida == 1:
                            op == 1
                        else:
                            opVeh == 1
                    elif opVeh == 2: #Opción Vehículo = Patente Vehículo
                        print("""
                        1.Ingresar nueva patente
                        2.Salir
                        """)
                        if salida == 1:
                            print("Ingrese su nueva patente.")
                            patente = int(input())
                            l_patenVeh.append(patente)
                            print("Los datos ingresados son: ",l_patenVeh)
                            print("Guardado exitoso.")
                            if salida == 2:
                                print("Guardado exitoso.")
                                op == 1
                    elif opVeh == 3: #Opcion Vehiculo = marca
                        print("Ingrese marca de Vehículo: ")
                        print("Considere el mmínimo de carácteres es 5 y el máximo 15.")
                        marca = str(input())
                        l_marcaVeh.append(marca)
                        print("Los datos ingresados son: ",l_marcaVeh)
                        print(""""
                        ¿Quisiera volver al menú principal?
                        1.Si
                        2.No
                        """)
                        salida = int(input())
                        if salida == 1:
                            op == 1
                        else:
                            opVeh == 3
                    if opVeh == 4: #Opcion Vehiculo = precio
                        print("Ingrese nuevo precio:")
                        precio = int(input())
                        if precio >=5000000:
                            l_precioVeh.append(precio)
                            print("Los datos ingresados son: ",l_precioVeh)
                            print("Ingreso exitoso!")
                            print(""""
                            ¿Quisiera volver al menú principal?
                            1.Si
                            2.No
                            """)
                            salida = int(input())
                            if salida == 1:
                                op == 1
                            else:
                                opVeh == 4
                        else:
                            print("El mínimo de ingreso es: $5.000.000.")
                            print(""""
                            ¿Quisiera volver al menú principal?
                            1.Si
                            2.No
                            """)
                            salida = int(input())
                            if salida == 1:
                                op == 1
                            else:
                                opVeh == 4
                if eleccion == 2:
                    print("Ingrese fecha de registro:")
                    fechreg = int(input())
                    l_fechreg.append(fechreg)
                    print("Sus datos se han ingresado con exito.")
                if eleccion == 3:
                    print("Ingrese :")
                    fechreg = int(input())
                    l_fechreg.append(fechreg)
                    print("Sus datos se han ingresado con exito.")

            if op == 2:
                Buscador()
                print(""""
                ¿Quisiera volver al menú principal?
                1.Si
                2.No
                """)
                salida = int(input())
                if salida == 1:
                    op == 1
                else:
                    opVeh == 4
            if op == 3:
                imprecion = random.randint(1500,3500)
                print("""
                Ingrese su certificado requerido:
                1.Emisión de contaminantes
                2.Anotaciones Vigentes
                3.Multas
                4.Salir
                """)
                imp = int(input())
                if imp == 1:
                    print("Su certificado se ha imprimido con éxito!")
                    print("Su valor es: $",imprecion)
                    print("Datos ingresados")
                    print(l_marcaVeh,l_patenVeh,l_precioVeh,l_tipoVeh)
                if imp == 2:
                    print("Su certificado se ha imprimido con éxito!")
                    print("Su valor es: $",imprecion)
                    print("Datos ingresados")
                    print(l_marcaVeh,l_patenVeh,l_precioVeh,l_tipoVeh)
                if imp == 3:
                    print("Su certificado se ha imprimido con éxito!")
                    print("Su valor es: $",imprecion)
                    print("Datos ingresados.")
                    print(l_marcaVeh,l_patenVeh,l_precioVeh,l_tipoVeh)
                if imp == 4:
                    print("Ha salido con éxito.")
                    break
            if op == 4:
                print("Gracias por ocupar el programa.")
        except ValueError:
            print("Su valor no ha sido leída.")









