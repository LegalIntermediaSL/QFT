# Mecanismo de Higgs y Ruptura Espontanea

**Nivel:** Avanzado  
**Dificultad:** Alta  
**Tiempo estimado:** 25-35 min  
**Prerequisitos recomendados:** [Sector Fermionico y Quiralidad](03_sector_fermionico_y_quiralidad.md) · [Resumen del modulo](README.md)


## Proposito

Este documento resume el papel del campo de Higgs, el vacio no trivial y la generacion de masas gauge en el Modelo Estandar.

Su importancia no reside solo en la existencia del boson de Higgs, sino en que resuelve una tension estructural: como dar masa a los bosones débiles sin destruir la consistencia gauge de la teoria.

## 1. Campo de Higgs

El Higgs se introduce como un doblete complejo de $SU(2)_L$, tipicamente denotado por

$$
H.
$$

Su sector lagrangiano se escribe como

$$
\mathcal{L}_{\text{Higgs}}
= (D_\mu H)^\dagger (D^\mu H)
  + m^2 H^\dagger H
  - \lambda (H^\dagger H)^2.
$$

La estructura del potencial es la que permite seleccionar un vacio no trivial. Esa es la pieza realmente decisiva del mecanismo.

## 2. Potencial y vacio

La idea fisica es que el potencial se elige de modo que el vacio no este en $H=0$, sino en una configuracion con valor esperado no nulo:

$$
\langle H \rangle \neq 0.
$$

Eso rompe espontaneamente

$$
SU(2)_L \times U(1)_Y \to U(1)_{\text{EM}}.
$$

La palabra "espontaneamente" es esencial: el lagrangiano sigue respetando la simetria, pero el estado de vacio escogido por la teoria no la manifiesta de la misma manera.

## 3. Masas de bosones gauge

El mecanismo de Higgs permite que:

- $W^\pm$ y $Z$ adquieran masa;
- el foton permanezca sin masa;
- la estructura gauge fundamental de la teoria se conserve.

Ese es uno de los grandes logros conceptuales del Modelo Estandar.

La masa gauge no se introduce entonces como un parche externo, sino como una consecuencia de expandir la teoria alrededor del vacio correcto.

Si se desarrolla el termino cinetico del Higgs alrededor del vacio,

$$
(D_\mu H)^\dagger (D^\mu H),
$$

aparecen terminos cuadraticos en los campos gauge que se leen como masas efectivas. De manera esquematica, el resultado es

$$
m_W = \frac{gv}{2},
\qquad
m_Z = \frac{v}{2}\sqrt{g^2+g'^2},
$$

mientras que el foton permanece sin masa.

## 4. Angulo de Weinberg y espectro fisico

La misma mezcla neutra que reorganiza $W^3_\mu$ y $B_\mu$ en $A_\mu$ y $Z_\mu$ permite escribir

$$
\cos\theta_W = \frac{g}{\sqrt{g^2+g'^2}},
\qquad
\sin\theta_W = \frac{g'}{\sqrt{g^2+g'^2}}.
$$

Con esto aparece tambien la relacion muy usada

$$
m_Z = \frac{m_W}{\cos\theta_W}.
$$

Estas formulas condensan de forma elegante la estructura del sector gauge roto.

Tambien dejan ver que las masas de $W$ y $Z$ no son parametros arbitrarios totalmente independientes, sino cantidades relacionadas por la estructura interna de la teoria.

## 5. Escala electrodébil

El valor esperado del Higgs

$$
v \approx 246\ \text{GeV}
$$

fija la escala electrodébil y conecta directamente la teoria con magnitudes observables.

Esa escala es una de las bisagras de toda la fenomenologia del Modelo Estandar: a partir de ella se organizan masas gauge, Yukawas y lectura efectiva de muchos procesos.

## 6. Bosones de Goldstone y gauge unitario

En el lenguaje mas completo, el doblete de Higgs contiene grados de libertad que, tras la ruptura espontanea, se reorganizan en:

- un modo escalar fisico, el boson de Higgs;
- tres modos de Goldstone que se "absorben" para dar polarizaciones longitudinales a $W^\pm$ y $Z$.

Esta lectura ayuda a entender por que los bosones vectoriales masivos tienen el numero correcto de grados de libertad despues de la ruptura.

Sin esta reorganizacion, el recuento de grados de libertad seria inconsistente. Esa es otra forma de ver que el mecanismo de Higgs no es un adorno, sino una solucion estructural.

## 7. Lectura pedagogica

El Higgs no debe entenderse solo como "la particula descubierta en el LHC". Antes que eso, es el mecanismo que hace compatible:

- invariancia gauge;
- masas para bosones debiles;
- renormalizabilidad.

Esta es probablemente la mejor forma de enseñarlo: primero como principio organizador de la teoria, y solo despues como estado excitado observable.

## 8. Ejemplo corto de lectura

El punto esencial no es "añadir una particula Higgs" al inventario, sino entender que un vacio no simetrico reorganiza la teoria:

- los campos gauge siguen presentes;
- la simetria del lagrangiano se conserva;
- el espectro observable cambia porque el vacio selecciona una direccion en el espacio interno.

En esa reorganizacion, los campos $W^\pm$, $Z$ y $A$ no se interpretan igual que antes de la ruptura: cambian las combinaciones fisicas relevantes y aparecen terminos de masa sin haber roto explicitamente la simetria en el lagrangiano.

Ese cambio de base fisica es lo que hace tan natural la conexion con el capitulo anterior sobre mezcla electrodébil.

## Cuaderno asociado
- `../../Cuadernos/ejemplos/10_mezcla_electrodebil_y_masas_gauge.ipynb`: usarlo para revisar las relaciones estructurales entre $g$, $g'$, $\theta_W$, $m_W$ y $m_Z$ a partir del vacio del Higgs.
- `../../Cuadernos/ejemplos/07_modelo_estandar_panorama.ipynb`: usarlo para ubicar el sector de Higgs dentro del lagrangiano completo.

## 10. Advertencias utiles

- Ruptura espontanea no significa ruptura explicita de la simetria en el lagrangiano.
- El foton sin masa no es un accidente: refleja la simetria electromagnetica no rota.
- El boson de Higgs observado es la excitacion cuantica alrededor del vacio, no "el vacio mismo".
- Los terminos de masa de $W$ y $Z$ no se insertan a mano: emergen al expandir el termino cinetico del Higgs alrededor del vacio.

## 11. Preguntas de comprobacion

- Por que no pueden ponerse masas gauge a mano.
- Que significa que el vacio rompa espontaneamente la simetria.
- Por que el foton queda sin masa mientras $W$ y $Z$ no.
- Como se relacionan $m_W$, $m_Z$ y el angulo de Weinberg.

## Ejercicios sugeridos

1. Explicar por que introducir masas gauge a mano rompería la estructura de simetria de la teoria.
2. Describir como el vacio del Higgs reorganiza los grados de libertad fisicos del sector electrodébil.
3. Relacionar ruptura espontanea, mezcla neutra y masas de $W$ y $Z$ en una sola cadena conceptual.

## 12. Referencias y lecturas recomendadas

- Base: Schwartz, mecanismo de Higgs y ruptura electrodébil.
- Complementaria: Tong, notas sobre Higgs en teorias gauge.
- Profundizacion: PDG, resumen del sector de Higgs.


---

## Navegacion del tutorial

[(anterior) Sector Fermionico y Quiralidad](03_sector_fermionico_y_quiralidad.md) | [(siguiente) Yukawas, Masas y Parametros del Modelo Estandar](05_yukawas_masas_y_parametros.md)
