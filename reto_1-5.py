def anagrama(lista):
  # Lista auxiliar donde se guardarán las palabras convertidas en listas de letras ordenadas
  lista_2 = []
  
  # Lista final donde se almacenarán las palabras que son anagramas entre sí
  lista_final = []

  # Recorre cada palabra de la lista original
  for palabra in lista:
    # Lista temporal para almacenar las letras de la palabra actual
    letras = []
    
    # Separa cada letra de la palabra y la agrega a la lista "letras"
    for letra in palabra:
      letras.append(letra)
    
    # Ordena las letras de la palabra alfabéticamente
    letras.sort()
    
    # Agrega la lista de letras ordenadas a "lista_2"
    lista_2.append(letras)

  # Compara cada palabra con todas las demás usando sus versiones ordenadas
  for i in range(len(lista)):

    for j in range(len(lista)):
      
      # Verifica que no sea la misma posición y que tengan las mismas letras ordenadas
      if i != j and lista_2[i] == lista_2[j]:
        # Si son iguales, significa que son anagramas, así que se agrega la palabra original
        lista_final.append(lista[i])
  
  # Retorna la lista con las palabras que tienen al menos un anagrama en la lista original
  return lista_final


# Prueba:
lista1 = ["amor", "roma", "perro", "gato"]
resultado = anagrama(lista1)
print(resultado)