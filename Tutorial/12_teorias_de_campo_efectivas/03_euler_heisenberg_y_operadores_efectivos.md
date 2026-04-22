# Euler-Heisenberg y operadores efectivos

**Nivel:** Avanzado  
**Dificultad:** Alta  
**Tiempo estimado:** 25-35 min  
**Prerequisitos recomendados:** [Teoria de Fermi como EFT](02_teoria_de_fermi_como_eft.md) · [Resumen del modulo](README.md)


## 1. Proposito

Este documento presenta otro ejemplo clasico de EFT: la aparicion de auto-interacciones efectivas del campo electromagnetico inducidas por efectos cuanticos de electrones pesados en procesos de baja energia.

## 2. Maxwell clasico y linealidad

La electrodinamica clasica en vacio se describe por

$$
\mathcal{L}_{\mathrm{Maxwell}} = -\frac{1}{4}F_{\mu\nu}F^{\mu\nu}.
$$

Esta teoria es lineal: en ausencia de fuentes, dos ondas electromagneticas simplemente se superponen.

Sin embargo, en QED el vacio contiene fluctuaciones de pares cargados virtuales que modifican esa intuicion a energia finita.

## 3. Integrando electrones pesados

Si nos concentramos en fotones con energia mucho menor que la masa del electron,

$$
E \ll m_e,
$$

los electrones no se producen como estados externos reales, pero sus lazos dejan una huella en la accion efectiva del campo electromagnetico.

La lagrangiana efectiva adquiere correcciones de orden superior como

$$
\mathcal{L}_{\mathrm{EH}}
= -\frac{1}{4}F_{\mu\nu}F^{\mu\nu}
+ \frac{a}{m_e^4}(F_{\mu\nu}F^{\mu\nu})^2
+ \frac{b}{m_e^4}(F_{\mu\nu}\tilde{F}^{\mu\nu})^2
+ \cdots
$$

Esta es la idea central de la lagrangiana de Euler-Heisenberg.

Lo notable es que el sector ligero de la EFT contiene solo fotones, mientras que la informacion del electron queda encapsulada en los coeficientes de operadores de dimension superior. Es un ejemplo muy limpio de una teoria UV completamente conocida que produce una EFT no trivial.

## 4. Que nos dice esta estructura

Los nuevos terminos muestran que:

- el vacio cuantico polarizable genera interacciones efectivas entre fotones;
- la linealidad clasica de Maxwell deja de ser exacta cuando incluimos efectos cuanticos;
- esas correcciones quedan fuertemente suprimidas por potencias de la masa electronica.

En otras palabras, la QED completa induce una EFT puramente fotonica a baja energia.

El hecho de que la supresion aparezca como $1/m_e^4$ no es accidental. Los primeros operadores no triviales construidos con $F_{\mu\nu}$ y compatibles con las simetrias relevantes tienen dimension ocho. Por eso su coeficiente debe cargar dimension $-4$.

## 5. Operadores y simetrias

Los operadores efectivos deben respetar:

- invariancia gauge;
- simetrias relativistas;
- las restricciones discretas relevantes si no se introducen fuentes que las rompan.

Por eso las correcciones no toman cualquier forma arbitraria: quedan organizadas por combinaciones invariantes construidas con $F_{\mu\nu}$ y $\tilde{F}_{\mu\nu}$.

En particular, en ausencia de violaciones explicitas de paridad o CP, los invariantes mas relevantes son

$$
F_{\mu\nu}F^{\mu\nu}
\qquad\text{y}\qquad
F_{\mu\nu}\tilde{F}^{\mu\nu}.
$$

Sus cuadrados generan exactamente la clase de operadores que aparece en Euler-Heisenberg.

## 6. Lectura en terminos de campos electricos y magneticos

La combinacion

$$
F_{\mu\nu}F^{\mu\nu}
$$

se relaciona con $B^2-E^2$, mientras que

$$
F_{\mu\nu}\tilde{F}^{\mu\nu}
$$

esta ligada a $\mathbf{E}\cdot\mathbf{B}$. Esto permite una lectura fisica bastante intuitiva:

- el vacio cuantico responde de manera no lineal a campos intensos;
- la respuesta depende de invariantes relativistas del fondo electromagnetico;
- la EFT resume esa polarizacion del vacio sin tener que recalcular el lazo de electrones en cada caso.

## 7. Lectura fisica

El mensaje pedagogico no es que vayamos a medir facilmente dispersion foton-foton en un curso introductorio, sino que:

- los lazos cuanticos pueden generar interacciones ausentes a nivel clasico;
- las EFT permiten resumirlas sin recalcular toda la teoria UV en cada proceso IR;
- las simetrias mandan sobre la forma de los operadores.

Este ejemplo es especialmente valioso porque destruye una intuicion clasica demasiado rigida: el vacio no es simplemente "nada", sino un medio cuantico capaz de polarizarse.

## 8. Ejemplo corto de lectura

Aunque la electrodinamica clasica no permite que dos rayos de luz interactuen directamente en el vacio, la QED predice una auto-interaccion efectiva muy pequeña inducida por lazos de electrones. Euler-Heisenberg es justamente la forma efectiva de escribir esa fisica a baja energia.

## Cuaderno asociado
- `../../Cuadernos/ejemplos/15_operadores_efectivos_y_power_counting.ipynb`: usarlo para reforzar la idea de operadores efectivos suprimidos por la escala pesada.

## 10. Advertencias utiles

- La lagrangiana de Euler-Heisenberg es una descripcion de baja energia, no la sustitucion universal de QED.
- No todas las correcciones cuanticas se reducen a un solo operador; aparece una torre organizada por simetrias y dimensiones.
- El ejemplo es muy valioso porque muestra EFT incluso dentro de una teoria renormalizable y muy bien establecida.

## 11. Preguntas de comprobacion

- Por que Maxwell clasico es lineal y QED efectiva no lo es del todo.
- Que papel juega la masa del electron en la supresion de los operadores.
- Por que las correcciones deben escribirse en combinaciones gauge invariantes.

## 12. Referencias y lecturas recomendadas

- Base: notas sobre accion efectiva en QED y Euler-Heisenberg.
- Complementaria: textos de campos externos y polarizacion del vacio.
- Profundizacion: derivaciones funcionales de la accion efectiva en fondos electromagneticos.


---

## Navegacion del tutorial

[(anterior) Teoria de Fermi como EFT](02_teoria_de_fermi_como_eft.md) | [(siguiente) Gravedad como teoria efectiva](04_gravedad_como_teoria_efectiva.md)