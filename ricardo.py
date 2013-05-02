#PROYECTO FINAL 'PROGRAMACIÓN' MAYO 8, 2013

inventario={} 
from contra import user1 #Importar desde otro archivo: CÉSAR FRAGOSO    
from contra import user2
from contra import pwd1
from contra import pwd2

def cargartxt(): #JACQUI ORTA Y VÍCTOR VALDEZ
    print('\n')
    
    try:
        archivo=open("inventario.txt","r") #open("archivo.txt","r")
       
        for linea in archivo:
            cont=0
            for i in linea:
                cont=cont+1
                if i==':':
                    break
            uno=linea[:cont-1]
            dos=linea[cont:len(linea)-1]
            add(uno,dos)
        archivo.close() #Close, para dejar de usar el archivo
    except IOError as e: #Checa si hay un error de Input-Output-Error
        print("Error: ",e) #Se guarda en la variable 'e'
    


def menu ():#VERO PADILLA    #Se define el menu para comenzar.
    print("*****Sistema de Inventario*****")
    print("0.-  Salir")
    print("1.-  Cargar archivo de inventario")
    print("2.-  Agregar artículos")
    print("3.-  Eliminar artículo")
    print("4.-  Generar archivo de inventario")
    print("5.-  Imprime inventario")
    op=int( input("Escoge una opción "))
    print()
    return op


def submenu():#JAVIER AVILA
    print("""
1.- Borrar todo el artículo
2.- Restar cantidad"""


    )
    op=int(input("¿Cómo lo quieres borrar? "))
    return op




def contra():#RICARDO GARZA
    flag=0


    
    
    while True:
        usuario=input("Usuario: ")
        contra=input("Contraseña: ")
        
        if flag==2:
            print("Has excedido el número de intentos. ")
            return 1
        if usuario==user1 and contra==pwd1:
            return 0
        elif usuario==user2 and contra==pwd2:
            return 0
        else:
            flag=flag+1
            print("Error")
            continue

    
def add(new,mean): #JUAN CARLOS FLORES
    if new not in inventario: 
        inventario[new]=mean
    else:
        temp=inventario[new]
        
        nuevo=temp+mean
        inventario[new]=nuevo

    
def deli(new,mean): #ANDRÉS SIERRA
    if new not in inventario: 
        inventario[new]=mean
    else:
        temp=int(inventario[new])

        if temp > mean:
            nuevo=temp-mean
            inventario[new]=nuevo
        else:
            print("Quieres borrar más de los que hay.")

        
        
def writefile():#RICARDO GARZA

    try: 
        archw= open("inv.txt","w")
        archw.write("Artículo".ljust(15)+ "Cantidad".ljust(15)+"\n")
        archw.write("===========================\n")
        for i in inventario:
            archw.write(str(i).ljust(15)+ str(inventario[i]).ljust(15)+"\n")
        archw.close()
    except IOError:
        print("No se puede escribir el archivo.")
    
flag1=0

while True:
    try:#FRANCISCO LÓPEZ Y FERNANDO RAMÍREZ
        if flag1==0:
            veces=contra()
            if veces==0:
               
                print("Bienvenido")
                print()
            else: break #
        
        flag1=1
        
        op=menu()#JUAN CARLOS FLORES

        if op==0:
            break

        elif op==1:#DIEGO RUBIO
            cargartxt()
            print("Se cargó el inventario desde el archivo...")
            print()

        elif op==2:#LUDOVICO CÁRDENAS
            new=input("¿Qué artículo quieres agregar? ")
            mean=int(input("¿Cuántos artículos son? "))
            
            add(new,mean)
   
        elif op==3:#ANDRÉS SIERRA

            sub=submenu()
            delete=input("¿Qué artículo quieres borrar? ")
            if sub==1:
                
                if delete in inventario:
                    del(inventario[delete])
                    print("Se borró: ",delete)
                else:
                    print("Esa expresión no existe.")
            elif sub==2:
                cuantos=int(input("¿Cuántos quieres quitar? "))
                deli(delete,cuantos)
              
        elif op==4:#CRISTINA SOTOMAYOR
            writefile()
                
        elif op==5:#JULIA GUILLERMO Y MARIO GARCÍA
            for i in inventario:
                print(i,"=",inventario[i])#imprime todo el diccionario
            
        else:#CESAR CHAVEZ
            print("Escribe una opción correcta.")
            print()
    except ValueError:#ITZEL GUZMÁN
        print("Escribe sólo números.")
        input()
