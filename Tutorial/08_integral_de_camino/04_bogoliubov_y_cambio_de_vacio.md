# Transformaciones de Bogoliubov y Cambio de Vacio

**Nivel:** Intermedio  
**Dificultad:** Media-Alta  
**Tiempo estimado:** 18-25 min  
**Prerequisitos recomendados:** [Accion Efectiva y Potencial Efectivo](03_accion_efectiva_y_potencial_efectivo.md) · [Resumen del modulo](README.md)


## 1. Proposito

Este documento introduce una idea que conecta integral de camino, cuantizacion, espacio-tiempo curvo y el modulo avanzado de informacion y agujeros negros: distintas descomposiciones modales del mismo campo pueden conducir a nociones distintas de vacio y de particula.

## 2. El punto de partida

En QFT, definir particulas equivale a elegir una descomposicion del campo en modos de frecuencia positiva y negativa. Esa eleccion determina operadores de creacion y aniquilacion, y por tanto una nocion de vacio.

Pero esa descomposicion no siempre es unica de forma absoluta. Puede depender del observador, del fondo o de la estructura temporal del problema.

En un espacio-tiempo estacionario y con una nocion clara de tiempo global, la separacion entre frecuencia positiva y negativa suele estar bien comportada. Cuando esa estructura falta o cambia entre observadores, la nocion de particula deja de ser universal.

## 3. Transformaciones de Bogoliubov

Dos juegos distintos de modos pueden relacionarse mediante una transformacion de Bogoliubov. Esquematicamente:

$$
a_k' = \alpha_k a_k + \beta_k a_k^\dagger,
$$

con coeficientes que mezclan creacion y aniquilacion.

La presencia de terminos con $a_k^\dagger$ en la transformacion es la señal de que la nueva definicion de partícula no coincide con la anterior.

En forma un poco mas completa, si un conjunto de modos $\{u_k\}$ y otro $\{v_k\}$ describen la misma solucion del campo, se puede escribir esquematicamente

$$
v_k = \sum_j \left(\alpha_{kj} u_j + \beta_{kj} u_j^\ast\right).
$$

La mezcla con modos conjugados es exactamente lo que, al cuantizar, se traduce en mezcla entre aniquilacion y creacion.

## 4. Numero de particulas y coeficientes $\beta$

La razon por la que los coeficientes $\beta$ son tan importantes es que controlan cuantas particulas detecta un observador asociado a la nueva descomposicion cuando el sistema esta en el vacio de la antigua. Esquematicamente, el numero esperado de excitaciones viene controlado por cantidades del tipo

$$
\langle 0|N'_k|0\rangle \sim |\beta_k|^2.
$$

Eso resume una idea central:

- si $\beta_k = 0$, ambas nociones de vacio son compatibles para ese modo;
- si $\beta_k \neq 0$, aparece produccion efectiva de particulas o cambio de vacio.

## 5. Consecuencia fisica

Si el vacio definido por un conjunto de operadores no es aniquilado por el nuevo conjunto, entonces un observador asociado a la segunda descomposicion puede detectar particulas donde el primero describe vacio.

Esta idea no es una rareza matematica. Es la estructura conceptual que aparece en:

- produccion de particulas en fondos variables;
- efecto Unruh;
- radiacion de Hawking;
- teoria cuantica de campos en espacio-tiempo curvo.

## 6. Ejemplo minimo: oscilador dependiente del tiempo

Una intuicion muy util viene de un oscilador armonico con frecuencia dependiente del tiempo. Si la frecuencia cambia entre el pasado y el futuro, la nocion natural de cuanto en la region inicial no tiene por que coincidir con la nocion natural en la region final. La transformacion entre ambos juegos de operadores es precisamente del tipo Bogoliubov.

Este ejemplo muestra que la idea no depende exclusivamente de agujeros negros o relatividad general. La mezcla entre creacion y aniquilacion ya aparece cuando la estructura modal del sistema cambia con el tiempo.

## 7. Relacion con el formalismo funcional

Aunque las transformaciones de Bogoliubov suelen introducirse en lenguaje canonico, su interpretacion es muy natural desde el punto de vista funcional:

- cambian la forma en que se organiza la expansion modal;
- modifican la lectura fisica de excitaciones y vacio;
- muestran que la nocion de particula es derivada, no primaria.

Esto enlaza muy bien con el espiritu general del tutorial: los campos son fundamentales, y las particulas dependen de como se leen sus excitaciones.

## 8. Puente con el modulo 11

El efecto Unruh y la radiacion de Hawking no se entienden bien si se cree que el vacio es una nocion absoluta e inmutable. Las transformaciones de Bogoliubov ofrecen justamente el lenguaje para explicar por que:

- distintos observadores no comparten la misma nocion operacional de particula;
- un vacio puede parecer termico desde otra perspectiva;
- la informacion accesible depende de la region y del observador.

## 9. Ejemplo corto de lectura

Si una descomposicion modal mezcla operadores de creacion y aniquilacion de otra descomposicion, ya no estamos hablando del mismo vacio fisico. Esa es la razon profunda por la que "no ver particulas" puede ser una afirmacion dependiente del observador.

## Cuaderno asociado
- `../../Cuadernos/ejemplos/08_entrelazamiento_y_horizontes.ipynb`: usarlo para conectar la dependencia del observador con horizontes y termicidad efectiva.

## 11. Advertencias utiles

- Bogoliubov no significa "crear particulas de la nada" en un sentido ingenuo.
- La nocion de partícula en QFT es contextual, no puramente absoluta.
- No toda diferencia de coordenadas implica por si sola una diferencia fisica en la nocion de vacio; importa la estructura modal y el observador relevante.

## 12. Preguntas de comprobacion

- Por que una transformacion de Bogoliubov mezcla creacion y aniquilacion.
- Que relacion tiene esta mezcla con la no unicidad del vacio.
- Como prepara esto el efecto Unruh y la radiacion de Hawking.

## Ejercicios sugeridos

1. Explicar por que dos observadores pueden no compartir la misma nocion de vacio fisico.
2. Describir como una mezcla entre creacion y aniquilacion cambia la lectura de partículas presentes en un estado.
3. Relacionar cambio de vacio, observador acelerado y termicidad efectiva.

## 13. Referencias y lecturas recomendadas

- Base: Birrell y Davies, transformaciones de Bogoliubov en campos cuanticos.
- Complementaria: reseñas pedagogicas sobre cambio de vacio y observador.
- Profundizacion: textos de QFT en espacio-tiempo curvo y cuantizacion dependiente del observador.


---

## Navegacion del tutorial

[(anterior) Accion Efectiva y Potencial Efectivo](03_accion_efectiva_y_potencial_efectivo.md) | [(siguiente) Origen de las Divergencias y Regularizacion](../09_renormalizacion/01_origen_de_las_divergencias_y_regularizacion.md)
