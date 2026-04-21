# Accion Efectiva y Potencial Efectivo

**Nivel:** Intermedio  
**Dificultad:** Media-Alta  
**Tiempo estimado:** 25-35 min  
**Prerequisitos recomendados:** [Funcional Generador y Correladores](02_funcional_generador_y_correladores.md) · [Resumen del modulo](README.md)


## 1. Proposito

Este documento extiende el formalismo funcional hacia dos objetos de gran importancia: la accion efectiva y el potencial efectivo. Ambos permiten resumir correcciones cuanticas y estudiar vacios, simetrias y estabilidad de forma mas estructural.

## 2. De $Z[J]$ a $W[J]$

Si

$$
Z[J]
$$

genera correladores completos, entonces

$$
W[J] = -i\ln Z[J]
$$

genera correladores conectados. Esta transformacion ya es conceptualmente importante porque separa la informacion redundante de diagramas desconectados.

La diferencia no es un mero detalle algebraico. Los diagramas desconectados contienen factores de vacio que no aportan nueva informacion dinamica sobre propagacion o interaccion entre inserciones. Tomar el logaritmo reorganiza la teoria en los bloques conectados realmente relevantes.

## 3. Campo clasico efectivo

Se define el campo clasico efectivo asociado a la fuente por

$$
\phi_c(x) = \frac{\delta W[J]}{\delta J(x)}.
$$

Este objeto puede leerse como el valor esperado del campo en presencia de la fuente externa. No es aun el campo clasico de la teoria original, sino el campo "promedio" que emerge del funcional generador conectado.

Es util insistir en esta idea: $\phi_c(x)$ no es simplemente una configuracion arbitraria elegida a mano, sino la respuesta media del sistema cuando se aplica la fuente $J(x)$. Por eso actua como variable natural al pasar de una descripcion en terminos de fuentes a una descripcion en terminos de campos promedio.

## 4. Accion efectiva

La accion efectiva $\Gamma[\phi_c]$ se obtiene mediante una transformacion de Legendre:

$$
\Gamma[\phi_c] = W[J] - \int d^4x\, J(x)\phi_c(x),
$$

donde ahora $J$ debe entenderse como funcional de $\phi_c$.

La importancia de $\Gamma$ es enorme:

- sus ecuaciones de movimiento ya incluyen correcciones cuanticas;
- genera funciones 1PI;
- organiza el estudio de vacios y ruptura espontanea de simetria.

Mas precisamente, si variamos la accion efectiva,

$$
\frac{\delta \Gamma[\phi_c]}{\delta \phi_c(x)} = -J(x),
$$

y en ausencia de fuente obtenemos la condicion cuantica de movimiento

$$
\frac{\delta \Gamma[\phi_c]}{\delta \phi_c(x)} = 0.
$$

Esta ecuacion reemplaza a la ecuacion clasica del lagrangiano bare cuando ya se han incorporado los efectos de las fluctuaciones.

## 5. Funciones 1PI

Una razon poderosa para introducir $\Gamma$ es que sus derivadas funcionales generan vertices irreducibles a una particula, o funciones 1PI. Estas son los ladrillos estructurales de la teoria cuántica porque:

- reconstruyen correladores completos al reinsertarse con propagadores;
- resumen correcciones de la dinamica de manera compacta;
- permiten identificar masas, acoplamientos y potenciales efectivos renormalizados.

Pedagogicamente, puede verse asi:

- $Z[J]$ genera todo;
- $W[J]$ limpia los desconectados;
- $\Gamma[\phi_c]$ organiza la teoria en terminos de vertices elementales corregidos cuánticamente.

## 6. Potencial efectivo

Cuando el campo es constante o casi constante, la parte relevante de la accion efectiva puede resumirse en el potencial efectivo

$$
V_{\text{eff}}(\phi_c).
$$

Este potencial no es el potencial clasico original sin mas. Incluye, en principio, efectos de las fluctuaciones cuanticas.

Para un campo espacialmente constante, suele escribirse esquematicamente

$$
\Gamma[\phi_c] = - \int d^4x\, V_{\mathrm{eff}}(\phi_c) + \text{terminos con derivadas}.
$$

Esto deja claro por que el potencial efectivo es solo una parte de la accion efectiva: captura la energia del fondo uniforme, mientras que la dinamica espacial y temporal requiere tambien terminos con derivadas.

## 7. Por que importa fisicamente

El potencial efectivo es una herramienta central para entender:

- estabilidad del vacio;
- ruptura espontanea de simetria;
- cambios en la estructura del minimo al incluir correcciones cuanticas;
- transiciones de fase y vacios metastables.

En este sentido, actua como un puente muy natural entre integral de camino, renormalizacion y temas del Modelo Estandar.

## 8. Ejemplo intuitivo: ruptura radiativa

Una de las lecciones mas interesantes del potencial efectivo es que los efectos cuánticos pueden cambiar cualitativamente la estructura del vacio. Un potencial clasico aparentemente simple puede adquirir:

- nuevos minimos;
- minimos desplazados;
- barreras entre vacios;
- metastabilidad.

Ese tipo de fenomeno muestra que la cuantizacion no solo corrige numeros pequeños en amplitudes, sino que puede reorganizar la fase misma del sistema.

## 9. Ejemplo corto de lectura

Si el potencial clasico tiene un minimo en cierto valor del campo, el potencial efectivo puede desplazar, deformar o incluso reorganizar ese minimo una vez que se incorporan fluctuaciones cuanticas. Esa es una de las formas mas claras de ver que la teoria cuantica no solo corrige amplitudes, sino tambien la propia estructura del vacio.

## 10. Cuaderno asociado

- `../../Cuadernos/ejemplos/11_integral_de_camino_y_accion_efectiva.ipynb`: usarlo para fijar la cadena conceptual entre integral funcional, accion efectiva y potencial efectivo, y para visualizar de forma pedagogica como las correcciones cuanticas pueden deformar el vacio.
- `../../Cuadernos/problemas_resueltos/08_accion_y_noether.ipynb`: usarlo para reforzar el papel de la accion como punto de partida estructural.
- `../../Cuadernos/problemas_resueltos/09_cuantizacion_del_campo_escalar.ipynb`: usarlo para revisar el campo libre que luego sirve de base para las correcciones funcionales.

## 11. Advertencias utiles

- El campo clasico efectivo $\phi_c$ no debe confundirse automaticamente con un campo clasico sin fluctuaciones.
- El potencial efectivo depende del esquema y de la escala de renormalizacion en ciertos detalles.
- El minimo del potencial clasico y el del potencial efectivo no tienen por que coincidir exactamente.

## 12. Preguntas de comprobacion

- Que diferencia conceptual hay entre $Z[J]$, $W[J]$ y $\Gamma[\phi_c]$.
- Por que el potencial efectivo es util para estudiar vacios.
- En que sentido la accion efectiva incorpora ya correcciones cuanticas.

## 13. Referencias y lecturas recomendadas

- Base: Peskin y Schroeder, accion efectiva y funciones 1PI.
- Complementaria: Zee, lectura conceptual del potencial efectivo.
- Profundizacion: textos de campo efectivo y ruptura espontanea de simetria.


---

## Navegacion del tutorial

[(anterior) Funcional Generador y Correladores](02_funcional_generador_y_correladores.md) | [(siguiente) Transformaciones de Bogoliubov y Cambio de Vacio](04_bogoliubov_y_cambio_de_vacio.md)