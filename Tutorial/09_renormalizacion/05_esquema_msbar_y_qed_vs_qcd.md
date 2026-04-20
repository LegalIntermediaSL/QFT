# Esquema $\overline{\text{MS}}$ y Comparacion QED vs QCD

## 1. Proposito

Este documento profundiza en dos ideas muy usadas en la practica moderna: el esquema de renormalizacion $\overline{\text{MS}}$ y la diferencia cualitativa entre el running coupling en QED y en QCD.

## 2. Del polo al esquema

Una vez identificadas divergencias en regularizacion dimensional, todavia queda decidir que parte exacta se absorbe en la definicion de los parametros renormalizados. Esa decision define un esquema de renormalizacion.

## 3. Esquema MS y $\overline{\text{MS}}$

En el esquema MS se sustraen los polos en $1/\varepsilon$. En $\overline{\text{MS}}$ se absorben ademas ciertas constantes asociadas a la regularizacion dimensional, lo que simplifica mucho expresiones perturbativas.

Pedagogicamente, el mensaje importante es:

- el esquema no cambia la fisica completa;
- si cambia la forma intermedia de los parametros renormalizados;
- algunos esquemas resultan mucho mas comodos para calculos sistematicos.

## 4. QED

En QED, la funcion beta efectiva es positiva a nivel introductorio. Eso significa que el acoplamiento electromagnetico crece lentamente con la escala.

La lectura intuitiva suele asociarse a polarizacion del vacio:

- el vacio cuantico corrige la carga observada;
- a distancias mas cortas o energias mas altas se "ve" una carga efectiva mayor.

## 5. QCD

En QCD ocurre algo mucho mas sorprendente: la funcion beta es negativa en el regimen relevante.

Eso produce:

- libertad asintotica a altas energias;
- interacciones fuertes a bajas energias;
- una intuicion fisica muy distinta de la de QED.

## 6. Por que difieren

La diferencia profunda nace de la estructura gauge:

- QED es abeliana y el foton no se autoacopla del mismo modo;
- QCD es no abeliana y los gluones interactuan entre si.

Ese autoacoplamiento del sector gauge modifica radicalmente el flujo de renormalizacion.

## 7. Ejemplo corto de lectura

Si dos teorias gauge tienen reglas de Feynman parecidas pero funciones beta con signo opuesto, su fisica de escalas puede ser casi opuesta. Ese es precisamente el caso de QED y QCD.

## 8. Cuaderno asociado

- `../../Cuadernos/problemas_resueltos/10_interacciones_y_perturbaciones.ipynb`: usarlo para recordar como los lazos aparecen desde la expansion perturbativa.

## 9. Advertencias utiles

- El esquema $\overline{\text{MS}}$ es una convención extremadamente útil, no una ley fundamental de la naturaleza.
- Cambiar de esquema no debe alterar observables completos bien calculados.
- Comparar QED y QCD solo por "fuerza del acoplamiento" sin mirar la funcion beta puede inducir intuiciones equivocadas.

## 10. Preguntas de comprobacion

- Que papel juega un esquema de renormalizacion.
- Por que $\overline{\text{MS}}$ es tan frecuente en la practica.
- Por que QED y QCD muestran comportamientos opuestos al correr con la escala.

## 11. Referencias y lecturas recomendadas

- Base: Peskin y Schroeder, running couplings y teoria gauge.
- Complementaria: Tong, interpretacion cualitativa de QED y QCD.
- Profundizacion: textos de QCD perturbativa y renormalizacion moderna.


---

## Navegacion del tutorial

[(anterior) Funcion Beta y Running Couplings](04_funcion_beta_y_running_couplings.md) | [(siguiente) Panorama del Lagrangiano del Modelo Estandar](../10_modelo_estandar/01_lagrangiano_del_modelo_estandar.md)
