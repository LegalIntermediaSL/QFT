# Transformaciones de Bogoliubov y Cambio de Vacio

## 1. Proposito

Este documento introduce una idea que conecta integral de camino, cuantizacion, espacio-tiempo curvo y el modulo avanzado de informacion y agujeros negros: distintas descomposiciones modales del mismo campo pueden conducir a nociones distintas de vacio y de particula.

## 2. El punto de partida

En QFT, definir particulas equivale a elegir una descomposicion del campo en modos de frecuencia positiva y negativa. Esa eleccion determina operadores de creacion y aniquilacion, y por tanto una nocion de vacio.

Pero esa descomposicion no siempre es unica de forma absoluta. Puede depender del observador, del fondo o de la estructura temporal del problema.

## 3. Transformaciones de Bogoliubov

Dos juegos distintos de modos pueden relacionarse mediante una transformacion de Bogoliubov. Esquematicamente:

$$
a_k' = \alpha_k a_k + \beta_k a_k^\dagger,
$$

con coeficientes que mezclan creacion y aniquilacion.

La presencia de terminos con $a_k^\dagger$ en la transformacion es la señal de que la nueva definicion de partícula no coincide con la anterior.

## 4. Consecuencia fisica

Si el vacio definido por un conjunto de operadores no es aniquilado por el nuevo conjunto, entonces un observador asociado a la segunda descomposicion puede detectar particulas donde el primero describe vacio.

Esta idea no es una rareza matematica. Es la estructura conceptual que aparece en:

- produccion de particulas en fondos variables;
- efecto Unruh;
- radiacion de Hawking;
- teoria cuantica de campos en espacio-tiempo curvo.

## 5. Relacion con el formalismo funcional

Aunque las transformaciones de Bogoliubov suelen introducirse en lenguaje canonico, su interpretacion es muy natural desde el punto de vista funcional:

- cambian la forma en que se organiza la expansion modal;
- modifican la lectura fisica de excitaciones y vacio;
- muestran que la nocion de particula es derivada, no primaria.

Esto enlaza muy bien con el espiritu general del tutorial: los campos son fundamentales, y las particulas dependen de como se leen sus excitaciones.

## 6. Puente con el modulo 11

El efecto Unruh y la radiacion de Hawking no se entienden bien si se cree que el vacio es una nocion absoluta e inmutable. Las transformaciones de Bogoliubov ofrecen justamente el lenguaje para explicar por que:

- distintos observadores no comparten la misma nocion operacional de particula;
- un vacio puede parecer termico desde otra perspectiva;
- la informacion accesible depende de la region y del observador.

## 7. Ejemplo corto de lectura

Si una descomposicion modal mezcla operadores de creacion y aniquilacion de otra descomposicion, ya no estamos hablando del mismo vacio fisico. Esa es la razon profunda por la que "no ver particulas" puede ser una afirmacion dependiente del observador.

## 8. Cuaderno asociado

- `../../Cuadernos/ejemplos/08_entrelazamiento_y_horizontes.ipynb`: usarlo para conectar la dependencia del observador con horizontes y termicidad efectiva.

## 9. Advertencias utiles

- Bogoliubov no significa "crear particulas de la nada" en un sentido ingenuo.
- La nocion de partícula en QFT es contextual, no puramente absoluta.
- No toda diferencia de coordenadas implica por si sola una diferencia fisica en la nocion de vacio; importa la estructura modal y el observador relevante.

## 10. Preguntas de comprobacion

- Por que una transformacion de Bogoliubov mezcla creacion y aniquilacion.
- Que relacion tiene esta mezcla con la no unicidad del vacio.
- Como prepara esto el efecto Unruh y la radiacion de Hawking.

## 11. Referencias y lecturas recomendadas

- Base: Birrell y Davies, transformaciones de Bogoliubov en campos cuanticos.
- Complementaria: reseñas pedagogicas sobre cambio de vacio y observador.
- Profundizacion: textos de QFT en espacio-tiempo curvo y cuantizacion dependiente del observador.


---

## Navegacion del tutorial

[(anterior) Accion Efectiva y Potencial Efectivo](03_accion_efectiva_y_potencial_efectivo.md) | [(siguiente) Origen de las Divergencias y Regularizacion](../09_renormalizacion/01_origen_de_las_divergencias_y_regularizacion.md)
