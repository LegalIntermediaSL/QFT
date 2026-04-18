# Articulo 2: Accion, Densidad Lagrangiana y Teorema de Noether

## Introduccion

Buena parte de la elegancia de la Teoria Cuantica de Campos proviene de que su dinamica puede escribirse a traves de un unico objeto: la accion. Una vez elegida la densidad lagrangiana correcta, las ecuaciones de movimiento, las simetrias y muchas propiedades estructurales quedan codificadas de forma compacta.

## 1. La accion en teoria de campos

Para un sistema de campos `phi_a(x)`, la accion se escribe como:

`S[phi] = integral d^4x L(phi_a, partial_mu phi_a)`

Aqui `L` es la densidad lagrangiana, no la lagrangiana mecanica ordinaria. Su dependencia local en el campo y sus derivadas permite formular la teoria de manera relativista y covariante.

El principio variacional dice que la dinamica fisica satisface:

`delta S = 0`

frente a variaciones admisibles del campo.

## 2. Ecuaciones de Euler-Lagrange para campos

Al variar la accion se obtiene:

`partial L / partial phi_a - partial_mu (partial L / partial (partial_mu phi_a)) = 0`

Estas son las ecuaciones de Euler-Lagrange en teoria de campos. A partir de una sola expresion generadora, la teoria produce las ecuaciones dinamicas del sistema.

Ejemplo para un campo escalar libre real:

`L = 1/2 partial_mu phi partial^mu phi - 1/2 m^2 phi^2`

La ecuacion correspondiente es:

`(partial_mu partial^mu + m^2) phi = 0`

que es precisamente la ecuacion de Klein-Gordon.

## 3. Por que la lagrangiana es tan importante

La densidad lagrangiana concentra informacion en varios niveles:

- determina las ecuaciones de movimiento;
- hace visibles las simetrias;
- separa terminos libres de terminos de interaccion;
- permite construir corrientes conservadas;
- sirve como puerta de entrada tanto a la cuantizacion canonica como a la integral de camino.

En muchas teorias modernas, escribir una lagrangiana plausible guiada por simetrias ya constituye una parte esencial del trabajo teorico.

## 4. Simetrias continuas

Una simetria continua transforma los campos de manera infinitesimal sin cambiar la accion. Esto puede incluir:

- traslaciones del espacio-tiempo;
- rotaciones y boosts;
- cambios de fase globales;
- transformaciones internas mas generales.

Cuando una simetria continua deja invariante la accion, aparece una corriente conservada. Esta es la idea central del teorema de Noether.

## 5. Teorema de Noether

En lenguaje sencillo, el teorema de Noether afirma:

- a cada simetria continua diferenciable de la accion le corresponde una ley de conservacion;
- a cada corriente conservada le corresponde una carga conservada bajo condiciones adecuadas.

Ejemplos clasicos:

- invariancia temporal -> conservacion de la energia;
- invariancia espacial -> conservacion del momento lineal;
- invariancia rotacional -> conservacion del momento angular;
- simetria global de fase -> conservacion de una carga interna.

## 6. Ejemplo de simetria de fase

Consideremos un campo escalar complejo `phi`. Si la teoria es invariante bajo:

`phi -> exp(i alpha) phi`

con `alpha` constante, entonces existe una corriente conservada asociada. Esa simetria global `U(1)` es un modelo pedagogico central porque anticipa la estructura de teorias gauge mas ricas.

La leccion importante es que las cantidades conservadas no aparecen como accidentes; brotan de la estructura simetrica de la accion.

## 7. De simetria global a simetria local

Si el parametro `alpha` deja de ser constante y pasa a depender de `x`, la teoria ya no suele permanecer invariante sin introducir nuevos campos compensadores. De esta exigencia emerge la idea de simetria gauge.

Este paso es crucial en la fisica moderna:

- obliga a introducir conexiones o potenciales gauge;
- organiza interacciones fundamentales;
- explica por que ciertos campos mediadores aparecen de forma natural.

Asi, una exigencia de simetria local no solo restringe la teoria: tambien genera contenido fisico.

## 8. Mirada estructural

Desde una perspectiva amplia, la accion y Noether cumplen dos papeles complementarios:

- la accion dice como evoluciona el sistema;
- las simetrias dicen que rasgos de esa evolucion son estructuralmente estables.

Esta combinacion vuelve a la teoria de campos mucho mas que una lista de ecuaciones. La convierte en una arquitectura guiada por principios.

## Cierre

Aprender a leer una teoria a traves de su densidad lagrangiana es uno de los cambios de mentalidad mas importantes en QFT. Una vez que se domina esa mirada, las ecuaciones de movimiento, las corrientes conservadas y la logica de las interacciones empiezan a verse como partes de un mismo diseño conceptual.
