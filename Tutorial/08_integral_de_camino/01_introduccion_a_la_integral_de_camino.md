# Introduccion a la Integral de Camino

**Nivel:** Intermedio  
**Dificultad:** Media-Alta  
**Tiempo estimado:** 25-35 min  
**Prerequisitos recomendados:** [Modulo anterior](../07_gauge_y_qed/README.md) · [Resumen del modulo](README.md)


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

Un modo util de verlo es escribir

$$
U(t_f,t_i)=e^{-iH(t_f-t_i)/\hbar}
$$

y factorizar el intervalo total en $N$ pasos de tamaño $\varepsilon=(t_f-t_i)/N$:

$$
U(t_f,t_i)=\left(e^{-iH\varepsilon/\hbar}\right)^N.
$$

Entre cada factor se inserta una resolucion de la identidad en la base de posiciones,

$$
\mathbf{1}=\int dx_n\, |x_n\rangle \langle x_n|.
$$

Para un Hamiltoniano de la forma

$$
H=\frac{p^2}{2m}+V(x),
$$

el elemento de matriz de cada paso puede aproximarse para $\varepsilon$ pequeño y reorganizarse como

$$
\langle x_{n+1}|e^{-iH\varepsilon/\hbar}|x_n\rangle
\sim
\exp\!\left[
\frac{i\varepsilon}{\hbar}
\left(
\frac{m}{2}\left(\frac{x_{n+1}-x_n}{\varepsilon}\right)^2
-V(x_n)
\right)
\right].
$$

Al multiplicar todos los factores, el exponente se suma y reproduce la version discretizada de la accion clasica

$$
S[x]=\int_{t_i}^{t_f}dt\, L(x,\dot x).
$$

Esto deja clara una intuicion esencial: la accion no se introduce artificialmente en la teoria cuantica, sino que emerge de la estructura temporal de la evolucion.

## 4. Fase, interferencia y limite clasico

La expresion

$$
e^{iS/\hbar}
$$

resume dos ideas a la vez:

- toda historia admisible contribuye;
- no todas contribuyen con el mismo peso neto, porque la fase oscila.

Si una familia de trayectorias produce variaciones grandes de $S$, sus fases apuntan en direcciones muy distintas en el plano complejo y tienden a cancelarse. En cambio, cuando la accion es estacionaria frente a pequeñas variaciones,

$$
\delta S = 0,
$$

la fase cambia mas lentamente y las contribuciones vecinas se refuerzan. De ahi emerge la ecuacion clasica como condicion de fase estacionaria.

Esta lectura evita un malentendido frecuente: la trayectoria clasica no se "impone" desde fuera, sino que aparece como aproximacion dominante cuando $S/\hbar$ es grande y la interferencia suprime historias alejadas del extremo de la accion.

## 5. De una coordenada a un campo

Para una particula, la suma se hace sobre trayectorias $x(t)$. Para una teoria de campos, la suma se hace sobre configuraciones de campo $\phi(x)$. De ahi la idea de integral funcional:

$$
\int \mathcal{D}\phi \, e^{iS[\phi]}.
$$

Aunque la notacion es formal, captura de manera compacta una enorme parte de la estructura cuantica de la teoria.

Pasar de una particula a un campo significa reemplazar:

- una trayectoria $x(t)$ por una configuracion $\phi(x)$;
- una integral ordinaria por una integral funcional;
- una suma sobre historias puntuales por una suma sobre historias del campo entero.

La diferencia conceptual es grande. Una trayectoria de particula vive sobre una linea temporal. Una configuracion de campo asigna un valor a cada punto del espacio-tiempo. Por eso, en QFT no se suman "caminos de una particula", sino historias completas del contenido dinamico del sistema.

En un campo escalar libre, por ejemplo,

$$
S[\phi] = \int d^4x \left[
\frac{1}{2}\partial_\mu \phi\, \partial^\mu \phi
- \frac{1}{2}m^2\phi^2
\right].
$$

La integral funcional

$$
\int \mathcal{D}\phi\, e^{iS[\phi]}
$$

recorre formalmente todas las configuraciones posibles de $\phi(x)$, no solo las soluciones de Euler-Lagrange.

## 6. Que gana la QFT con este lenguaje

La integral de camino:

- hace muy visible el papel de la accion;
- conecta de forma natural con simetrias y gauge;
- organiza correladores y teorias perturbativas con elegancia;
- facilita el paso a formulaciones mas geometricas y estadisticas.

Ademas, este lenguaje vuelve casi inevitables algunas construcciones que en el formalismo canonico aparecen mas tarde:

- fuentes externas y funcionales generadores;
- expansion perturbativa en terminos de correladores;
- tratamiento uniforme de campos escalares, fermionicos y gauge;
- rotacion euclidea y conexion con fisica estadistica.

## 7. Ejemplo minimo: oscilador armonico y campo libre

El oscilador armonico ya anticipa por que este formalismo es tan importante para QFT. Si un campo libre se descompone en modos normales, cada modo se comporta esencialmente como un oscilador. Entonces:

- una particula puntual enseña la logica de suma sobre historias;
- el oscilador armonico enseña como tratar sistemas cuadraticos;
- un campo libre aparece como un continuo de osciladores acoplados por la estructura espacial.

En sistemas cuadraticos, la integral de camino puede evaluarse exactamente porque la accion es gaussiana. Esa es una de las razones por las que los propagadores libres aparecen de forma tan natural en este enfoque.

## 8. Puente con la cuantizacion canonica

La integral de camino no compite con la cuantizacion canonica como si fueran dos teorias distintas. Son dos lenguajes para la misma fisica cuando ambos estan bien definidos.

La diferencia principal es de punto de partida:

- el enfoque canonico enfatiza operadores, conmutadores y espacio de Hilbert;
- el enfoque funcional enfatiza accion, correladores y suma sobre configuraciones.

En la practica:

- los correladores funcionales coinciden con productos tiempo-ordenados de operadores;
- los polos de los propagadores identifican las mismas excitaciones fisicas;
- la expansion perturbativa lleva a los mismos diagramas de Feynman.

Una manera compacta de resumir la relacion es:

- el enfoque canonico responde mejor a preguntas sobre operadores y estados;
- el enfoque funcional organiza mejor correladores, simetrias y teoria perturbativa;
- ambos deben coincidir en los observables fisicos.

## Cuaderno asociado

- Consulta los cuadernos asociados de este bloque en [Resumen del modulo](README.md) para reforzar el capitulo con practica guiada.

## 9. Advertencias utiles

- La medida $\mathcal{D}\phi$ es formal y exige cuidado matematico; en fisica se justifica operacionalmente por discretizacion, regularizacion y continuacion adecuada.
- La expresion de Minkowski con $e^{iS}$ es muy oscilatoria. En muchos contextos conviene rotar a tiempo imaginario para obtener integrales mejor comportadas.
- "Sumar todas las historias" no significa que todas tengan igual importancia observable; la interferencia sigue siendo la clave.

## 10. Preguntas de estudio

- Que cambia al pasar de trayectoria clasica unica a suma sobre historias.
- Por que el peso es $e^{iS}$.
- En que sentido una integral funcional generaliza una integral ordinaria.
- Por que la trayectoria clasica reaparece en el limite semiclasico.

## Ejercicios sugeridos

1. Explicar por que la integral de camino no reemplaza la accion, sino que la reutiliza como peso de la cuantizacion.
2. Comparar la idea de trayectoria clasica dominante con la nocion de suma sobre historias.
3. Describir por que el limite semiclasico recupera una lectura cercana a la dinamica clasica.

## 11. Cierre

La integral de camino no reemplaza por completo a la cuantizacion canonica, pero ofrece una perspectiva complementaria extraordinariamente poderosa sobre la teoria cuantica de campos.

## 12. Referencias y lecturas recomendadas

- Base: Zee, introduccion a integrales de camino.
- Complementaria: Srednicki, comienzo funcional del formalismo.
- Profundizacion: Peskin y Schroeder, derivacion de funcionales generadores y relacion con correladores.


---

## Navegacion del tutorial

[(anterior) Polarizaciones y Sumas de Espin en QED](../07_gauge_y_qed/05_polarizaciones_y_sumas_de_espin.md) | [(siguiente) Funcional Generador y Correladores](02_funcional_generador_y_correladores.md)
