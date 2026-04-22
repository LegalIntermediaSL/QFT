# Corriente de Dirac y Limite No Relativista

## 1. Proposito

Este documento profundiza en dos ideas que suelen quedar demasiado comprimidas en una introduccion: la corriente conservada asociada al campo de Dirac y el modo en que la teoria relativista recupera la fisica de Pauli a bajas energias.

## 2. Corriente de Dirac

La corriente de Dirac se escribe como

$$
j^\mu = \bar{\psi}\gamma^\mu\psi.
$$

Satisface la ecuacion de continuidad

$$
\partial_\mu j^\mu = 0.
$$

Esta corriente aparece tanto desde la ecuacion de Dirac como desde el teorema de Noether asociado a una simetria global de fase.

## 3. Interpretacion

La componente temporal $j^0$ tiene una interpretacion mas controlada que en el caso de Klein-Gordon. Esto fue una de las razones historicas por las que la ecuacion de Dirac se vio como un gran avance.

Ademas, la corriente prepara el camino natural hacia QED, porque el acoplamiento electromagnetico toma precisamente la forma

$$
j^\mu A_\mu.
$$

## 4. Simetria global y carga conservada

Si el lagrangiano es invariante bajo

$$
\psi \to e^{i\alpha}\psi,
$$

entonces existe una carga conservada asociada:

$$
Q = \int d^3x\, j^0.
$$

Este punto es conceptualmente importante porque muestra como una simetria interna muy simple organiza ya la estructura de la interaccion electromagnetica.

## 5. Limite no relativista

Una teoria relativista consistente debe recuperar la fisica ya conocida cuando las energias cineticas son pequenas comparadas con la masa. En la ecuacion de Dirac, eso implica separar componentes grandes y pequenas del espinor.

En ese regimen:

- las componentes grandes dominan;
- las pequenas quedan suprimidas;
- la dinamica efectiva se aproxima a la ecuacion de Pauli.

## 6. Por que importa este limite

El limite no relativista enseña tres cosas a la vez:

- Dirac contiene la mecanica cuantica previa como aproximacion;
- el espin no se añade a mano, sino que emerge naturalmente del formalismo relativista;
- el momento magnetico del fermion aparece de manera estructural.

## 7. Ejemplo corto de lectura

Si una teoria relativista del electron no reprodujera la fisica de Pauli a bajas energias, no seria una generalizacion aceptable. El limite no relativista funciona entonces como prueba de consistencia conceptual de la construccion de Dirac.

## 8. Cuaderno asociado

- `../../Cuadernos/problemas_resueltos/09_cuantizacion_del_campo_escalar.ipynb`: usarlo para comparar el paso de teoria libre a estructura modal, ahora en el contexto fermionico.
- `../../Cuadernos/problemas_resueltos/07_relatividad_y_campos.ipynb`: usarlo como apoyo de trasfondo relativista para el problema conceptual original.

## 9. Advertencias utiles

- La corriente de Dirac no debe confundirse sin mas con una densidad clasica local de partícula en todos los contextos.
- Limite no relativista no significa "ignorar relatividad", sino identificar el regimen en que su descripcion efectiva reproduce la teoria previa.
- El hecho de que Dirac recupere Pauli no trivializa el formalismo relativista; lo valida.

## 10. Preguntas de comprobacion

- De que simetria nace la corriente de Dirac.
- Por que la corriente es importante antes incluso de introducir gauge.
- Que papel cumple el limite no relativista en la interpretacion fisica de la teoria.

## 11. Referencias y lecturas recomendadas

- Base: Tong, corriente de Dirac y limite no relativista.
- Complementaria: Peskin y Schroeder, interpretacion fisica del campo de Dirac.
- Profundizacion: textos de espinores relativistas y ecuacion de Pauli como limite efectivo.


---

## Navegacion del tutorial

[(anterior) Algebra Gamma y Bilineales de Dirac](03_algebra_gamma_y_bilineales_de_dirac.md) | [(siguiente) Quiralidad, Espinores de Weyl y Fermiones de Majorana](05_quiralidad_weyl_y_majorana.md)
