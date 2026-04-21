# Mezcla de Sabor: CKM y PMNS

## Objetivo

Este apendice resume la idea de mezcla de sabor en el Modelo Estandar y en sus extensiones minimas para neutrinos. La meta es fijar con claridad que significan las matrices CKM y PMNS, por que aparecen y que clase de fenomenologia condensan.

No se trata solo de memorizar nombres de matrices, sino de entender un hecho estructural profundo: la base natural de interaccion y la base natural de masas no coinciden en general.

## 1. Base de interaccion y base de masa

Una de las lecciones mas importantes del sector de Yukawa es que la base en la que los fermiones se organizan de forma natural en la interaccion gauge no coincide necesariamente con la base en la que sus matrices de masa quedan diagonales.

Esta diferencia entre bases es el origen de la mezcla de sabor.

La lectura fisica es muy importante: la teoria no dice simplemente “cada fermion tiene una masa y ya”. Tambien dice que los estados que participan naturalmente en las corrientes cargadas pueden ser combinaciones lineales de los estados de masa.

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

Esta es una de las mejores ilustraciones de como una diferencia algebraica entre bases termina convirtiendose en una huella experimental muy concreta.

## 4. Parametros de CKM

Para tres generaciones, la matriz CKM contiene:

- tres angulos de mezcla;
- una fase fisica responsable de violacion de $CP$.

Este es un ejemplo precioso de como la estructura algebraica del lagrangiano termina traduciendose en observables experimentales muy concretos.

En la practica, esto significa que el sector quark del Modelo Estandar no solo mezcla sabores, sino que tambien contiene una fuente interna de violacion de $CP$ que puede medirse en procesos hadronicos y decaimientos.

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

Esto ultimo es especialmente importante: el sector leptónico no solo replica la idea de mezcla, sino que puede contener informacion extra sobre la naturaleza misma de la masa de los neutrinos.

## 8. Conexion con quiralidad y Yukawas

CKM y PMNS no son accesorios fenomenologicos que se añaden despues. Emergen del mismo problema estructural ya visto en el tutorial:

- la teoria es quiral;
- las masas fermionicas nacen del sector de Yukawa;
- diagonalizar masas y leer corrientes no es, en general, la misma operacion.

Por eso este apendice se entiende mejor no como fenomenologia aislada, sino como una consecuencia directa de la estructura quiral del Modelo Estandar.

## 9. Violacion de CP

Una de las razones mas importantes para estudiar CKM es que ofrece una fuente fisica de violacion de $CP$ dentro del Modelo Estandar. Esto enlaza directamente con:

- el apendice sobre simetrias discretas y CPT;
- la estructura de sabor;
- la fenomenologia de mesones y transiciones debiles.

En el sector leptónico, una fase de Dirac y posibles fases de Majorana abren ademas una ventana potencial hacia nueva fisica y leptogenesis, aunque eso ya excede el alcance de este tutorial.

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

## 13. Cierre

CKM y PMNS son dos de las mejores pruebas de que el lagrangiano del Modelo Estandar no solo organiza particulas y acoplamientos, sino tambien la forma en que distintas bases fisicas dejan huellas observables. La mezcla de sabor es, en ese sentido, una traduccion experimental muy directa de la estructura algebraica profunda del sector de Yukawa.

## 14. Referencias y lecturas recomendadas

- Base: Schwartz o textos introductorios de fenomenologia del Modelo Estandar.
- Complementaria: PDG, resumen de matriz CKM, mezcla leptónica y parametros de sabor.
- Profundizacion: textos de fisica de sabor y neutrinos.
