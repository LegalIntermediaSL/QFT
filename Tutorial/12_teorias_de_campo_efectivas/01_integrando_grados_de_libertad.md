# Integrando grados de libertad

## 1. Proposito

Este documento introduce el corazon conceptual de una teoria de campo efectiva: describir fisica a baja energia sin retener explicitamente todos los grados de libertad microscopicos.

## 2. La intuicion fisica

Si un experimento opera a energias $E \ll \Lambda$, no puede producir de forma real estados con masa del orden de $\Lambda$. Esos estados pesados no desaparecen por completo, pero su efecto puede resumirse en correcciones locales para los campos ligeros.

La idea es muy parecida a muchas aproximaciones de la fisica:

- no hace falta seguir cada molecula para describir hidrodinamica;
- no hace falta seguir cada detalle del nucleo para escribir una teoria atomica efectiva;
- no hace falta retener todas las particulas pesadas para describir fisica IR.

## 3. Ejemplo minimo con campo ligero y pesado

Consideremos una teoria con un campo ligero $\phi$ y un campo pesado $\Phi$:

$$
\mathcal{L} = \frac{1}{2}(\partial \phi)^2 - \frac{1}{2}m^2 \phi^2
+ \frac{1}{2}(\partial \Phi)^2 - \frac{1}{2}M^2 \Phi^2
- g\, \Phi \phi^2,
$$

con $M \gg m$.

Si trabajamos a energias mucho menores que $M$, el campo $\Phi$ no se produce como particula real. Sin embargo, al intercambiarse virtualmente induce una interaccion efectiva entre campos ligeros.

## 4. Integral de camino y accion efectiva

En el formalismo funcional:

$$
Z[J] = \int \mathcal{D}\phi \, \mathcal{D}\Phi \;
\exp\!\left(iS[\phi,\Phi] + i \int d^4x\, J\phi \right).
$$

Definimos una accion efectiva para el campo ligero integrando el campo pesado:

$$
\exp\!\left(iS_{\mathrm{eff}}[\phi]\right)
= \int \mathcal{D}\Phi \; \exp\!\left(iS[\phi,\Phi]\right).
$$

La teoria resultante ya no contiene $\Phi$ de forma explicita, pero si retiene sus efectos en una expansion en operadores locales.

## 5. Expansion en operadores efectivos

La forma general de la densidad lagrangiana efectiva es

$$
\mathcal{L}_{\mathrm{eff}}
= \mathcal{L}_{d\leq 4}
+ \sum_{n>4}\frac{c_n}{\Lambda^{\,n-4}}\mathcal{O}_n,
$$

donde $\Lambda$ representa la escala pesada relevante y $\mathcal{O}_n$ es un operador de dimension de masa $n$.

Esto organiza la teoria de forma muy poderosa:

- operadores relevantes: $d<4$;
- operadores marginales: $d=4$;
- operadores irrelevantes: $d>4$.

A bajas energias, los operadores irrelevantes quedan suprimidos por potencias de $E/\Lambda$.

## 6. Power counting y supresion por escala

Si un operador tiene dimension seis, su contribucion tipica aparece como

$$
\frac{1}{\Lambda^2}\mathcal{O}_6.
$$

Eso significa que sus efectos relativos suelen escalar como

$$
\left(\frac{E}{\Lambda}\right)^2.
$$

Pedagogicamente, esta es una de las ideas mas importantes del modulo: la EFT no ignora nueva fisica UV, sino que organiza de forma controlada cuan visible es a la escala de interes.

## 7. Desacoplamiento

El teorema de Appelquist-Carazzone resume la intuicion de que, en muchas teorias renormalizables, los grados de libertad muy pesados desacoplan de la fisica IR salvo por:

- redefiniciones de parametros ligeros;
- correcciones locales suprimidas por potencias de la escala pesada.

Ese desacoplamiento no es magia: nace de la combinacion entre simetrias, expansion en momentos y separacion clara de escalas.

## 8. Ejemplo corto de lectura

Si una particula pesada de masa $M$ media una interaccion entre campos ligeros, a energias muy por debajo de $M$ no necesitamos seguir su propagador completo. Su efecto dominante se puede reemplazar por un contacto local mas coeficientes suprimidos por $1/M^2$, $1/M^4$, etc.

## 9. Cuaderno asociado

- `../../Cuadernos/ejemplos/15_operadores_efectivos_y_power_counting.ipynb`: usarlo para fijar el conteo dimensional y la lectura de operadores efectivos segun la escala de corte.

## 10. Advertencias utiles

- Integrar un campo pesado no siempre significa simplemente "borrarlo"; significa resumir su efecto en nuevos operadores y coeficientes.
- La expansion efectiva depende de la jerarquia de escalas. Si $E$ deja de ser pequeño frente a $\Lambda$, la EFT pierde control.
- No toda EFT es perturbativamente simple, pero casi siempre sigue siendo una organizacion muy util.

## 11. Preguntas de comprobacion

- Que significa integrar grados de libertad pesados.
- Por que aparecen operadores de dimension mayor que cuatro.
- Como se estima la importancia de un operador usando $E/\Lambda$.

## 12. Referencias y lecturas recomendadas

- Base: notas introductorias sobre EFT y desacoplamiento.
- Complementaria: Burgess, introducciones pedagogicas a EFT.
- Profundizacion: textos sobre matching funcional y expansion de operadores.


---

## Navegacion del tutorial

[(anterior) Curva de Page y Unitaridad](../11_qft_informacion_y_agujeros_negros/04_curva_de_page_y_unitaridad.md) | [(siguiente) Teoria de Fermi como EFT](02_teoria_de_fermi_como_eft.md)
