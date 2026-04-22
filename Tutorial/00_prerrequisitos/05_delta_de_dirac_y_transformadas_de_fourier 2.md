# Delta de Dirac y Transformadas de Fourier

## 1. Proposito

La QFT cambia constantemente entre espacio de posiciones y espacio de momentos. Para hacer ese cambio con soltura hace falta dominar dos herramientas: la transformada de Fourier y la delta de Dirac.

## 2. Idea general de Fourier

La transformada de Fourier permite descomponer una funcion en modos de frecuencia o de momento. En una variable, de forma esquematica:

$$
f(x) = \int \frac{dk}{2\pi}\,\tilde{f}(k)e^{ikx},
$$

$$
\tilde{f}(k) = \int dx\, f(x)e^{-ikx}.
$$

En QFT, esta descomposicion es natural porque los modos de momento son especialmente adecuados para describir propagacion libre y cuantizacion.

## 3. Fourier en tres y cuatro dimensiones

En fisica de particulas aparecen con frecuencia expresiones como

$$
f(\mathbf{x}) = \int \frac{d^3p}{(2\pi)^3}\,\tilde{f}(\mathbf{p})e^{i\mathbf{p}\cdot\mathbf{x}},
$$

y tambien integrales sobre cuatro-momento:

$$
\int \frac{d^4p}{(2\pi)^4}\, e^{-ip\cdot x}.
$$

Estas formulas son la base de:

- expansiones modales de campos;
- propagadores;
- reglas de Feynman en espacio de momentos.

## 4. Delta de Dirac

La delta de Dirac no es una funcion ordinaria, sino una distribucion definida por su accion bajo integracion:

$$
\int dx\, \delta(x-a)f(x)=f(a).
$$

Su funcion es seleccionar el valor de una funcion en un punto.

## 5. Propiedades basicas de la delta

Propiedades fundamentales:

$$
\delta(x-a)=\delta(a-x),
$$

$$
\int dx\, \delta(x-a)=1,
$$

$$
\delta(\alpha x)=\frac{1}{|\alpha|}\delta(x).
$$

En varias dimensiones:

$$
\int d^3x\, \delta^{(3)}(\mathbf{x}-\mathbf{a})f(\mathbf{x}) = f(\mathbf{a}).
$$

## 6. Conexion entre Fourier y delta

Una de las identidades mas usadas en QFT es

$$
\int \frac{dk}{2\pi}e^{ik(x-y)}=\delta(x-y),
$$

y en tres dimensiones

$$
\int \frac{d^3p}{(2\pi)^3}e^{i\mathbf{p}\cdot(\mathbf{x}-\mathbf{y})}
= \delta^{(3)}(\mathbf{x}-\mathbf{y}).
$$

Esta relacion explica por que la delta aparece naturalmente cuando se cambia de base entre posiciones y momentos.

## 7. Campos y expansion en modos

Cuando un campo libre se expande en modos, la normalizacion se elige de forma que las relaciones de conmutacion y las ortogonalidades entre modos produzcan deltas de Dirac. Por eso la delta no es una herramienta marginal: esta incrustada en el formalismo desde la cuantizacion misma.

## 8. Conservacion del momento

En espacio de momentos, la invariancia traslacional genera deltas de conservacion del momento. Por ejemplo, en un vertice de Feynman aparece tipicamente:

$$
(2\pi)^4 \delta^{(4)}\left(\sum p_{\text{entrantes}} - \sum p_{\text{salientes}}\right).
$$

Esto expresa que el momento total se conserva en la interaccion.

## 9. Distribuciones y precauciones

La delta de Dirac no debe tratarse como una funcion comun evaluada punto por punto. Tiene sentido dentro de integrales y como objeto de distribucion. Esta distincion importa mucho cuando se manipulan identidades formales en QFT.

## 10. Ejemplo conceptual

Si dos modos de momento son ortogonales salvo cuando sus momentos coinciden, esa ortogonalidad se expresa mediante una delta:

$$
\langle \mathbf{p}|\mathbf{q}\rangle \propto \delta^{(3)}(\mathbf{p}-\mathbf{q}).
$$

Esto conecta directamente la base de momentos con la estructura del espacio de estados.

## 11. Preguntas de estudio

- Que significa que la delta de Dirac sea una distribucion.
- Como se relacionan la delta y la transformada de Fourier.
- Por que la conservacion del momento aparece naturalmente como una delta.
- Por que el espacio de momentos es tan util en QFT.

## 12. Ejercicios sugeridos

1. Usa la definicion de la delta para mostrar que $\int dx\, \delta(x-a)f(x)=f(a)$.
2. Demuestra la identidad de Fourier que produce $\delta(x-y)$.
3. Explica por que una delta de cuatro-momento en un vertice expresa invariancia traslacional.

## 13. Cierre

Fourier y la delta de Dirac son parte del lenguaje operativo diario de la QFT. Sin ellas, las expansiones en modos, los propagadores y las reglas de Feynman quedan practicamente ilegibles.

## 14. Referencias y lecturas recomendadas

- Base: apuntes de analisis de Fourier y distribuciones para fisicos.
- Complementaria: cualquier curso de mecanica cuantica con base de momentos y deltas de ortogonalidad.
- Profundizacion: textos matematicos elementales sobre distribuciones y transformadas.


---

## Navegacion del tutorial

[(anterior) Simetrias y Grupos Basicos](04_simetrias_y_grupos_basicos.md) | [(siguiente) Conceptos Fundamentales de Teoria Cuantica de Campos](../01_fundamentos_conceptuales/01_conceptos_fundamentales.md)
