# Motivacion y Ecuacion de Dirac

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

## 4. Espinores

Un espinor no es simplemente un vector ordinario de cuatro componentes sin significado adicional. Es un objeto que transforma bajo una representacion espinorial del grupo de Lorentz.

La necesidad de introducir espinores revela una leccion profunda:

- los fermiones relativistas no caben en el mismo lenguaje geometrico que escalares o vectores;
- la estructura de simetria del espacio-tiempo distingue clases de objetos mas ricas;
- el espin aparece como parte intrinseca del formalismo relativista.

## 5. Corriente conservada

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

## 6. Soluciones y estructura de energia

La ecuacion de Dirac admite soluciones de energia positiva y negativa. Historicamente, esto fue interpretado primero mediante la idea del mar de Dirac. En la formulacion moderna de QFT, la lectura correcta es distinta: esas soluciones se reorganizan dentro de la cuantizacion del campo y se interpretan en terminos de particulas y antiparticulas.

Esta es una de las grandes lecciones del modulo:

- la ecuacion de Dirac no elimina el problema de las energias negativas aislando una sola particula;
- lo reinterpreta correctamente en el contexto de teoria de campos.

## 7. Antiparticulas

La ecuacion de Dirac predice de forma natural la existencia de antiparticulas asociadas a fermiones cargados. Este fue uno de sus mayores triunfos conceptuales y experimentales.

Lo que parecia una rareza algebraica en realidad contenia una prediccion fisica real: a cada electron le corresponde un positron con la misma masa y carga opuesta.

## 8. Ecuacion de Dirac y simetria de Lorentz

La covariancia de la ecuacion exige que el espinor y las matrices gamma transformen de manera coordinada bajo el grupo de Lorentz. No basta con escribir una ecuacion elegante: hay que garantizar que su forma sea la misma para todos los observadores inerciales.

Esa exigencia conecta:

- la forma algebraica de la ecuacion;
- la representacion espinorial;
- la estructura relativista del espacio-tiempo.

## 9. Papel pedagogico del modulo

La ecuacion de Dirac cumple varios papeles simultaneos:

- introduce fermiones relativistas;
- prepara la cuantizacion de campos fermionicos;
- hace visible la relacion entre espin, relatividad y antiparticulas;
- sirve como puente natural hacia gauge y QED.

## 10. Preguntas de estudio

- Por que Dirac quiso una ecuacion lineal en derivadas.
- Que significa que las matrices gamma satisfacen una algebra de Clifford.
- Por que $\psi$ debe ser un espinor y no un escalar.
- Como aparece la idea de antiparticula en este contexto.

## 11. Ejercicios sugeridos

1. Explica por que una ecuacion lineal relativista, al cuadrarse, debe recuperar una relacion del tipo Klein-Gordon.
2. Muestra verbalmente como la algebra anticommutadora de las matrices gamma codifica la metrica del espacio-tiempo.
3. Describe la diferencia conceptual entre soluciones de energia negativa en una teoria de una sola particula y en una teoria de campos.

## 12. Cierre

La ecuacion de Dirac no es solo una ecuacion mejorada para electrones. Es la puerta de entrada a toda la teoria relativista de fermiones, y uno de los lugares donde la QFT muestra con mas claridad que la matematica correcta anticipa nueva fisica.
