# Simetrias y Grupos Basicos

**Nivel:** Fundacional  
**Dificultad:** Media  
**Tiempo estimado:** 25-35 min  
**Prerequisitos recomendados:** [Oscilador Armonico Cuantico](03_oscilador_armonico_cuantico.md) · [Resumen del modulo](README.md)


## 1. Proposito

La QFT no se organiza solo por ecuaciones, sino por simetrias. Este documento introduce el lenguaje minimo de simetria, grupo, generador y representacion necesario para entender por que el formalismo de la teoria tiene la forma que tiene.

La idea central es muy poderosa: en fisica moderna, muchas teorias no se construyen adivinando ecuaciones y comprobando despues si funcionan, sino fijando los grados de libertad y exigiendo que respeten determinadas simetrias. Esa exigencia reduce enormemente la arbitrariedad.

## 2. Que es una simetria

Una simetria es una transformacion que deja invariante algun aspecto esencial del sistema, por ejemplo:

- la accion;
- las ecuaciones de movimiento;
- un conjunto de observables;
- la forma de las leyes fisicas para distintos observadores.

En fisica moderna, las simetrias no son solo descripciones elegantes: actuan como principios constructivos. Indican que cantidades pueden conservarse, que terminos son admisibles en el lagrangiano y que tipo de interacciones pueden existir.

## 3. Simetrias discretas y continuas

Una primera distincion importante es:

- simetrias discretas, como paridad o conjugacion de carga;
- simetrias continuas, como rotaciones, traslaciones o cambios globales de fase.

Las simetrias continuas son especialmente importantes porque, via el teorema de Noether, se asocian a cantidades conservadas. Las discretas, aunque no generen corrientes conservadas del mismo modo, siguen siendo cruciales para clasificar procesos y detectar reglas de seleccion.

## 4. Que es un grupo

Matematicamente, un grupo es un conjunto de transformaciones cerrado bajo composicion, con identidad e inversos. En fisica, pensar en grupos permite organizar sistematicamente:

- transformaciones espaciales;
- transformaciones relativistas;
- simetrias internas;
- simetrias gauge.

No hace falta una formulacion abstracta completa al principio, pero si entender que un grupo codifica composicion coherente de simetrias. Si realizamos dos transformaciones sucesivas de la teoria, el resultado debe seguir siendo una transformacion admisible del mismo tipo.

## 5. Generadores infinitesimales

Las simetrias continuas pueden estudiarse cerca de la identidad mediante generadores. Por ejemplo, una transformacion infinitesimal puede escribirse esquematicamente como

$$
U(\epsilon) \approx 1 + i\epsilon T,
$$

donde $T$ es un generador.

Estos generadores contienen la informacion local del grupo y son muy utiles tanto en mecanica cuantica como en QFT. En fisica cuantica suelen adquirir una interpretacion especialmente concreta:

- el momento genera traslaciones;
- el momento angular genera rotaciones;
- ciertas cargas internas generan transformaciones de fase o rotaciones internas.

Asi aparece una conexion profunda entre simetria, algebra y observable conservado.

## 6. Representaciones

Una representacion especifica como actua una simetria sobre un tipo de objeto. En QFT esto es esencial, porque distintos campos transforman en distintas representaciones:

- escalares;
- vectores;
- espinores;
- multipletes internos.

Decir que un campo pertenece a cierta representacion no es un detalle ornamental: determina que interacciones y que terminos lagrangianos son posibles.

Por ejemplo:

- un escalar no lleva indices de Lorentz;
- un vector transforma con un indice espaciotemporal;
- un espinor transforma en una representacion distinta, propia del grupo de Lorentz.

Esa informacion decide como pueden contraerse indices y que combinaciones producen cantidades invariantes.

## 7. Simetrias del espacio-tiempo e internas

Conviene distinguir:

- simetrias del espacio-tiempo, como el grupo de Poincare;
- simetrias internas, como cambios de fase o simetrias gauge.

Las primeras organizan geometria, masa y espin. Las segundas organizan cargas, multipletes y estructura de interaccion.

Aunque ambas se describan con lenguaje de grupos, no juegan exactamente el mismo papel. Las simetrias del espacio-tiempo dicen como cambia la descripcion entre observadores o bajo desplazamientos y rotaciones. Las internas actuan en espacios abstractos de componentes, sabores o cargas.

## 8. Ejemplo: simetria global de fase

Si un campo complejo transforma como

$$
\phi \to e^{i\alpha}\phi,
$$

con $\alpha$ constante, decimos que la teoria posee una simetria global $U(1)$. Esta es una de las simetrias mas simples, pero muy instructiva:

- muestra como una fase puede ser fisicamente relevante;
- ilustra el teorema de Noether;
- prepara el salto a simetria gauge local.

Este ejemplo condensa una parte enorme de la logica que se repetira despues. Primero se identifica una simetria global, luego se estudia su corriente conservada y finalmente se pregunta que ocurre si la fase depende del punto del espacio-tiempo.

## 9. Del grupo a la teoria fisica

En la practica, la estrategia moderna suele ser:

1. elegir los campos;
2. fijar las simetrias;
3. escribir el lagrangiano mas general compatible con ellas;
4. extraer consecuencias fisicas.

Este modo de construir teorias es una de las razones por las que el lenguaje de grupos y representaciones es tan central. Una vez impuestas las simetrias, no todo termino imaginable esta permitido. La simetria se convierte en un criterio de seleccion.

## 10. Simetrias gauge

Una simetria gauge no es simplemente una simetria global hecha mas complicada. Al promover una simetria a local, la teoria obliga a introducir nuevos campos y nuevas estructuras geometricas, como derivadas covariantes. De aqui nacen teorias fundamentales como:

- QED;
- QCD;
- el sector electrodébil del Modelo Estandar.

La intuicion minima que conviene retener es esta: una simetria gauge local fuerza la aparicion de conexiones, campos mediadores e interacciones compatibles con una redundancia local del formalismo.

## Cuaderno asociado

- Consulta los cuadernos asociados de este bloque en [Resumen del modulo](README.md) para reforzar el capitulo con practica guiada.

## 11. Preguntas de comprobacion
- Que diferencia hay entre simetria discreta y continua.
- Que es un generador infinitesimal.
- Por que las representaciones importan para los campos cuanticos.
- Que diferencia hay entre simetrias del espacio-tiempo e internas.
- Por que en fisica moderna las simetrias funcionan como principio de construccion y no solo como propiedad secundaria.

## 12. Ejercicios sugeridos

1. Explica por que una rotacion espacial forma parte de un grupo continuo.
2. Describe el significado fisico de una simetria global $U(1)$.
3. Redacta una explicacion breve de por que la simetria gauge local obliga a introducir nueva estructura en la teoria.
4. Da un ejemplo de cantidad conservada asociada a una simetria continua.

## 13. Cierre

La QFT es, en gran medida, una teoria de campos guiada por simetrias. Entender grupos, generadores y representaciones convierte muchas formulas que parecen arbitrarias en consecuencias estructurales naturales.

Cuanto antes se asiente esta idea, mas facil resulta leer el resto del tutorial. Muchas corrientes conservadas, muchos terminos del lagrangiano y muchas restricciones dinamicas son simplemente huellas directas de una simetria subyacente.

## 14. Referencias y lecturas recomendadas

- Base: introducciones breves a grupos continuos y simetrias para fisicos.
- Complementaria: Zee, intuicion sobre simetria como principio organizador.
- Profundizacion: textos de grupos de Lie y representaciones orientados a fisica de particulas.


---

## Navegacion del tutorial

[(anterior) Oscilador Armonico Cuantico](03_oscilador_armonico_cuantico.md) | [(siguiente) Delta de Dirac y Transformadas de Fourier](05_delta_de_dirac_y_transformadas_de_fourier.md)