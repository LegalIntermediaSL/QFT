# Teorema de Noether y Papel Organizador de las Simetrias

**Nivel:** Fundacional  
**Dificultad:** Media  
**Tiempo estimado:** 25-35 min  
**Prerequisitos recomendados:** [Principio de Accion y Ecuaciones de Campo](01_principio_de_accion_y_ecuaciones_de_campo.md) · [Resumen del modulo](README.md)


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

Una manera breve de leer la cadena conceptual es:

- simetria continua;
- corriente conservada;
- carga constante en el tiempo.

Eso convierte a Noether en un puente directo entre geometria de la teoria y dinamica observable.

## 5. Ejemplos fundamentales

Los ejemplos mas importantes al inicio del curso son:

- traslaciones temporales -> energia;
- traslaciones espaciales -> momento lineal;
- rotaciones -> momento angular;
- fase global $U(1)$ -> carga interna conservada.

La gran leccion es que las leyes de conservacion no son hechos separados. Son huellas de simetrias.

Este cambio de perspectiva es enorme. En vez de memorizar una lista de cantidades conservadas, aprendemos a derivarlas desde principios estructurales.

## 6. Ejemplo de fase global

Consideremos un campo escalar complejo $\phi$. Si la teoria es invariante bajo

$$
\phi \to e^{i\alpha}\phi,
$$

con $\alpha$ constante, entonces existe una corriente conservada asociada. Este ejemplo parece modesto, pero es pedagogicamente crucial porque enseguida conduce a la idea de simetria gauge.

La clave aqui es que la transformacion actua en el espacio interno del campo, no desplazando el punto del espacio-tiempo. Eso muestra con claridad que se entiende por simetria interna.

## 7. Bosquejo minimo de derivacion

No hace falta aqui una derivacion completa con todo el detalle tecnico, pero si conviene registrar la logica. Si bajo una transformacion infinitesimal del campo

$$
\phi \to \phi + \delta \phi
$$

la accion cambia a lo sumo en un termino de borde, entonces al usar las ecuaciones de Euler-Lagrange la variacion restante puede reorganizarse como una divergencia:

$$
\partial_\mu j^\mu = 0.
$$

La corriente de Noether aparece precisamente al identificar que combinacion de campos y derivadas queda dentro de esa divergencia.

## 8. De global a local

Si promovemos $\alpha$ a funcion del espacio-tiempo,

$$
\alpha \to \alpha(x),
$$

la teoria deja de ser invariante en general. Recuperar esa invariancia requiere introducir nuevos campos y una derivada covariante. Este paso da origen a teorias gauge como la electrodinamica cuantica.

Por eso las simetrias no solo restringen la teoria: tambien pueden generar estructura dinamica nueva.

En ese paso ocurre algo conceptualmente decisivo: la simetria deja de ser solo una propiedad pasiva de la teoria y empieza a exigir la introduccion de campos gauge que medien nuevas interacciones.

## 9. Tensor energia-momento

Las traslaciones del espacio-tiempo conducen a una corriente particularmente importante: el tensor energia-momento. Aunque su tratamiento completo puede refinarse despues, desde ahora conviene retener la idea de que energia y momento se organizan en un objeto tensorial directamente ligado a la simetria traslacional.

Ese hecho es otro ejemplo del poder de la formulacion lagrangiana: lo que en otras aproximaciones pareceria una lista separada de magnitudes dinamicas aqui aparece de manera estructural.

## 10. Simetria como criterio de construccion

En teoria de campos moderna, a menudo se procede en este orden:

1. decidir el contenido de campos;
2. decidir las simetrias que la teoria debe respetar;
3. escribir el lagrangiano mas general compatible con esas simetrias;
4. estudiar las consecuencias fisicas.

Este modo de construir teorias es una de las razones por las que Noether tiene un papel tan central.

Y esa forma de trabajar se vuelve cada vez mas poderosa al avanzar en el curso: primero en teorias gauge, luego en el Modelo Estandar y finalmente en teorias efectivas.

## 11. Simetria rota y simetria oculta

Conviene mencionar desde ya que una simetria puede estar presente en la accion y, sin embargo, no manifestarse de forma obvia en el estado de vacio. Ese fenomeno, la ruptura espontanea de simetria, sera esencial mas adelante.

Por ahora basta con registrar la idea: la accion puede tener mas simetria que el estado fundamental alrededor del cual expandimos la teoria.

## Cuaderno asociado

- Consulta los cuadernos asociados de este bloque en [Resumen del modulo](README.md) para reforzar el capitulo con practica guiada.

## 12. Advertencias utiles

- No toda cantidad conservada se reconoce facilmente si no se identifica la simetria subyacente.
- Noether se formula de manera mas limpia para simetrias continuas, no para discretas.
- Invariancia de la accion no significa inmovilidad trivial; significa estabilidad estructural bajo cierta transformacion.

## 13. Preguntas de control

- Que diferencia hay entre simetria del espacio-tiempo e interna.
- Como se pasa de una simetria continua a una corriente conservada.
- Por que una simetria de fase global prepara el camino hacia teorias gauge.
- En que sentido las simetrias sirven para construir teorias y no solo para describirlas.

## 14. Cierre

El teorema de Noether enseña una de las lecciones mas profundas de la fisica teorica: la conservacion es la sombra dinamica de la simetria. En QFT, esa conexion no es perifrica; es uno de los hilos que organizan casi toda la disciplina.

## 15. Referencias y lecturas recomendadas

- Base: Tong, Noether y corrientes conservadas.
- Complementaria: Srednicki, formulacion lagrangiana de simetrias continuas.
- Profundizacion: textos clasicos sobre accion, simetria y cantidades conservadas.


---

## Navegacion del tutorial

[(anterior) Principio de Accion y Ecuaciones de Campo](01_principio_de_accion_y_ecuaciones_de_campo.md) | [(siguiente) Portada 03: Cuantizacion Canonica del Campo Escalar Libre](../portada_03_cuantizacion_canonica_del_campo_escalar.md)