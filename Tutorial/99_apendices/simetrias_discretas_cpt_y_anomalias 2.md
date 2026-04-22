# Simetrias Discretas, CPT y Anomalias

## Objetivo

Este apendice ofrece una vista compacta de tres temas que aparecen una y otra vez al avanzar en QFT: las simetrias discretas $C$, $P$ y $T$, el papel estructural del teorema CPT y la idea de anomalia cuantica. No pretende sustituir un tratamiento formal completo, pero si fijar el mapa conceptual para enlazar los modulos de fermiones, gauge y Modelo Estandar.

## 1. Simetrias discretas

A diferencia de una simetria continua, una simetria discreta no se parametriza por un numero pequeno continuamente variable. En QFT las tres mas importantes son:

- **$C$**: conjugacion de carga;
- **$P$**: paridad;
- **$T$**: inversion temporal.

Estas transformaciones no organizan corrientes de Noether del mismo modo que una simetria continua, pero siguen imponiendo restricciones fuertes sobre lagrangianas, amplitudes y observables.

## 2. Conjugacion de carga $C$

La conjugacion de carga intercambia, de forma esquematica, particulas y antiparticulas. En una teoria con fermiones cargados, esto cambia el signo de cargas internas relevantes y reorganiza la lectura de corrientes y bilineales.

Pedagogicamente, $C$ sirve para entender mejor:

- por que aparecen antiparticulas en la ecuacion de Dirac;
- como se transforman corrientes vectoriales y axiales;
- por que ciertos terminos son compatibles o incompatibles con una simetria dada.

## 3. Paridad $P$

La paridad invierte la orientacion espacial:

$$
\mathbf{x} \to -\mathbf{x}.
$$

En teorias relativistas esto afecta de forma distinta a escalares, pseudoescalares, vectores y axial-vectores. Por eso la clasificacion de bilineales de Dirac no es solo notacional: ayuda a leer rapidamente como se comporta un termino frente a $P$.

Una de las grandes lecciones historicas de la fisica de particulas es que la interaccion debil viola paridad.

## 4. Inversion temporal $T$

La transformacion temporal invierte el sentido del tiempo. Su tratamiento tecnico es mas delicado que el de $C$ y $P$, pero conceptualmente importa porque conecta:

- estructura de amplitudes;
- propiedades de reversibilidad;
- formulaciones profundas del teorema CPT.

En un primer contacto pedagogico conviene recordar que la accion de $T$ en teoria cuantica no se reduce a cambiar $t \to -t$ de manera ingenua.

## 5. Combinaciones $CP$, $PT$ y $CPT$

En la practica, muchas discusiones fisicas se formulan no solo en terminos de $C$, $P$ o $T$ por separado, sino de sus combinaciones. La mas importante es:

$$
CPT.
$$

El teorema CPT afirma, de manera esquematica, que una QFT local, relativista y unitaria bien construida debe ser invariante bajo la transformacion combinada $CPT$.

## 6. Importancia del teorema CPT

El teorema CPT no es un detalle decorativo. Resume una conexion profunda entre:

- localidad;
- covariancia relativista;
- estructura cuantica consistente.

Por eso cualquier discusion sobre una posible violacion de CPT suele tomarse como una señal de que alguna hipotesis estructural muy profunda de la teoria esta siendo modificada.

## 7. Violacion de paridad y de $CP$

El sector debil del Modelo Estandar ofrece dos lecciones centrales:

- viola paridad de forma maxima en su estructura quiral;
- permite violacion de $CP$ en el sector de sabor.

Esto vuelve especialmente util estudiar $C$, $P$ y $CP$ despues de los modulos `06`, `07` y `10`, donde la quiralidad y las corrientes electrodébiles ya estan sobre la mesa.

## 8. Que es una anomalia

Una anomalia aparece cuando una simetria de la teoria clasica no sobrevive intacta tras la cuantizacion o la regularizacion. Esta idea debe manejarse con cuidado:

- no toda ruptura cuantica de una simetria tiene el mismo estatus fisico;
- algunas anomalias son consistentes y observables;
- otras harian inconsistente la teoria si afectaran a una simetria gauge.

## 9. Anomalias globales y gauge

Conviene distinguir, al menos conceptualmente:

- **anomalias globales**, que pueden reflejar efectos fisicos reales sin destruir necesariamente la consistencia de la teoria;
- **anomalias gauge**, que en una teoria fundamental local suelen ser inaceptables porque rompen la consistencia de la simetria gauge cuantica.

Esta distincion es crucial para entender por que la cancelacion de anomalias en el Modelo Estandar no es un accidente numerologico, sino una condicion estructural.

## 10. Ejemplo pedagogico: anomalia quiral

La anomalia quiral es el ejemplo mas famoso. Muestra que una corriente axial que parece conservada en el nivel clasico puede dejar de serlo al cuantizar. Sin entrar aqui en la cuenta completa, la leccion conceptual es fuerte:

- la cuantizacion no siempre preserva todas las simetrias aparentes del lagrangiano clasico;
- el lenguaje de diagramas y regularizacion puede revelar obstrucciones profundas;
- las corrientes axiales merecen tratarse con especial cuidado.

## 11. Conexion con el Modelo Estandar

En el Modelo Estandar, la asignacion de cargas y representaciones fermionicas esta fuertemente restringida por la necesidad de cancelar anomalias gauge. Esto enlaza de forma muy natural con:

- quiralidad de los fermiones;
- estructura electrodébil;
- contenido por generaciones.

## 12. Uso recomendado dentro del tutorial

Este apendice se aprovecha mejor despues de estudiar:

- [Algebra gamma y bilineales de Dirac](../06_fermiones_y_dirac/03_algebra_gamma_y_bilineales_de_dirac.md)
- [Quiralidad, espinores de Weyl y fermiones de Majorana](../06_fermiones_y_dirac/05_quiralidad_weyl_y_majorana.md)
- [QED y lagrangiano fundamental](../07_gauge_y_qed/02_qed_y_lagrangiano_fundamental.md)
- [Sector fermionico y quiralidad](../10_modelo_estandar/03_sector_fermionico_y_quiralidad.md)
- [Corrientes cargadas y neutras](../10_modelo_estandar/06_corrientes_cargadas_y_neutras.md)

## 13. Cuaderno asociado

- `../../Cuadernos/ejemplos/13_simetrias_discretas_y_cpt.ipynb`: usarlo para fijar el mapa conceptual entre $C$, $P$, $T$ y $CPT$, y distinguir violaciones discretas concretas de la estructura global protegida por el teorema CPT.

## 14. Preguntas de comprobacion

- Por que la violacion de paridad no contradice el teorema CPT.
- Que diferencia conceptual hay entre una anomalia global y una anomalia gauge.
- Por que la anomalia quiral es un ejemplo tan importante en QFT.
- Como se conecta la cancelacion de anomalias con la consistencia del Modelo Estandar.

## 15. Referencias y lecturas recomendadas

- Base: Schwartz o Peskin, discusiones introductorias sobre simetrias discretas y anomalias.
- Complementaria: Tong, notas utiles para quiralidad y estructura gauge.
- Profundizacion: textos de QFT avanzados sobre anomalia axial, cancelacion de anomalias y teorema CPT.
