# Teorema de Noether: Ejemplos Explicitos

**Nivel:** Fundacional  
**Dificultad:** Media  
**Tiempo estimado:** 35-50 min  
**Prerequisitos recomendados:** [Teorema de Noether y Papel Organizador de las Simetrias](02_teorema_de_noether_y_simetria.md) · [Resumen del modulo](README.md)

## Proposito

Este capitulo desarrolla tres aplicaciones concretas del teorema de Noether: la simetria traslacional produce el 4-momento, la simetria de fase U(1) produce la carga conservada, y la simetria de Lorentz produce el tensor de momento angular.

## 1. Introduccion: de la formula a los calculos

El capitulo anterior presento el teorema de Noether en su formulacion general. Ahora se trata de ejecutarlo en casos concretos, desde el principio, sin saltarse pasos. El objetivo es que al terminar este capitulo sea posible aplicar Noether a cualquier simetria continua de una teoria con campos.

La formula general de Noether dice: si la accion es invariante bajo $\phi \to \phi + \epsilon \Delta\phi$ entonces la corriente

$$
j^\mu = \frac{\partial \mathcal{L}}{\partial(\partial_\mu \phi)} \Delta\phi - \mathcal{F}^\mu
$$

es conservada, donde $\mathcal{F}^\mu$ aparece cuando la variacion de la densidad lagrangiana es una derivada total $\delta\mathcal{L} = \partial_\mu \mathcal{F}^\mu$.

## 2. La receta paso a paso

Para aplicar Noether en un caso concreto conviene seguir estos pasos:

1. Escribir la simetria explicita: $x^\mu \to x^\mu + \delta x^\mu$ y $\phi \to \phi + \delta\phi$.
2. Calcular la variacion de la lagrangiana bajo esa transformacion.
3. Identificar si la variacion es exactamente cero o una derivada total.
4. Si es una derivada total, extraer $\mathcal{F}^\mu$.
5. Construir la corriente de Noether.
6. Verificar la conservacion usando las ecuaciones de movimiento.

Este procedimiento se aplica a continuacion en tres ejemplos fundamentales.

## 3. Ejemplo 1: traslaciones espacio-temporales y el 4-momento

Consideramos un campo escalar real $\phi(x)$ con lagrangiana

$$
\mathcal{L} = \frac{1}{2}\partial_\mu\phi\,\partial^\mu\phi - \frac{1}{2}m^2\phi^2.
$$

Una traslacion infinitesimal es $x^\mu \to x^\mu + \epsilon^\nu$ (con $\epsilon^\nu$ constante). El campo cambia como

$$
\phi(x) \to \phi(x - \epsilon) = \phi(x) - \epsilon^\nu \partial_\nu \phi(x).
$$

Calculamos la variacion de la lagrangiana:

$$
\delta\mathcal{L} = -\epsilon^\nu \partial_\nu \mathcal{L} = -\partial_\nu(\epsilon^\nu \mathcal{L}).
$$

Esta es una derivada total, con $\mathcal{F}^\nu = -\epsilon^\nu\mathcal{L}$ (modulo convencion de signo). La corriente de Noether asociada a la traslacion en la direccion $\nu$ es

$$
j^\mu_{(\nu)} = \frac{\partial\mathcal{L}}{\partial(\partial_\mu\phi)}\partial_\nu\phi - \delta^\mu_\nu\mathcal{L} = \partial^\mu\phi\,\partial_\nu\phi - \delta^\mu_\nu\mathcal{L}.
$$

Definiendo el tensor energia-momento como $T^{\mu\nu} = j^\mu_{(\nu)}$:

$$
T^{\mu\nu} = \partial^\mu\phi\,\partial^\nu\phi - \eta^{\mu\nu}\mathcal{L}.
$$

La condicion de conservacion $\partial_\mu T^{\mu\nu} = 0$ puede verificarse usando la ecuacion de Klein-Gordon. La carga conservada asociada a la traslacion temporal es la energia total:

$$
P^0 = E = \int d^3x\, T^{00} = \int d^3x\left[\frac{1}{2}(\partial_t\phi)^2 + \frac{1}{2}(\nabla\phi)^2 + \frac{1}{2}m^2\phi^2\right].
$$

La carga conservada asociada a la traslacion espacial en la direccion $i$ es el momento lineal:

$$
P^i = \int d^3x\, T^{0i} = \int d^3x\,\partial_t\phi\,\partial^i\phi.
$$

El 4-vector $(E, \mathbf{P})$ se transforma como un 4-vector de Lorentz, como corresponde a los generadores de traslacion del grupo de Poincare.

## 4. Verificacion de la conservacion del tensor energia-momento

Para verificar que $\partial_\mu T^{\mu\nu} = 0$ se calcula:

$$
\partial_\mu T^{\mu\nu} = \partial_\mu(\partial^\mu\phi\,\partial^\nu\phi) - \partial^\nu\mathcal{L}.
$$

Usando $\partial_\mu(\partial^\mu\phi) = -m^2\phi$ (ecuacion de Klein-Gordon) y la regla de la cadena para $\partial^\nu\mathcal{L}$:

$$
\partial^\nu\mathcal{L} = \partial^\nu\phi\,\partial_\mu\partial^\mu\phi + \partial^\mu\phi\,\partial^\nu\partial_\mu\phi - m^2\phi\,\partial^\nu\phi.
$$

Reuniendo los terminos con la ecuacion de movimiento se comprueba la cancelacion. Este calculo explicit el mecanismo: la conservacion es consecuencia directa de las ecuaciones de Euler-Lagrange.

## 5. Ejemplo 2: simetria de fase global U(1) y carga conservada

Consideramos ahora un campo escalar complejo $\phi$ con lagrangiana

$$
\mathcal{L} = \partial_\mu\phi^*\,\partial^\mu\phi - m^2\phi^*\phi.
$$

Esta lagrangiana es invariante bajo la transformacion de fase global

$$
\phi \to e^{i\alpha}\phi, \qquad \phi^* \to e^{-i\alpha}\phi^*,
$$

con $\alpha$ constante real. Infinitesimalmente ($\alpha \to \epsilon$ infinitesimal):

$$
\delta\phi = i\epsilon\phi, \qquad \delta\phi^* = -i\epsilon\phi^*.
$$

Calculamos la variacion de la lagrangiana:

$$
\delta\mathcal{L} = \partial_\mu(\delta\phi^*)\,\partial^\mu\phi + \partial_\mu\phi^*\,\partial^\mu(\delta\phi) - m^2(\delta\phi^*)\phi - m^2\phi^*(\delta\phi).
$$

Sustituyendo:

$$
\delta\mathcal{L} = -i\epsilon\partial_\mu\phi^*\,\partial^\mu\phi + i\epsilon\partial_\mu\phi^*\,\partial^\mu\phi - m^2(-i\epsilon\phi^*\phi + i\epsilon\phi^*\phi) = 0.
$$

La lagrangiana es estrictamente invariante, $\delta\mathcal{L} = 0$. La corriente de Noether es entonces

$$
j^\mu = \frac{\partial\mathcal{L}}{\partial(\partial_\mu\phi)}\Delta\phi + \frac{\partial\mathcal{L}}{\partial(\partial_\mu\phi^*)}\Delta\phi^*
$$

con $\Delta\phi = i\phi$ y $\Delta\phi^* = -i\phi^*$:

$$
j^\mu = i\phi\,\partial^\mu\phi^* - i\phi^*\,\partial^\mu\phi = i(\phi\,\partial^\mu\phi^* - \phi^*\,\partial^\mu\phi).
$$

Con la convencion de signos habitual en la literatura se define la corriente con signo opuesto:

$$
j^\mu = -i(\phi^*\partial^\mu\phi - \phi\partial^\mu\phi^*).
$$

La carga conservada es

$$
Q = \int d^3x\, j^0 = -i\int d^3x\left(\phi^*\partial_t\phi - \phi\partial_t\phi^*\right).
$$

Tras la cuantizacion canonica, esta carga se convierte en el operador numero de particulas menos numero de antiparticulas:

$$
\hat Q = \hat N - \hat{\bar N}.
$$

Es la carga interna conservada bajo U(1). Si se identifica este U(1) con el electromagnetismo, $Q$ es la carga electrica.

## 6. Ejemplo 3: simetria de Lorentz y tensor de momento angular

Las transformaciones de Lorentz infinitesimales son

$$
x^\mu \to x^\mu + \omega^{\mu\nu}x_\nu,
$$

con $\omega^{\mu\nu} = -\omega^{\nu\mu}$ antisimetrico. El campo escalar transforma como

$$
\delta\phi = -\omega^{\mu\nu}x_\nu\partial_\mu\phi.
$$

Bajo esta transformacion, la variacion de la lagrangiana es una derivada total:

$$
\delta\mathcal{L} = -\omega^{\mu\nu}x_\nu\partial_\mu\mathcal{L} = -\partial_\mu(\omega^{\mu\nu}x_\nu\mathcal{L}) + \omega^{\mu\nu}\eta_{\mu\nu}\mathcal{L}.
$$

El ultimo termino se anula porque $\omega^{\mu\nu}\eta_{\mu\nu} = 0$ (contraccion de un tensor antisimetrico con uno simetrico).

La corriente de Noether asociada al parametro $\omega^{\rho\sigma}$ es el tensor

$$
\mathcal{M}^{\mu\rho\sigma} = x^\rho T^{\mu\sigma} - x^\sigma T^{\mu\rho},
$$

donde $T^{\mu\nu}$ es el tensor energia-momento del ejemplo anterior. Este tensor satisface

$$
\partial_\mu\mathcal{M}^{\mu\rho\sigma} = 0
$$

cuando se usan las ecuaciones de movimiento y la conservacion de $T^{\mu\nu}$.

Las cargas conservadas son las componentes del tensor de momento angular:

$$
J^{\rho\sigma} = \int d^3x\,\mathcal{M}^{0\rho\sigma} = \int d^3x\left(x^\rho T^{0\sigma} - x^\sigma T^{0\rho}\right).
$$

En particular, las componentes espaciales $J^{ij}$ forman el momento angular orbital, y las componentes $J^{0i}$ generan los boosts.

Para campos con spin no nulo aparecen terminos adicionales que contribuyen al momento angular intrinseco (spin).

## 7. El tensor energia-momento mejorado

El tensor energia-momento calculado por el procedimiento de Noether canonico no siempre es simetrico ni trazablemente cero. Para la maxima utilidad fisica, especialmente en el acoplamiento con la gravedad, se prefiere el tensor energia-momento de Belinfante-Rosenfeld, que es simetrico y gauge invariante:

$$
\Theta^{\mu\nu} = T^{\mu\nu} + \partial_\rho S^{\rho\mu\nu},
$$

donde $S^{\rho\mu\nu}$ es un tensor que se construye de forma que $\Theta^{\mu\nu}$ sea simetrico. Este "mejoramiento" no cambia las cargas conservadas porque el termino adicional es una divergencia.

## 8. Corriente axial y anomalias

Si la lagrangiana es invariante bajo una simetria axial $\phi \to e^{i\alpha\gamma^5}\phi$, el teorema de Noether predice una corriente axial conservada. Sin embargo, a nivel cuantico esta conservacion puede romperse por efectos de lazo. Esta rotura es la anomalia axial, y tiene consecuencias fisicas importantes como la desintegracion $\pi^0 \to \gamma\gamma$.

Las anomalias muestran que las simetrias clasicas no siempre se preservan tras la cuantizacion, un hecho que el teorema de Noether, formulado en el nivel clasico, no puede detectar por si solo.

## 9. Resumen: tres simetrias, tres cargas

| Simetria | Generador | Corriente | Carga conservada |
|:---|:---|:---|:---|
| Traslacion temporal | $\partial_t$ | $T^{0\nu}$ | Energia $E$ |
| Traslacion espacial | $\partial_i$ | $T^{0i}$ | Momento $P^i$ |
| Fase global $U(1)$ | $\phi \to e^{i\alpha}\phi$ | $j^\mu$ | Carga $Q$ |
| Rotacion | $M_{ij}$ | $\mathcal{M}^{0ij}$ | Momento angular $J^{ij}$ |
| Boost | $M_{0i}$ | $\mathcal{M}^{00i}$ | Generador de boost |

## 10. Corrientes conservadas en la teoria cuantizada

Tras la cuantizacion, las corrientes de Noether se convierten en operadores. Las cargas conservadas generan las simetrias a nivel de operadores:

$$
[Q, \phi(x)] = \Delta\phi(x),
$$

donde $\Delta\phi$ es la variacion infinitesimal del campo bajo la simetria. Esta relacion establece que las cargas de Noether son los generadores de las simetrias en el formalismo operatorial.

En particular:

- $[P^\mu, \phi(x)] = -i\partial^\mu\phi(x)$ (el 4-momento genera traslaciones);
- $[Q, \phi] = i\phi$ (la carga U(1) genera la rotacion de fase).

## 11. Importancia practica

El teorema de Noether no es solo un resultado estetico. En la practica de la QFT se usa constantemente para:

- construir corrientes conservadas a partir de lagrangianas dadas;
- identificar que cantidades se conservan en cada interaccion;
- detectar violaciones de simetria cuando la conservacion falla;
- construir identidades de Ward que restringen las amplitudes de dispersion.

## Cuaderno asociado

- Consulta los cuadernos asociados de este bloque en [Resumen del modulo](README.md) para reforzar el capitulo con practica guiada.

## 12. Preguntas de comprobacion

- Por que la variacion de la lagrangiana bajo traslaciones es una derivada total y no estrictamente cero.
- Como se construye el tensor energia-momento canonico a partir de la corriente de Noether de la simetria traslacional.
- Que diferencia hay entre la corriente de Noether de una simetria interna U(1) y la de una simetria espaciotemporal.
- Por que la carga de Noether de una simetria U(1) se interpreta como carga electrica tras la cuantizacion.
- Como aparece el momento angular orbital en el tensor de momento angular derivado de la simetria de Lorentz.

## 13. Ejercicios sugeridos

1. Derivar el tensor energia-momento para la lagrangiana del campo escalar complejo $\mathcal{L} = \partial_\mu\phi^*\partial^\mu\phi - m^2\phi^*\phi$ y verificar que satisface $\partial_\mu T^{\mu\nu} = 0$ usando las ecuaciones de Euler-Lagrange.
2. Para la lagrangiana del campo de Maxwell $\mathcal{L} = -\frac{1}{4}F_{\mu\nu}F^{\mu\nu}$, aplicar el procedimiento de Noether a la simetria traslacional y construir el tensor energia-momento canonico.
3. Verificar que la carga U(1) del campo escalar complejo satisface $[Q, \phi] = \phi$ a nivel de corchetes de Poisson clasicos.

## 14. Cierre

Los tres ejemplos de este capitulo muestran que el teorema de Noether no es una afirmacion abstracta, sino una maquinaria calculable. Traslaciones, fases y transformaciones de Lorentz producen, via Noether, las cantidades conservadas mas fundamentales de la QFT. Dominar estos calculos es una de las habilidades tecnicas mas importantes del curso.

## 15. Referencias y lecturas recomendadas

- Base: Srednicki, capitulos 22-23, corrientes de Noether y tensor energia-momento.
- Complementaria: Tong, notas sobre corrientes conservadas con calculos explicitos.
- Profundizacion: Itzykson y Zuber, seccion sobre simetrias e identidades de Ward.


---

## Navegacion del tutorial

[(anterior) Teorema de Noether y Papel Organizador de las Simetrias](02_teorema_de_noether_y_simetria.md) | [(siguiente) Simetrias Internas y Cargas Conservadas](04_simetrias_internas_y_cargas_conservadas.md)
