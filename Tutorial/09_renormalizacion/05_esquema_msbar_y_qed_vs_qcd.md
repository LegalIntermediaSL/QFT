# Esquema $\overline{\text{MS}}$ y Comparacion QED vs QCD

**Nivel:** Intermedio  
**Dificultad:** Media-Alta  
**Tiempo estimado:** 18-25 min  
**Prerequisitos recomendados:** [Funcion Beta y Running Couplings](04_funcion_beta_y_running_couplings.md) · [Resumen del modulo](README.md)


## 1. Proposito

Este documento profundiza en dos ideas muy usadas en la practica moderna: el esquema de renormalizacion $\overline{\text{MS}}$ y la diferencia cualitativa entre el running coupling en QED y en QCD.

## 2. Del polo al esquema

Una vez identificadas divergencias en regularizacion dimensional, todavia queda decidir que parte exacta se absorbe en la definicion de los parametros renormalizados. Esa decision define un esquema de renormalizacion.

Este punto es importante porque muestra que la renormalizacion no termina cuando encontramos el polo divergente. Aun hace falta especificar como se reorganizan las partes finitas y que convencion se adopta para definir los parametros efectivos.

## 3. Esquema MS y $\overline{\text{MS}}$

En el esquema MS se sustraen los polos en $1/\varepsilon$. En $\overline{\text{MS}}$ se absorben ademas ciertas constantes asociadas a la regularizacion dimensional, lo que simplifica mucho expresiones perturbativas.

Mas concretamente, en $\overline{\mathrm{MS}}$ se absorben junto con el polo algunas constantes estandar que aparecen repetidamente al expandir integrales dimensionales. La idea pedagogica no es memorizar la combinacion exacta, sino entender por que el esquema produce formulas mas limpias y comparables entre calculos distintos.

Pedagogicamente, el mensaje importante es:

- el esquema no cambia la fisica completa;
- si cambia la forma intermedia de los parametros renormalizados;
- algunos esquemas resultan mucho mas comodos para calculos sistematicos.

## 4. Por que $\overline{\mathrm{MS}}$ domina la practica

El esquema $\overline{\mathrm{MS}}$ aparece por todas partes en QFT moderna porque:

- encaja muy bien con regularizacion dimensional;
- simplifica el calculo de funciones beta y anomalous dimensions;
- facilita comparar resultados perturbativos entre autores y procesos distintos;
- es especialmente natural en teorias gauge y en fenomenologia de precision.

No es el unico esquema posible, pero si uno de los mas eficientes cuando el objetivo es correr acoplamientos y organizar expansiones sistematicas.

## 5. QED

En QED, la funcion beta efectiva es positiva a nivel introductorio. Eso significa que el acoplamiento electromagnetico crece lentamente con la escala.

La lectura intuitiva suele asociarse a polarizacion del vacio:

- el vacio cuantico corrige la carga observada;
- a distancias mas cortas o energias mas altas se "ve" una carga efectiva mayor.

En una lectura intuitiva, la nube de pares cargados virtuales apantalla la carga desnuda. Cuanto mas de cerca se observa la fuente, menos apantallada aparece y mayor resulta la carga efectiva medida.

## 6. QCD

En QCD ocurre algo mucho mas sorprendente: la funcion beta es negativa en el regimen relevante.

Eso produce:

- libertad asintotica a altas energias;
- interacciones fuertes a bajas energias;
- una intuicion fisica muy distinta de la de QED.

Ese comportamiento explica dos rasgos fundamentales:

- por que la perturbacion funciona bien a energias altas en QCD;
- por que el confinamiento y la dinamica no perturbativa dominan a energias bajas.

## 7. Por que difieren

La diferencia profunda nace de la estructura gauge:

- QED es abeliana y el foton no se autoacopla del mismo modo;
- QCD es no abeliana y los gluones interactuan entre si.

Ese autoacoplamiento del sector gauge modifica radicalmente el flujo de renormalizacion.

En resumen muy cualitativo:

- en QED domina el apantallamiento por materia cargada;
- en QCD compiten quarks y gluones, y el sector gauge no abeliano inclina el balance hacia libertad asintotica.

## 8. Ejemplo corto de lectura

Si dos teorias gauge tienen reglas de Feynman parecidas pero funciones beta con signo opuesto, su fisica de escalas puede ser casi opuesta. Ese es precisamente el caso de QED y QCD.

## 9. Cuaderno asociado

- `../../Cuadernos/problemas_resueltos/10_interacciones_y_perturbaciones.ipynb`: usarlo para recordar como los lazos aparecen desde la expansion perturbativa.

## 10. Advertencias utiles

- El esquema $\overline{\text{MS}}$ es una convención extremadamente útil, no una ley fundamental de la naturaleza.
- Cambiar de esquema no debe alterar observables completos bien calculados.
- Comparar QED y QCD solo por "fuerza del acoplamiento" sin mirar la funcion beta puede inducir intuiciones equivocadas.

## 11. Preguntas de comprobacion

- Que papel juega un esquema de renormalizacion.
- Por que $\overline{\text{MS}}$ es tan frecuente en la practica.
- Por que QED y QCD muestran comportamientos opuestos al correr con la escala.

## 12. Referencias y lecturas recomendadas

- Base: Peskin y Schroeder, running couplings y teoria gauge.
- Complementaria: Tong, interpretacion cualitativa de QED y QCD.
- Profundizacion: textos de QCD perturbativa y renormalizacion moderna.


---

## Navegacion del tutorial

[(anterior) Funcion Beta y Running Couplings](04_funcion_beta_y_running_couplings.md) | [(siguiente) Panorama del Lagrangiano del Modelo Estandar](../10_modelo_estandar/01_lagrangiano_del_modelo_estandar.md)