# Yukawas, Masas y Parametros del Modelo Estandar

**Nivel:** Avanzado  
**Dificultad:** Alta  
**Tiempo estimado:** 18-25 min  
**Prerequisitos recomendados:** [Mecanismo de Higgs y Ruptura Espontanea](04_mecanismo_de_higgs_y_ruptura_espontanea.md) · [Resumen del modulo](README.md)


## Proposito

Este documento cierra el modulo mostrando como aparecen las masas fermionicas, las mezclas entre generaciones y el inventario de parametros libres.

Es un capitulo importante porque deja ver una tension muy instructiva: el Modelo Estandar es extraordinariamente predictivo, pero no determina desde primeros principios todos los numeros que utiliza. Precisamente por eso el sector de Yukawa es una de las puertas mas claras hacia fisica mas alla del modelo.

## 1. Sector de Yukawa

Los terminos de Yukawa tienen la forma general

$$
\mathcal{L}_{\text{Yukawa}}
= -Y^d_{ij}\,\bar{Q}_i H d_{jR}
   -Y^u_{ij}\,\bar{Q}_i \tilde{H} u_{jR}
   -Y^e_{ij}\,\bar{L}_i H e_{jR}
   + \text{h.c.},
$$

con

$$
\tilde{H} = i\sigma_2 H^*.
$$

La estructura de estos terminos no es arbitraria. Es la forma mas general compatible con la simetria gauge electrodébil y con el contenido de campos fermionicos del modelo.

## 2. De acoplamientos a masas

Tras la ruptura espontanea de simetria, los acoplamientos de Yukawa se convierten efectivamente en masas fermionicas. Ese es el mecanismo que evita introducir terminos de masa incompatibles con la simetria electrodébil inicial.

Cuando el Higgs adquiere valor esperado de vacio, de forma esquematica $v/\sqrt{2}$, aparece una relacion del tipo

$$
m_f \sim \frac{y_f v}{\sqrt{2}},
$$

para cada fermion en una base ya diagonalizada. Esto deja ver con claridad que las jerarquias de masa estan directamente ligadas a jerarquias en los acoplamientos de Yukawa.

## 3. Mezcla entre generaciones

Las matrices de Yukawa no son, en general, diagonales en una misma base para todos los campos. Al diagonalizarlas aparecen:

- masas fisicas;
- matriz CKM para quarks;
- matriz PMNS en formulaciones con masas de neutrinos.

La presencia de matrices no diagonales significa que la base natural para las interacciones gauge no coincide, en general, con la base en la que las masas son diagonales. Esa desalineacion es la fuente de la mezcla de sabores.

## 4. Parametros libres

El Modelo Estandar es extraordinariamente preciso, pero no fija todos sus parametros desde primeros principios. Eso incluye:

- constantes de acoplamiento gauge;
- masas fermionicas;
- masas y acoplamientos del sector de Higgs;
- angulos y fases de mezcla;
- otros parametros como $\bar{\theta}$ de QCD.

Esta lista es una forma compacta de ver el limite explicativo del modelo. Sabemos como usar esos parametros y medirlos, pero no sabemos por que toman exactamente esos valores ni por que muestran jerarquias tan pronunciadas.

## 5. Poder predictivo y limite

La teoria es poderosa no porque tenga cero parametros, sino porque, una vez fijados experimentalmente, permite calcular una enorme cantidad de procesos con precision extrema.

Esa es una leccion metodologica importante. Una teoria puede ser muy profunda aunque no derive todos sus numeros desde principios ultimos, siempre que la estructura que impone sobre procesos y relaciones observables sea lo bastante fuerte.

## 6. Ejemplo corto de lectura

Un acoplamiento de Yukawa pequeno no es un detalle puramente algebraico: significa que, tras la ruptura espontanea, la masa asociada al fermion tambien sera pequena frente a la escala electrodébil. Esta es una manera rapida de leer la jerarquia de masas directamente desde la estructura del lagrangiano.

Por eso el sector de Yukawa concentra una parte grande del misterio del sabor. Las masas de los fermiones abarcan muchos ordenes de magnitud y el modelo describe esa realidad, pero no la explica de fondo.

## 7. Cuaderno asociado

- `../../Cuadernos/problemas_resueltos/11_modelo_estandar_estructura.ipynb`: usarlo para revisar mezcla entre generaciones y parametros libres.

## 8. Advertencias utiles

- Tener parametros libres no vuelve trivial a la teoria.
- La mezcla entre generaciones no es un detalle opcional, sino una parte estructural de la fenomenologia.
- El problema de por que esos parametros toman esos valores sigue abierto.
- La ruptura espontanea genera masas, pero no elimina por si sola el problema de entender la jerarquia de esas masas.

## 9. Preguntas de comprobacion

- Por que el sector de Yukawa es necesario para las masas fermionicas.
- Que informacion codifican CKM y PMNS.
- En que sentido el Modelo Estandar es a la vez exitoso e incompleto.

## 10. Cierre

El sector de Yukawa es una de las zonas mas fecundas del Modelo Estandar. Une simetria gauge, ruptura electrodébil, masas fermionicas y mezcla entre generaciones, pero al mismo tiempo deja abiertas algunas de las preguntas mas profundas de la fisica de particulas: por que existe la jerarquia de masas, por que hay tres generaciones y de donde nace exactamente la estructura de sabor.

## 11. Referencias y lecturas recomendadas

- Base: Schwartz, Yukawas y masas en el Modelo Estandar.
- Complementaria: PDG, parametros y tablas fenomenologicas.
- Profundizacion: textos de fenomenologia electrodébil y de sabor.


---

## Navegacion del tutorial

[(anterior) Mecanismo de Higgs y Ruptura Espontanea](04_mecanismo_de_higgs_y_ruptura_espontanea.md) | [(siguiente) Corrientes Cargadas y Neutras](06_corrientes_cargadas_y_neutras.md)