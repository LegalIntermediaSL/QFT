# Introduccion a la Integral de Camino

## 1. Proposito

La integral de camino ofrece una formulacion de la teoria cuantica profundamente distinta de la cuantizacion canonica. En lugar de centrarse en operadores y espacios de Fock como punto de partida, organiza las amplitudes como suma sobre historias posibles.

## 2. Idea fisica

En mecanica clasica, una particula sigue una trayectoria que extremiza la accion. En la formulacion de Feynman, la teoria cuantica asigna amplitud a todas las trayectorias posibles, ponderadas por un factor de fase:

$$
e^{iS}.
$$

La trayectoria clasica emerge como aproximacion dominante en el limite semiclasico, no como unica posibilidad fundamental.

Una lectura intuitiva muy util es:

- cada trayectoria contribuye con una fase;
- trayectorias muy distintas suelen cancelarse por interferencia;
- cerca de la trayectoria clasica, la fase varia menos y la contribucion neta puede reforzarse.

## 3. Derivacion discreta esquematica

La formula de integral de camino no aparece de la nada. Puede motivarse dividiendo la amplitud de evolucion

$$
\langle x_f,t_f | x_i,t_i \rangle
$$

en muchos intervalos de tiempo pequenos e insertando resoluciones de la identidad entre ellos. El resultado es una integral multiple sobre posiciones intermedias:

$$
\int \prod_{n=1}^{N-1} dx_n \, e^{iS_{\text{discr}}[x]/\hbar}.
$$

Al tomar formalmente el limite de muchos pasos temporales, esa integral multiple se convierte en una integral funcional sobre trayectorias.

Este argumento no es una demostracion rigurosa en el sentido matematico fuerte, pero si es la derivacion fisica estandar y la que mejor comunica de donde sale la estructura de la integral de camino.

## 4. De una coordenada a un campo

Para una particula, la suma se hace sobre trayectorias $x(t)$. Para una teoria de campos, la suma se hace sobre configuraciones de campo $\phi(x)$. De ahi la idea de integral funcional:

$$
\int \mathcal{D}\phi \, e^{iS[\phi]}.
$$

Aunque la notacion es formal, captura de manera compacta una enorme parte de la estructura cuantica de la teoria.

Pasar de una particula a un campo significa reemplazar:

- una trayectoria $x(t)$ por una configuracion $\phi(x)$;
- una integral ordinaria por una integral funcional;
- una suma sobre historias puntuales por una suma sobre historias del campo entero.

## 5. Ventajas conceptuales

La integral de camino:

- hace muy visible el papel de la accion;
- conecta de forma natural con simetrias y gauge;
- organiza correladores y teorias perturbativas con elegancia;
- facilita el paso a formulaciones mas geometricas y estadisticas.

## 6. Puente con la cuantizacion canonica

La integral de camino no compite con la cuantizacion canonica como si fueran dos teorias distintas. Son dos lenguajes para la misma fisica cuando ambos estan bien definidos.

La diferencia principal es de punto de partida:

- el enfoque canonico enfatiza operadores, conmutadores y espacio de Hilbert;
- el enfoque funcional enfatiza accion, correladores y suma sobre configuraciones.

En la practica:

- los correladores funcionales coinciden con productos tiempo-ordenados de operadores;
- los polos de los propagadores identifican las mismas excitaciones fisicas;
- la expansion perturbativa lleva a los mismos diagramas de Feynman.

## 7. Preguntas de estudio

- Que cambia al pasar de trayectoria clasica unica a suma sobre historias.
- Por que el peso es $e^{iS}$.
- En que sentido una integral funcional generaliza una integral ordinaria.
- Por que la trayectoria clasica reaparece en el limite semiclasico.

## 8. Cierre

La integral de camino no reemplaza por completo a la cuantizacion canonica, pero ofrece una perspectiva complementaria extraordinariamente poderosa sobre la teoria cuantica de campos.

## 9. Referencias y lecturas recomendadas

- Base: Zee, introduccion a integrales de camino.
- Complementaria: Srednicki, comienzo funcional del formalismo.
- Profundizacion: Peskin y Schroeder, derivacion de funcionales generadores y relacion con correladores.


---

## Navegacion del tutorial

[(anterior) Polarizaciones y Sumas de Espin en QED](../07_gauge_y_qed/05_polarizaciones_y_sumas_de_espin.md) | [(siguiente) Funcional Generador y Correladores](02_funcional_generador_y_correladores.md)
