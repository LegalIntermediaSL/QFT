# Glosario de Notacion y Conceptos Basicos

Este glosario ya no funciona solo como lista de simbolos. Su objetivo es reunir, en un mismo lugar, convenciones tecnicas y definiciones cortas de conceptos que reaparecen a lo largo del tutorial.

## 1. Espacio-tiempo y metrica

- **Firma de la metrica**: se usa la convencion de fisica de particulas
  $$
  \eta_{\mu\nu} = \mathrm{diag}(+1,-1,-1,-1).
  $$
- **Cuadrivector**: objeto con componentes $x^\mu=(t,\mathbf{x})$ o $p^\mu=(E,\mathbf{p})$ que transforma covariantemente bajo Lorentz.
- **Producto escalar relativista**:
  $$
  p\cdot x = p_\mu x^\mu = Et-\mathbf{p}\cdot\mathbf{x}.
  $$
- **Separacion espacial**: caso en que $(x-y)^2<0$, relevante para causalidad microfisica.

## 2. Unidades naturales

- **Unidades naturales**: convencion en la que
  $$
  c=\hbar=1.
  $$
  En estas unidades, masa, energia e inverso de longitud o tiempo se miden con la misma dimension.

## 3. Cuantizacion y operadores

- **Conmutador bosonico**:
  $$
  [a_\mathbf{p},a_\mathbf{q}^\dagger]=(2\pi)^3\delta^{(3)}(\mathbf{p}-\mathbf{q}).
  $$
- **Anticonmutador fermionico**:
  $$
  \{a_\mathbf{p},a_\mathbf{q}^\dagger\}=(2\pi)^3\delta^{(3)}(\mathbf{p}-\mathbf{q}).
  $$
- **Normalizacion relativista de estados**:
  $$
  \langle \mathbf{p}|\mathbf{q}\rangle=(2\pi)^3 2E_\mathbf{p}\delta^{(3)}(\mathbf{p}-\mathbf{q}).
  $$
- **Espacio de Fock**: espacio de estados que contiene sectores con numero variable de particulas.
- **Vacio**: estado base aniquilado por todos los operadores de aniquilacion del conjunto de modos considerado.

## 4. Fourier y espacio de momentos

- **Transformada de Fourier**:
  $$
  \phi(x)=\int \frac{d^4p}{(2\pi)^4}e^{-ip\cdot x}\tilde{\phi}(p),
  \qquad
  \tilde{\phi}(p)=\int d^4x\, e^{ip\cdot x}\phi(x).
  $$
- **On-shell**: condicion en la que el momento satisface la relacion de dispersion fisica, por ejemplo $p^2=m^2$ para una particula libre de masa $m$.
- **Off-shell**: caso en que una variable de integracion interna no satisface necesariamente la relacion on-shell; aparece de forma natural en propagadores y lineas internas.

## 5. Espinores y algebra de Dirac

- **Algebra de Clifford**:
  $$
  \{\gamma^\mu,\gamma^\nu\}=2\eta^{\mu\nu}.
  $$
- **Adjunto de Dirac**:
  $$
  \bar{\psi}=\psi^\dagger\gamma^0.
  $$
- **Notacion slash**:
  $$
  \slashed{a}=a_\mu\gamma^\mu.
  $$
- **Quiralidad**: propiedad asociada a la accion de $\gamma^5$ y a los proyectores quirales; es central en el sector debil del Modelo Estandar.

## 6. Correladores, propagadores y scattering

- **Correlador**: valor esperado de un producto de operadores de campo, a menudo temporalmente ordenado. Es uno de los objetos mas naturales del formalismo.
- **Propagador**: funcion de Green asociada al operador cinetico libre; en teoria perturbativa aparece como factor de linea interna.
- **Amputacion**: procedimiento por el que se retiran los propagadores externos de un correlador para aislar la amplitud fisica relevante.
- **LSZ**: esquema que conecta correladores del vacio con amplitudes entre estados asintoticos.
- **Estado asintotico**: estado que, muy en el pasado o en el futuro, puede describirse aproximadamente como libre y sirve para definir scattering.
- **Matriz $S$**: operador que conecta estados de entrada y salida y del que se extraen amplitudes observables.

## 7. Simetrias y estructura gauge

- **Simetria global**: transformacion con parametros constantes en el espacio-tiempo.
- **Simetria local o gauge**: transformacion con parametros dependientes del punto, que exige introducir campos gauge para mantener la invariancia.
- **Derivada covariante**: reemplazo de $\partial_\mu$ que incorpora los campos gauge y codifica como cada campo transforma bajo las simetrias locales.
- **Corriente conservada**: corriente asociada a una simetria continua por el teorema de Noether.
- **Corriente cargada**: corriente del sector electrodébil mediada por $W^\pm$, que cambia el componente dentro del doblete.
- **Corriente neutra**: corriente mediada por el boson $Z$, distinta de la corriente electromagnetica aunque relacionada con ella por la mezcla electrodébil.

## 8. Renormalizacion y escalas

- **Regularizacion**: procedimiento para hacer bien definidas expresiones divergentes introduciendo un parametro auxiliar o una modificacion controlada.
- **Renormalizacion**: reorganizacion de parametros y campos para expresar predicciones en terminos de magnitudes fisicas bien definidas.
- **Funcion beta**: objeto que describe como cambia un acoplamiento con la escala de renormalizacion.
- **Running coupling**: acoplamiento efectivo dependiente de la escala.
- **Teoria efectiva**: teoria valida en un rango de energias dado, organizada para capturar la fisica relevante sin describir necesariamente el ultravioleta completo.
- **Renormalizable**: teoria cuya estructura de divergencias puede absorberse en un numero controlado de parametros del lagrangiano.

## 9. Higgs y estructura electrodébil

- **Ruptura espontanea de simetria**: situacion en la que el lagrangiano es simetrico, pero el vacio seleccionado no lo es.
- **Valor esperado del vacio**: valor no nulo de un campo en el estado de vacio; en el sector de Higgs se denota tipicamente por $v$.
- **Angulo de Weinberg**: parametro que organiza la mezcla entre $W^3_\mu$ y $B_\mu$ para producir el foton y el boson $Z$.
- **Boson de Goldstone**: modo sin masa asociado a una ruptura espontanea continua; en el sector electrodébil, los modos pertinentes se reorganizan como polarizaciones longitudinales de bosones gauge masivos.

## 10. Conceptos de frontera

- **Entrelazamiento**: correlacion cuantica no reducible a una descripcion de subsistemas independientes.
- **Efecto Unruh**: percepcion termica del vacio de Minkowski por un observador uniformemente acelerado.
- **Curva de Page**: esquema conceptual para seguir la evolucion de la entropia de entrelazamiento de la radiacion en evaporacion de agujeros negros.
- **Vacio efectivo**: nocion de vacio relevante para un observador, una aproximacion o una teoria efectiva dada; puede no coincidir con la intuicion clasica de "nada".

---
[Volver al Indice del Tutorial](../README.md)
