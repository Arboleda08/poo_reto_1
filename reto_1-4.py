def mayor_suma(lista): 
  # Lista donde se almacenarán las sumas de pares consecutivos
  lista_final = []
  
  # Recorre la lista hasta el penúltimo elemento
  for i in range(len(lista)-1):
    # Suma el elemento actual con el siguiente
    suma = lista[i] + lista[i+1]
    
    # Agrega la suma a la lista de resultados
    lista_final.append(suma)
  
  # Obtiene el valor máximo de todas las sumas calculadas
  mayor = max(lista_final)
  
  # Retorna la mayor suma de pares consecutivos
  return mayor


# Prueba:
lista1 = [1, 2, 3, 4, 5]
resultado = mayor_suma(lista1)
print(resultado)
