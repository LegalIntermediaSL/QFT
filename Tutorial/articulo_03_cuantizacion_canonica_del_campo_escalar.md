# Articulo 3: Cuantizacion Canonica del Campo Escalar Libre

## Introduccion

El campo escalar libre es la puerta de entrada clasica a la Teoria Cuantica de Campos. Es el ejemplo mas simple en el que puede verse, con formulas concretas, como un campo clasico se transforma en un objeto cuantico capaz de crear y aniquilar particulas.

## 1. Punto de partida clasico

Consideremos la densidad lagrangiana:

`L = 1/2 partial_mu phi partial^mu phi - 1/2 m^2 phi^2`

De las ecuaciones de Euler-Lagrange se obtiene:

`(partial_mu partial^mu + m^2) phi = 0`

El campo `phi(x)` puede expandirse en modos de Fourier. Cada modo se comporta de forma analoga a un oscilador armonico.

## 2. Momento conjugado

En cuantizacion canonica se identifica primero el momento conjugado al campo:

`pi(x) = partial L / partial (partial_0 phi) = dot phi(x)`

El par `(phi, pi)` juega un papel similar al de posicion y momento en mecanica cuantica ordinaria.

## 3. Promocion a operadores

El paso cuantico consiste en promover `phi` y `pi` a operadores que satisfacen relaciones de conmutacion a tiempo igual:

`[phi(t,x), pi(t,y)] = i delta^3(x-y)`

y

`[phi(t,x), phi(t,y)] = [pi(t,x), pi(t,y)] = 0`

Estas relaciones codifican la estructura cuantica del sistema.

## 4. Expansion en modos

El campo cuantizado se escribe tipicamente como:

`phi(x) = integral d^3p [ a(p) exp(-ipx) + a^dagger(p) exp(ipx) ]`

omitiendo factores de normalizacion para resaltar la estructura.

Aqui:

- `a(p)` actua como operador de aniquilacion;
- `a^dagger(p)` actua como operador de creacion.

No son simples artificios algebraicos. Son los objetos que permiten construir el espacio de estados de la teoria.

## 5. Vacio y estados de particulas

Se define un estado de vacio `|0>` por la condicion:

`a(p) |0> = 0`

para todo `p`.

Aplicando operadores de creacion se generan estados excitados:

`a^dagger(p) |0>`

representa un estado de una particula con momento `p`, mientras que productos sucesivos de operadores de creacion generan estados de muchas particulas.

Este es el momento conceptual clave: el espacio de Hilbert de la teoria ya no describe una sola particula, sino sectores con numero variable de excitaciones.

## 6. Hamiltoniano

El hamiltoniano del campo libre puede reescribirse en terminos de los operadores `a` y `a^dagger`. Su forma revela que el sistema equivale a una coleccion infinita de osciladores armonicos cuanticos desacoplados, uno por cada modo de momento.

Esto explica por que la cuantizacion del campo escalar resulta manejable:

- cada modo se cuantiza como un oscilador;
- el campo completo se obtiene al reunir todos los modos;
- las particulas aparecen como cuantos de excitacion de esos osciladores.

## 7. Interpretacion fisica

La cuantizacion canonica del campo escalar deja varias ideas firmes:

- el campo es el objeto fundamental;
- las particulas son excitaciones del campo;
- el vacio es el estado base del conjunto;
- la creacion y aniquilacion de particulas se incorpora de manera natural.

Con esto queda preparada la entrada a teorias mas ricas, donde aparecen espin, gauge, fermiones e interacciones.

## 8. Limites del caso libre

Aunque pedagogicamente esencial, el campo libre no contiene toda la fisica interesante. No describe dispersion realista, decaimientos ni correcciones radiativas. Para eso hay que introducir terminos de interaccion y pasar a metodos perturbativos o no perturbativos.

Sin embargo, el caso libre es irrenunciable porque establece:

- el lenguaje de operadores;
- la definicion de vacio y estados;
- la interpretacion de los cuantos del campo.

## Cierre

Aprender bien el campo escalar libre equivale a aprender el alfabeto de la QFT. No contiene toda la literatura, pero sin ese alfabeto el resto del idioma se vuelve innecesariamente opaco.
