#Autor: Daniela Estrella Tovar
#Crear un código que ejecute una de las diversas opciones que presenta el programa.

import pygame   # Librería de pygame
import random
import math

# Dimensiones de la pantalla
ANCHO = 800
ALTO = 800
# Colores
BLANCO = (255, 255, 255)  # R,G,B en el rango [0,255], 0 ausencia de color, 255 toda la intensidad
VERDE_BANDERA = (27, 94, 32)    # un poco de rojo, más de verde, un poco de azul
ROJO = (255, 0, 0)      # solo rojo, nada de verde, nada de azul
AZUL = (0, 0, 255)      # nada de rojo, ni verde, solo azul
NEGRO= (0,0,0)


#Funciones para Figura 1
def dibujarCirculosyCuadros(ventana):
    for radio in range (10,ALTO//2, 10):
        pygame.draw.circle(ventana, NEGRO, (ANCHO//2, ALTO//2), radio, 1)

    for lado in range(10, ALTO//2, 10):
        pygame.draw.rect(ventana, NEGRO, (lado, lado, ANCHO-lado*2, ALTO-lado*2), 1)

def generarColor():
    rojo= random.randint(0,255)
    verde= random.randint(0,255)
    azul= random.randint(0,255)

    return(rojo,verde,azul)

def dibujarCircyCu():
    pygame.init()
    ventana = pygame.display.set_mode((ANCHO, ALTO))
    reloj = pygame.time.Clock()
    termina = False

    while not termina:  # Ciclo principal, MIENTRAS la variable termina sea False, el ciclo se repite automáticamente
        # Procesa los eventos que recibe
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:  # El usuario hizo click en el botón de salir
                termina = True      # Queremos terminar el ciclo


        ventana.fill(BLANCO)

        dibujarCirculosyCuadros(ventana)

        pygame.display.flip()  # Actualiza trazos (Si no llamas a esta función, no se dibuja)
        reloj.tick(40)  # 40 fps

    pygame.quit()

#Funciones para Figura2
def dibujarLineasEstrella(ventana):
    for y in range (0,ALTO//2+1,10):
        colorAleatorio= generarColor()
        pygame.draw.line(ventana, colorAleatorio, (0+y,ALTO//2), (ANCHO//2, ALTO//2-y))
    for y in range (0,ANCHO//2+1,10):
        colorAleatorio= generarColor()
        pygame.draw.line(ventana, colorAleatorio, (ANCHO-y,ALTO//2), (ANCHO//2, ALTO//2+y))
    for y in range(0, ALTO // 2 + 1, 10):
        colorAleatorio = generarColor()
        pygame.draw.line(ventana, colorAleatorio,(ANCHO // 2, ALTO // 2 - y),(ANCHO - y, ALTO // 2) )
    for y in range(0, ALTO // 2 + 1, 10):
        xFinal = y + 10
        colorAleatorio = generarColor()
        pygame.draw.line(ventana, colorAleatorio, (ANCHO // 2, ALTO // 2 + y),(0 + y, ALTO // 2))

def dibujarEstrella():
    pygame.init()
    ventana = pygame.display.set_mode((ANCHO, ALTO))
    reloj = pygame.time.Clock()
    termina = False

    while not termina:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:  # El usuario hizo click en el botón de salir
                termina = True      # Queremos terminar el ciclo


        ventana.fill(BLANCO)

        dibujarLineasEstrella(ventana)
        pygame.display.flip()  # Actualiza trazos (Si no llamas a esta función, no se dibuja)
        reloj.tick(40)  # 40 fps

    pygame.quit()

#Funciones para Figura 3
def dibujarDoceCirculos(ventana):
    for alfa in range(30,390,30):
        angRadianes= math.radians(alfa)
        x=150*math.cos(angRadianes)
        y= 150*math.sin(angRadianes)
        pygame.draw.circle(ventana, NEGRO, (int(x+ANCHO//2), int(ALTO//2-y)),150, 1)

def dibujarCirculos():
    pygame.init()
    ventana = pygame.display.set_mode((ANCHO, ALTO))
    reloj = pygame.time.Clock()
    termina = False

    while not termina:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:  # El usuario hizo click en el botón de salir
                termina = True      # Queremos terminar el ciclo


        ventana.fill(BLANCO)

        dibujarDoceCirculos(ventana)
        pygame.display.flip()  # Actualiza trazos (Si no llamas a esta función, no se dibuja)
        reloj.tick(40)  # 40 fps

    pygame.quit()

#Calcular el valor aproximado de Pi
def aproximarPI(n):
    suma=0
    for d in range (1,n+1): #1,2,3.. n
        fraccion= 1/ d**2
        suma+=fraccion

    aproxPI= (6*suma)**0.5
    return aproxPI #Falta el print

#Contar números de cuatro dígitos que sean divisibles entre 37
def calcularNumeros37():
    cantidadNum=0
    for num in range (1000, 10000):
        if num%37==0:
            cantidadNum+=1
    return cantidadNum

#Imprimir pirámides de números
def dibujarpiramidesNum():
    piramideUno=0
    for n in range(1,10):
        piramideUno= piramideUno *10+n
        resultadoUno= piramideUno*8+n
        print(piramideUno,"*8+",n,"=",resultadoUno)

    piramideDos=0
    for digit in range(1,10):
        piramideDos= piramideDos*10+1
        resultadoDos= piramideDos*piramideDos
        print(piramideDos,"*", piramideDos,"=",resultadoDos,)




# Función principal, aquí resuelves el problema
def main():
    print("""Misión 5. Seleccione qué es lo que desea hacer:
    1.Dibujar Cuadros y Círculos
    2.Dibujar Parábolas
    3.Dibujar Círculos
    4.Aproximar Pi
    5.Contar divisibles entre 37
    6.Imprimir pirámides de Números
    0.Salir
""")
    decision = 7
    while decision != 0:
        decision = int(input("Teclee el número de la acción que desea hacer y presione Enter: "))
        if decision == 1:
            dibujarCircyCu()
            print("Si desea ejecutar otra acción: ")
        elif decision == 2:
            dibujarEstrella()
            print("Si desea ejecutar otra acción: ")
        elif decision == 3:
            dibujarCirculos()
            print("Si desea ejecutar otra acción: ")
        elif decision == 4:
            n=int(input("Introduce un número para aproximar:"))
            aproximarPI(n)
            pi=aproximarPI(n)
            print(pi)
            print("Si desea ejecutar otra acción: ")
        elif decision == 5:
            calcularNumeros37()
            cantidadNum = calcularNumeros37()
            print("La cantidad de números de 4 dígitos divisibles entre 37 son:", cantidadNum)
            print("Si desea ejecutar otra acción: ")
        elif decision == 6:
            dibujarpiramidesNum()
            print("Si desea ejecutar otra acción: ")
        elif decision <0 or decision>6:
            print("""El número ingresado no es válido.             
Teclee un número válido Ó 0 para salir del programa""")
    print("Hasta luego")






# Llamas a la función principal
main()