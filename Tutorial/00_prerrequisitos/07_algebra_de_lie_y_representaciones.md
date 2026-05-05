# Algebra de Lie y Representaciones

**Nivel:** Fundacional  
**Dificultad:** Media-Alta  
**Tiempo estimado:** 30-40 min  
**Prerequisitos recomendados:** [Simetrias y Grupos Basicos](04_simetrias_y_grupos_basicos.md) · [Resumen del modulo](README.md)


## 1. Proposito

El modulo 04 introdujo la idea de grupo y simetria. Este capitulo da el siguiente paso: pasar de la intuicion de simetria al lenguaje algebraico preciso que necesita la QFT para clasificar campos, construir lagrangianos y entender las interacciones gauge.

Las algebras de Lie codifican la estructura local de los grupos de Lie. En la practica, casi todo el calculo con simetrias en QFT se hace al nivel del algebra, no del grupo completo. Entender $\mathfrak{su}(2)$, $\mathfrak{su}(3)$ y las representaciones es suficiente para leer la mayor parte del Modelo Estandar.

## 2. De grupo a algebra

Un grupo de Lie es un grupo que es ademas una variedad diferenciable. Sus elementos pueden parametrizarse continuamente. La idea central es que la estructura del grupo cerca de la identidad esta completamente codificada en su algebra de Lie.

Si $g(\theta)$ es un elemento del grupo parametrizado por $\theta$, el generador correspondiente es

$$
T = -i\,\frac{dg}{d\theta}\bigg|_{\theta=0}.
$$

Los generadores son el alfabeto del algebra. Toda la informacion de las transformaciones infinitesimales esta en ellos.

## 3. Relaciones de conmutacion

El algebra de Lie de un grupo queda definida por las relaciones de conmutacion de sus generadores:

$$
[T_a, T_b] = i\,f_{abc}\,T_c,
$$

donde los $f_{abc}$ son las constantes de estructura del grupo. Estas constantes no son arbitrarias: satisfacen la identidad de Jacobi y determinan por completo la estructura algebraica.

La importancia de estas relaciones es que son independientes de la representacion particular que se use. El algebra es el objeto abstracto; la representacion es una realizacion concreta como matrices.

## 4. El algebra $\mathfrak{su}(2)$

El ejemplo mas importante para QFT es $\mathfrak{su}(2)$, cuyas relaciones de conmutacion son

$$
[T_a, T_b] = i\,\varepsilon_{abc}\,T_c, \qquad a,b,c \in \{1,2,3\}.
$$

Aqui $\varepsilon_{abc}$ es el tensor de Levi-Civita. Esta algebra es identica formalmente a la del momento angular en mecanica cuantica.

Los generadores de $\mathfrak{su}(2)$ en la representacion fundamental son las matrices de Pauli divididas por dos:

$$
T_a = \frac{\sigma_a}{2}, \qquad
\sigma_1 = \begin{pmatrix}0&1\\1&0\end{pmatrix},\quad
\sigma_2 = \begin{pmatrix}0&-i\\i&0\end{pmatrix},\quad
\sigma_3 = \begin{pmatrix}1&0\\0&-1\end{pmatrix}.
$$

En QFT, $\mathfrak{su}(2)$ aparece como simetria de isospin, como sector del grupo electrodebil y como parte estructural del grupo de Poincare.

## 5. El algebra $\mathfrak{su}(3)$

El grupo $SU(3)$ tiene ocho generadores. En la representacion fundamental se construyen a partir de las matrices de Gell-Mann $\lambda_a$:

$$
T_a = \frac{\lambda_a}{2}, \qquad a=1,\ldots,8.
$$

Las relaciones de conmutacion son

$$
[T_a, T_b] = i\,f_{abc}\,T_c,
$$

con constantes de estructura $f_{abc}$ antisimetricas.

$\mathfrak{su}(3)$ es el algebra de gauge de la cromodinamica cuantica (QCD). Sus ocho generadores corresponden a los ocho gluones. La representacion fundamental tiene dimension tres y describe los quarks; la representacion adjunta tiene dimension ocho y describe los gluones.

## 6. Representaciones irreducibles

Una representacion de un algebra de Lie es una aplicacion lineal que asigna matrices a cada generador, preservando las relaciones de conmutacion. Dos representaciones son equivalentes si estan relacionadas por un cambio de base.

Las representaciones irreducibles (irreps) son las que no pueden descomponerse en bloques menores. Son el analogo de las frecuencias propias de un sistema: los objetos mas simples que no pueden fragmentarse.

Para $\mathfrak{su}(2)$, las irreps se etiquetan por el espin $j = 0, \frac{1}{2}, 1, \frac{3}{2}, \ldots$ y tienen dimension $2j+1$:

- $j=0$: singlete, un estado;
- $j=\frac{1}{2}$: doblete, dos estados, representacion fundamental;
- $j=1$: triplete, tres estados, representacion adjunta.

En QFT, los campos fisicos se clasifican segun la representacion de Lorentz en la que transforman. Un campo escalar vive en la representacion trivial; un campo de Dirac, en la representacion espinorial; un boson vectorial, en la representacion vectorial.

## 7. Operador de Casimir

El operador de Casimir de un grupo es un operador que conmuta con todos los generadores:

$$
[C, T_a] = 0 \quad \text{para todo } a.
$$

Por el lema de Schur, en una representacion irreducible $C$ actua como un multiplo de la identidad. Su autovalor etiqueta la representacion.

Para $\mathfrak{su}(2)$, el Casimir cuadratico es

$$
C_2 = T_a T_a = j(j+1)\mathbf{1}.
$$

En QFT, los Casimir aparecen sistematicamente en calculos de QCD (factor $C_F = 4/3$ en procesos con quarks, $C_A = 3$ en procesos con gluones) y en la clasificacion de estados del Modelo Estandar.

## 8. Representacion adjunta

Todo grupo de Lie tiene una representacion natural: la representacion adjunta, donde los generadores actuan sobre el propio espacio del algebra mediante conmutadores:

$$
(T_a)_{bc} = -i\,f_{abc}.
$$

La dimension de la representacion adjunta coincide con el numero de generadores del grupo. Para $SU(2)$ es tres; para $SU(3)$ es ocho.

En el Modelo Estandar, los bosones gauge viven siempre en la representacion adjunta. Esto explica directamente por que existen tres bosones $W$ (adjunta de $SU(2)$) y ocho gluones (adjunta de $SU(3)$).

## 9. Descomposicion de representaciones

El producto tensorial de dos representaciones puede descomponerse en suma directa de irreps:

$$
j_1 \otimes j_2 = |j_1 - j_2| \oplus \cdots \oplus (j_1 + j_2).
$$

Para $\mathfrak{su}(2)$, el ejemplo clasico es la suma de dos espines $\frac{1}{2}$:

$$
\frac{1}{2} \otimes \frac{1}{2} = 0 \oplus 1.
$$

Esta regla de descomposicion esta detras de la clasificacion de estados en mecanica cuantica y de la construccion de operadores invariantes en QFT.

## 10. Conexion con los campos

En QFT, cada campo queda clasificado por:

- su representacion bajo el grupo de Lorentz (espinorial, vectorial, escalar);
- su representacion bajo los grupos de gauge internos ($SU(3)\times SU(2)\times U(1)$);
- sus numeros cuanticos (carga, color, debil isospin, hipercarga).

Esa clasificacion no es una convencion: es la que determina que interacciones puede tener el campo, que terminos pueden aparecer en el lagrangiano y que procesos fisicos genera.

Por eso entender representaciones no es un detalle matematico accesorio. Es el lenguaje en el que esta escrita la estructura del Modelo Estandar.

## Cuaderno asociado

- Consulta los cuadernos asociados de este bloque en [Resumen del modulo](README.md) para reforzar el capitulo con practica guiada.

## 11. Preguntas de comprobacion

- Que informacion contiene el algebra de Lie de un grupo que no esta en el grupo mismo.
- Por que las constantes de estructura determinan completamente el algebra.
- Que diferencia hay entre la representacion fundamental y la adjunta de $SU(2)$.
- Que significa que el operador de Casimir sea proporcional a la identidad en una irrep.
- Por que los bosones gauge viven siempre en la representacion adjunta.

## 12. Ejercicios sugeridos

1. Verifica que las matrices de Pauli satisfacen $[\sigma_a/2, \sigma_b/2] = i\varepsilon_{abc}\sigma_c/2$.
2. Calcula el operador de Casimir $T_a T_a$ en la representacion fundamental de $SU(2)$ y verifica que da $\frac{3}{4}\mathbf{1}$.
3. Descompone el producto $\frac{1}{2}\otimes 1$ de $\mathfrak{su}(2)$ en irreps y da las dimensiones de cada termino.
4. Explica en palabras por que $SU(3)$ tiene ocho generadores y que papel fisico juegan en QCD.
5. Identifica la representacion de Lorentz y de gauge del campo electromagnetico $A_\mu$ en QED.

## 13. Cierre

Las algebras de Lie y sus representaciones son la gramatica de la QFT moderna. Una vez que se entiende que cada campo vive en una representacion especifica de un grupo de simetria, la mayor parte de la estructura del Modelo Estandar deja de ser arbitraria y aparece como la unica opcion compatible con las simetrias elegidas.

Este capitulo cierra el modulo de prerrequisitos. A partir del modulo 01, toda esa maquinaria empieza a trabajar junta para construir la teoria.

## 14. Referencias y lecturas recomendadas

- Base: cualquier introduccion a grupos de Lie para fisicos, como Georgi, *Lie Algebras in Particle Physics*.
- Complementaria: Zee, *Group Theory in a Nutshell for Physicists*, para una perspectiva muy directa.
- Profundizacion: Peskin y Schroeder, apendice de QCD; Cheng y Li para clasificacion de representaciones en el Modelo Estandar.


---

## Navegacion del tutorial

[(anterior) Calculo Funcional y Derivadas Funcionales](06_calculo_funcional_y_derivadas.md) | [(siguiente) Unidades Naturales y Fisicas](08_unidades_naturales_y_fisicas.md)
