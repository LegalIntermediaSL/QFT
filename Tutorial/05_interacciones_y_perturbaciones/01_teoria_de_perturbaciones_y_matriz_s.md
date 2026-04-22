# Teoria de Perturbaciones y Matriz S

**Nivel:** Nucleo  
**Dificultad:** Media  
**Tiempo estimado:** 25-35 min  
**Prerequisitos recomendados:** [Modulo anterior](../04_cuantizacion_del_campo_escalar/README.md) · [Resumen del modulo](README.md)


## 1. Introduccion

Las teorias libres son esenciales para entender la estructura del espacio de estados, pero la fisica experimental rara vez se reduce a sistemas sin interaccion. Para describir dispersion, decaimientos y produccion de particulas necesitamos introducir terminos interactuantes.

## 2. Separacion entre parte libre e interaccion

Un lagrangiano tipico se organiza como

$$
\mathcal{L} = \mathcal{L}_0 + \mathcal{L}_{\text{int}},
$$

donde $\mathcal{L}_0$ es la parte libre y $\mathcal{L}_{\text{int}}$ contiene acoplamientos no lineales. Por ejemplo, en una teoria escalar se puede tomar

$$
\mathcal{L}_{\text{int}} = -\frac{\lambda}{4!}\phi^4.
$$

La utilidad de esta separacion es que la teoria libre se resuelve exactamente y la interaccion se trata como correccion organizada.

Esta separacion no es solo tecnica. Refleja una estrategia fisica: partimos de un problema cuyo espacio de estados controlamos bien y construimos sobre el una expansion que captura progresivamente la complejidad de las interacciones reales.

Tambien deja clara una limitacion: si la interaccion es demasiado fuerte o modifica radicalmente el espectro, la separacion entre "parte libre conocida" y "correccion pequena" puede dejar de ser util.

## 3. Que significa resolver la teoria libre

Resolver la teoria libre significa, en esencia:

- conocer sus modos normales;
- cuantizar los campos;
- construir su espacio de Fock;
- identificar su hamiltoniano y sus excitaciones asintoticas.

Sin esa base, la teoria de perturbaciones carece de punto de apoyo. Por eso el estudio de campos libres no es una etapa preliminar aburrida, sino la infraestructura sobre la que se construye todo el formalismo perturbativo.

De hecho, todo el lenguaje de particulas asintoticas, propagadores y diagramas depende de haber entendido primero con precision que significa un cuanto libre del campo.

## 4. Estados asintoticos

En el enfoque de scattering suponemos que muy lejos en el pasado y en el futuro las particulas pueden tratarse como aproximadamente libres. Eso permite definir:

- estados de entrada;
- estados de salida;
- amplitudes de transicion entre ambos.

La idea no es que la interaccion desaparezca siempre literalmente, sino que hay regimens asintoticos donde la descripcion libre vuelve a ser una buena aproximacion operacional.

En ese sentido, los estados asintoticos son una interfaz entre la descripcion teorica y el laboratorio: representan las configuraciones de entrada y salida que un detector puede preparar o medir con relativa claridad.

Esto explica por que el formalismo de matriz S funciona especialmente bien en problemas de scattering relativista y no necesariamente en cualquier situacion dinamica arbitraria.

## 5. Matriz S

El objeto central es la matriz $S$, que conecta estados iniciales y finales:

$$
|\text{out}\rangle = S |\text{in}\rangle.
$$

Sus elementos de matriz contienen la informacion observable necesaria para calcular secciones eficaces y tasas de decaimiento.

Conviene subrayar que la matriz $S$ no es un observable cualquiera. Es el organizador global de la teoria de scattering. En ella se condensan las amplitudes que luego se traducen en predicciones experimentales.

En muchos textos se escribe

$$
S = 1 + iT,
$$

para separar la parte trivial "no pasa nada" de la parte verdaderamente interactiva, contenida en el operador $T$.

## 6. Imagen de interaccion

Una forma muy util de organizar la teoria de perturbaciones es la imagen de interaccion. En ella:

- la evolucion debida a la parte libre se trata exactamente;
- la evolucion debida a la interaccion se incorpora en operadores dependientes del tiempo;
- las amplitudes se expanden en serie temporalmente ordenada.

Este esquema hace transparente la expansion en potencias del acoplamiento.

La imagen de interaccion resulta especialmente natural porque separa con claridad el problema exactamente soluble de la parte libre y la complejidad introducida por la interaccion. Sin esa separacion, la serie perturbativa seria mucho menos transparente.

Ademas, es el marco en el que la ordenacion temporal y la expansion de Dyson adquieren una interpretacion operacional muy clara.

## 7. Serie de Dyson

Formalmente, la matriz $S$ puede expresarse como una serie de Dyson:

$$
S = T \exp\left(-i\int d^4x\, \mathcal{H}_{\text{int}}(x)\right),
$$

donde $T$ denota orden temporal. Expandiendo la exponencial se obtiene una suma de terminos con numero creciente de inserciones de la interaccion.

Cada orden en esta expansion corresponde a una clase de contribuciones perturbativas. Es util escribir los primeros terminos:

$$
S = 1 - i\int d^4x\, \mathcal{H}_{\text{int}}(x)
 - \frac{1}{2}\int d^4x\, d^4y \, T\left\{\mathcal{H}_{\text{int}}(x)\mathcal{H}_{\text{int}}(y)\right\} + \cdots
$$

Asi se ve con claridad que cada orden añade nuevas inserciones de la interaccion y, por tanto, nuevas clases de procesos y correcciones.

Esta serie no es todavia un conjunto de diagramas, pero ya contiene todo su contenido combinatorio. Los diagramas de Feynman apareceran enseguida como una forma mucho mas eficiente de organizar esta expansion.

## 8. Que se calcula realmente

En QFT no se calculan trayectorias clasicas de particulas individuales. Se calculan amplitudes. De ellas se derivan probabilidades y observables experimentales despues de tomar modulos cuadrados, promedios, sumas sobre polarizaciones y fases de espacio apropiadas.

Esta diferencia conceptual es clave:

- amplitud no es probabilidad;
- probabilidad no es seccion eficaz;
- diagrama no es trayectoria.

Insistir en estas diferencias evita varias confusiones comunes al empezar: el formalismo perturbativo trabaja primero con amplitudes complejas, y solo al final se construyen cantidades positivas comparables con experimento.

## 9. Del elemento de matriz al observable

Entre una amplitud y un numero experimental hay varios pasos intermedios. En problemas de scattering, por ejemplo, suele extraerse una amplitud invariante $\mathcal{M}$ a partir del elemento de matriz de $S$, y luego se construyen:

- secciones eficaces diferenciales;
- secciones eficaces totales;
- anchos de decaimiento;
- distribuciones angulares.

Esto es importante pedagogicamente porque ayuda a no confundir el formalismo perturbativo con el dato final del experimento. El formalismo produce amplitudes; el puente hacia el laboratorio pasa por una capa adicional de interpretacion cinemática.

Por eso un mismo elemento de matriz puede contribuir de maneras distintas segun el observable que se quiera construir: no todo problema experimental se reduce al mismo tipo de promedio o integracion sobre espacio de fases.

## 10. Parametro pequeno y validez perturbativa

La teoria de perturbaciones funciona cuando el acoplamiento relevante es suficientemente pequeno como para que la expansion ordenada tenga sentido practico. Si la interaccion es fuerte, la serie puede converger mal o ser poco util. Eso explica por que hay regimens donde los metodos perturbativos son extraordinarios y otros donde resultan insuficientes.

Tambien conviene recordar que "pequeno" puede depender de la escala. Un acoplamiento puede ser manejable perturbativamente en cierto rango de energias y dejar de serlo en otro. Por eso la teoria de perturbaciones se conecta de manera natural con la idea de corrida de acoplamientos y grupo de renormalizacion.

Este punto es especialmente importante en teorias gauge: una teoria puede ser debilmente acoplada en un regimen ultravioleta y fuertemente acoplada en el infrarrojo, o al reves.

## 11. Correcciones de orden superior

Los primeros ordenes de la expansion suelen capturar el comportamiento dominante. Los terminos de orden superior introducen:

- correcciones radiativas;
- renormalizacion de parametros;
- estructura de lazos;
- sensibilidad a escalas internas.

Por eso la expansion perturbativa no solo es una aproximacion; tambien es una manera de clasificar sistematicamente efectos fisicos.

## 12. Ejemplo conceptual en teoria $\phi^4$

En una teoria con

$$
\mathcal{L}_{\text{int}} = -\frac{\lambda}{4!}\phi^4,
$$

el primer proceso de scattering $2\to2$ aparece ya a orden $\lambda$. A ordenes superiores aparecen lazos que corrigen:

- la propagacion efectiva;
- la intensidad del acoplamiento;
- la dependencia con la energia del proceso.

Este ejemplo simple basta para mostrar todo el esqueleto del formalismo perturbativo sin necesidad de introducir aun las complicaciones del Modelo Estandar.

En ese ejemplo ya se ve la logica completa:

- el termino de interaccion define el vertice;
- el propagador libre conecta inserciones;
- los ordenes superiores introducen lazos y renormalizacion.

## Cuaderno asociado

- Consulta los cuadernos asociados de este bloque en [Resumen del modulo](README.md) para reforzar el capitulo con practica guiada.

## 13. Advertencias utiles

- No toda teoria interactuante es bien tratable perturbativamente.
- La matriz $S$ requiere cuidado conceptual cuando no hay estados asintoticos libres bien definidos.
- La serie de Dyson es una expansion formal, no una licencia para ignorar los dominios de validez.

## 14. Preguntas de control

- Que papel cumple la separacion entre $\mathcal{L}_0$ y $\mathcal{L}_{\text{int}}$.
- Por que la teoria libre es la base indispensable del formalismo perturbativo.
- Que significa que los estados sean asintoticamente libres.
- Que informa un elemento de matriz de $S$.
- Por que una amplitud no debe confundirse con una probabilidad ya final.

## 15. Ejercicios sugeridos

1. Escribe los tres primeros terminos de la expansion de Dyson y explica verbalmente que representa cada uno.
2. Describe la diferencia entre estado asintotico libre, amplitud de scattering y seccion eficaz.
3. Explica por que la teoria de perturbaciones no es simplemente "hacer una aproximacion", sino tambien una forma de clasificar tipos de efectos fisicos.

## 16. Cierre

La teoria de perturbaciones ofrece un puente entre la estructura abstracta de la teoria y los numeros que se comparan con experimentos. Ese puente se vuelve especialmente poderoso cuando se reorganiza graficamente en diagramas de Feynman.

## 17. Referencias y lecturas recomendadas

- Base: Tong, matriz S y serie de Dyson.
- Complementaria: Peskin y Schroeder, teoria perturbativa en QFT.
- Profundizacion: textos de scattering relativista y amplitudes.


---

## Navegacion del tutorial

[(anterior) Propagador, Causalidad y Funcion de Green](../04_cuantizacion_del_campo_escalar/03_propagador_causalidad_y_funcion_de_green.md) | [(siguiente) Diagramas de Feynman y Reglas de Calculo](02_diagramas_de_feynman_y_reglas.md)