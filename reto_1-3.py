def lista(x,y):
  # Se reciben dos valores: x (inicio del rango) y y (fin del rango)
  x = x
  y = y
  
  # Lista donde se almacenarán los números primos encontrados
  Lista_primos = []
  
  # Se recorre cada número dentro del rango desde x hasta y (sin incluir y)
  for n in range(x,y):
    # Se asume inicialmente que el número es primo
    primo = True
    
    # Se verifica si el número tiene divisores distintos de 1 y él mismo
    for i in range(2,n):
      # Si el número es divisible por i, no es primo
      if n%i == 0:
        primo = False

    # Si después de verificar no se encontraron divisores, se considera primo
    if primo:
      # Se agrega el número primo a la lista
      Lista_primos.append(n)
  
  # Se retorna la lista con todos los números primos encontrados en el rango
  return Lista_primos


#prueba:
lista1 = lista(5,20)
print(lista1)