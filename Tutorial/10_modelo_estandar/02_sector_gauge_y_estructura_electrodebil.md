# Sector Gauge y Estructura Electrodébil

**Nivel:** Avanzado  
**Dificultad:** Alta  
**Tiempo estimado:** 25-35 min  
**Prerequisitos recomendados:** [Panorama del Lagrangiano del Modelo Estandar](01_lagrangiano_del_modelo_estandar.md) · [Resumen del modulo](README.md)


## Proposito

Este documento presenta el armazon gauge del Modelo Estandar y organiza el papel de los campos gauge en los sectores fuerte y electrodébil.

## 1. Grupo gauge del Modelo Estandar

La teoria se construye sobre

$$
SU(3)_c \times SU(2)_L \times U(1)_Y.
$$

Cada factor define una simetria local y, por tanto, un conjunto de bosones de gauge:

- $G_\mu^a$ para color;
- $W_\mu^a$ para isospin debil;
- $B_\mu$ para hipercarga.

## 2. Tensores de campo

Los tensores de campo se denotan tipicamente por

$$
G_{\mu\nu}^a, \qquad W_{\mu\nu}^a, \qquad B_{\mu\nu}.
$$

El bloque cinetico toma la forma

$$
\mathcal{L}_{\text{gauge}}
= -\frac{1}{4}G_{\mu\nu}^a G^{a\,\mu\nu}
  -\frac{1}{4}W_{\mu\nu}^a W^{a\,\mu\nu}
  -\frac{1}{4}B_{\mu\nu} B^{\mu\nu}.
$$

## 3. Abeliano frente a no abeliano

La gran diferencia conceptual entre $U(1)$ y los factores no abelianos es que en estos ultimos el propio tensor de campo contiene terminos no lineales. Eso implica:

- autoacoplamiento de los bosones gauge;
- dinamica mas rica;
- diferencia profunda entre QED y QCD.

## 4. Estructura electrodébil

Antes de la ruptura espontanea, el sector electrodébil esta descrito por

$$
SU(2)_L \times U(1)_Y.
$$

Los campos $W_\mu^a$ y $B_\mu$ no coinciden aun con las particulas fisicas observadas. Tras la ruptura:

- una combinacion queda como foton;
- las otras producen los bosones $W^\pm$ y $Z$.

## 5. Derivada covariante

Toda la estructura de acoplamiento entre materia y gauge se condensa en la derivada covariante. En el Modelo Estandar esta incorpora:

- generadores de color;
- generadores de $SU(2)_L$;
- hipercarga.

Por eso leer la derivada covariante equivale, en gran medida, a leer como cada campo "siente" cada interaccion.

En el sector electrodébil, una forma esquematica muy util es

$$
D_\mu = \partial_\mu - ig\, T^a W_\mu^a - ig' \frac{Y}{2} B_\mu.
$$

Esta expresion permite ver de un vistazo que:

- $g$ controla el acoplamiento de $SU(2)_L$;
- $g'$ controla el acoplamiento de hipercarga;
- la carga electrica observable aun no aparece de forma aislada antes de la mezcla electrodébil.

## 6. Mezcla electrodébil

Despues de la ruptura espontanea, los campos neutros $W_\mu^3$ y $B_\mu$ se reorganizan en combinaciones fisicas:

$$
A_\mu = B_\mu \cos\theta_W + W_\mu^3 \sin\theta_W,
$$

$$
Z_\mu = - B_\mu \sin\theta_W + W_\mu^3 \cos\theta_W.
$$

Aqui $\theta_W$ es el angulo de Weinberg. Esta mezcla es uno de los rasgos distintivos del Modelo Estandar: el foton no es un campo gauge primitivo aislado, sino una combinacion particular seleccionada por el vacio.

## 7. Relacion entre acoplamientos

El angulo de Weinberg organiza la relacion entre los acoplamientos del sector electrodébil. De manera esquematica,

$$
\tan\theta_W = \frac{g'}{g},
$$

y la carga electrica efectiva queda conectada con ellos por relaciones del tipo

$$
e = g\sin\theta_W = g'\cos\theta_W.
$$

Esto ayuda a entender como emerge el electromagnetismo como simetria no rota del sector electrodébil.

## 8. Ejemplo corto de lectura

Si un campo no transforma bajo cierto factor del grupo gauge, entonces la parte correspondiente de la derivada covariante actua trivialmente sobre el. Esta observacion ayuda a leer la teoria sin memorizarla toda de golpe:

- un leptón no siente color;
- un singlete de $SU(2)_L$ no siente el acoplamiento debil del mismo modo que un doblete;
- la estructura de cargas puede leerse directamente desde la forma de $D_\mu$.

La mezcla entre $W_\mu^3$ y $B_\mu$ añade una segunda leccion importante: la carga electrica fisica es una combinacion reorganizada de isospin debil e hipercarga, no una etiqueta puesta externamente.

## 9. Cuaderno asociado

- `../../Cuadernos/ejemplos/10_mezcla_electrodebil_y_masas_gauge.ipynb`: usarlo para seguir la mezcla entre $W^3$ y $B$, fijar el papel del angulo de Weinberg y visualizar la reorganizacion del sector neutro.
- `../../Cuadernos/ejemplos/07_modelo_estandar_panorama.ipynb`: usarlo para identificar los sectores gauge y su notacion.

## 10. Advertencias utiles

- No conviene confundir isospin debil con espin ordinario.
- El foton no aparece como uno de los campos gauge primitivos del lagrangiano electrodébil.
- Los sectores no abelianos no son QED con indices extra: su algebra cambia la dinamica.
- El angulo de Weinberg no es una decoracion notacional: resume la mezcla fisica del sector neutro.

## 11. Preguntas de comprobacion

- Que diferencia estructural hay entre el sector gauge de QED y el de QCD.
- Por que los bosones gauge no abelianos pueden autoacoplarse.
- Que papel juega la derivada covariante en el Modelo Estandar.
- Por que el foton y el boson $Z$ aparecen como combinaciones de $W^3$ y $B$.

## 12. Referencias y lecturas recomendadas

- Base: Schwartz, capitulos de gauge y estructura electrodébil.
- Complementaria: Peskin y Schroeder, teorias gauge no abelianas.
- Profundizacion: PDG, resumen del sector gauge del Modelo Estandar.


---

## Navegacion del tutorial

[(anterior) Panorama del Lagrangiano del Modelo Estandar](01_lagrangiano_del_modelo_estandar.md) | [(siguiente) Sector Fermionico y Quiralidad](03_sector_fermionico_y_quiralidad.md)