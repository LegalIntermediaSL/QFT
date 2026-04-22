# Mezcla de Sabor: CKM y PMNS

## Objetivo

Este apendice resume la idea de mezcla de sabor en el Modelo Estandar y en sus extensiones minimas para neutrinos. La meta es fijar con claridad que significan las matrices CKM y PMNS, por que aparecen y que clase de fenomenologia condensan.

## 1. Base de interaccion y base de masa

Una de las lecciones mas importantes del sector de Yukawa es que la base en la que los fermiones se organizan de forma natural en la interaccion gauge no coincide necesariamente con la base en la que sus matrices de masa quedan diagonales.

Esta diferencia entre bases es el origen de la mezcla de sabor.

## 2. Mezcla en el sector quark

En quarks, al diagonalizar las matrices de Yukawa de tipo ascendente y descendente, las rotaciones necesarias no coinciden en general. Como resultado, la corriente cargada debil no queda diagonal en sabor y aparece la matriz CKM:

$$
V_{\text{CKM}}.
$$

Su papel conceptual es simple:

- organiza como se mezclan sabores de quarks en interacciones cargadas;
- contiene angulos de mezcla y una fase fisica;
- codifica violacion de $CP$ en el sector quark.

## 3. Donde aparece CKM

La matriz CKM aparece en la corriente cargada del sector quark de forma esquematica como

$$
\bar{u}_L \gamma^\mu V_{\text{CKM}} d_L\, W_\mu^+ + \text{h.c.}
$$

Esto significa que:

- el boson $W$ conecta quarks up-type con combinaciones lineales de quarks down-type;
- las transiciones de sabor no tienen todas la misma intensidad;
- la estructura de mezcla es parte intrinseca de la corriente cargada, no un añadido externo.

## 4. Parametros de CKM

Para tres generaciones, la matriz CKM contiene:

- tres angulos de mezcla;
- una fase fisica responsable de violacion de $CP$.

Este es un ejemplo precioso de como la estructura algebraica del lagrangiano termina traduciendose en observables experimentales muy concretos.

## 5. Mezcla en el sector leptónico

En el Modelo Estandar minimo sin masas de neutrinos, una matriz PMNS fisicamente no aparece de la misma forma que CKM. Pero en extensiones minimas con masas de neutrinos, la diagonalizacion del sector leptónico genera una matriz de mezcla:

$$
U_{\text{PMNS}}.
$$

Su papel es análogo al de CKM, aunque la fenomenologia asociada es distinta.

## 6. Donde aparece PMNS

La matriz PMNS organiza la desalineacion entre estados de sabor leptónico y estados de masa neutrínicos. Su consecuencia fisica mas famosa es la oscilacion de neutrinos.

De forma conceptual:

- los neutrinos producidos con un sabor bien definido no tienen por que ser estados de masa puros;
- la evolucion temporal relativa de los estados de masa produce oscilaciones entre sabores;
- la mezcla leptónica se observa de manera distinta a la quark, pero responde a la misma idea general de desalineacion entre bases.

## 7. Diferencia entre CKM y PMNS

Aunque ambas matrices describen mezcla, conviene no tratarlas como copias exactas:

- CKM se manifiesta en transiciones de sabor del sector quark mediadas por corrientes cargadas;
- PMNS se vuelve visible sobre todo en oscilaciones de neutrinos;
- la estructura numerica de sus angulos de mezcla es muy distinta;
- en el sector leptónico pueden aparecer fases adicionales si los neutrinos son de Majorana.

## 8. Conexion con quiralidad y Yukawas

CKM y PMNS no son accesorios fenomenologicos que se añaden despues. Emergen del mismo problema estructural ya visto en el tutorial:

- la teoria es quiral;
- las masas fermionicas nacen del sector de Yukawa;
- diagonalizar masas y leer corrientes no es, en general, la misma operacion.

## 9. Violacion de CP

Una de las razones mas importantes para estudiar CKM es que ofrece una fuente fisica de violacion de $CP$ dentro del Modelo Estandar. Esto enlaza directamente con:

- el apendice sobre simetrias discretas y CPT;
- la estructura de sabor;
- la fenomenologia de mesones y transiciones debiles.

## 10. Uso recomendado dentro del tutorial

Este apendice se aprovecha mejor despues de estudiar:

- [Sector fermionico y quiralidad](../10_modelo_estandar/03_sector_fermionico_y_quiralidad.md)
- [Yukawas, masas y parametros](../10_modelo_estandar/05_yukawas_masas_y_parametros.md)
- [Corrientes cargadas y neutras](../10_modelo_estandar/06_corrientes_cargadas_y_neutras.md)
- [Simetrias discretas, CPT y anomalias](simetrias_discretas_cpt_y_anomalias.md)

## 11. Cuaderno asociado

- `../../Cuadernos/problemas_resueltos/16_ckm_pmns_y_mezcla_de_sabor.ipynb`: usarlo para seguir de forma guiada la idea de desalineacion entre base de interaccion y base de masa, y comparar el papel de CKM y PMNS.

## 12. Preguntas de comprobacion

- Por que la mezcla de sabor aparece al diagonalizar matrices de masa.
- En que tipo de corriente aparece CKM de manera directa.
- Por que PMNS se conecta naturalmente con oscilaciones de neutrinos.
- Que relacion conceptual existe entre mezcla de sabor y violacion de $CP$.

## 13. Referencias y lecturas recomendadas

- Base: Schwartz o textos introductorios de fenomenologia del Modelo Estandar.
- Complementaria: PDG, resumen de matriz CKM, mezcla leptónica y parametros de sabor.
- Profundizacion: textos de fisica de sabor y neutrinos.
