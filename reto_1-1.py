def calculadora_simple(x: float, y: float, operacion: str):
#Se evalúa el tipo de operación ingresada por el usuario

  if operacion == "+": 
    # Devuelve la suma de x e y.
    return x + y
  
  elif operacion == "-":
    # Devuelve la diferencia entre x e y.
    return x - y
  
  elif operacion == "/":
    # Devuelve el cociente de x e y, siempre que y no sea cero para evitar errores de división por cero.
    return x / y
  
  elif operacion == "*":
    # Devuelve el producto de x e y.
    return x * y
  
  else:
    print("Operación no válida. Por favor, ingrese una operación válida (+, -, /, *).")


# Prueba:
result = calculadora_simple(10, 5, "+")
print(result)