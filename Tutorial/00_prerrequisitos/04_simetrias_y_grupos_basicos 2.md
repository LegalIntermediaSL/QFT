# Simetrias y Grupos Basicos

## 1. Proposito

La QFT no se organiza solo por ecuaciones, sino por simetrias. Este documento introduce el lenguaje minimo de simetria, grupo, generador y representacion necesario para entender por que el formalismo de la teoria tiene la forma que tiene.

## 2. Que es una simetria

Una simetria es una transformacion que deja invariante algun aspecto esencial del sistema, por ejemplo:

- la accion;
- las ecuaciones de movimiento;
- un conjunto de observables.

En fisica moderna, las simetrias no son solo descripciones elegantes: actuan como principios constructivos.

## 3. Simetrias discretas y continuas

Una primera distincion importante es:

- simetrias discretas, como paridad o conjugacion de carga;
- simetrias continuas, como rotaciones o traslaciones.

Las simetrias continuas son especialmente importantes porque, via el teorema de Noether, se asocian a cantidades conservadas.

## 4. Que es un grupo

Matematicamente, un grupo es un conjunto de transformaciones cerrado bajo composicion, con identidad e inversos. En fisica, pensar en grupos permite organizar sistematicamente:

- transformaciones espaciales;
- transformaciones relativistas;
- simetrias internas;
- simetrias gauge.

No hace falta una formulacion abstracta completa al principio, pero si entender que un grupo codifica composicion coherente de simetrias.

## 5. Generadores infinitesimales

Las simetrias continuas pueden estudiarse cerca de la identidad mediante generadores. Por ejemplo, una transformacion infinitesimal puede escribirse esquematicamente como

$$
U(\epsilon) \approx 1 + i\epsilon T,
$$

donde $T$ es un generador.

Estos generadores contienen la informacion local del grupo y son muy utiles tanto en mecanica cuantica como en QFT.

## 6. Representaciones

Una representacion especifica como actua una simetria sobre un tipo de objeto. En QFT esto es esencial, porque distintos campos transforman en distintas representaciones:

- escalares;
- vectores;
- espinores;
- multipletes internos.

Decir que un campo pertenece a cierta representacion no es un detalle ornamental: determina que interacciones y que terminos lagrangianos son posibles.

## 7. Simetrias del espacio-tiempo e internas

Conviene distinguir:

- simetrias del espacio-tiempo, como el grupo de Poincare;
- simetrias internas, como cambios de fase o simetrias de gauge.

Las primeras organizan geometria, masa y espin. Las segundas organizan cargas, multipletes y estructura de interaccion.

## 8. Ejemplo: simetria global de fase

Si un campo complejo transforma como

$$
\phi \to e^{i\alpha}\phi,
$$

con $\alpha$ constante, decimos que la teoria posee una simetria global $U(1)$. Esta es una de las simetrias mas simples, pero muy instructiva:

- muestra como una fase puede ser fisicamente relevante;
- ilustra el teorema de Noether;
- prepara el salto a simetria gauge local.

## 9. Del grupo a la teoria fisica

En la practica, la estrategia moderna suele ser:

1. elegir los campos;
2. fijar las simetrias;
3. escribir el lagrangiano mas general compatible con ellas;
4. extraer consecuencias fisicas.

Este modo de construir teorias es una de las razones por las que el lenguaje de grupos y representaciones es tan central.

## 10. Simetrias gauge

Una simetria gauge no es simplemente una simetria global hecha mas complicada. Al promover una simetria a local, la teoria obliga a introducir nuevos campos y nuevas estructuras geometricas, como derivadas covariantes. De aqui nacen teorias fundamentales como:

- QED;
- QCD;
- el sector electrodébil del Modelo Estandar.

## 11. Preguntas de estudio

- Que diferencia hay entre simetria discreta y continua.
- Que es un generador infinitesimal.
- Por que las representaciones importan para los campos cuanticos.
- Que diferencia hay entre simetrias del espacio-tiempo e internas.

## 12. Ejercicios sugeridos

1. Explica por que una rotacion espacial forma parte de un grupo continuo.
2. Describe el significado fisico de una simetria global $U(1)$.
3. Redacta una explicacion breve de por que la simetria gauge local obliga a introducir nueva estructura en la teoria.

## 13. Cierre

La QFT es, en gran medida, una teoria de campos guiada por simetrias. Entender grupos, generadores y representaciones convierte muchas formulas que parecen arbitrarias en consecuencias estructurales naturales.

## 14. Referencias y lecturas recomendadas

- Base: introducciones breves a grupos continuos y simetrias para fisicos.
- Complementaria: Zee, intuicion sobre simetria como principio organizador.
- Profundizacion: textos de grupos de Lie y representaciones orientados a fisica de particulas.


---

## Navegacion del tutorial

[(anterior) Oscilador Armonico Cuantico](03_oscilador_armonico_cuantico.md) | [(siguiente) Delta de Dirac y Transformadas de Fourier](05_delta_de_dirac_y_transformadas_de_fourier.md)
