# Calculo Funcional y Derivadas Funcionales

**Nivel:** Fundacional  
**Dificultad:** Media-Alta  
**Tiempo estimado:** 30-40 min  
**Prerequisitos recomendados:** [Delta de Dirac y Transformadas de Fourier](05_delta_de_dirac_y_transformadas_de_fourier.md) · [Resumen del modulo](README.md)


## 1. Proposito

La integral de camino y el formalismo funcional de la QFT exigen manejar con soltura derivadas e integrales de funcionales. Este capitulo fija ese lenguaje antes de que aparezca en contextos mas tecnicos, donde se da por sabido sin reexplicacion.

Un funcional asigna un numero a cada funcion. La derivada funcional mide como cambia ese numero cuando la funcion cambia infinitesimalmente en un punto. Esas dos ideas son suficientes para leer la mayor parte del formalismo de la integral de camino.

## 2. Que es un funcional

Un funcional es una aplicacion que asigna un escalar a cada funcion de un espacio dado. En fisica, el ejemplo mas inmediato es la accion:

$$
S[\phi] = \int d^4x\, \mathcal{L}(\phi(x), \partial_\mu \phi(x)).
$$

Dado un campo $\phi(x)$, la accion produce un numero. Cambiar la forma del campo da un numero distinto. $S$ no es una funcion de una variable sino una maquina que toma una funcion completa como entrada.

Otros ejemplos de funcionales:

- el valor medio de un observable en funcion del estado cuantico;
- la amplitud de transicion entre configuraciones del campo;
- el generador de correladores $Z[J]$ en la formulacion funcional.

La intuicion correcta es pensar en un funcional como una funcion de infinitas variables, una por cada punto del espacio-tiempo.

## 3. Variacion de un funcional

Dado un funcional $F[\phi]$, su variacion bajo $\phi(x) \to \phi(x) + \epsilon\,\eta(x)$ es

$$
\delta F[\phi] = F[\phi + \epsilon\,\eta] - F[\phi],
$$

expandida a primer orden en $\epsilon$.

Para la accion, esta variacion produce las ecuaciones de Euler-Lagrange. Exigir que $\delta S = 0$ para variaciones arbitrarias $\eta$ con condiciones de contorno fijas da exactamente las ecuaciones de movimiento del campo. Este es el principio de accion estacionaria.

## 4. Derivada funcional

La derivada funcional $\delta F / \delta \phi(y)$ mide cuanto cambia $F[\phi]$ cuando el campo se perturba localmente en el punto $y$. Se define formalmente como

$$
\frac{\delta F[\phi]}{\delta \phi(y)} = \lim_{\epsilon \to 0} \frac{F[\phi + \epsilon\,\delta^{(4)}(x-y)] - F[\phi]}{\epsilon}.
$$

La perturbacion es una delta de Dirac concentrada en $y$: se esta midiendo la respuesta del funcional a un cambio puntual del campo.

Esto es exactamente el analogo continuo de la derivada parcial. Si $F$ dependiera de $N$ variables discretas $\phi_i$, tendriamos $\partial F / \partial \phi_j$. Al pasar al limite continuo, el indice discreto $j$ se convierte en el punto continuo $y$.

## 5. Reglas de calculo

Las derivadas funcionales satisfacen reglas analogas a las derivadas ordinarias.

**Linealidad:**

$$
\frac{\delta}{\delta \phi(y)}\bigl(aF[\phi] + bG[\phi]\bigr) = a\,\frac{\delta F}{\delta \phi(y)} + b\,\frac{\delta G}{\delta \phi(y)}.
$$

**Regla del producto:**

$$
\frac{\delta}{\delta \phi(y)}\bigl(F[\phi]\,G[\phi]\bigr) = \frac{\delta F}{\delta \phi(y)}\,G[\phi] + F[\phi]\,\frac{\delta G}{\delta \phi(y)}.
$$

**Resultado basico:**

$$
\frac{\delta \phi(x)}{\delta \phi(y)} = \delta^{(4)}(x-y).
$$

Este ultimo resultado es la clave. La delta de Dirac aqui juega el papel del Kronecker $\delta_{ij}$ en el caso discreto.

## 6. Ejemplo: accion del campo escalar libre

La accion del campo escalar libre en cuatro dimensiones es

$$
S[\phi] = \int d^4x \left(\frac{1}{2}(\partial_\mu\phi)^2 - \frac{1}{2}m^2\phi^2\right).
$$

Aplicando la definicion de derivada funcional:

$$
\frac{\delta S}{\delta \phi(y)} = -\partial^2\phi(y) - m^2\phi(y) = 0,
$$

donde $\partial^2 = \partial_\mu\partial^\mu$ es el operador de d'Alembert. Esta es exactamente la ecuacion de Klein-Gordon. El principio de accion estacionaria reproduce las ecuaciones de movimiento del campo mediante derivacion funcional.

## 7. Funcional generador

En el formalismo de la integral de camino se introduce una fuente externa $J(x)$ acoplada al campo:

$$
Z[J] = \int \mathcal{D}\phi\, e^{i S[\phi] + i\int d^4x\, J(x)\phi(x)}.
$$

Las derivadas funcionales de $Z$ respecto a $J$ generan los correladores del campo:

$$
\langle \phi(x_1)\cdots\phi(x_n)\rangle \propto \left.\frac{\delta^n Z[J]}{\delta J(x_1)\cdots\delta J(x_n)}\right|_{J=0}.
$$

Este es el puente entre el formalismo funcional y los observables fisicos. Todo el calculo perturbativo en QFT puede reformularse en terminos de derivadas funcionales de $Z[J]$.

## 8. Integral funcional: intuicion

La integral de camino

$$
\int \mathcal{D}\phi\, (\cdots)
$$

es una integral sobre todas las configuraciones posibles del campo. Puede pensarse como el limite de una integral ordinaria sobre los valores del campo en una red de puntos, con la red refinandose hasta el continuo.

No hace falta un tratamiento riguroso para usar bien el formalismo. Basta retener dos ideas:

- la medida $\mathcal{D}\phi$ suma sobre todas las historias del campo;
- las derivadas funcionales respecto a fuentes extraen informacion sobre correladores.

La mayor parte del calculo practico en QFT funcional se reduce a manipular $Z[J]$ con las reglas de derivacion del punto 5.

## 9. Conexion con la mecanica cuantica ordinaria

En mecanica cuantica de una particula, la integral de camino de Feynman integra sobre todas las trayectorias $x(t)$:

$$
\langle x_f | e^{-iHT} | x_i\rangle = \int \mathcal{D}x\, e^{iS[x]}.
$$

En QFT, las trayectorias se reemplazan por configuraciones del campo $\phi(x,t)$. La estructura formal es identica: se pondera cada configuracion con su fase de accion. La diferencia es que el espacio de integracion pasa de ser el espacio de trayectorias de una particula a ser el espacio de configuraciones de un campo.

## Cuaderno asociado

- `../../Cuadernos/problemas_resueltos/23_calculo_funcional.ipynb`

## 10. Preguntas de comprobacion

- Que diferencia hay entre una funcion y un funcional.
- Por que la derivada funcional usa una delta de Dirac en lugar de un incremento ordinario.
- Como se obtiene la ecuacion de Klein-Gordon a partir de la accion del campo escalar.
- Que papel juega la fuente $J(x)$ en el funcional generador.
- Cual es el analogo discreto de $\delta\phi(x)/\delta\phi(y) = \delta^{(4)}(x-y)$.

## 11. Ejercicios sugeridos

1. Calcula $\delta S / \delta \phi(y)$ para $S[\phi] = \int d^4x\, \phi^4(x)$ y verifica que el resultado es proporcional a $\phi^3(y)$.
2. Aplica la regla del producto funcional para derivar $\delta(\phi^2(x)) / \delta\phi(y)$.
3. Comprueba que la ecuacion de Klein-Gordon se obtiene de $\delta S/\delta\phi = 0$ para la accion del campo escalar libre.
4. Escribe el funcional generador $Z[J]$ para una teoria libre y calcula $\delta Z/\delta J(x)$ formalmente.
5. Explica en palabras que mide la cantidad $\delta^2 Z/\delta J(x)\delta J(y)\big|_{J=0}$ en terminos de correladores.

## 12. Cierre

El calculo funcional es el lenguaje en el que esta escrita la QFT moderna. Con derivadas funcionales y la nocion de funcional generador, los correladores, las ecuaciones de movimiento y la integral de camino quedan unificados en un formalismo coherente.

Dominar estas pocas reglas — derivada funcional, regla del producto, resultado basico $\delta\phi(x)/\delta\phi(y)=\delta^{(4)}(x-y)$ — evita mucha confusion cuando el formalismo aparece en los modulos centrales del tutorial.

## 13. Referencias y lecturas recomendadas

- Base: Tong, *Quantum Field Theory*, notas sobre la integral de camino, disponible libremente.
- Complementaria: Zee, *QFT in a Nutshell*, cap. I.2-I.3 para la idea de suma sobre historias.
- Profundizacion: Peskin y Schroeder, cap. 9 para el desarrollo sistematico del formalismo funcional.


---

## Navegacion del tutorial

[(anterior) Delta de Dirac y Transformadas de Fourier](05_delta_de_dirac_y_transformadas_de_fourier.md) | [(siguiente) Algebra de Lie y Representaciones](07_algebra_de_lie_y_representaciones.md)
