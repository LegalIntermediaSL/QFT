# Panorama del Lagrangiano del Modelo Estandar

## Proposito

El Lagrangiano del Modelo Estandar es una de las expresiones mas densas y exitosas de toda la fisica teorica moderna. Reune en una sola estructura matematica la interaccion fuerte, la interaccion electrodébil, la dinamica de quarks y leptones, el mecanismo de Higgs y la generacion de masas de fermiones, todo ello dentro de una teoria cuantica de campos renormalizable.

Este documento no pretende derivar el Modelo Estandar desde cero, sino ofrecer una lectura estructural de su arquitectura y orientar el recorrido del modulo.

## 1. Vision general

El Modelo Estandar se construye sobre el grupo de gauge

$$
SU(3)_c \times SU(2)_L \times U(1)_Y.
$$

Cada factor controla un tipo de interaccion y determina el contenido de campos gauge correspondiente:

- $SU(3)_c$ describe la cromodinamica cuantica, con gluones como bosones de gauge;
- $SU(2)_L \times U(1)_Y$ describe el sector electrodébil antes de la ruptura espontanea de simetria;
- la combinacion adecuada despues de la ruptura deja como simetria no rota a $U(1)_{\text{EM}}$.

Desde un punto de vista estructural, el lagrangiano del Modelo Estandar puede dividirse en cuatro bloques:

1. sector de gauge;
2. sector fermionico;
3. sector de Higgs;
4. sector de Yukawa.

## 2. Ruta del modulo

Para no comprimir todo en una sola nota, este modulo queda organizado asi:

1. `01_lagrangiano_del_modelo_estandar.md`
   - panorama general del modulo y mapa conceptual.
2. `02_sector_gauge_y_estructura_electrodebil.md`
   - grupo de gauge, tensores de campo y arquitectura electrodébil.
3. `03_sector_fermionico_y_quiralidad.md`
   - generaciones, dobletes, singletes y quiralidad de la interaccion debil.
4. `04_mecanismo_de_higgs_y_ruptura_espontanea.md`
   - potencial de Higgs, vacio no trivial y masas de $W$ y $Z$.
5. `05_yukawas_masas_y_parametros.md`
   - masas fermionicas, matrices de mezcla, parametros libres y poder predictivo.

## 3. Esquema sintetico del lagrangiano

De forma muy resumida, suele pensarse el Lagrangiano del Modelo Estandar como

$$
\begin{aligned}
\mathcal{L}_{\text{SM}}
&= \mathcal{L}_{\text{gauge}} \\
&\quad + \mathcal{L}_{\text{ferm}} \\
&\quad + \mathcal{L}_{\text{Higgs}} \\
&\quad + \mathcal{L}_{\text{Yukawa}}.
\end{aligned}
$$

Este esquema no muestra todos los indices, generaciones y estructuras de grupo, pero si deja clara la arquitectura conceptual de la teoria.

## 4. Por que este modulo importa

El Modelo Estandar es la gran prueba de que la estrategia de la QFT funciona en el mundo real:

- simetrias gauge;
- campos fermionicos quirales;
- ruptura espontanea de simetria;
- renormalizacion;
- predicciones de precision.

Por eso este modulo no es un apendice exotico. Es el punto donde muchos de los hilos del tutorial convergen en una teoria fisica concreta.

## 5. Ejemplo guiado de lectura

Si se ve el simbolo

$$
\mathcal{L}_{\text{SM}} = \mathcal{L}_{\text{gauge}} + \mathcal{L}_{\text{ferm}} + \mathcal{L}_{\text{Higgs}} + \mathcal{L}_{\text{Yukawa}},
$$

una primera lectura util no consiste en memorizar todos los indices, sino en preguntarse:

- que campos se propagan;
- que simetrias organizan el acoplamiento;
- de donde salen las masas;
- que parte del lagrangiano controla mezcla y sabor.

Ese cambio de lectura vuelve mucho mas manejable un objeto que, visto por primera vez, puede parecer inmanejable.

## 6. Cuaderno asociado

- `../../Cuadernos/ejemplos/07_modelo_estandar_panorama.ipynb`: usarlo para recorrer la descomposicion del lagrangiano por bloques.
- `../../Cuadernos/problemas_resueltos/11_modelo_estandar_estructura.ipynb`: usarlo para repasar preguntas estructurales del modulo.

## 7. Preguntas de estudio

- Que papel cumple cada factor del grupo $SU(3)_c \times SU(2)_L \times U(1)_Y$.
- Por que la interaccion debil es quiral.
- Como evita el mecanismo de Higgs introducir masas gauge a mano.
- Por que el sector de Yukawa es indispensable para las masas fermionicas.
- En que sentido el Modelo Estandar es predictivo y, al mismo tiempo, incompleto.

## 8. Cierre

El Lagrangiano del Modelo Estandar no es solo una formula larga. Es la compresion extrema de decadas de intuicion fisica, simetria gauge, estructura cuantica y contraste experimental. Leerlo por bloques permite ver que no es una acumulacion arbitraria de terminos, sino una construccion altamente restringida por los principios de la teoria cuantica de campos.

## 9. Referencias y lecturas recomendadas

- Base: Schwartz, panoramica del Modelo Estandar y su lagrangiano.
- Complementaria: Tong, notas de gauge y electrodinamica electrodébil.
- Profundizacion: Peskin y Schroeder o el PDG para detalles fenomenologicos y convenciones.


---

## Navegacion del tutorial

[(anterior) Esquema $\overline{\text{MS}}$ y Comparacion QED vs QCD](../09_renormalizacion/05_esquema_msbar_y_qed_vs_qcd.md) | [(siguiente) Sector Gauge y Estructura Electrodébil](02_sector_gauge_y_estructura_electrodebil.md)
