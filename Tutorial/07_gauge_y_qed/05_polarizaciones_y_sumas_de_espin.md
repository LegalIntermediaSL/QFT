# Polarizaciones y Sumas de Espin en QED

**Nivel:** Nucleo  
**Dificultad:** Media-Alta  
**Tiempo estimado:** 18-25 min  
**Prerequisitos recomendados:** [Scattering Basico en QED](04_scattering_basico_en_qed.md) · [Resumen del modulo](README.md)


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

Esta reorganizacion es uno de los grandes alivios tecnicos del formalismo relativista: en vez de seguir caso por caso cada espinor externo, se sustituye el problema por identidades de completitud y algebra gamma sistematica.

## 4. Sumas de espin

Las relaciones de completitud se escriben de forma esquematica como

$$
\sum_s u^{(s)}(p)\bar{u}^{(s)}(p) = \not p + m,
$$

y una expresion analoga para los espinores $v$.

Estas identidades son fundamentales porque transforman el problema de manejar espinores individuales en un problema de algebra gamma controlable.

Una vez usadas estas relaciones, el modulo al cuadrado de la amplitud suele expresarse en trazas del tipo

$$
\mathrm{Tr}\!\left[(\not p' + m)\gamma^\mu(\not p + m)\gamma^\nu\right],
$$

que ya puede evaluarse con identidades estándar del algebra de Dirac.

## 5. Polarizaciones del foton

Para fotones externos reales, las polarizaciones fisicas se describen por vectores $\epsilon^\mu(k)$ sujetos a restricciones ligadas a gauge y a la naturaleza sin masa del foton.

La idea esencial es:

- el foton no tiene cuatro polarizaciones fisicas independientes;
- la redundancia gauge debe tratarse con cuidado;
- en observables gauge invariantes, las componentes no fisicas no deben contaminar el resultado final.

Para fotones reales, la transversidad impone que las polarizaciones fisicas sean solo dos. Esa es una señal muy importante de que el formalismo covariante contiene redundancia gauge que debe desaparecer al pasar a observables.

## 6. Lectura pragmatica

En muchos calculos introductorios de QED:

- las sumas de espin convierten amplitudes en trazas;
- las polarizaciones se tratan con reglas de completitud apropiadas;
- la identidad de Ward ayuda a controlar que la parte no fisica no sobreviva.

En la practica, la identidad de Ward cumple un papel de seguridad conceptual: si reemplazar $\epsilon^\mu(k)$ por el momento $k^\mu$ no hace desaparecer la contribucion gauge-dependiente, el calculo probablemente esta mal organizado o no es gauge invariante.

## 7. De amplitud a seccion eficaz

Una vez sumados espines y tratadas las polarizaciones, el paso hacia un observable requiere aun:

- promediar sobre grados de libertad iniciales no preparados;
- incluir factores de flujo y espacio de fases;
- identificar que variables cinematicas se miden realmente.

Esto explica por que esta capa tecnica no es ornamental: es el puente entre el formalismo de amplitudes y los numeros comparables con experimento.

## 8. Ejemplo corto de lectura

Si una amplitud parece volverse inmanejable por la presencia de muchos espinores externos, la suma de espin no es un truco cosmetico: es la herramienta que la convierte en una expresion trazable y computable.

## 9. Cuaderno asociado

- `../../Cuadernos/ejemplos/06_diagramas_de_feynman_basicos.ipynb`: usarlo para recordar la estructura elemental de amplitudes y diagramas.
- `../../Cuadernos/problemas_resueltos/10_interacciones_y_perturbaciones.ipynb`: usarlo como base para la logica perturbativa y el paso a observables.

## 10. Advertencias utiles

- Sumar sobre espines no significa olvidar la estructura fermionica, sino reorganizarla de forma mas eficiente.
- La completitud de polarizaciones debe usarse con cuidado en presencia de gauge.
- Un observable mal calculado puede retener componentes no fisicas si no se respeta la estructura gauge de la amplitud.

## 11. Preguntas de comprobacion

- Por que las sumas de espin llevan de espinores a trazas.
- Que relacion hay entre polarizaciones del foton y redundancia gauge.
- Por que esta capa tecnica es necesaria para pasar de amplitudes a secciones eficaces.

## 12. Referencias y lecturas recomendadas

- Base: Peskin y Schroeder, trazas, sumas de espin y polarizaciones.
- Complementaria: Schwartz, tecnicas practicas para amplitudes relativistas.
- Profundizacion: textos de scattering relativista y calculo de observables en QED.


---

## Navegacion del tutorial

[(anterior) Scattering Basico en QED](04_scattering_basico_en_qed.md) | [(siguiente) Introduccion a la Integral de Camino](../08_integral_de_camino/01_introduccion_a_la_integral_de_camino.md)