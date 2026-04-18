# Teorema de Noether y Papel Organizador de las Simetrias

## 1. Introduccion

Las simetrias no son un adorno estetico de la teoria. En fisica moderna funcionan como principios constructivos. En QFT esto se vuelve especialmente claro gracias al teorema de Noether: cuando la accion es invariante bajo una familia continua de transformaciones, aparece una corriente conservada.

## 2. Que es una simetria

Llamamos simetria a una transformacion que deja invariante la teoria en un sentido apropiado. Dependiendo del contexto, esto puede significar:

- invariancia de la accion;
- invariancia de las ecuaciones de movimiento;
- invariancia de observables fisicos.

En el contexto lagrangiano, la formulacion mas util es la invariancia de la accion.

## 3. Simetrias del espacio-tiempo e internas

Conviene distinguir dos grandes familias:

- simetrias del espacio-tiempo, como traslaciones, rotaciones y boosts;
- simetrias internas, que actuan sobre las componentes de los campos sin mover directamente el punto del espacio-tiempo.

Esta distincion ayuda a organizar las cantidades conservadas y a entender que tipo de estructura fisica esta siendo protegida.

## 4. Enunciado fisico de Noether

De manera esquematica, si una accion es invariante bajo una transformacion continua parametrizada por un parametro infinitesimal, entonces existe una corriente $j^\mu$ tal que

$$
\partial_\mu j^\mu = 0.
$$

Integrando la componente temporal, se obtiene una carga conservada

$$
Q = \int d^3x\, j^0.
$$

Bajo condiciones razonables de contorno, esta carga no cambia con el tiempo.

## 5. Ejemplos fundamentales

Los ejemplos mas importantes al inicio del curso son:

- traslaciones temporales -> energia;
- traslaciones espaciales -> momento lineal;
- rotaciones -> momento angular;
- fase global $U(1)$ -> carga interna conservada.

La gran leccion es que las leyes de conservacion no son hechos separados. Son huellas de simetrias.

## 6. Ejemplo de fase global

Consideremos un campo escalar complejo $\phi$. Si la teoria es invariante bajo

$$
\phi \to e^{i\alpha}\phi,
$$

con $\alpha$ constante, entonces existe una corriente conservada asociada. Este ejemplo parece modesto, pero es pedagogicamente crucial porque enseguida conduce a la idea de simetria gauge.

## 7. De global a local

Si promovemos $\alpha$ a funcion del espacio-tiempo,

$$
\alpha \to \alpha(x),
$$

la teoria deja de ser invariante en general. Recuperar esa invariancia requiere introducir nuevos campos y una derivada covariante. Este paso da origen a teorias gauge como la electrodinamica cuantica.

Por eso las simetrias no solo restringen la teoria: tambien pueden generar estructura dinamica nueva.

## 8. Tensor energia-momento

Las traslaciones del espacio-tiempo conducen a una corriente particularmente importante: el tensor energia-momento. Aunque su tratamiento completo puede refinarse despues, desde ahora conviene retener la idea de que energia y momento se organizan en un objeto tensorial directamente ligado a la simetria traslacional.

Ese hecho es otro ejemplo del poder de la formulacion lagrangiana: lo que en otras aproximaciones pareceria una lista separada de magnitudes dinamicas aqui aparece de manera estructural.

## 9. Simetria como criterio de construccion

En teoria de campos moderna, a menudo se procede en este orden:

1. decidir el contenido de campos;
2. decidir las simetrias que la teoria debe respetar;
3. escribir el lagrangiano mas general compatible con esas simetrias;
4. estudiar las consecuencias fisicas.

Este modo de construir teorias es una de las razones por las que Noether tiene un papel tan central.

## 10. Simetria rota y simetria oculta

Conviene mencionar desde ya que una simetria puede estar presente en la accion y, sin embargo, no manifestarse de forma obvia en el estado de vacio. Ese fenomeno, la ruptura espontanea de simetria, sera esencial mas adelante.

Por ahora basta con registrar la idea: la accion puede tener mas simetria que el estado fundamental alrededor del cual expandimos la teoria.

## 11. Advertencias utiles

- No toda cantidad conservada se reconoce facilmente si no se identifica la simetria subyacente.
- Noether se formula de manera mas limpia para simetrias continuas, no para discretas.
- Invariancia de la accion no significa inmovilidad trivial; significa estabilidad estructural bajo cierta transformacion.

## 12. Preguntas de control

- Que diferencia hay entre simetria del espacio-tiempo e interna.
- Como se pasa de una simetria continua a una corriente conservada.
- Por que una simetria de fase global prepara el camino hacia teorias gauge.
- En que sentido las simetrias sirven para construir teorias y no solo para describirlas.

## 13. Cierre

El teorema de Noether enseña una de las lecciones mas profundas de la fisica teorica: la conservacion es la sombra dinamica de la simetria. En QFT, esa conexion no es perifrica; es uno de los hilos que organizan casi toda la disciplina.
