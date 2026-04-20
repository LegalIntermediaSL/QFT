# Renormalizacion y Grupo de Renormalizacion

## 1. Proposito

Una vez regularizada una teoria, el siguiente paso es expresar observables finitos en terminos de parametros fisicos. Esa es la tarea de la renormalizacion. El grupo de renormalizacion, a su vez, organiza como cambian los acoplamientos con la escala.

## 2. Idea de renormalizacion

En lugar de identificar sin mas los parametros del lagrangiano con los observados experimentalmente, se distinguen:

- parametros desnudos;
- parametros renormalizados;
- observables fisicos.

Los infinitos de las correcciones perturbativas se absorben en redefiniciones apropiadas de los parametros.

Este cambio de perspectiva es decisivo: el parametro desnudo no es necesariamente un numero que pueda medirse de forma directa. La teoria conecta esos parametros con cantidades fisicas a traves de la dinamica cuantica y de condiciones de renormalizacion elegidas a cierta escala.

## 3. Contraterminos

Una forma operativa de implementar la renormalizacion es añadir contraterminos al lagrangiano. Estos ajustan:

- masas;
- constantes de acoplamiento;
- normalizacion de campos.

La teoria renormalizada se formula de modo que las predicciones finales para cantidades medibles resulten finitas.

En una teoria escalar tipica se reescriben los parametros como

$$
m_0^2 = m^2 + \delta m^2, \qquad \lambda_0 = \lambda + \delta\lambda,
$$

y se hace algo analogo con la normalizacion del campo. Los terminos $\delta m^2$, $\delta\lambda$ y sus analogos absorben las partes divergentes.

## 4. Ejemplo conceptual a un lazo

Retomando la teoria $\phi^4$, una correccion a un lazo puede desplazar la masa medida del campo. En vez de aceptar que la masa "se vuelve infinita", la renormalizacion dice:

- el parametro original del lagrangiano no es directamente la masa fisica;
- las fluctuaciones cuanticas corrigen esa relacion;
- el contratermino ajusta el parametro desnudo para que la masa observada permanezca finita y bien definida.

Este es un cambio conceptual mas profundo que una simple receta algebraica.

## 5. Dependencia en escala

Una gran leccion de la renormalizacion es que los parametros efectivos de la teoria dependen de la escala a la que se los mide. Esta dependencia no es un defecto: es parte del contenido fisico de la QFT.

En regularizacion dimensional suele introducirse una escala de renormalizacion $\mu$ para mantener dimensiones correctas. Esa escala recuerda que el valor numerico de un acoplamiento depende del proceso y de la energia a la que se define.

## 6. Grupo de renormalizacion

El grupo de renormalizacion describe precisamente como cambian los acoplamientos con la escala. De ahi emergen ideas centrales como:

- corrida de acoplamientos;
- escalas caracteristicas de una teoria;
- comportamiento ultravioleta e infrarrojo;
- teorias efectivas.

La herramienta tecnica que resume esta dependencia es la funcion beta,

$$
\beta(g) = \mu \frac{dg}{d\mu}.
$$

Su signo y magnitud informan como cambia un acoplamiento al explorar energias mas altas o mas bajas.

Por ejemplo:

- en QED, el acoplamiento efectivo crece lentamente con la energia;
- en QCD, decrece a altas energias, lo que conduce a libertad asintotica.

## 7. Renormalizable versus efectiva

La perspectiva moderna enseña que incluso una teoria no renormalizable en el sentido tradicional puede ser extremadamente util como teoria efectiva dentro de cierto rango de energias. Esto amplia mucho la interpretacion de lo que significa una teoria fisica valida.

Esta perspectiva evita una lectura demasiado rigida:

- una teoria efectiva no es una teoria fallida;
- es una descripcion controlada valida en cierto dominio;
- su dependencia en escala codifica precisamente donde deja de ser suficiente.

## 8. Preguntas de estudio

- Que diferencia hay entre parametro desnudo y parametro fisico.
- Que papel cumplen los contraterminos.
- Por que los acoplamientos dependen de la escala.
- En que sentido una teoria efectiva puede seguir siendo muy poderosa.
- Que informacion fisica resume una funcion beta.

## 9. Cierre

La renormalizacion no es un truco para esconder infinitos. Es una de las ideas mas profundas de la fisica moderna sobre como la teoria cambia al cambiar la escala de descripcion.

## 10. Referencias y lecturas recomendadas

- Base: Peskin y Schroeder, renormalizacion perturbativa y grupo de renormalizacion.
- Complementaria: Tong, explicacion conceptual de corrida de acoplamientos.
- Profundizacion: Weinberg o Zinn-Justin para una lectura mas estructural de teorias efectivas y renormalizacion.


---

## Navegacion del tutorial

[(anterior) Origen de las Divergencias y Regularizacion](01_origen_de_las_divergencias_y_regularizacion.md) | [(siguiente) Regularizacion Dimensional en $\phi^4$](03_regularizacion_dimensional_en_phi4.md)
