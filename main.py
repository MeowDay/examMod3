#--------------Listas preasignadas------------

lista = ["Harry Houdini", "Newton", "David Blaine", "Hawking", "Messi", "Teller", "Einstein", "Pele", "Juanes"]

magos = [lista[0], lista[2], lista[5]]

cientificos = [lista[1], lista[3], lista[6]]

#--------------Funciones----------
def hacer_grandioso(x):
    i = f"El gran {x}"
    return i

def imprimir_nombre():
    for item in lista:
        print(item,end="")
        if (lista.index(item)+1)<len(lista):
            print(", ", end="")
    print("\n")

def imprimir_elm(x):
      for item in x:
        if (x.index(item)+1)<len(x):
            print(item,", " , end="")
        else:
            print(item, "\n")
    
#--------------Definiendo grupo otros-----------------
otros=[]
for i in lista:
    if (i not in magos) and (i not in cientificos):
        otros += [i]

#------------Definiendo a los magos grandiosos----------------

magosGran=[]
for i in range(len(magos)):
    j=hacer_grandioso(magos[i])
    magosGran+=[j]
    

#-----------------------------Programa------------------
validar= True
while validar:
    elec = input("""
            \033[96m Bienvenid@ a mi Evaluación de Modulo! Por favor elije como quieres correr este programa: \033[0m

                \033[91m Escribe 1\033[0m para correr el programa tal como se solicita en la evaluación.
                \033[91m Escribe 2\033[0m para correr el programa seleccionando que elemento imprimir.
                \033[91m Escribe 3\033[0m para Salir del programa.
                                            \033[91m Ingresa 1, 2 o 3: \033[0m""")
    if elec =="1":
        print("\033[91m Has elegido correr el programa según la evaluación. a continuación se muestran los elementos en las listas solicitadas: \033[0m")

        print("\n""\033[93mLos nombres antes de ser modificados son: \033[0m",end="")
        imprimir_nombre()

        print("\033[93mLos nombres de los Magos son: \033[0m", end="")
        imprimir_elm(magos)

        print("\033[93mLos nombres de los Cientificos son: \033[0m", end="")
        imprimir_elm(cientificos)
        

        print("\033[93mLos nombres de los Otros personajes son: \033[0m", end="")
        imprimir_elm(otros)

        print("\033[93mLos nombres de los Magos grandiosos son: \033[0m", end="")
        imprimir_elm(magosGran)

        print("\033[95mVolviendo al menú Principal...\033[0m")
        
    elif elec =="2":
        validar2= True
        while validar:
            elec2 = input("""
                \033[96m Selecciona el elemento a visualizar \033[0m

                    \033[91m Escribe 1\033[0m para ver la lista completa sin modificar.
                    \033[91m Escribe 2\033[0m para ver el listado de Magos.
                    \033[91m Escribe 3\033[0m para ver el listado de Cientificos.
                    \033[91m Escribe 4\033[0m para ver el listado de Otros personajes.
                    \033[91m Escribe 5\033[0m para ver el listado de Magos grandiosos.
                    \033[91m Escribe 6\033[0m para volver al menú principal.
                    \033[91m Escribe 7\033[0m para salir del programa.
                                            Ingresa la opción: """)
            
            print(f"\n \033[92mSELECCIONASTE LA OPCIÓN {elec2}\033[0")

            if elec2 == "1":
                print("\n""\033[93mLos nombres antes de ser modificados son: \033[0m",end="")
                imprimir_nombre()
            elif elec2 == "2":
                print("\033[93mLos nombres de los Magos son: \033[0m", end="")
                imprimir_elm(magos)
            elif elec2 == "3":
                print("\033[93mLos nombres de los Cientificos son: \033[0m", end="")
                imprimir_elm(cientificos)
            elif elec2 == "4":
                print("\033[93mLos nombres de los Otros personajes son: \033[0m", end="")
                imprimir_elm(otros)
            elif elec2 == "5":
                print("\033[93mLos nombres de los Magos grandiosos son: \033[0m", end="")
                imprimir_elm(magosGran)
            elif elec2 == "6":
                print("\033[95mHas seleccionado volver al menú principal\033[0m")
                break
            elif elec2 =="7":
                print("\033[95mFINALIZANDO PROGRAMA... ¡Hasta la próxima!\033[0m")
                validar = False
                validar2 = False        
            else:
                print("\n                              \033[95m>>>>>>>SELECCIÓN ERRONEA INTENTE NUEVAMENTE<<<<<<<\033[0m")
            
    elif elec =="3":
        print("\033[95mFINALIZANDO PROGRAMA... ¡Hasta la próxima!\033[0m")
        validar=False
    
    else:
        print("\n                              \033[95m>>>>>>>SELECCIÓN ERRONEA INTENTE NUEVAMENTE<<<<<<<\033[0m")
