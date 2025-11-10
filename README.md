# Programación Orientada a Objetos

## 1. Conceptos Fundamentales

La **Programación Orientada a Objetos (POO)** organiza el código alrededor de objetos que contienen datos y comportamientos. Los pilares principales son:

- **Encapsulación**: Ocultar los detalles internos de una clase
- **Herencia**: Crear nuevas clases basadas en clases existentes
- **Polimorfismo**: Mismo interfaz, diferentes implementaciones
- **Abstracción**: Definir interfaces sin implementación completa

## 2. Clases y Objetos

### Definición básica de una clase:

```python
class Punto:
    def __init__(self, x=0, y=0):
        self.__x = x  # Atributo privado
        self.__y = y
    
    def get_x(self):
        return self.__x
    
    def set_x(self, x):
        self.__x = x
    
    def mostrar_datos(self):
        print(f"(x,y) = ({self.__x}, {self.__y})")

# Uso
punto1 = Punto(3, 4)
punto1.mostrar_datos()  # (x,y) = (3, 4)
```

## 3. Encapsulación y Visibilidad

```python
class CuentaBancaria:
    def __init__(self, titular, saldo_inicial=0):
        self.__titular = titular      # Privado
        self.__saldo = saldo_inicial  # Privado
        self._tipo = "Ahorro"         # Protegido
    
    def depositar(self, monto):
        if monto > 0:
            self.__saldo += monto
    
    def get_saldo(self):
        return self.__saldo

cuenta = CuentaBancaria("Juan", 1000)
# cuenta.__saldo  # Error - atributo privado
print(cuenta.get_saldo())  # 1000
```

## 4. Herencia

```python
class Animal:
    def __init__(self, nombre):
        self.nombre = nombre
    
    def hacer_sonido(self):
        pass  # Método abstracto

class Perro(Animal):
    def __init__(self, nombre, raza):
        super().__init__(nombre)
        self.raza = raza
    
    def hacer_sonido(self):
        return "¡Guau!"

class Gato(Animal):
    def hacer_sonido(self):
        return "¡Miau!"

perro = Perro("Fido", "Labrador")
gato = Gato("Whiskers")
print(perro.hacer_sonido())  # ¡Guau!
print(gato.hacer_sonido())   # ¡Miau!
```

## 5. Polimorfismo

```python
class Circulo:
    def __init__(self, radio):
        self.radio = radio
    
    def area(self):
        return 3.1416 * self.radio ** 2

class Cuadrado:
    def __init__(self, lado):
        self.lado = lado
    
    def area(self):
        return self.lado ** 2

# Polimorfismo en acción
def calcular_area_total(figuras):
    return sum(figura.area() for figura in figuras)

figuras = [Circulo(5), Cuadrado(4), Circulo(3)]
print(f"Área total: {calcular_area_total(figuras)}")
```

## 6. Métodos Especiales

```python
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __str__(self):
        return f"Vector({self.x}, {self.y})"
    
    def __add__(self, otro):
        return Vector(self.x + otro.x, self.y + otro.y)
    
    def __eq__(self, otro):
        return self.x == otro.x and self.y == otro.y

v1 = Vector(2, 3)
v2 = Vector(1, 1)
v3 = v1 + v2
print(v3)        # Vector(3, 4)
print(v1 == v2)  # False
```

## 7. Relaciones entre Clases

### Asociación:
```python
class Estudiante:
    def __init__(self, nombre):
        self.nombre = nombre
        self.cursos = []

class Curso:
    def __init__(self, nombre):
        self.nombre = nombre

estudiante = Estudiante("Ana")
curso = Curso("Matemáticas")
estudiante.cursos.append(curso)
```

### Composición:
```python
class Motor:
    def __init__(self, tipo):
        self.tipo = tipo

class Auto:
    def __init__(self, marca, tipo_motor):
        self.marca = marca
        self.motor = Motor(tipo_motor)  # Composición

auto = Auto("Toyota", "V6")
```

## 8. Manejo de Excepciones

```python
class SaldoInsuficienteError(Exception):
    def __init__(self, saldo, monto):
        super().__init__(f"Saldo insuficiente: {saldo} para retirar {monto}")
        self.saldo = saldo
        self.monto = monto

class Cuenta:
    def __init__(self, saldo_inicial):
        self.saldo = saldo_inicial
    
    def retirar(self, monto):
        if monto > self.saldo:
            raise SaldoInsuficienteError(self.saldo, monto)
        self.saldo -= monto

try:
    cuenta = Cuenta(100)
    cuenta.retirar(150)
except SaldoInsuficienteError as e:
    print(f"Error: {e}")
```

## 9. Colecciones de Objetos

```python
class GestorPersonas:
    def __init__(self):
        self.__personas = []
    
    def agregar_persona(self, persona):
        self.__personas.append(persona)
    
    def buscar_por_dni(self, dni):
        for persona in self.__personas:
            if persona.dni == dni:
                return persona
        return None
    
    def listar_personas(self):
        for persona in self.__personas:
            print(persona)

class Persona:
    def __init__(self, dni, nombre, apellido):
        self.dni = dni
        self.nombre = nombre
        self.apellido = apellido
    
    def __str__(self):
        return f"{self.apellido}, {self.nombre} (DNI: {self.dni})"
```

## 10. Métodos de Clase y Estáticos

```python
class Utilidades:
    contador = 0  # Variable de clase
    
    def __init__(self):
        Utilidades.contador += 1
    
    @classmethod
    def obtener_contador(cls):
        return cls.contador
    
    @staticmethod
    def es_numero_par(numero):
        return numero % 2 == 0

print(Utilidades.es_numero_par(4))  # True
util1 = Utilidades()
util2 = Utilidades()
print(Utilidades.obtener_contador())  # 2
```

# Estructura de Datos y Algoritmos

## 1. PILA (Stack) - LIFO

### Teoría
Una pila es una estructura de datos que sigue el principio **LIFO** (Last In, First Out - Último en Entrar, Primero en Salir). Los elementos se insertan y eliminan siempre por el mismo extremo, llamado **tope**.

**Operaciones principales:**
- `insertar(x)`: Agrega un elemento al tope
- `suprimir()`: Elimina y retorna el elemento del tope
- `vacía()`: Verifica si la pila está vacía
- `recorrer()`: Procesa todos los elementos

### Aplicaciones
- Verificación de paréntesis balanceados
- Evaluación de expresiones
- Mecanismo de "deshacer" en aplicaciones
- Recursión (call stack)

### Implementación en Python (Representacion Secuencial)

```python
import numpy as np

class PILA:
    __PILA: np.array
    __tope: int
    def __init__(self, dimension = 5):
        self.__dimension = dimension
        self.__tope = -1
        self.__PILA = np.empty(self.__dimension, dtype = int)
    def insertar(self, num):
        resultado = 0
        if self.estaVacia():
            self.__tope += 1
            self.__PILA[self.__tope] = num
            resultado = num
        else: 
            if self.estaLlena():
                print("Lista llena")
            else:
                self.__tope += 1
                self.__PILA[self.__tope] = num
                resultado = num
        return resultado 
    def suprimir(self):
        resultado = 0
        if self.estaVacia():
            print("La lista esta vacia")
        else:
            resultado = self.__PILA[self.__tope]
            self.__tope -= 1
        return resultado   
    def recorrer(self):
        i = self.__tope
        while i >= 0:
            print(self.__PILA[i])
            i -= 1
    def estaVacia(self):
        return self.__tope == -1
    def estaLlena(self):
        return self.__tope == self.__dimension - 1

```

## 2. COLA (Queue) - FIFO

### Teoría
Una cola sigue el principio **FIFO** (First In, First Out - Primero en Entrar, Primero en Salir). Los elementos se insertan por un extremo (final) y se eliminan por el otro (frente).

**Operaciones principales:**
- `insertar(x)`: Agrega un elemento al final
- `suprimir()`: Elimina y retorna el elemento del frente
- `vacía()`: Verifica si la cola está vacía
- `recorrer()`: Procesa todos los elementos

### Aplicaciones
- Sistemas de simulación
- Colas de impresión
- Buffers de datos
- Búsqueda en amplitud (BFS)

### Implementación en Python (Representacion Secuencial - Cola Circular)

```python
import numpy as np

class Cola:
    __cola: np.array
    __max: int
    __ui: int
    __pr: int
    __cant: int
    def __init__(self, dimencion = 5):
        self.__max = dimencion
        self.__ui = 0
        self.__pr = 0
        self.__cant = 0
        self.__cola = np.empty(dimencion, dtype = int)
    def vacia(self):
        return self.__cant == 0
    def llena(self):
        return self.__cant == self.__max
    def insertar(self, numero):
        result = None
        if(self.llena()):
            print("La cola esta llena.")
        else:
            self.__cola[self.__ui] = numero
            self.__ui = (self.__ui + 1) % self.__max
            self.__cant += 1
            result = numero
        return result
    def suprimir(self):
        result = None
        if(self.vacia()):
            print("La cola esta vacia.")
        else:
            result = self.__cola[self.__pr]
            self.__cant -= 1
            self.__pr = (self.__pr + 1) % self.__max
        return result
    def recorrer(self):
        if(self.vacia()):
            print("La cola esta vacia.")
        else:
            i = self.__pr
            for _ in range(self.__cant):
                print(self.__cola[i])
                i = (i + 1) % self.__max
```

## 3. LISTA

### Teoría
Una lista es una secuencia ordenada de elementos que puede crecer y contraerse dinámicamente. Permite acceso, inserción y eliminación en cualquier posición.

**Operaciones principales:**
- `insertar(x, pos)`: Inserta elemento en posición específica
- `suprimir(pos)`: Elimina elemento de posición específica
- `recuperar(pos)`: Obtiene elemento de posición específica
- `buscar(x)`: Encuentra posición de elemento
- `vacía()`: Verifica si la lista está vacía

### Implementación en Python (Representacion Secuencial - Ordenada por Contenido)

```python
import numpy as np

class Lista:
    __lista: np.array
    __max: int
    __ult: int
    def __init__(self, dimension = 8):
        self.__ult = 0
        self.__max = dimension
        self.__lista = np.empty(dimension, dtype = int)
    def llena(self):
        return self.__ult == self.__max - 1
    def vacia(self):
        return self.__ult == 0
    def insertar(self, numero):
        result = None
        if(self.llena()):
            print("Lista llena")
        elif(self.vacia()):
            print("Lista vacia, insertando en la primer posicion...")
            self.__lista[self.__ult] = numero
            self.__ult += 1
            result = self.__lista[self.__ult - 1]
        else:
            i = 0
            while i < self.__ult and self.__lista[i] < numero:
                i += 1

            for j in range(self.__ult, i, - 1):
                self.__lista[j] = self.__lista[j - 1]
            
            self.__lista[i] = numero
            self.__ult += 1
        return result
    def suprimir(self, pos):
        result = None
        if(self.vacia()):
            print("Lista vacia.")
        elif(self.__ult < pos - 1):
            print("Posicion invalida.")
        else:
            result = self.__lista[pos - 1]
            for j in range(pos - 1, self.__ult):
                self.__lista[j] = self.__lista[j + 1]
            self.__ult -=1 
        return result
    def recorrer(self):
        i = 0
        while i < self.__ult:
            print(self.__lista[i])
            i += 1
    def buscar(self, elem):
        primero = 0 
        ultimo = self.__ult
        centro = None
        encontrado = False 
        result = None
        while not primero > ultimo and not encontrado:
            centro = (primero + ultimo) // 2
            if(self.__lista[centro] == elem):
                encontrado = True
                result = centro
            elif(self.__lista[centro] < elem):
                primero = centro - 1
            else:
                ultimo = centro + 1
        return result
    def recuperar(self, pos):
        result = None
        if(pos - 1 > self.__ult and pos - 1 < 0):
            print("Posicion invalida o lista vacia")
        else:
            result = self.__lista[pos]
        return result
    def primer(self):
        result = None
        if(self.vacia()):
            print("Lista vacia.")
        else:
            result = self.__lista[0]
        return result
    def ultimo(self):
        result = None
        if(self.vacia()):
            print("La lista esta vacia.")
        else:
            result = self.__lista[self.__ult - 1]
        return result
    def siguiente(self, pos):
        result = None
        if(pos + 1 > self.__ult or pos - 1 < 0):
            print("Posicion invalida")
        else:
            result = self.__lista[pos]
        return result
    def anterior(self, pos):
        result = None
        if(pos - 1 > self.__ult or pos - 2 < 0):
            print("Posicion invalida")
        else:
            result = self.__lista[pos - 2]
        return result

```
