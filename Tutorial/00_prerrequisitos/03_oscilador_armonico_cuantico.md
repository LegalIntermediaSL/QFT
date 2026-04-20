# Oscilador Armonico Cuantico

## 1. Proposito

El oscilador armonico cuantico es probablemente el ejemplo mas importante de toda la mecanica cuantica para quien quiera estudiar QFT. La razon es profunda: un campo libre puede descomponerse en modos, y cada modo se comporta como un oscilador armonico cuantico.

## 2. Oscilador armonico clasico

El sistema clasico se describe por el hamiltoniano

$$
H = \frac{p^2}{2m} + \frac{1}{2}m\omega^2 x^2.
$$

La ecuacion de movimiento es

$$
\ddot{x} + \omega^2 x = 0,
$$

y sus soluciones son oscilatorias con frecuencia $\omega$.

## 3. Cuantizacion

En mecanica cuantica se promueven posicion y momento a operadores con

$$
[x,p]=i\hbar.
$$

En unidades naturales se suele tomar $\hbar=1$, quedando

$$
[x,p]=i.
$$

El hamiltoniano conserva la misma forma formal, pero ahora actua sobre estados del espacio de Hilbert.

## 4. Operadores de subida y bajada

Se introducen los operadores

$$
a = \sqrt{\frac{m\omega}{2}}\,x + \frac{i}{\sqrt{2m\omega}}\,p,
$$

$$
a^\dagger = \sqrt{\frac{m\omega}{2}}\,x - \frac{i}{\sqrt{2m\omega}}\,p,
$$

que satisfacen

$$
[a,a^\dagger]=1.
$$

Estos operadores reorganizan el problema de forma mucho mas elegante que resolver directamente la ecuacion diferencial de Schrodinger.

## 5. Hamiltoniano en forma algebraica

Con estos operadores, el hamiltoniano se reescribe como

$$
H = \omega\left(a^\dagger a + \frac{1}{2}\right).
$$

Esta expresion deja visible la estructura espectral del sistema.

## 6. Estado fundamental y excitaciones

Se define el estado fundamental $|0\rangle$ por

$$
a|0\rangle = 0.
$$

Los estados excitados se construyen aplicando sucesivamente $a^\dagger$:

$$
|n\rangle \propto (a^\dagger)^n|0\rangle.
$$

Los autovalores de energia son

$$
E_n = \omega\left(n+\frac{1}{2}\right),
\qquad n=0,1,2,\ldots
$$

## 7. Cuanto de excitacion

La gran leccion conceptual del oscilador cuantico es que la energia se organiza en cuantos discretos. Cada aplicacion de $a^\dagger$ aumenta la energia en una unidad $\omega$.

En QFT, esa estructura se traslada a cada modo del campo:

- el vacio del campo juega el papel de estado fundamental;
- los operadores de creacion excitan modos;
- esas excitaciones son las particulas.

## 8. Numero de ocupacion

El operador

$$
N = a^\dagger a
$$

cuenta el numero de excitaciones del oscilador:

$$
N|n\rangle = n|n\rangle.
$$

Esta idea de numero de ocupacion es crucial para el paso al espacio de Fock en QFT.

## 9. Por que este ejemplo es central para QFT

Un campo libre puede entenderse como una coleccion infinita de osciladores, uno por cada modo de momento. Por eso, casi todo el lenguaje de la cuantizacion canonica de campos ya esta contenido en miniatura aqui:

- vacio;
- excitaciones discretas;
- operadores de creacion y aniquilacion;
- base de numero de ocupacion.

## 10. Energia de punto cero

El termino

$$
\frac{1}{2}\omega
$$

del estado fundamental muestra que incluso el vacio del oscilador tiene energia no nula. Esta observacion es la semilla conceptual de la energia de vacio en teoria de campos, donde una coleccion infinita de modos produce cuestiones mucho mas sutiles.

## 11. Preguntas de estudio

- Por que los operadores $a$ y $a^\dagger$ simplifican tanto el problema.
- Que representa el operador numero.
- Por que el vacio del oscilador no tiene energia cero.
- Como se conecta este sistema con la cuantizacion de un campo libre.

## 12. Ejercicios sugeridos

1. Verifica que $[a,a^\dagger]=1$ a partir de $[x,p]=i$.
2. Reescribe el hamiltoniano del oscilador usando $a$ y $a^\dagger$.
3. Explica por que cada modo de un campo libre se comporta como un oscilador armonico cuantico.

## 13. Cierre

El oscilador armonico cuantico es el alfabeto algebraico de la QFT. Entenderlo bien reduce enormemente la dificultad conceptual del paso a los campos cuanticos.

## 14. Referencias y lecturas recomendadas

- Base: cualquier curso estandar de mecanica cuantica con operadores de creacion y aniquilacion.
- Complementaria: Zee o Tong para el puente entre oscilador y cuantizacion de campos.
- Profundizacion: textos de mecanica cuantica con enfasis en espacio de Fock y operadores numero.


---

## Navegacion del tutorial

[(anterior) Notacion Tensorial y Convenciones](02_notacion_tensorial_y_convenciones.md) | [(siguiente) Simetrias y Grupos Basicos](04_simetrias_y_grupos_basicos.md)
