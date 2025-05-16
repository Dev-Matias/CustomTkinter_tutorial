memoria = 0.0  # Inicializamos la memoria en 0.0 para trabajar con números de punto flotante

def mr():
  """Recupera el valor de la memoria."""
  return memoria

def m_plus(valor_actual):
  """Suma el valor actual a la memoria."""
  global memoria  # Indicamos que vamos a modificar la variable global memoria
  memoria += valor_actual
  print(f"Memoria actualizada: {memoria}") # Opcional: mostrar la memoria

def m_minus(valor_actual):
  """Resta el valor actual de la memoria."""
  global memoria  # Indicamos que vamos a modificar la variable global memoria
  memoria -= valor_actual
  print(f"Memoria actualizada: {memoria}") # Opcional: mostrar la memoria

# Ejemplo de uso:
print(f"Valor inicial de la memoria: {memoria}")

m_plus(10.5)
m_plus(5)
print(f"Valor actual en memoria después de M+: {mr()}")

m_minus(3)
print(f"Valor actual en memoria después de M-: {mr()}")

print(f"Recuperando el valor de la memoria con MR: {mr()}")