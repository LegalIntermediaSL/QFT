# Oscilador Armonico Cuantico

**Nivel:** Fundacional  
**Dificultad:** Media  
**Tiempo estimado:** 25-35 min  
**Prerequisitos recomendados:** [Notacion Tensorial y Convenciones](02_notacion_tensorial_y_convenciones.md) · [Resumen del modulo](README.md)


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

Conviene detenerse en un punto conceptual: este sistema no es importante solo porque sea soluble, sino porque es el ejemplo universal de pequenas oscilaciones alrededor de un equilibrio. Cuando un sistema mas complicado se linealiza cerca de un minimo de energia, el primer comportamiento que emerge es precisamente el de un conjunto de osciladores armonicos desacoplados. En QFT, al expandir un campo libre en modos de Fourier, cada modo juega exactamente ese papel.

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

Si uno resolviera el problema directamente en representacion de posicion, encontraria una ecuacion diferencial perfectamente tratable. Pero la forma algebraica del problema es mucho mas valiosa para QFT, porque hace visible como se organiza el espectro en niveles discretos y como aparecen naturalmente operadores que cambian el numero de excitaciones.

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

La eleccion de coeficientes no es arbitraria. Se fija de manera que:

- $a$ y $a^\dagger$ sean adimensionales;
- el algebra tome una forma elemental;
- el hamiltoniano quede expresado en terminos del operador numero.

## 5. Hamiltoniano en forma algebraica

Con estos operadores, el hamiltoniano se reescribe como

$$
H = \omega\left(a^\dagger a + \frac{1}{2}\right).
$$

Esta expresion deja visible la estructura espectral del sistema.

Si definimos

$$
N = a^\dagger a,
$$

entonces

$$
[N,a^\dagger]=a^\dagger,
\qquad
[N,a]=-a,
$$

lo que muestra que $a^\dagger$ aumenta en una unidad el numero de excitacion y $a$ lo disminuye en una unidad.

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

La lectura fisica de esta formula es muy instructiva:

- $n$ cuenta cuantos cuantos de excitacion contiene el sistema;
- el termino $\frac{1}{2}\omega$ indica que incluso el estado base tiene energia no nula.

## 7. Cuanto de excitacion

La gran leccion conceptual del oscilador cuantico es que la energia se organiza en cuantos discretos. Cada aplicacion de $a^\dagger$ aumenta la energia en una unidad $\omega$.

En QFT, esa estructura se traslada a cada modo del campo:

- el vacio del campo juega el papel de estado fundamental;
- los operadores de creacion excitan modos;
- esas excitaciones son las particulas.

Por eso en teoria cuantica de campos una particula libre puede entenderse como el cuanto elemental asociado a un modo del campo. No es una entidad añadida desde fuera del formalismo, sino una excitacion de su estructura cuantizada.

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

Aqui ocurre un cambio de perspectiva importante. En mecanica cuantica de una particula solemos preguntar por la amplitud de encontrar la particula en cierta region. En el lenguaje de numero de ocupacion, en cambio, preguntamos cuantas excitaciones hay en cada modo disponible. Esa reorganizacion conceptual es la que hace natural el numero variable de particulas.

## 9. Por que este ejemplo es central para QFT

Un campo libre puede entenderse como una coleccion infinita de osciladores, uno por cada modo de momento. Por eso, casi todo el lenguaje de la cuantizacion canonica de campos ya esta contenido en miniatura aqui:

- vacio;
- excitaciones discretas;
- operadores de creacion y aniquilacion;
- base de numero de ocupacion.

Mas explicitamente, al cuantizar un campo libre, el hamiltoniano adopta la forma de una suma o integral de osciladores independientes, uno por cada momento:

$$
H \sim \int d^3p \, \omega_{\mathbf p}\left(a^\dagger_{\mathbf p} a_{\mathbf p} + \frac{1}{2}\right).
$$

La diferencia con el oscilador ordinario no es estructural, sino que ahora existe un continuo de modos.

## 10. Energia de punto cero

El termino

$$
\frac{1}{2}\omega
$$

del estado fundamental muestra que incluso el vacio del oscilador tiene energia no nula. Esta observacion es la semilla conceptual de la energia de vacio en teoria de campos, donde una coleccion infinita de modos produce cuestiones mucho mas sutiles.

En muchos contextos no gravitatorios importan solo diferencias de energia, y por eso puede parecer que esta constante no tiene consecuencias. Aun asi, desde el punto de vista conceptual es esencial, porque anticipa que el vacio cuantico no es un estado trivial ni carente de estructura.

## 11. Preguntas de estudio

- Por que los operadores $a$ y $a^\dagger$ simplifican tanto el problema.
- Que representa el operador numero.
- Por que el vacio del oscilador no tiene energia cero.
- Como se conecta este sistema con la cuantizacion de un campo libre.
- Que cambia al pasar de una descripcion en posicion a una descripcion en numero de ocupacion.

## 12. Ejercicios sugeridos

1. Verifica que $[a,a^\dagger]=1$ a partir de $[x,p]=i$.
2. Reescribe el hamiltoniano del oscilador usando $a$ y $a^\dagger$.
3. Explica por que cada modo de un campo libre se comporta como un oscilador armonico cuantico.
4. Demuestra que $a|n\rangle \propto |n-1\rangle$ y $a^\dagger|n\rangle \propto |n+1\rangle$.
5. Explica por que el estado fundamental no puede tener energia menor que $\frac{1}{2}\omega$.

## 13. Cierre

El oscilador armonico cuantico es el alfabeto algebraico de la QFT. Entenderlo bien reduce enormemente la dificultad conceptual del paso a los campos cuanticos.

Si este capitulo queda firme, el resto de la cuantizacion canonica resulta mucho menos intimidante: vacio, operadores modales, espacio de Fock y particulas aparecen como extensiones naturales de una estructura que ya estaba presente aqui.

## 14. Referencias y lecturas recomendadas

- Base: cualquier curso estandar de mecanica cuantica con operadores de creacion y aniquilacion.
- Complementaria: Zee o Tong para el puente entre oscilador y cuantizacion de campos.
- Profundizacion: textos de mecanica cuantica con enfasis en espacio de Fock y operadores numero.


---

## Navegacion del tutorial

[(anterior) Notacion Tensorial y Convenciones](02_notacion_tensorial_y_convenciones.md) | [(siguiente) Simetrias y Grupos Basicos](04_simetrias_y_grupos_basicos.md)