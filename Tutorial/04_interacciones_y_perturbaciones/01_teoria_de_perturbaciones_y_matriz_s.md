# Teoria de Perturbaciones y Matriz S

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

## 3. Estados asintoticos

En el enfoque de scattering suponemos que muy lejos en el pasado y en el futuro las particulas pueden tratarse como aproximadamente libres. Eso permite definir:

- estados de entrada;
- estados de salida;
- amplitudes de transicion entre ambos.

La idea no es que la interaccion desaparezca siempre literalmente, sino que hay regimens asintoticos donde la descripcion libre vuelve a ser una buena aproximacion operacional.

## 4. Matriz S

El objeto central es la matriz $S$, que conecta estados iniciales y finales:

$$
|\text{out}\rangle = S |\text{in}\rangle.
$$

Sus elementos de matriz contienen la informacion observable necesaria para calcular secciones eficaces y tasas de decaimiento.

## 5. Imagen de interaccion

Una forma muy util de organizar la teoria de perturbaciones es la imagen de interaccion. En ella:

- la evolucion debida a la parte libre se trata exactamente;
- la evolucion debida a la interaccion se incorpora en operadores dependientes del tiempo;
- las amplitudes se expanden en serie temporalmente ordenada.

Este esquema hace transparente la expansion en potencias del acoplamiento.

## 6. Serie de Dyson

Formalmente, la matriz $S$ puede expresarse como una serie de Dyson:

$$
S = T \exp\left(-i\int d^4x\, \mathcal{H}_{\text{int}}(x)\right),
$$

donde $T$ denota orden temporal. Expandiendo la exponencial se obtiene una suma de terminos con numero creciente de inserciones de la interaccion.

Cada orden en esta expansion corresponde a una clase de contribuciones perturbativas.

## 7. Que se calcula realmente

En QFT no se calculan trayectorias clasicas de particulas individuales. Se calculan amplitudes. De ellas se derivan probabilidades y observables experimentales despues de tomar modulos cuadrados, promedios, sumas sobre polarizaciones y fases de espacio apropiadas.

Esta diferencia conceptual es clave:

- amplitud no es probabilidad;
- probabilidad no es seccion eficaz;
- diagrama no es trayectoria.

## 8. Parametro pequeno y validez perturbativa

La teoria de perturbaciones funciona cuando el acoplamiento relevante es suficientemente pequeno como para que la expansion ordenada tenga sentido practico. Si la interaccion es fuerte, la serie puede converger mal o ser poco util. Eso explica por que hay regimens donde los metodos perturbativos son extraordinarios y otros donde resultan insuficientes.

## 9. Correcciones de orden superior

Los primeros ordenes de la expansion suelen capturar el comportamiento dominante. Los terminos de orden superior introducen:

- correcciones radiativas;
- renormalizacion de parametros;
- estructura de lazos;
- sensibilidad a escalas internas.

Por eso la expansion perturbativa no solo es una aproximacion; tambien es una manera de clasificar sistematicamente efectos fisicos.

## 10. Advertencias utiles

- No toda teoria interactuante es bien tratable perturbativamente.
- La matriz $S$ requiere cuidado conceptual cuando no hay estados asintoticos libres bien definidos.
- La serie de Dyson es una expansion formal, no una licencia para ignorar los dominios de validez.

## 11. Preguntas de control

- Que papel cumple la separacion entre $\mathcal{L}_0$ y $\mathcal{L}_{\text{int}}$.
- Que significa que los estados sean asintoticamente libres.
- Que informa un elemento de matriz de $S$.
- Por que una amplitud no debe confundirse con una probabilidad ya final.

## 12. Cierre

La teoria de perturbaciones ofrece un puente entre la estructura abstracta de la teoria y los numeros que se comparan con experimentos. Ese puente se vuelve especialmente poderoso cuando se reorganiza graficamente en diagramas de Feynman.
