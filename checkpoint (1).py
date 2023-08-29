# Importante: No modificar ni el nombre ni los argumetos que reciben las funciones, sólo deben escribir
# código dentro de las funciones ya definidas.

def numeroBinario(numero):
    '''
    Esta función recibe como argumento un número entero mayor ó igual a cero y lo devuelve en su 
    representación binaria. Debe recibir y devolver un valor de tipo entero.
    En caso de que el parámetro no sea de tipo entero y mayor a -1 debe retornar nulo.
    Recibe un argumento:
        numero: Será el número que se convertirá a binario.
    Ej:
        NumeroBinario(12) debe retornar 1100
        NumeroBinario(2) debe retornar 10
        NumeroBinario(14) debe retornar 1110
    '''
    #Tu código aca:
    if type(numero) == int and numero >= 0:
         resto_lista = []
         while numero >= 1: 
            resto = numero % 2
            resto_lista.append(str(resto))
            numero = numero // 2 
         resto_lista.reverse()
         resto_cadena = "".join(resto_lista)
         return int(resto_cadena)
         
    else:
         return None

def dividirMultiplicar(lista):
   '''
   La función recibe como argumento una lista de números enteros, y debe retornar una lista con 
   los siguientes parámetros:
   1.Los números que sean positivos y pares se deben dividir por 2, y el resultado expresado 
   como entero (sin decimales, no redondeando, debe tomar sólo la parte entera de la división por 2).
   2.Los números negativos multiplicados por 2.
   3.Los que no cumplan los criterios anteriores deben quedar igual al valor original.
   4.Ordernar los números de mayor a menor.
   Ej: dividirMultiplicar([2,4,1,-3]): debe retornar: [2, 1, 1, -6]
   '''   
   #Tu código acá
   lista_nueva = []
   for element in lista:
         
         if element>=2 and element % 2 ==0:
            elemento_nuevo = element//2
            lista_nueva.append(elemento_nuevo)
         elif element < 0:
            elemento_nuevo = element*2
            lista_nueva.append(elemento_nuevo)
         else:
            elemento_nuevo = element 
            lista_nueva.append(elemento_nuevo) 

   lista_nueva_ordenada = sorted((lista_nueva),reverse = True)
   return lista_nueva_ordenada

def crearDiccionario(lista):
   '''
   La función recibe como argumento una lista de números enteros, y debe retornar un diccionario con tres claves, "multiplos3", 'cuadrados", "menores_promedio".
   Para la clave "multiplos3", el valor debe ser una lista con los múltiplos de 3 de la lista original.
   Para la clave "cuadrados", el valor debe ser una lista con los valores de la lista original elevados al cuadrado.
   Para la clave "menores_promedio", el valor debe ser una lista con los valores menores al promedio de la lista original.
   EJ: crearDiccionario([3,6,7,12]): debe retornar: {'multiplos3': [3, 6, 12], 'cuadrados': [9, 36, 49, 144], 'menores_promedio': [3, 6]}
   '''
   #Tu código acá
   diccionario = {"multiplos3": [] , "cuadrados":[]  , "menores_promedio": [] }
   promedio = sum(lista)/len(lista)
   for numero in lista:
      diccionario["cuadrados"].append(numero ** 2)
      if numero % 3 ==0:
         diccionario["multiplos3"].append(numero)
      if numero < promedio:
         diccionario["menores_promedio"].append(numero)
   return diccionario
   

def trianguloRectangulo(a,b,c):
   '''
   La función debe recibir como argumentos el valor en cm de los lados de un triángulo (a y b son los catetos), 
   y dado estos valores, retornar True si en efecto corresponden a un triángulo rectángulo, 
   o False en caso contrario. Sólo se debe poder pasar valores enteros como argumentos de la función,
     caso contrario debe retornar nulo.
   EJ: trianguloRectangulo(3.5,3.5,2.4), debe retornar nulo
   EJ: trianguloRectangulo(3,3,3), debe retornar False
   EJ: trianguloRectangulo(3,4,5), debe retornar True
   '''
   #Tu código acá
   if type(a)==int and type(b)==int and type(c)==int:
      return c**2 == b**2 + a**2
   else:
      return None
   

def ciudadesPoblacion(diccionario):
   '''
   Dado el siguiente diccionario ciudades, la función debe retornar una lista de listas, donde cada elemento de la lista sea una lista con el par ['ciudad', población], pero sólo de las ciudades que comiencen con la letra 'B', y como último elemento de la lista el par ['promedio', promedio de población] con el promedio de población de las ciudades seleccionadas.
   Ej: Si se pidiera ciudades que comiencen con la letra 'S', debe devolver: [['São Paulo', 21048514], ['Santiago de Chile', 7112808],['promedio', 14080661.0]]

   ciudades = {
      'São Paulo': 21048514,
      'Buenos Aires': 14975587,
      'Río de Janeiro': 11902701,
      'Bogotá': 10777931,
      'Lima': 10479899,
      'Santiago de Chile': 7112808,
      'Belo Horizonte': 6006091,
      'Caracas': 5622798,
      'Brasília': 4291577
      }
      Pista: investigar método de string startswith()
   '''
   #Tu código acá
   ciudades = {
         'São Paulo': 21048514,
         'Buenos Aires': 14975587,
         'Río de Janeiro': 11902701,
         'Bogotá': 10777931,
         'Lima': 10479899,
         'Santiago de Chile': 7112808,
         'Belo Horizonte': 6006091,
         'Caracas': 5622798,
         'Brasília': 4291577}

   lista_pedida = []
   acumulador = 0
   for key, value in ciudades.items():
         if key.startswith('B')== True:
               lista_pedida.append([key, value])
               acumulador = acumulador + value     
   lista_pedida.append(['promedio', acumulador/len(lista_pedida)])
   return lista_pedida



def ordenarPalabras(palabras):
   '''
   La función recibe como argumento una secuencia de palabras unidas por guiones, 
   y debe retornar las mismas palabras, unidas por guiones, pero en orden alfabético.
     Si el argumento que se le pasa no es un string o no contiene guiones, debe retornar nulo.
   EJ: ordenarPalabras('saco-libro-casa') debe retornar 'casa-libro-saco'
   EJ: ordenarPalabras('Hola') debe retornar nulo
   Pista: investigar métodos de string
   '''
   #Tu código acá
   if type(palabras) == str and '-' in palabras:
      lista_palabras = palabras.split('-')
      lista_palabras.sort()
      return "-".join(lista_palabras)
   else:
      return None

def stringEspejo(texto):
    '''
    La función recibe como argumento una cadena de texto y retorna la cadena invertida, pero sólo
      si tiene más de tres caracteres, sino debe retornar nulo.
    EJ: stringEspejo('Hola Mundo') debe retornar 'odnuM aloH'
    EJ: stringEspejo('Hoy') debe retornar nulo
    '''
    #Tu código acá
    if len(texto)>3:
      cadena_invertida = ""
      texto[::-1]
      for letra in texto:
         cadena_invertida = letra + cadena_invertida
      return cadena_invertida
    else:
      return None
    
