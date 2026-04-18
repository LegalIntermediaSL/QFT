# Articulo 4: Interacciones, Amplitudes y Diagramas de Feynman

## Introduccion

Una vez entendidos los campos libres, aparece la pregunta decisiva: como se describen los procesos fisicos reales, donde las particulas se dispersan, se transforman y producen nuevas excitaciones. La respuesta lleva a la teoria de perturbaciones y a los diagramas de Feynman.

## 1. Del campo libre al campo interactuante

Una teoria libre tiene ecuaciones lineales y soluciones relativamente simples. Pero la mayor parte de la fisica interesante exige introducir interacciones. En una lagrangiana, eso suele verse como terminos no cuadraticos en los campos.

Ejemplo esquematico:

`L = L_libre + L_int`

donde `L_int` podria contener terminos como `lambda phi^4`.

Esos terminos permiten que los cuantos del campo se influyan mutuamente y produzcan procesos no triviales.

## 2. Que calculamos en una teoria interactuante

En lugar de seguir trayectorias clasicas puntuales, la QFT calcula amplitudes de probabilidad entre estados iniciales y finales. A partir de ellas se extraen:

- secciones eficaces;
- tasas de decaimiento;
- probabilidades de dispersion;
- correcciones a masas y acoplamientos.

El objeto central suele estar relacionado con el operador `S`, que conecta estados asintoticos del pasado y del futuro.

## 3. Expansion perturbativa

Muchas teorias fisicas se estudian suponiendo que la intensidad de interaccion es suficientemente pequena como para expandir cantidades observables en potencias del acoplamiento.

La idea es:

- resolver exactamente la parte libre;
- tratar la interaccion como correccion;
- ordenar el calculo por niveles de complejidad.

Cada orden de esta expansion puede representarse de forma compacta mediante diagramas de Feynman.

## 4. Que son los diagramas de Feynman

Un diagrama de Feynman no es una foto del proceso microscopico. Es una herramienta de contabilidad matematica. Cada diagrama representa un termino en la expansion perturbativa de una amplitud.

Un diagrama codifica:

- lineas externas asociadas a estados iniciales o finales;
- lineas internas asociadas a propagadores;
- vertices asociados a interacciones.

Su poder pedagogico es enorme porque traduce expresiones integrales complejas en una sintaxis visual compacta.

## 5. Reglas de Feynman

Cada teoria tiene sus propias reglas de Feynman, derivadas de la lagrangiana. Esas reglas indican:

- que factor corresponde a cada propagador;
- que factor corresponde a cada vertice;
- como integrar sobre momentos internos;
- como imponer conservacion del momento en cada vertice.

Asi, el diagrama no reemplaza el calculo: lo organiza.

## 6. Un ejemplo conceptual simple

En una teoria `phi^4`, un vertice elemental conecta cuatro lineas del campo escalar. A orden mas bajo, ese vertice ya permite procesos de dispersion entre dos particulas entrantes y dos salientes.

Incluso un ejemplo tan simple muestra ideas profundas:

- la interaccion esta codificada localmente en la lagrangiana;
- la expansion perturbativa ordena las contribuciones;
- los diagramas traducen algebra en estructura visual.

## 7. Correcciones cuanticas

Los diagramas con lazos internos introducen correcciones radiativas. Son precisamente estos terminos los que suelen generar integrales divergentes y obligan a discutir regularizacion y renormalizacion.

Por eso los diagramas de Feynman cumplen una doble funcion:

- facilitan el calculo practico;
- revelan donde aparecen los problemas ultravioletas de la teoria.

## 8. Advertencias utiles

Al empezar, conviene evitar varios malentendidos:

- un diagrama no describe una trayectoria clasica literal;
- las lineas internas no representan particulas observables propagandose como objetos clasicos;
- sumar diagramas es sumar contribuciones de amplitud, no probabilidades directas;
- el formalismo depende del regimen perturbativo y no agota toda la QFT.

## Cierre

Los diagramas de Feynman son una de las herramientas mas famosas de la fisica teorica porque convierten calculos perturbativos muy abstractos en una sintaxis visual poderosa. Pero su verdadero sentido solo se entiende bien cuando se los ve como lo que son: una expresion organizada de la estructura cuantica de las interacciones.
