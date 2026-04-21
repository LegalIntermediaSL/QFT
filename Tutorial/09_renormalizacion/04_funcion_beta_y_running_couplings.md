# Funcion Beta y Running Couplings

## 1. Proposito

Este documento desarrolla la idea de que los acoplamientos no son numeros fijos absolutos, sino cantidades dependientes de la escala. La funcion beta organiza precisamente esa dependencia.

## 2. Escala de renormalizacion

Una vez renormalizada la teoria, los parametros quedan definidos a una cierta escala $\mu$. Cambiar esa escala cambia el valor numerico del acoplamiento renormalizado, aunque los observables fisicos completos no deberian depender de esa eleccion de forma espuria.

## 3. Definicion de la funcion beta

La funcion beta de un acoplamiento $g$ se define por

$$
\beta(g) = \mu \frac{dg}{d\mu}.
$$

Esta expresion resume como evoluciona el acoplamiento al variar la escala de observacion o de definicion.

En la practica, esta ecuacion es una ecuacion diferencial de flujo. Si a un orden dado se obtiene, por ejemplo,

$$
\beta(g) \simeq b\, g^3,
$$

entonces el running se determina integrando una ecuacion del tipo

$$
\mu\frac{dg}{d\mu} = b\, g^3.
$$

## 4. Lectura fisica

La funcion beta no es solo un artefacto de renormalizacion. Codifica contenido fisico:

- si $\beta(g) > 0$, el acoplamiento crece con la escala;
- si $\beta(g) < 0$, decrece con la escala;
- sus ceros pueden señalar puntos fijos con estructura especial.

## 5. Ejemplos famosos

Dos ejemplos pedagogicos dominan la intuicion moderna:

- en QED, el acoplamiento electromagnetico crece lentamente con la energia;
- en QCD, el acoplamiento fuerte disminuye a altas energias, produciendo libertad asintotica.

Esta diferencia ayuda a entender por que los quarks se comportan casi libres a energias muy altas y, al mismo tiempo, no se observan aislados a bajas energias.

## 6. Running coupling como idea efectiva

Hablar de "constante de acoplamiento" puede inducir a error. En QFT, lo que realmente se mide en distintos procesos suele ser una constante efectiva dependiente de la escala caracteristica del problema.

La leccion central es:

- la teoria cambia su apariencia al cambiar la resolucion con que la observamos;
- esa variacion no destruye la teoria;
- es una de sus predicciones mas distintivas.

Si se integra esquematicamente la ecuacion anterior entre una escala de referencia $\mu_0$ y una escala $\mu$, se obtiene una expresion del tipo

$$
\frac{1}{g^2(\mu)} = \frac{1}{g^2(\mu_0)} - 2b \ln\!\left(\frac{\mu}{\mu_0}\right),
$$

lo que deja ver de forma directa por que el signo de $b$ controla si el acoplamiento crece o decrece al aumentar la escala.

## 7. Ejemplo corto de lectura

Si dos experimentos extraen valores ligeramente distintos de un mismo acoplamiento a energias muy diferentes, eso no implica necesariamente inconsistencia experimental. Puede ser justamente la manifestacion del running coupling predicho por la QFT.

## 8. Cuaderno asociado

- `../../Cuadernos/problemas_resueltos/10_interacciones_y_perturbaciones.ipynb`: usarlo para reforzar la idea de que los lazos modifican amplitudes y parametros efectivos.
- `../../Cuadernos/problemas_resueltos/15_regularizacion_dimensional_y_running.ipynb`: usarlo para fijar la lectura del polo en $1/\varepsilon$, de la escala $\mu$ y de una ley de running elemental.

## 9. Advertencias utiles

- Un acoplamiento corriendo no significa que toda la fisica dependa arbitrariamente del esquema.
- La escala de renormalizacion $\mu$ no coincide siempre sin mas con la energia fisica de cualquier proceso, aunque suele elegirse cerca de la escala relevante.
- La funcion beta es un objeto dependiente del esquema en ciertos detalles, pero su lectura fisica cualitativa suele ser muy robusta.

## 10. Preguntas de comprobacion

- Que resume la funcion beta.
- Por que QED y QCD muestran comportamientos distintos al variar la escala.
- En que sentido un running coupling es una prediccion fisica y no un mero accidente del calculo.

## 11. Referencias y lecturas recomendadas

- Base: Tong, running couplings y grupo de renormalizacion.
- Complementaria: Peskin y Schroeder, funcion beta y escalas.
- Profundizacion: Weinberg o Zinn-Justin sobre puntos fijos, teorias efectivas y flujo de renormalizacion.


---

## Navegacion del tutorial

[(anterior) Regularizacion Dimensional en $\phi^4$](03_regularizacion_dimensional_en_phi4.md) | [(siguiente) Esquema $\overline{\text{MS}}$ y Comparacion QED vs QCD](05_esquema_msbar_y_qed_vs_qcd.md)
