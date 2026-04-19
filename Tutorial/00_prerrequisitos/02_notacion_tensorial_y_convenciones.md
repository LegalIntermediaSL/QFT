# Notacion Tensorial y Convenciones

## 1. Proposito

La QFT usa una notacion compacta y altamente estructurada. Este documento fija las convenciones minimas necesarias para leer expresiones relativistas sin que la notacion se convierta en una barrera.

## 2. Indices y suma de Einstein

En relatividad se usan indices para distinguir componentes de objetos geometricos. La convencion de suma de Einstein establece que, si un indice aparece repetido una vez arriba y una vez abajo, se sobreentiende la suma sobre sus valores:

$$
A_\mu B^\mu = \sum_{\mu=0}^3 A_\mu B^\mu.
$$

Esta convencion hace la escritura mucho mas compacta y es ubicua en QFT.

## 3. Indices covariantes y contravariantes

Un cuatro-vector puede escribirse con indice arriba o abajo:

$$
x^\mu, \qquad x_\mu.
$$

La metrica relativista permite subir y bajar indices:

$$
x_\mu = \eta_{\mu\nu}x^\nu,
\qquad
x^\mu = \eta^{\mu\nu}x_\nu.
$$

Con la convencion

$$
\eta_{\mu\nu} = \eta^{\mu\nu} = \mathrm{diag}(1,-1,-1,-1),
$$

se tiene

$$
x_\mu = (t,-\mathbf{x}).
$$

## 4. Indices griegos y latinos

En fisica de particulas suele usarse:

- indices griegos $\mu,\nu,\rho,\sigma$ para componentes del espacio-tiempo, de $0$ a $3$;
- indices latinos $i,j,k$ para componentes espaciales, de $1$ a $3$;
- otros indices latinos o letras adicionales para color, sabor, espin interno o representaciones de grupo.

Leer bien esos indices es importante porque cada uno identifica una estructura distinta de la teoria.

## 5. Derivadas relativistas

La derivada respecto al espacio-tiempo se escribe

$$
\partial_\mu = \frac{\partial}{\partial x^\mu}.
$$

Con nuestra convencion de metrica,

$$
\partial^\mu = \eta^{\mu\nu}\partial_\nu.
$$

El operador d'Alembertiano se define como

$$
\Box = \partial_\mu \partial^\mu.
$$

En la convencion $(+,-,-,-)$:

$$
\Box = \partial_t^2 - \nabla^2.
$$

Este operador aparece constantemente en ecuaciones relativistas como la de Klein-Gordon.

## 6. Integrales relativistas

La medida basica de integracion en espacio-tiempo es

$$
d^4x = dt\, d^3x.
$$

En una accion relativista se escribe tipicamente

$$
S = \int d^4x\, \mathcal{L}.
$$

En espacio de momentos aparece la medida

$$
d^4p,
$$

y con frecuencia la integral sobre tres-momento

$$
\int \frac{d^3p}{(2\pi)^3}.
$$

## 7. Producto escalar relativista

El producto entre dos cuatro-vectores $a^\mu$ y $b^\mu$ es

$$
a\cdot b = a_\mu b^\mu.
$$

Con la metrica $(+,-,-,-)$:

$$
a\cdot b = a^0b^0 - \mathbf{a}\cdot\mathbf{b}.
$$

Este signo menos en la parte espacial es una de las fuentes mas frecuentes de errores de calculo al empezar.

## 8. Convenciones de metrica

No todos los textos usan la misma metrica. Las dos convenciones mas comunes son:

$$
(+,-,-,-)
\qquad \text{y} \qquad
(-,+,+,+).
$$

La fisica no cambia, pero si cambian algunos signos intermedios en:

- normas de cuatro-vectores;
- definicion del d'Alembertiano;
- terminos cineticos de lagrangianas.

Por eso es indispensable declarar la convencion usada en cada documento tecnico.

## 9. Tensores antisimetricos y ejemplo electromagnetico

Un tensor de rango dos puede tener propiedades de simetria o antisimetra. Un ejemplo central es el tensor de campo electromagnetico

$$
F_{\mu\nu} = \partial_\mu A_\nu - \partial_\nu A_\mu.
$$

Su antisimetra

$$
F_{\mu\nu} = -F_{\nu\mu}
$$

reduce el numero de componentes independientes y refleja la estructura del campo electromagnetico.

## 10. Convenciones utiles en QFT

Algunas notaciones que aparecen una y otra vez son:

- $\bar{\psi} = \psi^\dagger \gamma^0$ para el adjunto de Dirac;
- $\mathcal{L}$ para la densidad lagrangiana;
- $D_\mu$ para derivada covariante;
- $\langle 0| \cdots |0\rangle$ para correladores de vacio;
- $T\{\cdots\}$ para orden temporal.

No hace falta dominarlas todas desde el inicio, pero si conviene familiarizarse con su presencia.

## 11. Errores frecuentes

- olvidar la suma de Einstein;
- perder signos al subir y bajar indices;
- confundir $d^4x$ con $d^3x$;
- mezclar dos convenciones de metrica en el mismo calculo;
- no distinguir indices espaciales de indices de grupo o sabor.

## 12. Preguntas de estudio

- Como se suben y bajan indices.
- Que representa el operador $\Box$.
- Por que las convenciones de metrica importan aunque no cambien la fisica.
- Que significa la notacion compacta $A_\mu B^\mu$.

## 13. Ejercicios sugeridos

1. Calcula explicitamente $x_\mu x^\mu$ para $x^\mu=(t,x,y,z)$ con la metrica $(+,-,-,-)$.
2. Escribe el producto escalar $p_\mu x^\mu$ separando componente temporal y espacial.
3. Muestra que $F_{\mu\nu}$ es antisymetrico por construccion.

## 14. Cierre

La notacion tensorial no es un lujo de estilo. Es el lenguaje que vuelve compacta, covariante y legible la estructura de la teoria relativista.
