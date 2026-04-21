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

Si el campo pesado aparece de manera cuadratica o casi cuadratica, esta integracion puede hacerse exactamente o en expansion controlada. En lenguaje menos tecnico: no estamos "adivinando" la EFT, sino derivandola a partir de la teoria completa bajo el supuesto clave de separacion de escalas.

## 5. Integrar no es olvidar

Una confusion comun es pensar que integrar un grado de libertad pesado equivale a negar su existencia. No es asi. Integrarlo significa:

- dejar de describirlo como una excitacion explicita en el espectro accesible;
- conservar su huella en coeficientes y operadores efectivos;
- reorganizar la teoria para energias donde ese grado de libertad no puede ponerse on-shell.

En particular, una particula pesada puede seguir afectando fuertemente:

- masas y acoplamientos renormalizados;
- procesos virtuales;
- simetrias efectivas del sector ligero.

## 6. Expansion en operadores efectivos

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

Esta expansion no es solo una lista de correcciones. Es una jerarquia organizada por simetria y dimension. Si dos operadores tienen la misma dimension, las simetrias del problema y el detalle de la UV completion determinan cual aparece y con que coeficiente.

## 7. Power counting y supresion por escala

Si un operador tiene dimension seis, su contribucion tipica aparece como

$$
\frac{1}{\Lambda^2}\mathcal{O}_6.
$$

Eso significa que sus efectos relativos suelen escalar como

$$
\left(\frac{E}{\Lambda}\right)^2.
$$

Pedagogicamente, esta es una de las ideas mas importantes del modulo: la EFT no ignora nueva fisica UV, sino que organiza de forma controlada cuan visible es a la escala de interes.

Conviene no interpretar esta estimacion como una ley exacta independiente del proceso. El factor $(E/\Lambda)^2$ da el orden de magnitud esperado, pero el tamaño real tambien depende de:

- el coeficiente de Wilson del operador;
- factores cinematicos adicionales;
- simetrias que puedan anular o suprimir ciertos terminos;
- si el observable aparece ya a nivel arbol o solo a lazo.

## 8. Ejemplo de eliminacion clasica del campo pesado

En el ejemplo con

$$
\mathcal{L}_{\text{int}} = -g\,\Phi \phi^2,
$$

si buscamos la ecuacion de movimiento clasica del campo pesado y despreciamos derivadas frente a $M^2$, obtenemos esquematicamente

$$
\Phi \approx -\frac{g}{M^2}\phi^2.
$$

Al sustituir esta solucion de vuelta en el lagrangiano, aparece un operador efectivo del tipo

$$
\Delta \mathcal{L}_{\mathrm{eff}} \sim \frac{g^2}{M^2}\phi^4.
$$

Esta cuenta no reemplaza la derivacion funcional completa, pero comunica muy bien la logica del desacoplamiento: el propagador pesado se colapsa en una interaccion local cuando el momento transferido es pequeño comparado con $M$.

## 9. Desacoplamiento

El teorema de Appelquist-Carazzone resume la intuicion de que, en muchas teorias renormalizables, los grados de libertad muy pesados desacoplan de la fisica IR salvo por:

- redefiniciones de parametros ligeros;
- correcciones locales suprimidas por potencias de la escala pesada.

Ese desacoplamiento no es magia: nace de la combinacion entre simetrias, expansion en momentos y separacion clara de escalas.

Tambien conviene registrar el matiz importante: no todo grado de libertad pesado desacopla de manera ingenua. Si su masa esta ligada a la ruptura de una simetria o a una estructura anomala, pueden sobrevivir efectos menos triviales en bajas energias. Por eso el desacoplamiento debe leerse como principio muy poderoso, pero no como reflejo automatico sin revisar la estructura teorica.

## 10. Ejemplo corto de lectura

Si una particula pesada de masa $M$ media una interaccion entre campos ligeros, a energias muy por debajo de $M$ no necesitamos seguir su propagador completo. Su efecto dominante se puede reemplazar por un contacto local mas coeficientes suprimidos por $1/M^2$, $1/M^4$, etc.

## 11. Donde aparece esta idea en fisica real

La idea de integrar grados de libertad aparece en casi todos los grandes ejemplos modernos:

- la teoria de Fermi al eliminar el boson $W$ a bajas energias;
- el lagrangiano de Euler-Heisenberg al integrar electrones en procesos de fotones suaves;
- SMEFT al parametrizar nueva fisica pesada por encima de la escala electrodébil;
- gravedad efectiva al organizar correcciones de energia baja a la relatividad general.

Por eso este lenguaje no es una tecnica marginal, sino una forma estandar de pensar en QFT contemporanea.

## 12. Cuaderno asociado

- `../../Cuadernos/ejemplos/15_operadores_efectivos_y_power_counting.ipynb`: usarlo para fijar el conteo dimensional y la lectura de operadores efectivos segun la escala de corte.

## 13. Advertencias utiles

- Integrar un campo pesado no siempre significa simplemente "borrarlo"; significa resumir su efecto en nuevos operadores y coeficientes.
- La expansion efectiva depende de la jerarquia de escalas. Si $E$ deja de ser pequeño frente a $\Lambda$, la EFT pierde control.
- No toda EFT es perturbativamente simple, pero casi siempre sigue siendo una organizacion muy util.

## 14. Preguntas de comprobacion

- Que significa integrar grados de libertad pesados.
- Por que aparecen operadores de dimension mayor que cuatro.
- Como se estima la importancia de un operador usando $E/\Lambda$.

## 15. Referencias y lecturas recomendadas

- Base: notas introductorias sobre EFT y desacoplamiento.
- Complementaria: Burgess, introducciones pedagogicas a EFT.
- Profundizacion: textos sobre matching funcional y expansion de operadores.


---

## Navegacion del tutorial

[(anterior) Curva de Page y Unitaridad](../11_qft_informacion_y_agujeros_negros/04_curva_de_page_y_unitaridad.md) | [(siguiente) Teoria de Fermi como EFT](02_teoria_de_fermi_como_eft.md)
