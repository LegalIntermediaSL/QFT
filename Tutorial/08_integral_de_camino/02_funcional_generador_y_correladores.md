# Funcional Generador y Correladores

**Nivel:** Intermedio  
**Dificultad:** Media-Alta  
**Tiempo estimado:** 25-35 min  
**Prerequisitos recomendados:** [Introduccion a la Integral de Camino](01_introduccion_a_la_integral_de_camino.md) · [Resumen del modulo](README.md)


## 1. Proposito

Una vez aceptada la integral de camino, el siguiente paso natural es introducir el funcional generador, que sirve para producir sistematicamente correladores y amplitudes.

## 2. Fuente externa

Se introduce una fuente clasica $J(x)$ acoplada al campo y se define formalmente

$$
Z[J] = \int \mathcal{D}\phi \, \exp\left(iS[\phi] + i\int d^4x\, J(x)\phi(x)\right).
$$

Este objeto contiene informacion sobre toda la teoria.

La fuente $J(x)$ es una herramienta auxiliar. No es necesariamente un nuevo campo dinamico del problema; se introduce porque permite marcar inserciones del operador de campo mediante derivadas funcionales.

Una intuicion util es pensar que $J(x)$ "sondea" la teoria. Al deformar ligeramente la accion con un termino lineal en el campo, podemos registrar como responde el sistema. Las derivadas funcionales con respecto a la fuente extraen precisamente esa respuesta.

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

Esta propiedad es mas que una comodidad formal. Los correladores son los objetos que contienen la informacion observable mas importante de la teoria:

- la funcion de dos puntos identifica propagacion y espectro;
- las funciones de tres y cuatro puntos codifican interacciones;
- sus polos y residuos se conectan con masas, acoplamientos y amplitudes fisicas.

## 4. Normalizacion y significado de $Z[0]$

El factor $Z[0]$ aparece en la formula de correladores porque el funcional generador sin fuentes no tiene por que estar normalizado a uno. Dividir por $Z[0]$ elimina burbujas de vacio que no dependen de inserciones externas.

Pedagogicamente, esto aclara un punto importante:

- $Z[J]$ contiene tanto informacion fisica como factores globales del vacio;
- los correladores normalizados extraen la parte relevante para observables;
- por eso muchas veces se trabaja con objetos logaritmicos o conectados, donde esta limpieza ocurre de manera mas natural.

## 5. Integral gaussiana funcional

En una teoria libre, la accion es cuadratica en el campo. Esto convierte a $Z[J]$ en el analogo funcional de una integral gaussiana ordinaria. Esa es una de las razones de su enorme utilidad: las teorias libres pueden resolverse de forma casi exacta, y las interactuantes se construyen perturbativamente alrededor de ellas.

Esquematicamente,

$$
Z_0[J] \propto \exp\left(-\frac{i}{2}\int d^4x\,d^4y\, J(x)\Delta_F(x-y)J(y)\right),
$$

donde $\Delta_F$ es el propagador de Feynman.

La idea central es:

- el propagador aparece como nucleo de la gaussiana funcional;
- las derivadas respecto a $J$ reconstruyen correladores tiempo-ordenados.

Vale la pena conectar esto con una integral gaussiana ordinaria conocida:

$$
\int dx\, e^{-\frac{1}{2}ax^2+Jx}
\propto
e^{\frac{J^2}{2a}}.
$$

La version funcional repite exactamente esta logica, solo que ahora el indice discreto se reemplaza por un punto del espacio-tiempo y el inverso de la forma cuadratica se convierte en el propagador.

## 6. Funcion de dos puntos y propagador

Si derivamos dos veces el funcional gaussiano libre, obtenemos

$$
\langle 0|T\{\phi(x)\phi(y)\}|0\rangle = \Delta_F(x-y).
$$

Esta igualdad condensa una idea central: el propagador de Feynman no es un objeto añadido por conveniencia diagramatica, sino la funcion de dos puntos tiempo-ordenada de la teoria libre.

Por eso:

- invertir el operador cuadratico de la accion produce el propagador;
- el propagador controla la respuesta lineal del campo;
- en perturbacion, cada linea interna de un diagrama hereda exactamente esta estructura.

## 7. Relacion con perturbaciones

Separando accion libre e interaccion, el formalismo de integral de camino reproduce de forma elegante la expansion perturbativa y los diagramas de Feynman.

En la practica se escribe

$$
S[\phi] = S_0[\phi] + S_{\text{int}}[\phi],
$$

y se trata la parte interactuante como expansion formal alrededor de la teoria libre. De ahi emergen:

- propagadores a partir de la parte cuadratica;
- vertices a partir de los terminos de interaccion;
- diagramas como contabilidad grafica de las contracciones posibles.

En una teoria como $\phi^4$, por ejemplo, el termino de interaccion puede escribirse como un operador diferencial actuando sobre el funcional libre. Esta observacion organiza de manera compacta toda la expansion perturbativa sin tener que reconstruir desde cero cada correlador.

## 8. Conectados y funcional efectivo

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

La razon de introducir $W[J]$ es que el logaritmo elimina automaticamente diagramas desconectados de vacio. A su vez, $\Gamma[\phi_c]$ reorganiza la informacion en terminos de vertices propios o irreducibles 1PI, que son la base natural para estudiar dinamica efectiva y potenciales corregidos cuánticamente.

## Cuaderno asociado

- Consulta los cuadernos asociados de este bloque en [Resumen del modulo](README.md) para reforzar el capitulo con practica guiada.

## 9. Advertencias utiles

- La fuente $J(x)$ es auxiliar; no debe confundirse con una corriente fisica del sistema salvo que se declare expresamente esa interpretacion.
- El funcional generador es formal y suele requerir regularizacion en teorias interactivas.
- No todo correlador se interpreta directamente como amplitud de scattering; para eso hace falta aun el puente LSZ.

## 10. Preguntas de estudio

- Que papel cumple la fuente $J(x)$.
- Como se obtienen correladores a partir de $Z[J]$.
- Por que este formalismo conecta tan bien con teoria de perturbaciones.
- Que relacion hay entre la parte cuadratica de la accion y el propagador.

## Ejercicios sugeridos

1. Explicar por que introducir una fuente externa organiza el calculo de correladores.
2. Describir la diferencia conceptual entre $Z[J]$ y un correlador ya evaluado.
3. Relacionar la parte cuadratica de la accion con la aparicion del propagador libre.

## 11. Cierre

El funcional generador es una de las herramientas mas compactas y poderosas de la QFT. Resume correladores, organiza expansiones perturbativas y da acceso directo a la estructura observable de la teoria.

## 12. Referencias y lecturas recomendadas

- Base: Srednicki, funcional generador y correladores.
- Complementaria: Peskin y Schroeder, teoria libre, fuentes y propagadores.
- Profundizacion: Zee, lectura conceptual del papel de $Z[J]$ en la teoria de campos.


---

## Navegacion del tutorial

[(anterior) Introduccion a la Integral de Camino](01_introduccion_a_la_integral_de_camino.md) | [(siguiente) Accion Efectiva y Potencial Efectivo](03_accion_efectiva_y_potencial_efectivo.md)
