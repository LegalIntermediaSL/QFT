# Propagador, Causalidad y Funcion de Green

**Nivel:** Nucleo  
**Dificultad:** Media-Alta  
**Tiempo estimado:** 25-35 min  
**Prerequisitos recomendados:** [Cuantizacion Canonica y Espacio de Fock](02_cuantizacion_canonica_y_espacio_de_fock.md) · [Resumen del modulo](README.md)


## 1. Proposito

Este articulo cierra el modulo del campo escalar libre conectando la cuantizacion canonica con dos ideas que luego aparecen por todas partes en QFT: el propagador de Feynman y la lectura del campo como fuente de correladores. El objetivo es preparar el salto hacia interacciones, diagramas y amplitudes sin dejar un hueco conceptual entre espacio de Fock y teoria perturbativa.

## 2. Del campo cuantizado al correlador de dos puntos

Una vez cuantizado el campo, un objeto muy natural es el correlador temporalmente ordenado de dos campos:

$$
\langle 0|T\{\phi(x)\phi(y)\}|0\rangle.
$$

Este objeto contiene informacion sobre como una excitacion libre se propaga entre dos puntos del espacio-tiempo. No debe interpretarse como la trayectoria clasica de una particula, sino como una funcion de correlacion del vacio.

Aqui conviene subrayar una idea importante: el propagador no describe "lo que hace una particula concreta", sino la respuesta del formalismo de campo cuando se insertan operadores locales en dos puntos distintos. Esa distincion sera esencial cuando aparezcan lineas internas en diagramas.

## 3. Definicion del propagador de Feynman

Para el campo escalar libre se define

$$
\Delta_F(x-y)=\langle 0|T\{\phi(x)\phi(y)\}|0\rangle.
$$

El orden temporal significa:

- si $x^0>y^0$, el campo en $x$ actua a la izquierda;
- si $y^0>x^0$, el campo en $y$ actua a la izquierda.

Esta definicion ya anticipa por que el propagador de Feynman aparece tan naturalmente en teoria perturbativa.

La ordenacion temporal es importante porque asegura que el correlador este adaptado a la evolucion causal usada en la expansion de Dyson y en la formulacion funcional. No es un detalle decorativo, sino parte de la definicion del objeto correcto para scattering perturbativo.

En particular, el operador de orden temporal permite combinar en un mismo objeto los dos posibles ordenes relativos de los eventos, que despues se reorganizan de forma compacta en espacio de momentos.

## 4. Espacio de momentos e interpretacion

En espacio de momentos, el propagador libre adopta la forma familiar

$$
\tilde{\Delta}_F(p)=\frac{i}{p^2-m^2+i\epsilon}.
$$

Este factor es ubicuo en QFT. Aparece en:

- correladores libres;
- lineas internas de diagramas de Feynman;
- funciones de Green del operador cinetico;
- formulas de reduccion y amplitudes amputadas.

De hecho, buena parte del lenguaje diagramatico posterior consiste en reconocer que cada linea interna no es "una particula viajando" en sentido clasico, sino una copia de este bloque analitico basico.

Una forma util de leerlo es la siguiente:

- el denominador contiene la estructura de polos del espectro libre;
- el numerador escalar trivial refleja que no hay indices internos adicionales en el caso bosonico escalar;
- la prescripcion $i\epsilon$ fija la manera correcta de rodear los polos.

## 5. La prescripcion $i\epsilon$

El termino $i\epsilon$ no es cosmetico. Cumple varias funciones a la vez:

- desplaza los polos para definir correctamente la integral;
- fija la estructura causal del propagador de Feynman;
- permite distinguir la eleccion adecuada de contorno al integrar en energia.

Pedagogicamente conviene pensar que el $i\epsilon$ codifica la manera consistente de conectar el formalismo analitico con la condicion de vacio fisico.

Tambien es lo que permite seleccionar correctamente el contorno al integrar sobre $p^0$ y garantizar que el correlador obtenido corresponde al vacio de Feynman apropiado.

Sin esta prescripcion, la expresion formal del propagador quedaria ambigua justamente en los puntos donde su estructura analitica es mas importante.

## 6. Funcion de Green del operador de Klein-Gordon

El propagador libre satisface, en sentido distribucional,

$$
(\Box + m^2)\Delta_F(x-y) = -i\delta^{(4)}(x-y).
$$

Por eso se dice que $\Delta_F$ es una funcion de Green del operador de Klein-Gordon. Esta observacion es crucial porque:

- enlaza el lenguaje de ecuaciones diferenciales con el de correladores;
- explica por que una linea interna se asocia a la inversion del operador cinetico;
- prepara el terreno para la expansion perturbativa y la integral de camino.

En realidad, gran parte del formalismo perturbativo puede leerse como una teoria sistematica de invertir operadores cineticos y reorganizar esa inversion en presencia de interacciones.

Una buena intuicion es esta: cuantizar el campo no borra la estructura diferencial clasica, sino que la reorganiza en forma de correladores del vacio y funciones de Green distribucionales.

## 7. Causalidad microfisica y conmutadores

No todo correlador expresa causalidad de la misma manera. El objeto directamente ligado a causalidad microfisica es el conmutador

$$
[\phi(x),\phi(y)].
$$

En una teoria relativista bien construida, este conmutador se anula para separaciones espaciotemporales de tipo espacial:

$$
(x-y)^2<0.
$$

Esta propiedad expresa que observables locales separados espacialmente no deben influirse de forma causal.

Aqui aparece una distincion muy importante para evitar confusiones posteriores:

- el conmutador causal codifica microcausalidad;
- el propagador de Feynman codifica el correlador temporalmente ordenado util para perturbacion;
- ambos estan relacionados, pero no son el mismo objeto.

Esta diferencia explica por que el propagador de Feynman puede ser distinto de cero fuera del cono de luz sin que eso signifique una violacion operacional de causalidad.

## 8. Propagador y causalidad: una sutileza importante

Es facil confundirse aqui:

- el propagador de Feynman no es cero para separaciones espaciales;
- el objeto cuya anulacion protege la causalidad microfisica es el conmutador;
- el orden temporal del propagador responde a necesidades analiticas y de calculo, no a una lectura ingenua de "senal viajando".

Esto ayuda a desmontar una intuicion peligrosa: que cada linea de un diagrama representa una particula real moviendose entre dos eventos observables. En general, el propagador es un ingrediente de amplitud, no una trayectoria fisica directamente medible.

Esta distincion es muy importante antes de entrar en diagramas de Feynman, donde la palabra "propagador" puede inducir interpretaciones demasiado clasicas.

Tambien ayuda a entender por que en QFT aparecen naturalmente varios objetos relacionados pero distintos: propagadores de Feynman, retardados, avanzados y conmutadores causales. No todos sirven para la misma pregunta fisica.

## 9. Ejemplo corto de lectura

Si en una teoria libre se quiere resolver la respuesta del campo a una fuente puntual, el problema se organiza mediante una funcion de Green. En QFT, el mismo objeto que resuelve esa inversion del operador cinetico aparece despues como bloque elemental del calculo perturbativo.

Esa continuidad conceptual es una de las razones por las que el propagador ocupa un lugar tan central.

En el lenguaje clasico resuelve una ecuacion diferencial con fuente. En el lenguaje cuantico organiza correladores, lineas internas y amplitudes. Esa continuidad es una de las piezas mas elegantes de la transicion de teoria clasica de campos a QFT.

## 10. Puente hacia el modulo siguiente

En el modulo de interacciones, cada linea interna de un diagrama escalar cargara justamente un factor

$$
\frac{i}{p^2-m^2+i\epsilon}.
$$

Eso significa que el modulo `05` no introduce un objeto completamente nuevo: reutiliza el propagador libre como ladrillo basico para construir amplitudes perturbativas.

En ese sentido, este capitulo es el verdadero puente entre cuantizacion del campo libre y teoria de interaccion: aqui se aprende el primer bloque universal que luego reaparece en casi todos los calculos.

## Cuaderno asociado
- `../../Cuadernos/ejemplos/08_propagador_libre_y_causalidad.ipynb`: usarlo para inspeccionar la estructura del propagador libre, el papel de la prescripcion `i\epsilon` y la diferencia conceptual entre propagador y conmutador causal.
- `../../Cuadernos/ejemplos/05_cuantizacion_del_campo_escalar.ipynb`: usarlo para contrastar la expansion modal con la forma del propagador libre.
- `../../Cuadernos/problemas_resueltos/09_cuantizacion_del_campo_escalar.ipynb`: usarlo para revisar el paso entre conmutadores, vacio y correladores en el caso escalar.

## 12. Advertencias utiles

- El propagador no debe interpretarse como trayectoria clasica de una particula individual.
- La causalidad microfisica se controla con conmutadores locales, no solo inspeccionando correladores.
- El $i\epsilon$ es parte de la definicion fisica del propagador, no un adorno tecnico opcional.

## 13. Preguntas de comprobacion

- Que representa el correlador temporalmente ordenado de dos campos.
- Por que el propagador libre es una funcion de Green.
- Que papel cumple la prescripcion $i\epsilon$.
- Por que no debe confundirse propagador con conmutador causal.

## 14. Referencias y lecturas recomendadas

- Base: Peskin y Schroeder, propagador libre y cuantizacion canonica.
- Complementaria: Tong, presentacion clara de funciones de Green y causalidad.
- Profundizacion: Srednicki, correladores del vacio y estructura del propagador escalar.


---

## Navegacion del tutorial

[(anterior) Cuantizacion Canonica y Espacio de Fock](02_cuantizacion_canonica_y_espacio_de_fock.md) | [(siguiente) Portada 04: Interacciones, Amplitudes y Diagramas de Feynman](../portada_04_interacciones_y_diagramas_de_feynman.md)
