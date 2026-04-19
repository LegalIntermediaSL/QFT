# Campo Escalar Clasico y Modos Normales

## 1. Introduccion

Antes de cuantizar un campo conviene entender bien su estructura clasica. El campo escalar libre es el mejor laboratorio inicial porque combina:

- covariancia relativista;
- ecuacion de movimiento simple;
- expansion en modos manejable;
- conexion directa con el oscilador armonico.

## 2. Lagrangiana del campo escalar libre

Tomamos

$$
\mathcal{L} = \frac{1}{2}\partial_\mu \phi\,\partial^\mu \phi - \frac{1}{2}m^2\phi^2.
$$

La ecuacion de Euler-Lagrange asociada es

$$
\left(\partial_\mu\partial^\mu + m^2\right)\phi = 0.
$$

Esta es la ecuacion de Klein-Gordon para un campo real.

## 3. Soluciones tipo onda plana

Buscamos soluciones de la forma

$$
\phi(x) \sim e^{-ip\cdot x}.
$$

Sustituyendo en la ecuacion se obtiene la condicion on-shell:

$$
p^2 = m^2,
$$

o equivalentemente

$$
p^0 = E_{\mathbf p} = \sqrt{\mathbf p^2 + m^2}.
$$

Esto muestra que el espectro de modos del campo respeta la dispersion relativista.

## 4. Expansion general en modos

Un campo real libre puede expandirse como superposicion de soluciones de frecuencia positiva y negativa:

$$
\phi(x)=\int \frac{d^3p}{(2\pi)^3}\frac{1}{\sqrt{2E_{\mathbf p}}}
\left(a(\mathbf p)e^{-ip\cdot x}+a^*(\mathbf p)e^{ip\cdot x}\right).
$$

En el nivel clasico, los coeficientes $a(\mathbf p)$ son simplemente amplitudes complejas que parametrizan la solucion.

## 5. Campo como conjunto continuo de osciladores

La intuicion crucial aparece al observar que cada modo etiquetado por $\mathbf p$ evoluciona de manera analoga a un oscilador armonico. La frecuencia natural de ese modo es precisamente $E_{\mathbf p}$.

Esto significa que el campo libre puede entenderse como una coleccion infinita de osciladores, uno por cada modo de momento. Esta observacion es la bisagra entre la teoria clasica de campos y la cuantizacion.

## 6. Momento conjugado y estructura hamiltoniana

El momento conjugado es

$$
\pi(x)=\frac{\partial\mathcal{L}}{\partial(\partial_0\phi)}=\dot\phi(x).
$$

Con ello se puede construir la densidad hamiltoniana

$$
\mathcal{H} = \pi\dot\phi - \mathcal{L}
= \frac{1}{2}\pi^2 + \frac{1}{2}(\nabla\phi)^2 + \frac{1}{2}m^2\phi^2.
$$

La positividad de esta expresion para el caso libre real refuerza la interpretacion del sistema como superposicion de osciladores.

## 7. Condicion de realidad

Para un campo real, la expansion en modos no contiene coeficientes independientes para frecuencias positiva y negativa. La realidad del campo obliga a relacionarlos por conjugacion compleja. Esta observacion suele parecer tecnica, pero prepara el terreno para entender por que en la teoria cuantica aparecen operadores de creacion y aniquilacion vinculados entre si.

## 8. Que cambia al cuantizar

En el nivel clasico:

- $\phi$ es una variable de campo ordinaria;
- $\pi$ es su momento conjugado;
- los coeficientes modales son numeros complejos.

En el nivel cuantico:

- $\phi$ y $\pi$ se promueven a operadores;
- los coeficientes modales pasan a ser operadores;
- el espacio de soluciones se convierte en espacio de estados.

Por eso vale la pena entender bien la teoria clasica: la cuantizacion reutiliza casi toda su arquitectura.

## 9. Preguntas de control

- Como se obtiene la relacion de dispersion relativista a partir de la ecuacion de Klein-Gordon.
- Por que la expansion en modos es natural para un campo libre.
- En que sentido cada modo se comporta como un oscilador armonico.
- Que informacion aporta la densidad hamiltoniana.

## 10. Cierre

La teoria clasica del campo escalar libre ya contiene en germen casi todo lo necesario para la cuantizacion. El paso cuantico no inventa una estructura completamente nueva; reorganiza y promueve a operadores la estructura modal que ya estaba presente.
