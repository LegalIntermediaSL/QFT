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

La cobertura actual ya incluye:

- `06_fermiones_y_dirac/`: bilineales, proyectores quirales, corriente de Dirac y limite no relativista;
- `07_gauge_y_qed/`: derivada covariante, estructura gauge de QED, gauge-fixing y scattering elemental;
- `08_integral_de_camino/`: funcional generador, correladores, accion efectiva y potencial efectivo;
- `09_renormalizacion/`: regularizacion dimensional, running couplings, esquema $\\overline{\\mathrm{MS}}$ y comparacion QED/QCD;
- `10_modelo_estandar/`: mezcla electrodébil, masas de $W/Z$, corrientes cargadas y neutras, y sector de Higgs.

### Modulo 12. Teorias de Campo Efectivas

Se incorporan cuadernos para:

- conteo dimensional, operadores relevantes y operadores irrelevantes;
- matching a nivel arbol entre teoria UV y EFT;
- lectura del sector debil como teoria efectiva;
- jerarquias de escala y expansion gravitatoria efectiva;
- operador de Weinberg, seesaw y doble beta sin neutrinos;
- introduccion a coeficientes de Wilson y matching UV a SMEFT.

### Modulo 11. QFT, informacion y agujeros negros

Tambien se incorporan cuadernos para:

- entrelazamiento y estados reducidos;
- horizontes y termicidad efectiva;
- radiacion de Hawking y paradoja de la informacion;
- islas y entropia generalizada;
- intuicion holografica y reconstruccion de informacion.

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

## Cuarta hoja de ruta

La capa de integracion del nuevo modulo 12 ya queda iniciada con:

1. `ejemplos/15_operadores_efectivos_y_power_counting.ipynb`
Objetivo: fijar la supresion por escalas, la clasificacion por dimension y el sentido fisico del power counting.

2. `problemas_resueltos/17_fermi_y_matching_efectivo.ipynb`
Objetivo: seguir paso a paso el reemplazo del propagador de un boson pesado por un operador local de cuatro fermiones.

## Quinta hoja de ruta

Se cierra una capa de balance por modulos con:

1. `problemas_resueltos/18_corriente_de_dirac_y_limite_no_relativista.ipynb`
Objetivo: reforzar la corriente de Dirac y el paso al regimen no relativista en el modulo `06`.

2. `ejemplos/16_qed_derivada_covariante_y_ward.ipynb`
Objetivo: fijar la estructura gauge minima de QED y la intuicion de la identidad de Ward en el modulo `07`.

3. `problemas_resueltos/19_correladores_y_accion_efectiva.ipynb`
Objetivo: seguir la cadena entre $Z[J]$, correladores, $W[J]$ y $\\Gamma[\\phi_c]$ en el modulo `08`.

4. `ejemplos/17_esquema_msbar_y_qed_vs_qcd.ipynb`
Objetivo: reforzar el contraste cualitativo entre QED y QCD y el papel del esquema $\\overline{\\mathrm{MS}}$ en el modulo `09`.

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

Las prioridades mas claras ahora mismo ya no son cerrar huecos basicos, sino abrir una capa nueva de profundizacion:

1. una tanda futura de notebooks con calculos simbolicos un poco mas ricos en amplitudes y reglas de Feynman;
2. una capa futura mas tecnica sobre replica trick, superficies extremales y gravedad semiclasica refinada;
3. una capa futura de `matching` mas formal entre una UV completion sencilla y SMEFT;
4. una prolongacion fenomenologica mas cuantitativa de neutrinos, sabor y observables leptónicos.

## Sexta hoja de ruta

Se abre una capa avanzada inicial con:

1. `ejemplos/18_smeft_y_operador_de_weinberg.ipynb`
Objetivo: introducir la extension efectiva del Modelo Estandar y la relevancia especial del operador de dimension cinco.

2. `problemas_resueltos/20_majorana_y_seesaw.ipynb`
Objetivo: seguir la intuicion matricial minima del seesaw y su conexion con masas de neutrinos pequenas.

3. `problemas_resueltos/21_doble_beta_sin_neutrinos.ipynb`
Objetivo: fijar la relacion entre violacion de numero leptónico, neutrinos de Majorana y el observable $0\nu\beta\beta$.

4. `ejemplos/19_matching_uv_a_smeft.ipynb`
Objetivo: introducir el lenguaje de matching y coeficientes de Wilson al pasar de una teoria UV a SMEFT.

## Septima hoja de ruta

Se abre una capa avanzada en el modulo `11` con:

1. `ejemplos/20_islas_y_entropia_generalizada.ipynb`
Objetivo: fijar la lectura moderna de la curva de Page mediante entropia generalizada e inclusion de islas.

2. `problemas_resueltos/22_holografia_y_reconstruccion_de_informacion.ipynb`
Objetivo: ordenar el vocabulario minimo de borde, bulk, reconstruccion e informacion codificada de forma no local.

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
