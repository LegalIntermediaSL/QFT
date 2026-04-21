# Funcional Generador y Correladores

## 1. Proposito

Una vez aceptada la integral de camino, el siguiente paso natural es introducir el funcional generador, que sirve para producir sistematicamente correladores y amplitudes.

## 2. Fuente externa

Se introduce una fuente clasica $J(x)$ acoplada al campo y se define formalmente

$$
Z[J] = \int \mathcal{D}\phi \, \exp\left(iS[\phi] + i\int d^4x\, J(x)\phi(x)\right).
$$

Este objeto contiene informacion sobre toda la teoria.

La fuente $J(x)$ es una herramienta auxiliar. No es necesariamente un nuevo campo dinamico del problema; se introduce porque permite marcar inserciones del operador de campo mediante derivadas funcionales.

## 3. Correladores

Derivando funcionalmente respecto a la fuente y luego poniendo $J=0$, se obtienen correladores del campo:

$$
\langle 0|T\{\phi(x_1)\phi(x_2)\cdots\phi(x_n)\}|0\rangle.
$$

De forma mas explicita, el correlador de $n$ puntos puede escribirse esquematicamente como

$$
\langle 0|T\{\phi(x_1)\cdots\phi(x_n)\}|0\rangle
=
\left.
\frac{1}{Z[0]}
\left(\frac{1}{i}\frac{\delta}{\delta J(x_1)}\right)
\cdots
\left(\frac{1}{i}\frac{\delta}{\delta J(x_n)}\right)
Z[J]
\right|_{J=0}.
$$

Esta es una de las grandes virtudes del formalismo: convierte el calculo de correladores en una operacion sistematica sobre un unico objeto generador.

Mas explicitamente, una derivada funcional como

$$
\frac{1}{i}\frac{\delta Z[J]}{\delta J(x)}
$$

inserta un campo $\phi(x)$ dentro de la integral funcional. Repetir esa operacion genera correladores de orden superior.

## 4. Integral gaussiana funcional

En una teoria libre, la accion es cuadratica en el campo. Esto convierte a $Z[J]$ en el analogo funcional de una integral gaussiana ordinaria. Esa es una de las razones de su enorme utilidad: las teorias libres pueden resolverse de forma casi exacta, y las interactuantes se construyen perturbativamente alrededor de ellas.

Esquematicamente,

$$
Z_0[J] \propto \exp\left(-\frac{i}{2}\int d^4x\,d^4y\, J(x)\Delta_F(x-y)J(y)\right),
$$

donde $\Delta_F$ es el propagador de Feynman.

La idea central es:

- el propagador aparece como nucleo de la gaussiana funcional;
- las derivadas respecto a $J$ reconstruyen correladores tiempo-ordenados.

## 5. Relacion con perturbaciones

Separando accion libre e interaccion, el formalismo de integral de camino reproduce de forma elegante la expansion perturbativa y los diagramas de Feynman.

En la practica se escribe

$$
S[\phi] = S_0[\phi] + S_{\text{int}}[\phi],
$$

y se trata la parte interactuante como expansion formal alrededor de la teoria libre. De ahi emergen:

- propagadores a partir de la parte cuadratica;
- vertices a partir de los terminos de interaccion;
- diagramas como contabilidad grafica de las contracciones posibles.

## 6. Conectados y funcional efectivo

En un primer curso basta trabajar con $Z[J]$, pero conviene ubicar dos objetos derivados aun mas utiles:

- $W[J] = -i \ln Z[J]$, que genera correladores conectados;
- la accion efectiva $\Gamma[\phi_c]$, obtenida por transformacion de Legendre.

La definicion del campo clasico efectivo asociada a la fuente es

$$
\phi_c(x) = \frac{\delta W[J]}{\delta J(x)}.
$$

Y la transformacion de Legendre que conduce a la accion efectiva toma la forma

$$
\Gamma[\phi_c] = W[J] - \int d^4x\, J(x)\phi_c(x),
$$

donde implicitamente $J$ debe entenderse como funcional de $\phi_c$.

Estos objetos son muy importantes para estudiar vacios, ruptura de simetria, campos clasicos efectivos y correcciones cuanticas resumidas.

## 7. Preguntas de estudio

- Que papel cumple la fuente $J(x)$.
- Como se obtienen correladores a partir de $Z[J]$.
- Por que este formalismo conecta tan bien con teoria de perturbaciones.
- Que relacion hay entre la parte cuadratica de la accion y el propagador.

## 8. Cierre

El funcional generador es una de las herramientas mas compactas y poderosas de la QFT. Resume correladores, organiza expansiones perturbativas y da acceso directo a la estructura observable de la teoria.

## 9. Referencias y lecturas recomendadas

- Base: Srednicki, funcional generador y correladores.
- Complementaria: Peskin y Schroeder, teoria libre, fuentes y propagadores.
- Profundizacion: Zee, lectura conceptual del papel de $Z[J]$ en la teoria de campos.


---

## Navegacion del tutorial

[(anterior) Introduccion a la Integral de Camino](01_introduccion_a_la_integral_de_camino.md) | [(siguiente) Accion Efectiva y Potencial Efectivo](03_accion_efectiva_y_potencial_efectivo.md)
