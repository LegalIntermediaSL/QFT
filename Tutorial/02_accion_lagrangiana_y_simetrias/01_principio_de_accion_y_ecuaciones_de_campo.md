# Principio de Accion y Ecuaciones de Campo

## 1. Introduccion

La formulacion por accion es uno de los lenguajes mas potentes de la fisica teorica. En lugar de comenzar con fuerzas o ecuaciones aisladas, se introduce un funcional global cuya estacionariedad sintetiza la dinamica completa.

En teoria de campos, este lenguaje adquiere un valor especial porque hace visibles de una sola vez la localidad, la covariancia y la estructura de las interacciones.

## 2. De la mecanica clasica a la teoria de campos

En mecanica clasica ordinaria, la accion se escribe como

$$
S[q] = \int dt\, L(q,\dot q,t).
$$

En teoria de campos, la generalizacion natural consiste en reemplazar el tiempo por el espacio-tiempo completo y las coordenadas generalizadas por campos:

$$
S[\phi] = \int d^4x\, \mathcal{L}\bigl(\phi_a(x), \partial_\mu \phi_a(x)\bigr).
$$

El indice $a$ permite indicar que puede haber varios campos en la teoria.

## 3. Densidad lagrangiana y localidad

La cantidad fundamental ya no es una lagrangiana global, sino una densidad lagrangiana $\mathcal{L}$. Esta depende localmente de los campos y de un numero finito de sus derivadas. La razon de esta estructura es doble:

- se adapta a la relatividad especial;
- implementa la idea de interaccion local.

Una teoria local relativista casi siempre empieza proponiendo una $\mathcal{L}$ compatible con las simetrias relevantes.

## 4. Variacion de la accion

La dinamica se obtiene imponiendo que la accion sea estacionaria bajo variaciones arbitrarias de los campos que se anulan en la frontera:

$$
\delta S = 0.
$$

Al variar la accion y realizar integracion por partes, se obtiene la forma general de las ecuaciones de Euler-Lagrange:

$$
\frac{\partial \mathcal{L}}{\partial \phi_a}
- \partial_\mu\left(\frac{\partial \mathcal{L}}{\partial(\partial_\mu \phi_a)}\right)=0.
$$

Esta expresion resume el paso desde un principio global hasta ecuaciones diferenciales locales.

## 5. Ejemplo: campo escalar real

Para un campo escalar libre real, se toma

$$
\mathcal{L} = \frac{1}{2}\partial_\mu \phi\, \partial^\mu \phi - \frac{1}{2}m^2\phi^2.
$$

Aplicando Euler-Lagrange se obtiene

$$
\left(\partial_\mu \partial^\mu + m^2\right)\phi = 0,
$$

que es la ecuacion de Klein-Gordon.

Este ejemplo es importante porque muestra el patron general:

- termino cinetico;
- termino de masa;
- ecuacion de movimiento relativista.

## 6. Como leer una lagrangiana

Una buena practica al empezar QFT consiste en entrenar la mirada para leer rapidamente una densidad lagrangiana. En una primera pasada conviene preguntar:

- cuales son los campos dinamicos;
- cual es la parte cuadratica;
- cuales son las masas;
- si aparecen derivadas acopladas;
- si hay terminos de interaccion no lineales.

Esa lectura preliminar suele decir mucho antes de hacer un solo calculo detallado.

## 7. Dimensiones y unidades naturales

En muchos textos se usan unidades naturales $c=\hbar=1$. Eso hace que masas, energias e inversas de longitud compartan dimensiones compatibles. La accion suele tomarse adimensional en estas unidades, lo que ayuda a fijar las dimensiones de campos y acoplamientos.

Esta observacion no es decorativa. La contabilidad dimensional ayuda a anticipar:

- que terminos son admisibles;
- como escalan los acoplamientos;
- que tipo de teoria efectiva estamos escribiendo.

## 8. Terminos de interaccion

Si a la teoria libre del campo escalar se le añade un termino como

$$
\mathcal{L}_{\text{int}} = -\frac{\lambda}{4!}\phi^4,
$$

la ecuacion de movimiento deja de ser lineal:

$$
\left(\partial_\mu \partial^\mu + m^2\right)\phi + \frac{\lambda}{3!}\phi^3 = 0.
$$

Ya en este nivel clasico se ve una idea central: la forma de la lagrangiana controla de manera directa la complejidad dinamica de la teoria.

## 9. Por que la accion es el puente hacia la cuantizacion

La accion no solo organiza la teoria clasica. Tambien es el lenguaje desde el cual se construyen:

- la cuantizacion canonica, a traves de momentos conjugados y hamiltonianos;
- la integral de camino, a traves del peso $e^{iS}$;
- las reglas perturbativas, a traves de la separacion entre parte libre e interaccion.

Por eso dominar el principio de accion no es un lujo formal, sino un prerequisito real para entender la maquinaria de la QFT.

## 10. Errores frecuentes

- Pensar que la accion es solo una herramienta elegante para reescribir ecuaciones ya conocidas.
- Olvidar que la densidad lagrangiana debe ser un escalar relativista.
- Leer una lagrangiana sin distinguir entre parte libre y parte interactuante.
- Ignorar la informacion dimensional de los terminos.

## 11. Preguntas de control

- Que se gana al pasar de ecuaciones de movimiento directas a una formulacion por accion.
- Como se obtiene Euler-Lagrange para campos.
- Que informacion fisica se puede leer directamente de una lagrangiana simple.
- Por que la accion sirve tanto en el nivel clasico como en el cuantico.

## 12. Cierre

La accion es el punto de condensacion de la teoria. No es simplemente una forma compacta de escribir la dinamica: es el objeto que unifica localidad, simetria y estructura cuantizable en un mismo marco.
