# Renormalizacion y Grupo de Renormalizacion

**Nivel:** Intermedio  
**Dificultad:** Media-Alta  
**Tiempo estimado:** 25-35 min  
**Prerequisitos recomendados:** [Origen de las Divergencias y Regularizacion](01_origen_de_las_divergencias_y_regularizacion.md) · [Resumen del modulo](README.md)


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

Si se introduce una renormalizacion del campo

$$
\phi_0 = Z_\phi^{1/2}\phi,
$$

entonces parte de las correcciones cuanticas se reorganizan en el factor $Z_\phi$. Pedagogicamente esto es importante porque muestra que la renormalizacion no afecta solo a masas y acoplamientos: tambien modifica la normalizacion adecuada del campo que interpola entre el vacio y los estados de una particula.

## 4. Ejemplo conceptual a un lazo

Retomando la teoria $\phi^4$, una correccion a un lazo puede desplazar la masa medida del campo. En vez de aceptar que la masa "se vuelve infinita", la renormalizacion dice:

- el parametro original del lagrangiano no es directamente la masa fisica;
- las fluctuaciones cuanticas corrigen esa relacion;
- el contratermino ajusta el parametro desnudo para que la masa observada permanezca finita y bien definida.

Este es un cambio conceptual mas profundo que una simple receta algebraica.

Una forma de leerlo correctamente es la siguiente. Si calculamos una funcion de dos puntos a un lazo, la posicion del polo del propagador corregido define la masa fisica. Por tanto, la renormalizacion consiste en imponer condiciones que garanticen que ese polo siga apareciendo donde lo exige la masa medida. El contratermino no "borra" la fisica del lazo: la reorganiza para que la prediccion final tenga sentido experimental.

## 5. Esquemas de renormalizacion

No existe una unica forma de separar parte finita y parte divergente. Por eso aparecen distintos esquemas de renormalizacion, por ejemplo:

- esquema on-shell, donde se fijan directamente masas y residuos en el polo fisico;
- esquema minimal subtraction, que absorbe solo la parte divergente;
- esquema $\overline{\mathrm{MS}}$, muy usado por su comodidad en regularizacion dimensional.

Todos los esquemas bien definidos producen la misma fisica final cuando se comparan observables completos. Lo que cambia es la manera de parametrizar los pasos intermedios y la interpretacion inmediata de los parametros renormalizados.

## 6. Dependencia en escala

Una gran leccion de la renormalizacion es que los parametros efectivos de la teoria dependen de la escala a la que se los mide. Esta dependencia no es un defecto: es parte del contenido fisico de la QFT.

En regularizacion dimensional suele introducirse una escala de renormalizacion $\mu$ para mantener dimensiones correctas. Esa escala recuerda que el valor numerico de un acoplamiento depende del proceso y de la energia a la que se define.

Si una amplitud fisica no puede depender de una escala arbitraria introducida por el metodo de renormalizacion, entonces la dependencia explicita en $\mu$ debe cancelarse con la dependencia implicita de los parametros renormalizados. De esta exigencia nace la ecuacion del grupo de renormalizacion.

## 7. Grupo de renormalizacion

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

En version muy resumida, si $\beta(g)>0$, el acoplamiento aumenta al subir la escala; si $\beta(g)<0$, disminuye. Esta simple observacion organiza buena parte de la intuicion moderna sobre teorias gauge.

## 8. Punto fijo e intuicion de escalas

Un punto fijo del flujo renormalizacion satisface

$$
\beta(g_\star)=0.
$$

Los puntos fijos son importantes porque describen comportamientos invariantes de escala o casi invariantes. Aunque en este tutorial solo se necesita la intuicion basica, conviene registrar la idea:

- cerca de un punto fijo, la teoria cambia muy poco con la escala;
- los operadores pueden clasificarse por como se alejan o acercan a ese punto;
- esta lectura conecta la renormalizacion con la teoria de campos criticos y la fisica estadistica.

## 9. Renormalizable versus efectiva

La perspectiva moderna enseña que incluso una teoria no renormalizable en el sentido tradicional puede ser extremadamente util como teoria efectiva dentro de cierto rango de energias. Esto amplia mucho la interpretacion de lo que significa una teoria fisica valida.

Esta perspectiva evita una lectura demasiado rigida:

- una teoria efectiva no es una teoria fallida;
- es una descripcion controlada valida en cierto dominio;
- su dependencia en escala codifica precisamente donde deja de ser suficiente.

Un punto pedagogico importante es este: la renormalizabilidad estricta dejo de ser el unico criterio de respetabilidad teorica. Lo decisivo hoy es si la teoria organiza predicciones con expansion controlada y rango claro de validez.

## 10. Ejemplo conceptual de running

Imaginemos que medimos un acoplamiento a una escala $\mu_0$ y luego calculamos un proceso a una escala mucho mayor $\mu$. En vez de recalcular una y otra vez grandes logaritmos del tipo

$$
\log\!\left(\frac{\mu}{\mu_0}\right),
$$

el grupo de renormalizacion permite absorber sistematicamente esa dependencia en acoplamientos corridos. Esa es una de sus grandes virtudes practicas: no solo interpreta la fisica de escala, tambien reorganiza la perturbacion para volverla mas estable.

## 11. Preguntas de estudio

- Que diferencia hay entre parametro desnudo y parametro fisico.
- Que papel cumplen los contraterminos.
- Por que los acoplamientos dependen de la escala.
- En que sentido una teoria efectiva puede seguir siendo muy poderosa.
- Que informacion fisica resume una funcion beta.

## 12. Cierre

La renormalizacion no es un truco para esconder infinitos. Es una de las ideas mas profundas de la fisica moderna sobre como la teoria cambia al cambiar la escala de descripcion.

## 13. Referencias y lecturas recomendadas

- Base: Peskin y Schroeder, renormalizacion perturbativa y grupo de renormalizacion.
- Complementaria: Tong, explicacion conceptual de corrida de acoplamientos.
- Profundizacion: Weinberg o Zinn-Justin para una lectura mas estructural de teorias efectivas y renormalizacion.


---

## Navegacion del tutorial

[(anterior) Origen de las Divergencias y Regularizacion](01_origen_de_las_divergencias_y_regularizacion.md) | [(siguiente) Regularizacion Dimensional en $\phi^4$](03_regularizacion_dimensional_en_phi4.md)