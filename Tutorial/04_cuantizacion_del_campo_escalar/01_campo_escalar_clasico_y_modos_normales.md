# Campo Escalar Clasico y Modos Normales

**Nivel:** Nucleo  
**Dificultad:** Media  
**Tiempo estimado:** 25-35 min  
**Prerequisitos recomendados:** [Modulo anterior](../03_accion_y_simetrias/README.md) · [Resumen del modulo](README.md)

## Proposito

Este capitulo fija el laboratorio clasico del campo escalar libre para que la cuantizacion posterior surja sobre una base clara de ecuaciones de movimiento, modos normales y estructura relativista.

## 1. Introduccion

Antes de cuantizar un campo conviene entender bien su estructura clasica. El campo escalar libre es el mejor laboratorio inicial porque combina:

- covariancia relativista;
- ecuacion de movimiento simple;
- expansion en modos manejable;
- conexion directa con el oscilador armonico.

Es una eleccion pedagogica excelente porque es lo bastante simple para poder seguir todos los pasos a mano y, a la vez, lo bastante rica como para contener en germen gran parte del lenguaje posterior.

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

Aunque formalmente recuerda a una ecuacion de onda relativista, no debe leerse como la ecuacion de una particula individual en el sentido no relativista. Aqui describe la dinamica de un campo clasico distribuido en el espacio-tiempo.

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

La condicion $p^2=m^2$ es importante: indica que, para un modo libre, frecuencia y momento no son parametros independientes, sino que quedan ligados por la dinamica relativista del campo.

## 4. Expansion general en modos

Un campo real libre puede expandirse como superposicion de soluciones de frecuencia positiva y negativa:

$$
\phi(x)=\int \frac{d^3p}{(2\pi)^3}\frac{1}{\sqrt{2E_{\mathbf p}}}
\left(a(\mathbf p)e^{-ip\cdot x}+a^*(\mathbf p)e^{ip\cdot x}\right).
$$

En el nivel clasico, los coeficientes $a(\mathbf p)$ son simplemente amplitudes complejas que parametrizan la solucion.

Es importante remarcarlo porque la misma notacion se reutilizara mas adelante. Aqui todavia no son operadores de creacion ni aniquilacion; son solo coordenadas complejas en el espacio de soluciones clasicas.

## 5. Campo como conjunto continuo de osciladores

La intuicion crucial aparece al observar que cada modo etiquetado por $\mathbf p$ evoluciona de manera analoga a un oscilador armonico. La frecuencia natural de ese modo es precisamente $E_{\mathbf p}$.

Esto significa que el campo libre puede entenderse como una coleccion infinita de osciladores, uno por cada modo de momento. Esta observacion es la bisagra entre la teoria clasica de campos y la cuantizacion.

Esa bisagra es exactamente la razon por la que el oscilador armonico cuantico aparece como prerrequisito tan central. Cuantizar el campo sera, en esencia, cuantizar todos esos modos a la vez.

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

Ademas, la densidad hamiltoniana deja ver de donde procede la energia del campo:

- una parte cinetica asociada a $\pi^2$;
- una parte de gradiente asociada a variaciones espaciales;
- una parte de masa asociada a $\phi^2$.

## 7. Condicion de realidad

Para un campo real, la expansion en modos no contiene coeficientes independientes para frecuencias positiva y negativa. La realidad del campo obliga a relacionarlos por conjugacion compleja. Esta observacion suele parecer tecnica, pero prepara el terreno para entender por que en la teoria cuantica aparecen operadores de creacion y aniquilacion vinculados entre si.

Si el campo fuera complejo, en cambio, la estructura seria mas amplia y las partes de frecuencia positiva y negativa tendrian grados de libertad independientes. Ese sera el camino natural hacia teorias con carga conservada y simetrias $U(1)$.

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

No hay una ruptura total entre teoria clasica y cuantica. Lo que cambia no es la forma general del problema, sino el estatuto matematico de sus variables y la interpretacion fisica de sus modos.

## Cuaderno asociado

- Consulta los cuadernos asociados de este bloque en [Resumen del modulo](README.md) para reforzar el capitulo con practica guiada.

## 9. Preguntas de control

- Como se obtiene la relacion de dispersion relativista a partir de la ecuacion de Klein-Gordon.
- Por que la expansion en modos es natural para un campo libre.
- En que sentido cada modo se comporta como un oscilador armonico.
- Que informacion aporta la densidad hamiltoniana.

## 10. Advertencias utiles

- La expansion en modos de un campo libre no es una aproximacion, sino una descomposicion estructural.
- Un modo clasico no es todavia una particula: la interpretacion particula aparece tras cuantizar.
- La condicion on-shell no significa que toda configuracion clasica sea una onda plana unica.
- La ecuacion de Klein-Gordon clasica no debe confundirse con una teoria completa de una sola particula relativista.

## 11. Cierre

La teoria clasica del campo escalar libre ya contiene en germen casi todo lo necesario para la cuantizacion. El paso cuantico no inventa una estructura completamente nueva; reorganiza y promueve a operadores la estructura modal que ya estaba presente.

Esa continuidad conceptual es muy valiosa. Una vez que el estudiante ve al campo libre como una familia de modos armonicos, la cuantizacion deja de parecer un salto misterioso y se convierte en una extension natural del analisis clasico.

## 12. Referencias y lecturas recomendadas

- Base: Srednicki, campo escalar libre y expansion en modos.
- Complementaria: Tong, lectura pedagogica de Klein-Gordon y osciladores.
- Profundizacion: Peskin y Schroeder, formulacion clasica previa a la cuantizacion.


---

## Navegacion del tutorial

[(anterior) Portada 03: Cuantizacion Canonica del Campo Escalar Libre](../portada_03_cuantizacion_canonica_del_campo_escalar.md) | [(siguiente) Cuantizacion Canonica y Espacio de Fock](02_cuantizacion_canonica_y_espacio_de_fock.md)
