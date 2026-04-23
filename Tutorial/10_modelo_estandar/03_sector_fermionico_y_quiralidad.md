# Sector Fermionico y Quiralidad

**Nivel:** Avanzado  
**Dificultad:** Alta  
**Tiempo estimado:** 18-25 min  
**Prerequisitos recomendados:** [Sector Gauge y Estructura Electrodébil](02_sector_gauge_y_estructura_electrodebil.md) · [Resumen del modulo](README.md)


## Proposito

Este documento organiza el contenido fermionico del Modelo Estandar y explica por que la interaccion debil es quiral.

La idea no es solo listar campos, sino entender por que la teoria distingue de forma asimetrica entre componentes zurdas y diestras. Esa asimetria no es un detalle menor: es una marca estructural del Modelo Estandar.

## 1. Generaciones de fermiones

El Modelo Estandar contiene quarks y leptones organizados en generaciones. La repeticion generacional es empiricamente clara, aunque su origen profundo no esta explicado por la teoria.

Cada generacion contiene el mismo patron de representaciones gauge, cambiando solo masas y mezclas. Esta repeticion es una de las grandes pistas de que el Modelo Estandar, pese a su exito, probablemente no sea la ultima palabra.

## 2. Dobletes y singletes

La interaccion debil distingue entre componentes zurdas y derechas:

- los fermiones zurdos se agrupan en dobletes de $SU(2)_L$;
- los fermiones diestros son singletes de $SU(2)_L$.

Esto significa que el grupo gauge no actua de la misma manera sobre todas las componentes fermionicas.

Mas esquematicamente, para leptones y quarks aparecen multipletes izquierdos del tipo

$$
L_L = \begin{pmatrix}\nu_L \\ e_L \end{pmatrix},
\qquad
Q_L = \begin{pmatrix}u_L \\ d_L \end{pmatrix},
$$

mientras que $e_R$, $u_R$ y $d_R$ transforman como singletes bajo $SU(2)_L$. Esta diferencia de representaciones es la raiz algebraica de la quiralidad de la interaccion debil.

## 3. Quiralidad

La quiralidad no es un detalle tecnico. Es una marca estructural del Modelo Estandar:

- la interaccion debil viola paridad;
- los bosones $W$ se acoplan solo a corrientes zurdas;
- no puede escribirse ingenuamente un termino de masa fermionica manteniendo intacta la simetria electrodébil.

En otras palabras, la teoria no trata simetricamente izquierda y derecha antes de la ruptura electrodébil. Eso explica por que la paridad no es una simetria del sector debil.

## 4. Terminos cineticos

Esquematicamente, los terminos fermionicos toman la forma

$$
\mathcal{L}_{\text{ferm}} = i\bar{\psi}\gamma^\mu D_\mu \psi.
$$

Toda la informacion sobre cargas, representaciones y acoplamientos esta escondida en la forma concreta de $D_\mu$ para cada campo.

Es precisamente en la derivada covariante donde se codifica como cada fermion se acopla a los bosones gauge. La representacion y la hipercarga determinan su relacion con $W^\pm$, $Z$ y $\gamma$ tras la ruptura electrodébil.

## 5. Importancia conceptual

La estructura quiral explica por que:

- la masa fermionica no puede ponerse "a mano" sin mas;
- el Higgs es necesario;
- la fenomenologia de la interaccion debil es tan distinta de la electromagnetica.

Tambien explica por que las corrientes cargadas tienen una forma tan especifica y por que aparecen violaciones maximales de paridad en procesos debiles.

## 6. Ejemplo corto de lectura

Si se dice que "los $W$ se acoplan solo a fermiones zurdos", no significa que los fermiones diestros no existan, sino que ocupan representaciones distintas del grupo gauge. Esa diferencia de representaciones es precisamente lo que hace que la masa fermionica no pueda escribirse de la forma mas ingenua antes de la ruptura espontanea.

Esta observacion es el puente directo hacia el sector de Yukawa. Las masas fermionicas no se añaden como simples terminos de Dirac desnudos, sino que emergen tras acoplar los fermiones al Higgs de una forma compatible con la simetria gauge inicial.

## Cuaderno asociado
- `../../Cuadernos/problemas_resueltos/11_modelo_estandar_estructura.ipynb`: usarlo para repasar la organizacion quiral del sector fermionico.

## 8. Advertencias utiles

- Quiralidad y helicidad no son exactamente lo mismo, aunque se relacionan en ciertos limites.
- La violacion de paridad no significa falta de consistencia teorica, sino una propiedad experimental real del sector debil.
- El sector fermionico no se entiende bien si se ignoran las representaciones gauge.
- La palabra "zurdo" o "diestro" en este contexto alude a estructura quiral, no a una imagen geometrica ingenua.

## 9. Preguntas de comprobacion

- Por que la interaccion debil es quiral.
- Que diferencia hay entre dobletes y singletes de $SU(2)_L$.
- Por que el problema de las masas fermionicas se conecta directamente con el Higgs.

## Ejercicios sugeridos

1. Explicar por que la asignacion de dobletes y singletes gauge hace quiral al sector debil.
2. Comparar el papel de componentes izquierdas y derechas antes de la ruptura electrodébil.
3. Describir por que la masa fermionica no puede escribirse ingenuamente antes de introducir Yukawas e Higgs.

## 10. Cierre

El sector fermionico del Modelo Estandar muestra de forma muy nitida como la simetria gauge organiza la fisica. La quiralidad no es una rareza tecnica, sino el principio que determina la forma de las corrientes debiles, la necesidad del mecanismo de Higgs y buena parte de la fenomenologia observada.

## 11. Referencias y lecturas recomendadas

- Base: Tong o Schwartz, introduccion al sector fermionico del Modelo Estandar.
- Complementaria: Peskin y Schroeder, corrientes quirales y estructura electrodébil.
- Profundizacion: textos de fenomenologia del Modelo Estandar sobre corrientes cargadas y neutras.


---

## Navegacion del tutorial

[(anterior) Sector Gauge y Estructura Electrodébil](02_sector_gauge_y_estructura_electrodebil.md) | [(siguiente) Mecanismo de Higgs y Ruptura Espontanea](04_mecanismo_de_higgs_y_ruptura_espontanea.md)
