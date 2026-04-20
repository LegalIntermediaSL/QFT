# Polarizaciones y Sumas de Espin en QED

## 1. Proposito

Este documento añade una capa tecnica necesaria para pasar de amplitudes escritas formalmente a cantidades comparables con observables: el tratamiento de polarizaciones del foton y sumas de espin de fermiones.

## 2. Por que hace falta esta capa

Una amplitud de scattering no basta por si sola para obtener una seccion eficaz. Para pasar a observables suele ser necesario:

- promediar sobre espines iniciales no controlados;
- sumar sobre espines finales no observados;
- tratar adecuadamente polarizaciones del foton cuando corresponda.

## 3. Espinores externos

En amplitudes de QED aparecen objetos como

$$
\bar{u}(p')\gamma^\mu u(p).
$$

Cuando se calcula el modulo al cuadrado de la amplitud, la suma sobre espines permite reorganizar expresiones largas en trazas de matrices gamma.

## 4. Sumas de espin

Las relaciones de completitud se escriben de forma esquematica como

$$
\sum_s u^{(s)}(p)\bar{u}^{(s)}(p) = \not p + m,
$$

y una expresion analoga para los espinores $v$.

Estas identidades son fundamentales porque transforman el problema de manejar espinores individuales en un problema de algebra gamma controlable.

## 5. Polarizaciones del foton

Para fotones externos reales, las polarizaciones fisicas se describen por vectores $\epsilon^\mu(k)$ sujetos a restricciones ligadas a gauge y a la naturaleza sin masa del foton.

La idea esencial es:

- el foton no tiene cuatro polarizaciones fisicas independientes;
- la redundancia gauge debe tratarse con cuidado;
- en observables gauge invariantes, las componentes no fisicas no deben contaminar el resultado final.

## 6. Lectura pragmatica

En muchos calculos introductorios de QED:

- las sumas de espin convierten amplitudes en trazas;
- las polarizaciones se tratan con reglas de completitud apropiadas;
- la identidad de Ward ayuda a controlar que la parte no fisica no sobreviva.

## 7. Ejemplo corto de lectura

Si una amplitud parece volverse inmanejable por la presencia de muchos espinores externos, la suma de espin no es un truco cosmetico: es la herramienta que la convierte en una expresion trazable y computable.

## 8. Cuaderno asociado

- `../../Cuadernos/ejemplos/06_diagramas_de_feynman_basicos.ipynb`: usarlo para recordar la estructura elemental de amplitudes y diagramas.
- `../../Cuadernos/problemas_resueltos/10_interacciones_y_perturbaciones.ipynb`: usarlo como base para la logica perturbativa y el paso a observables.

## 9. Advertencias utiles

- Sumar sobre espines no significa olvidar la estructura fermionica, sino reorganizarla de forma mas eficiente.
- La completitud de polarizaciones debe usarse con cuidado en presencia de gauge.
- Un observable mal calculado puede retener componentes no fisicas si no se respeta la estructura gauge de la amplitud.

## 10. Preguntas de comprobacion

- Por que las sumas de espin llevan de espinores a trazas.
- Que relacion hay entre polarizaciones del foton y redundancia gauge.
- Por que esta capa tecnica es necesaria para pasar de amplitudes a secciones eficaces.

## 11. Referencias y lecturas recomendadas

- Base: Peskin y Schroeder, trazas, sumas de espin y polarizaciones.
- Complementaria: Schwartz, tecnicas practicas para amplitudes relativistas.
- Profundizacion: textos de scattering relativista y calculo de observables en QED.


---

## Navegacion del tutorial

[(anterior) Scattering Basico en QED](04_scattering_basico_en_qed.md) | [(siguiente) Introduccion a la Integral de Camino](../08_integral_de_camino/01_introduccion_a_la_integral_de_camino.md)
