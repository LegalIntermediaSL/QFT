# Motivacion y Ecuacion de Dirac

**Nivel:** Nucleo  
**Dificultad:** Media  
**Tiempo estimado:** 25-35 min  
**Prerequisitos recomendados:** [Modulo anterior](../05_interacciones_y_perturbaciones/README.md) · [Resumen del modulo](README.md)


## 1. Proposito

La ecuacion de Dirac representa uno de los hitos mas profundos de la fisica teorica del siglo XX. Nace del intento de construir una ecuacion cuantica relativista mejor comportada que la de Klein-Gordon para particulas de espin $1/2$, y termina introduciendo de forma natural espinores, antiparticulas y una nueva vision de la materia fermionica.

## 2. Que problema se queria resolver

La ecuacion de Klein-Gordon respeta la relacion relativista

$$
E^2 = \mathbf{p}^2 + m^2,
$$

pero es cuadratica en derivadas temporales. Esto hace mas dificil mantener una interpretacion probabilistica similar a la de Schrodinger para fermiones de espin $1/2$.

Dirac planteo una idea radical: buscar una ecuacion lineal tanto en derivadas temporales como espaciales, de modo que al cuadrarla reproduzca la relacion relativista correcta.

## 3. La idea de linealizacion

Dirac propone una ecuacion de la forma

$$
\left(i\gamma^\mu \partial_\mu - m\right)\psi = 0,
$$

donde:

- $\psi$ ya no es un escalar, sino un espinor;
- las $\gamma^\mu$ son matrices, no numeros ordinarios.

La condicion de consistencia exige que esas matrices satisfagan la algebra de Clifford:

$$
\{\gamma^\mu,\gamma^\nu\} = 2\eta^{\mu\nu}.
$$

Esta identidad garantiza que, al aplicar de nuevo el operador de Dirac, se recupere la ecuacion de Klein-Gordon componente a componente.

Si actuamos con el operador conjugado

$$
\left(i\gamma^\nu\partial_\nu + m\right),
$$

se obtiene

$$
\left(i\gamma^\nu\partial_\nu + m\right)\left(i\gamma^\mu\partial_\mu - m\right)\psi = 0.
$$

Al expandir, los terminos cruzados se cancelan y queda una expresion proporcional a

$$
\gamma^\nu\gamma^\mu\partial_\nu\partial_\mu + m^2.
$$

Como las derivadas conmutan, solo importa la parte simetrica de $\gamma^\nu\gamma^\mu$, y la algebra anticommutadora la reduce a

$$
\left(\Box + m^2\right)\psi = 0.
$$

Asi, cada componente del espinor satisface Klein-Gordon, pero la ecuacion original contiene informacion adicional sobre espin y estructura de antiparticulas.

## 4. Espinores y representaciones gamma

Un espinor no es simplemente un vector ordinario de cuatro componentes. Es un objeto que transforma bajo una representacion espinorial del grupo de Lorentz.

La necesidad de introducir espinores revela una leccion profunda:

- los fermiones relativistas no caben en el mismo lenguaje geometrico que escalares o vectores;
- la estructura de simetria del espacio-tiempo distingue clases de objetos mas ricas;
- el espin aparece como parte intrinseca del formalismo relativista.

La algebra de Clifford puede representarse con matrices $4\times 4$ en distintas bases. Dos de las mas usadas son:

- la base de Dirac, muy util para el limite no relativista;
- la base de Weyl o quiral, especialmente natural para estudiar quiralidad y el Modelo Estandar.

La base concreta no cambia la fisica. Lo relevante es la algebra y la forma en que el espinor transforma.

## 5. Corriente conservada y simetria global

De la ecuacion de Dirac puede construirse la corriente

$$
j^\mu = \bar{\psi}\gamma^\mu \psi,
$$

con

$$
\bar{\psi} = \psi^\dagger \gamma^0.
$$

Esta corriente satisface

$$
\partial_\mu j^\mu = 0.
$$

Una ventaja importante es que la componente temporal $j^0$ tiene mejor comportamiento para la interpretacion probabilistica que en el caso de Klein-Gordon.

Tambien es importante notar que esta corriente no aparece por magia. Si partimos del lagrangiano de Dirac

$$
\mathcal{L} = \bar{\psi}(i\gamma^\mu \partial_\mu - m)\psi
$$

e imponemos una simetria global de fase

$$
\psi \to e^{i\alpha}\psi,
$$

entonces el teorema de Noether conduce precisamente a $j^\mu$. Este punto prepara el paso natural al siguiente modulo: al promover la simetria de fase a local aparece el campo gauge electromagnetico.

## 6. Bilineales de Dirac

Los objetos construidos con $\psi$ y $\bar{\psi}$ se organizan en familias con significado distinto:

- escalar: $\bar{\psi}\psi$;
- vector: $\bar{\psi}\gamma^\mu\psi$;
- axial vector: $\bar{\psi}\gamma^\mu\gamma^5\psi$;
- pseudoscalar: $\bar{\psi}\gamma^5\psi$;
- tensor: $\bar{\psi}\sigma^{\mu\nu}\psi$, con $\sigma^{\mu\nu} = \frac{i}{2}[\gamma^\mu,\gamma^\nu]$.

Esta clasificacion importa porque no todos los terminos posibles en una lagrangiana son compatibles con simetria de Lorentz ni con otras simetrias internas o discretas.

Dos ejemplos centrales son:

- el termino de masa de Dirac, proporcional a $\bar{\psi}\psi$;
- la corriente electromagnetica, proporcional a $\bar{\psi}\gamma^\mu\psi$.

## 7. Soluciones y estructura de energia

La ecuacion de Dirac admite soluciones de energia positiva y negativa. Historicamente, esto fue interpretado primero mediante la idea del mar de Dirac. En la formulacion moderna de QFT, la lectura correcta es distinta: esas soluciones se reorganizan dentro de la cuantizacion del campo y se interpretan en terminos de particulas y antiparticulas.

Esta es una de las grandes lecciones del modulo:

- la ecuacion de Dirac no elimina el problema de las energias negativas aislando una sola particula;
- lo reinterpreta correctamente en el contexto de teoria de campos.

## 8. Antiparticulas

La ecuacion de Dirac predice de forma natural la existencia de antiparticulas asociadas a fermiones cargados. Este fue uno de sus mayores triunfos conceptuales y experimentales.

Lo que parecia una rareza algebraica en realidad contenia una prediccion fisica real: a cada electron le corresponde un positron con la misma masa y carga opuesta.

En el lenguaje moderno, las soluciones de frecuencia negativa se reinterpretan tras cuantizar el campo como modos asociados a operadores de creacion de antiparticulas. La teoria de campos resuelve asi un problema que el enfoque de una sola particula no podia acomodar con naturalidad.

## 9. Ecuacion de Dirac y simetria de Lorentz

La covariancia de la ecuacion exige que el espinor y las matrices gamma transformen de manera coordinada bajo el grupo de Lorentz. No basta con escribir una ecuacion elegante: hay que garantizar que su forma sea la misma para todos los observadores inerciales.

Esa exigencia conecta:

- la forma algebraica de la ecuacion;
- la representacion espinorial;
- la estructura relativista del espacio-tiempo.

## 10. Limite no relativista

Una comprobacion de consistencia muy valiosa es ver que la ecuacion de Dirac reproduce la fisica conocida a bajas energias. En ese regimen:

- la energia cinetica es pequena frente a la masa;
- las componentes "grandes" del espinor dominan sobre las "pequenas";
- la dinamica efectiva se aproxima a la ecuacion de Pauli para un fermion de espin $1/2$.

Esto muestra que Dirac no destruye la mecanica cuantica previa: la contiene como limite. Tambien explica por que el momento magnetico intrinseco del electron emerge de forma tan natural en la teoria relativista.

## 11. Papel pedagogico del modulo

La ecuacion de Dirac cumple varios papeles simultaneos:

- introduce fermiones relativistas;
- prepara la cuantizacion de campos fermionicos;
- hace visible la relacion entre espin, relatividad y antiparticulas;
- sirve como puente natural hacia gauge y QED.

## Cuaderno asociado

- Consulta los cuadernos asociados de este bloque en [Resumen del modulo](README.md) para reforzar el capitulo con practica guiada.

## 12. Preguntas de estudio

- Por que Dirac quiso una ecuacion lineal en derivadas.
- Que significa que las matrices gamma satisfacen una algebra de Clifford.
- Por que $\psi$ debe ser un espinor y no un escalar.
- Como aparece la idea de antiparticula en este contexto.
- Que papel cumplen los bilineales de Dirac en la construccion de interacciones.

## 13. Ejercicios sugeridos

1. Explica por que una ecuacion lineal relativista, al cuadrarse, debe recuperar una relacion del tipo Klein-Gordon.
2. Muestra verbalmente como la algebra anticommutadora de las matrices gamma codifica la metrica del espacio-tiempo.
3. Describe la diferencia conceptual entre soluciones de energia negativa en una teoria de una sola particula y en una teoria de campos.
4. Identifica que bilineal de Dirac interviene en el acoplamiento electromagnetico.

## 14. Cierre

La ecuacion de Dirac no es solo una ecuacion mejorada para electrones. Es la puerta de entrada a toda la teoria relativista de fermiones, y uno de los lugares donde la QFT muestra con mas claridad que la matematica correcta anticipa nueva fisica.

## 15. Referencias y lecturas recomendadas

- Base: Tong, secciones introductorias sobre la ecuacion de Dirac y espinores.
- Complementaria: Srednicki, capitulos iniciales sobre fermiones relativistas.
- Profundizacion: Peskin y Schroeder, tratamiento de espinores, bilineales y simetrias discretas.


---

## Navegacion del tutorial

[(anterior) Reglas de Feynman: Resumen Operativo](../05_interacciones_y_perturbaciones/04_reglas_de_feynman_resumen_operativo.md) | [(siguiente) Cuantizacion de Campos Fermionicos](02_cuantizacion_de_campos_fermionicos.md)