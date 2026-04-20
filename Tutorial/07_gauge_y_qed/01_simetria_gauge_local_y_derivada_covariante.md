# Simetria Gauge Local y Derivada Covariante

## 1. Proposito

Una de las ideas mas profundas de la fisica moderna es que ciertas interacciones fundamentales emergen al exigir invariancia bajo simetrias locales. Este documento desarrolla esa idea en el caso mas simple: una simetria de fase $U(1)$.

## 2. Simetria global

Consideremos un campo complejo $\phi$ o un espinor $\psi$ con una simetria global de fase:

$$
\psi \to e^{i\alpha}\psi,
$$

con $\alpha$ constante. Si la accion es invariante bajo esta transformacion, la teoria posee una corriente conservada asociada por el teorema de Noether.

## 3. De global a local

Ahora promovemos el parametro a funcion del espacio-tiempo:

$$
\alpha \to \alpha(x).
$$

En ese momento aparece un problema: la derivada ordinaria del campo ya no transforma de forma covariante, porque al derivar aparece un termino extra proporcional a $\partial_\mu \alpha(x)$.

## 4. Necesidad de un nuevo campo

Para restaurar la invariancia, se introduce un nuevo campo $A_\mu(x)$ y se reemplaza la derivada ordinaria por una derivada covariante:

$$
D_\mu = \partial_\mu + ieA_\mu.
$$

La idea es que $A_\mu$ transforme de manera que compense exactamente el termino adicional introducido por la derivada de la fase local.

## 5. Transformacion gauge

En el caso abeliano de $U(1)$, el campo gauge transforma como

$$
A_\mu \to A_\mu - \frac{1}{e}\partial_\mu \alpha(x),
$$

de modo que el objeto $D_\mu\psi$ se transforma de la misma forma que $\psi$.

Vale la pena comprobar la logica basica. Si

$$
\psi'(x) = e^{i\alpha(x)}\psi(x),
$$

entonces

$$
\partial_\mu \psi' = e^{i\alpha(x)}\left(\partial_\mu + i\partial_\mu \alpha\right)\psi.
$$

El termino extra $i\partial_\mu\alpha$ rompe la covariancia de la derivada ordinaria. La transformacion de $A_\mu$ esta elegida precisamente para cancelar ese exceso y restaurar una ley de transformacion homogena para $D_\mu\psi$.

La leccion conceptual es enorme: el campo gauge no se introduce como adorno. Es la estructura requerida para mantener la simetria local.

## 6. Campo electromagnetico como conexion gauge

Desde esta perspectiva, el potencial electromagnetico deja de ser solo un artificio de calculo y se interpreta como el campo gauge asociado a la simetria local $U(1)$. Su tensor de campo es

$$
F_{\mu\nu} = \partial_\mu A_\nu - \partial_\nu A_\mu.
$$

Este objeto es gauge invariante en el caso abeliano y contiene la informacion fisica del campo electromagnetico.

En terminos mas familiares:

- las componentes electricas y magneticas se empaquetan en $F_{\mu\nu}$;
- el potencial $A_\mu$ tiene redundancia gauge;
- los campos fisicos observables estan codificados en $F_{\mu\nu}$, no en una eleccion concreta de potencial.

El termino cinetico natural del campo gauge es

$$
-\frac{1}{4}F_{\mu\nu}F^{\mu\nu},
$$

porque es local, covariante y gauge invariante.

## 7. Ecuaciones de movimiento y corriente fuente

Al variar la accion respecto de $A_\mu$ aparecen las ecuaciones de Maxwell con fuente:

$$
\partial_\mu F^{\mu\nu} = j^\nu.
$$

En QED, la corriente fuente toma la forma

$$
j^\nu = e\bar{\psi}\gamma^\nu\psi.
$$

Esto resume la teoria en una frase: la corriente del campo de materia actua como fuente del campo gauge.

## 8. Significado geometrico

La derivada covariante puede interpretarse como una forma de comparar campos entre puntos vecinos respetando una simetria interna local. En formulaciones mas avanzadas, esto conecta con la idea geometrica de conexion sobre un fibrado.

No hace falta dominar ese lenguaje para usar QED, pero si conviene registrar la intuicion: la simetria local exige estructura geometrica nueva.

## 9. Fijacion de gauge

La invariancia gauge significa que distintas configuraciones de $A_\mu$ pueden representar la misma situacion fisica. Para cuantizar la teoria de manera operativa suele fijarse una condicion gauge, por ejemplo:

- gauge de Lorenz: $\partial_\mu A^\mu = 0$;
- gauge de Coulomb: $\nabla \cdot \mathbf{A} = 0$.

La fijacion de gauge no cambia los observables fisicos. Su funcion es eliminar redundancia y permitir una definicion controlada del propagador del foton.

## 10. Principio organizador

La gran moraleja del modulo es:

- una simetria global produce una corriente conservada;
- una simetria local exige un campo gauge;
- ese campo gauge describe una interaccion.

Esto explica por que las teorias gauge ocupan un lugar central en la fisica de particulas.

## 11. Preguntas de estudio

- Por que una simetria global no basta para introducir un campo gauge.
- Que problema aparece al hacer local una fase.
- Por que la derivada covariante resuelve ese problema.
- Como se interpreta fisicamente el campo $A_\mu$.
- Por que el tensor $F_{\mu\nu}$ es mas fisico que el potencial aislado.

## 12. Ejercicios sugeridos

1. Explica verbalmente por que $\partial_\mu \psi$ no transforma igual que $\psi$ cuando la fase depende de $x$.
2. Muestra como la transformacion de $A_\mu$ compensa el termino extra de la derivada.
3. Describe la diferencia conceptual entre corriente de Noether y campo gauge.
4. Explica por que fijar gauge no cambia los observables fisicos.

## 13. Cierre

La idea gauge es uno de los principios mas fecundos de la fisica moderna. En su forma mas simple ya contiene la semilla de QED y, en versiones mas ricas, del propio Modelo Estandar.

## 14. Referencias y lecturas recomendadas

- Base: Tong, secciones sobre simetria gauge local.
- Complementaria: Zee, presentacion conceptual del principio gauge.
- Profundizacion: Peskin y Schroeder, introduccion a QED y estructura de las teorias gauge.


---

## Navegacion del tutorial

[(anterior) Quiralidad, Espinores de Weyl y Fermiones de Majorana](../06_fermiones_y_dirac/05_quiralidad_weyl_y_majorana.md) | [(siguiente) QED y Lagrangiano Fundamental](02_qed_y_lagrangiano_fundamental.md)
