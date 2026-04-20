# Corrientes Cargadas y Neutras

## Proposito

Este documento organiza de manera mas explicita como aparecen las corrientes cargadas y neutras en el sector electrodébil del Modelo Estandar. El objetivo es ayudar a leer la estructura fisica de las interacciones debiles una vez que ya se entendieron el grupo gauge, la quiralidad y la ruptura espontanea.

## 1. Punto de partida

El sector electrodébil se construye a partir de

$$
SU(2)_L \times U(1)_Y.
$$

Los fermiones izquierdos aparecen en dobletes de $SU(2)_L$, mientras que muchos fermiones derechos aparecen como singletes. Esta asimetria es justamente la raiz de la naturaleza quiral de la interaccion debil.

## 2. Generadores y combinaciones utiles

Dentro de $SU(2)_L$ es comodo introducir

$$
T^\pm = T^1 \pm i T^2.
$$

Estas combinaciones son las que, al traducirse al lenguaje de los campos gauge fisicos, se conectan con los bosones

$$
W^\pm_\mu.
$$

El generador restante, junto con la hipercarga, participa en la mezcla que termina produciendo el foton y el boson $Z$.

## 3. Corrientes cargadas

Las corrientes cargadas son las que acoplan a los bosones $W^\pm$. De forma esquematica, tienen la estructura

$$
J^\mu_+ \sim \bar{\psi}_L \gamma^\mu T^+ \psi_L,
\qquad
J^\mu_- \sim \bar{\psi}_L \gamma^\mu T^- \psi_L.
$$

Fisicamente, estas corrientes:

- cambian el componente dentro del doblete electrodébil;
- conectan fermiones de distinta carga electrica;
- actuan solo sobre componentes izquierdas en el Modelo Estandar minimo.

## 4. Ejemplos fisicos

En leptones, la corriente cargada conecta por ejemplo:

- neutrino electronico con electron;
- neutrino muonico con muon;
- neutrino tau con tau.

En quarks, la situacion es análoga, pero aparece la estructura de mezcla entre generaciones, que en una formulacion completa se resume en la matriz CKM.

## 5. Corriente neutra

La corriente neutra se acopla al boson $Z_\mu$. A diferencia de la cargada, no cambia el tipo de fermion, pero si distingue combinaciones de isospin debil e hipercarga. Su estructura esquematica se resume en una combinacion del tipo

$$
J^\mu_Z \sim \bar{\psi}\gamma^\mu\left(T^3 - Q\sin^2\theta_W\right)\psi,
$$

donde:

- $T^3$ es el tercer generador debil;
- $Q$ es la carga electrica;
- $\theta_W$ es el angulo de Weinberg.

## 6. Corriente electromagnetica

Tras la mezcla electrodébil, la combinacion ortogonal al $Z$ da lugar al foton, que acopla a la corriente electromagnetica habitual:

$$
J^\mu_{\text{EM}} \sim \bar{\psi}\gamma^\mu Q \psi.
$$

Esta corriente es vectorial y conserva la carga electrica. Pedagogicamente es util subrayar que el electromagnetismo emerge como la simetria gauge no rota del sector electrodébil.

## 7. Diferencia conceptual entre cargada y neutra

La distincion esencial puede resumirse asi:

- la corriente cargada cambia sabor dentro de un multiplete y esta mediada por $W^\pm$;
- la corriente neutra no cambia carga electrica y esta mediada por el $Z$;
- la corriente electromagnetica queda mediada por el foton y sobrevive como simetria no rota.

## 8. Lectura fenomenologica minima

Las corrientes cargadas gobiernan procesos como:

- decaimiento beta;
- produccion o absorcion de neutrinos cargados;
- transiciones entre sabores de quarks.

Las corrientes neutras aparecen en:

- scattering neutro mediado por $Z$;
- procesos de precision electrodébil;
- observables sensibles al angulo de Weinberg.

## 9. Cuaderno asociado

- `../../Cuadernos/problemas_resueltos/11_modelo_estandar_estructura.ipynb`: usarlo para seguir la lectura de corrientes, cargas y sectores del lagrangiano.
- `../../Cuadernos/ejemplos/07_modelo_estandar_panorama.ipynb`: usarlo para situar la corriente electromagnetica como combinacion no rota del sector electrodébil.

## 10. Advertencias utiles

- Corriente neutra no significa ausencia de interaccion, sino interaccion sin cambio de carga electrica.
- La quiralidad del sector debil no es un detalle tecnico: esta escrita en la representacion gauge de los fermiones.
- La corriente electromagnetica final no coincide simplemente con una de las corrientes gauge primitivas antes de la ruptura.

## 11. Preguntas de comprobacion

- Por que las corrientes cargadas solo actuan sobre componentes izquierdas en el Modelo Estandar minimo.
- Que papel cumple el angulo de Weinberg en la corriente neutra.
- En que se diferencia una corriente neutra mediada por $Z$ de la corriente electromagnetica.
- Por que las corrientes cargadas cambian el componente dentro del doblete electrodébil.

## 12. Referencias y lecturas recomendadas

- Base: Schwartz, estructura de corrientes electrodébiles.
- Complementaria: Peskin y Schroeder, acoplamientos fermionicos del sector electrodébil.
- Profundizacion: PDG, resumen de observables y corrientes electrodébiles.


---

## Navegacion del tutorial

[(anterior) Yukawas, Masas y Parametros del Modelo Estandar](05_yukawas_masas_y_parametros.md) | [(siguiente) QFT, informacion y entrelazamiento](../11_qft_informacion_y_agujeros_negros/01_qft_informacion_y_entrelazamiento.md)
