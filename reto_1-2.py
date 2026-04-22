def palindromo(palabra: str):
  # Inicializa los índices en los extremos de la palabra.
  left = 0
  right = len(palabra) - 1
  
  # Los caracteres se comparan desde los extremos hacia el centro.
  while left < right:
    # Si los caracteres no coinciden, no es un palíndromo.
    
    if palabra[left] != palabra[right]:
      print(f"La palabra {palabra} no es un palíndromo")

    else: 
      # Si coinciden, muévase hacia el centro.
      left += 1
      right -= 1
      # Si la palabra original es igual a la palabra invertida, es un palíndromo.
      print(f"La palabra {palabra} es un palíndromo")


# Prueba:
palindromo("radar")

