# QED y Lagrangiano Fundamental

## 1. Proposito

La electrodinamica cuantica es la teoria gauge cuántica mas simple y, al mismo tiempo, una de las mas exitosas de toda la fisica. Este documento organiza su lagrangiano y su significado fisico.

## 2. Campos del problema

En QED aparecen dos tipos de campos:

- el campo fermionico de Dirac $\psi$, que representa electrones y positrones;
- el campo gauge electromagnetico $A_\mu$, asociado al foton.

La teoria describe tanto la propagacion de estos campos como su interaccion.

## 3. Lagrangiano de QED

La forma compacta del lagrangiano es

$$
\mathcal{L}_{\text{QED}}
= \bar{\psi}(i\gamma^\mu D_\mu - m)\psi
- \frac{1}{4}F_{\mu\nu}F^{\mu\nu},
$$

con

$$
D_\mu = \partial_\mu + ieA_\mu.
$$

Al expandir el termino fermionico aparece de manera explicita la interaccion:

$$
\bar{\psi}(i\gamma^\mu \partial_\mu - m)\psi
- e\bar{\psi}\gamma^\mu A_\mu \psi.
$$

## 4. Interpretacion por bloques

Este lagrangiano puede leerse en tres partes:

- propagacion libre del fermion;
- propagacion libre del campo electromagnetico;
- acoplamiento local entre ambos.

La parte de interaccion

$$
-e\bar{\psi}\gamma^\mu A_\mu \psi
$$

es el vertice elemental de QED.

## 5. Lectura fisica del vertice

Ese termino codifica procesos donde:

- un electron emite un foton;
- un electron absorbe un foton;
- un positron emite o absorbe un foton.

En lenguaje perturbativo, todo el formalismo de diagramas y amplitudes de QED se organiza alrededor de este acoplamiento elemental.

## 6. Gauge y conservacion de carga

La estructura gauge de QED no solo introduce el campo electromagnetico; tambien protege la conservacion de la carga electrica y organiza la teoria de manera altamente restringida. La interaccion no se pone a mano por gusto: aparece al imponer la simetria local correcta.

## 7. Por que QED es tan importante

QED es pedagogicamente central por varias razones:

- es la teoria gauge cuantica mas simple;
- ya contiene propagadores, vertices y correcciones radiativas;
- sirve de laboratorio para regularizacion y renormalizacion;
- muestra como una simetria local se convierte en una interaccion real.

## 8. Reglas de Feynman basicas

Sin entrar aun en todos los detalles tecnicos, la teoria produce reglas de Feynman con:

- propagador fermionico;
- propagador del foton;
- vertice proporcional a $\gamma^\mu$ y al acoplamiento $e$.

Estas reglas permiten calcular amplitudes de scattering, anchos de decaimiento y correcciones radiativas.

## 9. Renormalizacion en QED

QED es renormalizable, lo que significa que sus divergencias ultravioletas pueden absorberse de manera controlada en una redefinicion finita del numero apropiado de parametros fisicos. Esta es una de las razones de su exito predictivo extraordinario.

## 10. Preguntas de estudio

- Que campos aparecen en QED.
- Como se lee el termino de interaccion en el lagrangiano.
- Por que el acoplamiento electron-foton surge de la simetria gauge.
- Por que QED es tan importante como teoria modelo.

## 11. Ejercicios sugeridos

1. Separa el lagrangiano de QED en parte libre fermionica, parte libre gauge e interaccion.
2. Explica por que el termino $-e\bar{\psi}\gamma^\mu A_\mu \psi$ representa un acoplamiento local.
3. Describe por que QED prepara de manera natural la entrada al estudio de renormalizacion.

## 12. Cierre

QED es el ejemplo mas limpio de como la simetria gauge, la cuantizacion de campos y el formalismo perturbativo se unen en una teoria fisica de enorme precision experimental.
