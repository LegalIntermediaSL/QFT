# Simetrias Internas y Cargas Conservadas

**Nivel:** Fundacional  
**Dificultad:** Media-Alta  
**Tiempo estimado:** 35-50 min  
**Prerequisitos recomendados:** [Teorema de Noether: Ejemplos Explicitos](03_teorema_de_noether_ejemplos_explicitos.md) · [Resumen del modulo](README.md)

## Proposito

Este capitulo desarrolla las simetrias internas de grupos U(1), SU(2) y SU(3), sus corrientes conservadas de Noether, las cargas asociadas y la transicion conceptual hacia teorias gauge.

## 1. Introduccion: simetrias que actuan en el espacio interno

En los capitulos anteriores las simetrias estudiadas movian los puntos del espacio-tiempo: traslaciones, rotaciones, boosts. Las simetrias internas son de otro tipo: transforman las componentes del campo sin mover el punto de evaluacion.

Esta distincion no es solo clasificatoria. Las simetrias internas generan cargas conservadas que se identifican con numeros cuanticos internos como la carga electrica, el isospin o el color. Y cuando se promueven de globales a locales, generan interacciones gauge y dan origen a los bosones mediadores de las fuerzas fundamentales.

## 2. Simetria global versus simetria local

Una simetria global es una transformacion cuyo parametro es constante en todo el espacio-tiempo:

$$
\phi(x) \to g\,\phi(x), \qquad g \in G, \quad g \text{ constante}.
$$

Una simetria local (o gauge) permite que el parametro dependa del punto:

$$
\phi(x) \to g(x)\,\phi(x), \qquad g(x) \in G.
$$

El teorema de Noether se aplica directamente a simetrias globales. Las simetrias locales implican una estructura mucho mas rica: exigen la introduccion de campos de conexion (campos gauge) para mantener la invariancia.

En este capitulo se trabajan las simetrias globales y se sientan las bases para el paso a gauge que se desarrollara en el modulo 07.

## 3. Simetria U(1): carga electrica

El grupo U(1) es el grupo de fases complejas, $U(1) = \{e^{i\alpha} : \alpha \in \mathbb{R}\}$. Es el grupo de simetria interna mas simple.

Para un campo escalar complejo $\phi$ con lagrangiana

$$
\mathcal{L} = |\partial_\mu\phi|^2 - m^2|\phi|^2 - \frac{\lambda}{4}|\phi|^4,
$$

la transformacion global U(1) es

$$
\phi \to e^{iq\alpha}\phi, \qquad \phi^* \to e^{-iq\alpha}\phi^*,
$$

donde $q$ es la carga del campo. La corriente de Noether (del capitulo anterior) es:

$$
j^\mu = iq(\phi^*\partial^\mu\phi - \phi\partial^\mu\phi^*).
$$

Esta corriente satisface $\partial_\mu j^\mu = 0$ on-shell. La carga total

$$
Q = q\int d^3x\,j^0
$$

es conservada. Si se identifican varios campos con distintas cargas $q_i$, la carga total es aditiva. Esta estructura es la base de la conservacion de la carga electrica.

## 4. El generador de U(1)

El algebra de Lie de U(1) tiene un unico generador, que en la representacion de carga $q$ actua como

$$
T_q = q\,\cdot\,\mathbf{1}.
$$

La transformacion del campo es $\phi \to e^{i\alpha T_q}\phi$. La carga de Noether es la realizacion operatorial de este generador sobre el espacio de estados:

$$
[\hat Q, \hat\phi] = -q\hat\phi.
$$

La carga distingue particula de antiparticula: si $\hat Q\ket{p} = +q\ket{p}$, entonces $\hat Q\ket{\bar p} = -q\ket{\bar p}$.

## 5. Simetria SU(2): isospin

El grupo SU(2) es el grupo de matrices unitarias $2\times 2$ con determinante 1. Sus elementos se parametrizan como

$$
U = e^{i\alpha^a T^a}, \qquad a = 1, 2, 3,
$$

donde los generadores $T^a = \sigma^a/2$ (con $\sigma^a$ matrices de Pauli) satisfacen el algebra

$$
[T^a, T^b] = i\epsilon^{abc}T^c.
$$

Esta es el algebra de Lie de $\mathfrak{su}(2)$, que es la misma que la del momento angular en mecanica cuantica.

Consideremos un doblete de campos escalares

$$
\Phi = \begin{pmatrix}\phi_1 \\ \phi_2\end{pmatrix},
$$

con lagrangiana

$$
\mathcal{L} = (\partial_\mu\Phi)^\dagger(\partial^\mu\Phi) - m^2\Phi^\dagger\Phi - \frac{\lambda}{4}(\Phi^\dagger\Phi)^2.
$$

Esta lagrangiana es invariante bajo $\Phi \to U\Phi$ con $U \in SU(2)$ constante. Las tres corrientes de Noether son

$$
j^{\mu,a} = -i\Phi^\dagger T^a \overleftrightarrow{\partial^\mu} \Phi \equiv -i(\Phi^\dagger T^a \partial^\mu\Phi - (\partial^\mu\Phi^\dagger)T^a\Phi).
$$

Las tres cargas conservadas son

$$
I^a = \int d^3x\, j^{0,a},
$$

y satisfacen el algebra $[I^a, I^b] = i\epsilon^{abc}I^c$. Estas cargas se identifican con el isospin en fisica nuclear y de particulas.

## 6. Representaciones de SU(2)

Las representaciones irreducibles de SU(2) se etiquetan por el isospin $I = 0, 1/2, 1, 3/2, \ldots$, con $2I+1$ componentes. Las representaciones mas usadas en QFT son:

- Singlete: $I = 0$, una componente, invariante bajo SU(2).
- Doblete: $I = 1/2$, dos componentes, la representacion fundamental.
- Triplete: $I = 1$, tres componentes, la representacion adjunta de SU(2).

En el Modelo Estandar, los quarks y leptones de una generacion forman dobletes de izquierda y singletes de derecha bajo $SU(2)_L$.

## 7. Simetria SU(3): color

El grupo SU(3) es el grupo de matrices unitarias $3\times 3$ con determinante 1. Tiene $3^2 - 1 = 8$ generadores $T^a = \lambda^a/2$, donde $\lambda^a$ son las matrices de Gell-Mann, que satisfacen

$$
[T^a, T^b] = if^{abc}T^c.
$$

Las constantes de estructura $f^{abc}$ son completamente antisimetricas.

Para un triplete de quarks

$$
q = \begin{pmatrix}q_r \\ q_g \\ q_b\end{pmatrix},
$$

la simetria $q \to Uq$ con $U \in SU(3)$ produce ocho corrientes conservadas (una por generador), las corrientes de color. Las cargas de color forman el algebra de color de la QCD.

Las representaciones mas importantes de SU(3) son:

- Singlete de color: $\mathbf{1}$, invariante, como los hadrones observables.
- Triplete: $\mathbf{3}$, la representacion de los quarks.
- Antitriplete: $\bar{\mathbf{3}}$, la de los antiquarks.
- Octete: $\mathbf{8}$, la representacion adjunta, la de los gluones.

## 8. Simetrias como restricciones sobre el lagrangiano

Una de las aplicaciones mas importantes de las simetrias internas es que restringen drásticamente el tipo de terminos que pueden aparecer en el lagrangiano.

Un termino de masa de la forma $m^2\phi_1^*\phi_2$ seria permitido por Lorentz pero estaria prohibido si $\phi_1$ y $\phi_2$ tienen distintas cargas U(1). Igualmente, un termino de interaccion $\phi_1^\dagger\phi_2\phi_3$ solo es gauge invariante bajo SU(2) si los campos estan en la representacion correcta y el producto contiene un singlete.

En la practica esto significa:

1. Se especifica el contenido de campos y sus representaciones bajo las simetrias del modelo.
2. Se escribe el lagrangiano mas general compatible con todas las simetrias.
3. Se estudian las consecuencias fisicas.

Este es el procedimiento con el que se construyo el Modelo Estandar.

## 9. Multiplicidad de cargas

Cuando una teoria tiene varias simetrias internas, los campos llevan cargas bajo cada grupo:

$$
\phi \to e^{iq\alpha} U_{SU(2)} U_{SU(3)} \phi.
$$

Las cargas de Noether asociadas a cada factor del grupo producto son independientes. Un quark up, por ejemplo, tiene:

- Carga electrica $Q = +2/3$ bajo U(1) electromagnetico.
- Isospin $I_3 = +1/2$ bajo SU(2) debil (solo componente izquierda).
- Carga de color bajo SU(3).

Estas cargas no son independientes: la carga electrica en el Modelo Estandar es una combinacion de la hiperacarga Y y el isospin: $Q = I_3 + Y/2$.

## 10. De simetria global a simetria gauge

El paso de una simetria global a una gauge es conceptualmente simple pero consecuentemente rico. Si se exige que la lagrangiana sea invariante bajo

$$
\phi(x) \to e^{i\alpha(x)}\phi(x)
$$

con $\alpha(x)$ dependiente del punto, el termino cinetico $|\partial_\mu\phi|^2$ no es invariante porque

$$
\partial_\mu(e^{i\alpha}\phi) = e^{i\alpha}(\partial_\mu + i\partial_\mu\alpha)\phi.
$$

Para restaurar la invariancia hay que introducir un campo gauge $A_\mu$ y reemplazar la derivada ordinaria por la derivada covariante

$$
D_\mu = \partial_\mu - iqA_\mu,
$$

con la regla de transformacion $A_\mu \to A_\mu + \frac{1}{q}\partial_\mu\alpha$. Con esta sustitucion, $D_\mu\phi \to e^{i\alpha}D_\mu\phi$.

El campo gauge $A_\mu$ tiene su propia cinematica descrita por el tensor de campo $F_{\mu\nu} = \partial_\mu A_\nu - \partial_\nu A_\mu$. La teoria resultante es la electrodinamica cuantica.

Para SU(2) y SU(3) el mecanismo es analogo pero no abeliano: aparecen terminos de autointeraccion del campo gauge que no existen en QED.

## 11. Identidades de Ward y consistencia de la teoria gauge

En una teoria gauge, la corriente de Noether no es solo una cantidad conservada. Genera identidades entre amplitudes de dispersion, las identidades de Ward:

$$
q_\mu \mathcal{M}^\mu = 0,
$$

donde $q$ es el 4-momento del foton virtual y $\mathcal{M}^\mu$ la amplitud con un vertice de foton externo. Estas identidades son consecuencia directa de la invariancia gauge y garantizan la consistencia del calculo perturbativo.

Las identidades de Ward aseguran tambien que las polarizaciones no fisicas del foton no contribuyen a las amplitudes observables.

## 12. Simetrias aproximadas y ruptura

A veces una lagrangiana tiene una simetria aproximada que se rompe por terminos pequenos. El isospin de sabor $SU(2)_f$ que relaciona quarks up y down es una simetria aproximada, rota por la diferencia de masas $m_u \neq m_d$.

En esos casos las cargas no se conservan exactamente. El teorema de Noether se aplica en el limite de la simetria perfecta y las violaciones se tratan como perturbaciones.

## 13. La jerarquia de simetrias del Modelo Estandar

El Modelo Estandar se construye sobre el grupo gauge

$$
G_{SM} = SU(3)_c \times SU(2)_L \times U(1)_Y.
$$

Cada factor corresponde a una interaccion:

- $SU(3)_c$: fuerza fuerte, 8 gluones.
- $SU(2)_L$: fuerza debil izquierda, 3 bosones $W$.
- $U(1)_Y$: hiperacarga, 1 boson $B$.

Tras la ruptura espontanea de simetria por el campo de Higgs, $SU(2)_L \times U(1)_Y \to U(1)_{em}$, aparecen el foton y los bosones $W^\pm$ y $Z$.

Todo este edificio se construye sobre el principio de invariancia gauge, que es el principio de las simetrias internas locales.

## Cuaderno asociado

- Consulta los cuadernos asociados de este bloque en [Resumen del modulo](README.md) para reforzar el capitulo con practica guiada.

## 14. Preguntas de comprobacion

- Que diferencia conceptual hay entre una simetria global y una local, y que implica cada una para la estructura de la teoria.
- Cuantos generadores tiene el grupo SU(2) y por que se identifican con el algebra del momento angular.
- Por que la simetria SU(3) de color requiere exactamente 8 bosones gauge.
- Como se construye el lagrangiano mas general compatible con una simetria interna dada.
- Por que las identidades de Ward son consecuencia de la invariancia gauge.

## 15. Ejercicios sugeridos

1. Para la lagrangiana $\mathcal{L} = (\partial_\mu\Phi)^\dagger\partial^\mu\Phi - m^2\Phi^\dagger\Phi$ con $\Phi$ un doblete SU(2), verificar explicitamente que las tres corrientes de Noether $j^{\mu,a} = -i\Phi^\dagger T^a\overleftrightarrow{\partial^\mu}\Phi$ satisfacen $\partial_\mu j^{\mu,a} = 0$.
2. Mostrar que el termino $\Phi_1^\dagger\Phi_2$ donde $\Phi_1$ tiene hiperacarga $Y_1$ y $\Phi_2$ tiene hiperacarga $Y_2$ es invariante bajo U(1) solo si $Y_1 = Y_2$.
3. Construir el lagrangiano mas general de un campo escalar complejo invariante bajo $U(1) \times U(1)$ con dos campos de cargas $(q_1, 0)$ y $(0, q_2)$ respectivamente.
4. Verificar que la derivada covariante $D_\mu = \partial_\mu - iqA_\mu$ transforma covariantemente bajo una transformacion gauge U(1) local.

## 16. Cierre

Las simetrias internas son el mecanismo por el cual la estructura de grupo organiza los numeros cuanticos internos de la materia. Desde la simple carga U(1) hasta el color SU(3), el patrón es siempre el mismo: una simetria global produce cargas conservadas via Noether, y cuando se promueve a local exige la aparicion de bosones gauge. Este es el principio constructivo sobre el que se asienta todo el Modelo Estandar de la fisica de particulas.

## 17. Referencias y lecturas recomendadas

- Base: Srednicki, capitulos sobre simetrias de sabor, color e interacciones gauge.
- Complementaria: Peskin y Schroeder, capitulo 15, teoria de Yang-Mills y simetria gauge no abeliana.
- Profundizacion: Weinberg, vol. II, estructura gauge del Modelo Estandar.


---

## Navegacion del tutorial

[(anterior) Teorema de Noether: Ejemplos Explicitos](03_teorema_de_noether_ejemplos_explicitos.md) | [(siguiente) Modulo 04: Cuantizacion del Campo Escalar](../04_cuantizacion_del_campo_escalar/README.md)
