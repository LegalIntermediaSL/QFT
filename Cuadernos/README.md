# Cuadernos Jupyter

Este directorio reune notebooks de apoyo para el tutorial de Teoria Cuantica de Campos. Su funcion es complementar los documentos en Markdown con ejemplos computacionales, verificaciones simbolicas, ejercicios guiados y problemas resueltos.

## Estructura

- `ejemplos/`: notebooks breves orientados a ilustrar una idea, formula o tecnica.
- `problemas_resueltos/`: notebooks mas largos orientados a resolver ejercicios paso a paso.

## Cobertura actual

### Modulo 00. Prerrequisitos

- problemas resueltos de relatividad especial minima;
- notacion tensorial y convenciones;
- oscilador armonico cuantico;
- simetrias y grupos basicos;
- delta de Dirac y Fourier.

### Modulos 01 a 05 y lectura avanzada

Se añaden notebooks progresivamente para:

- fundamentos conceptuales;
- relatividad y campos;
- accion y simetrias;
- cuantizacion del campo escalar;
- interacciones y perturbaciones;
- modelo estandar como lectura avanzada.

### Modulos 06 a 10

La siguiente capa natural de cuadernos deberia cubrir:

- `06_fermiones_y_dirac/`: bilineales, corriente de Dirac, proyectores quirales y contraste Dirac/Weyl;
- `07_gauge_y_qed/`: derivada covariante, propagador del foton, scattering elemental y sumas de espin;
- `08_integral_de_camino/`: gaussianas funcionales, $Z[J]$, correladores y accion efectiva;
- `09_renormalizacion/`: regularizacion dimensional, polos $1/\epsilon$ y running couplings;
- `10_modelo_estandar/`: mezcla electrodébil, masas de $W/Z$, corrientes cargadas y neutras, y sector de Higgs.

### Modulo 11. QFT, informacion y agujeros negros

Tambien se incorporan cuadernos para:

- entrelazamiento y estados reducidos;
- horizontes y termicidad efectiva;
- radiacion de Hawking y paradoja de la informacion.

## Segunda hoja de ruta

Una continuacion natural de la primera tanda ya queda iniciada con:

1. `ejemplos/11_integral_de_camino_y_accion_efectiva.ipynb`
Objetivo: fijar la relacion entre integral funcional, accion efectiva y potencial efectivo.

2. `problemas_resueltos/15_regularizacion_dimensional_y_running.ipynb`
Objetivo: reforzar polos en $1/\varepsilon$, escala $\mu$ y running de acoplamientos.

3. `ejemplos/12_unruh_hawking_y_curva_de_page.ipynb`
Objetivo: conectar termicidad efectiva, efecto Unruh, Hawking y curva de Page.

## Tercera hoja de ruta

Una siguiente capa de consulta transversal queda iniciada con:

1. `ejemplos/13_simetrias_discretas_y_cpt.ipynb`
Objetivo: fijar el mapa conceptual entre $C$, $P$, $T$ y $CPT$.

2. `problemas_resueltos/16_ckm_pmns_y_mezcla_de_sabor.ipynb`
Objetivo: seguir de forma guiada la desalineacion entre base de interaccion y base de masa y comparar CKM con PMNS.

3. `ejemplos/14_anomalia_axial_y_cancelacion.ipynb`
Objetivo: distinguir anomalia axial, anomalias gauge y cancelacion de anomalias en el Modelo Estandar.

## Uso sugerido

Los cuadernos no reemplazan el desarrollo teorico del tutorial. Deben usarse para:

- comprobar identidades y derivaciones;
- explorar casos simples con calculo explicito;
- visualizar relaciones entre magnitudes fisicas;
- practicar con problemas seleccionados.

## Enlace con el tutorial

Cuando un documento teorico cite un cuaderno, conviene indicar explicitamente cual es su funcion. Por ejemplo:

- un notebook de `ejemplos/` puede servir para verificar una identidad, visualizar una relacion o seguir una cuenta corta;
- un notebook de `problemas_resueltos/` puede servir para practicar una derivacion mas larga o revisar una solucion guiada.

Las referencias mas utiles no son solo del tipo "ver notebook X", sino "usar notebook X para comprobar Y".

## Prioridades de expansion

Las prioridades mas claras ahora mismo son:

1. crear un notebook para el propagador libre y la causalidad en `04`:
   `ejemplos/08_propagador_libre_y_causalidad.ipynb` ya creado;
2. crear un notebook para LSZ y lectura de diagramas en `05`:
   `problemas_resueltos/12_lsz_y_amplitudes_escalares.ipynb` ya creado;
3. crear un notebook para bilineales y proyectores quirales en `06`:
   `ejemplos/09_bilineales_y_proyectores_quirales.ipynb` ya creado;
4. crear un notebook para gauge-fixing y amplitudes elementales en `07`:
   `problemas_resueltos/13_gauge_fixing_y_scattering_en_qed.ipynb` ya creado;
5. crear un notebook para mezcla electrodébil y masas gauge en `10`:
   `ejemplos/10_mezcla_electrodebil_y_masas_gauge.ipynb` ya creado;
6. crear un notebook para neutrinos y oscilaciones:
   `problemas_resueltos/14_neutrinos_y_oscilaciones.ipynb` ya creado.

## Hoja de ruta concreta

La primera hoja de ruta ya quedó materializada con esta secuencia:

1. `ejemplos/08_propagador_libre_y_causalidad.ipynb`
Objetivo: visualizar la estructura del propagador escalar libre, la prescripcion `i\epsilon` y el papel del conmutador causal.

2. `problemas_resueltos/12_lsz_y_amplitudes_escalares.ipynb`
Objetivo: seguir de forma guiada el paso entre correladores, amputacion y amplitud elemental en un caso escalar.

3. `ejemplos/09_bilineales_y_proyectores_quirales.ipynb`
Objetivo: comparar bilineales de Dirac, proyectores quirales y lectura fisica de corrientes vectoriales y axiales.

4. `problemas_resueltos/13_gauge_fixing_y_scattering_en_qed.ipynb`
Objetivo: revisar derivada covariante, propagador del foton y una amplitud basica de QED.

5. `ejemplos/10_mezcla_electrodebil_y_masas_gauge.ipynb`
Objetivo: seguir la mezcla entre $W^3$ y $B$, el angulo de Weinberg y las relaciones para $m_W$ y $m_Z$.

6. `problemas_resueltos/14_neutrinos_y_oscilaciones.ipynb`
Objetivo: introducir de forma guiada la diferencia entre estados de sabor y de masa y mostrar la idea basica de oscilacion.

## Convenciones

- Mantener nombres de archivo numerados y descriptivos.
- Añadir una celda inicial con objetivo, prerequisitos y resultado esperado.
- Preferir notebooks pequeños y enfocados antes que cuadernos demasiado generales.
- Si un notebook depende de librerias externas, documentarlo al inicio.
- Siempre que sea posible, enlazar el notebook con el documento teorico correspondiente del directorio `Tutorial/`.
