# Cuantizacion Canonica y Espacio de Fock

**Nivel:** Nucleo  
**Dificultad:** Media  
**Tiempo estimado:** 25-35 min  
**Prerequisitos recomendados:** [Campo Escalar Clasico y Modos Normales](01_campo_escalar_clasico_y_modos_normales.md) · [Resumen del modulo](README.md)

## Proposito

Este capitulo desarrolla la cuantizacion canonica del campo escalar y explica como emerge el espacio de Fock como lenguaje natural para una teoria con numero variable de particulas.

## 1. Introduccion

La cuantizacion canonica del campo escalar muestra de forma explicita como aparece una teoria con numero variable de particulas. Es uno de los puntos donde la QFT cambia de lenguaje de manera mas visible.

## 2. Reglas canonicas a tiempo igual

Partimos del par canonico $(\phi,\pi)$ y lo promovemos a operadores con relaciones de conmutacion

$$
[\phi(t,\mathbf x),\pi(t,\mathbf y)] = i\delta^{(3)}(\mathbf x-\mathbf y),
$$

$$
[\phi(t,\mathbf x),\phi(t,\mathbf y)] = 0,
\qquad
[\pi(t,\mathbf x),\pi(t,\mathbf y)] = 0.
$$

Estas relaciones son la version de campo de $[q,p]=i$.

La expresion "a tiempo igual" importa. Significa que imponemos la estructura cuantica sobre una hipersuperficie espacial fija y dejamos que la dinamica describa la evolucion temporal posterior. Asi se hace visible el parentesco directo con la mecanica hamiltoniana ordinaria.

## 3. Expansion operatorial

La expansion en modos del campo cuantizado toma la forma

$$
\phi(x)=\int \frac{d^3p}{(2\pi)^3}\frac{1}{\sqrt{2E_{\mathbf p}}}
\left(a(\mathbf p)e^{-ip\cdot x}+a^\dagger(\mathbf p)e^{ip\cdot x}\right).
$$

Los objetos $a(\mathbf p)$ y $a^\dagger(\mathbf p)$ ya no son numeros, sino operadores.

La relacion relativista

$$
E_{\mathbf p} = \sqrt{\mathbf p^2 + m^2}
$$

ya esta incorporada en esta expansion. No estamos sumando modos arbitrarios, sino soluciones libres con la dispersion correcta. Ademas, la presencia simultanea de exponentes positivos y negativos muestra que un campo hermitico contiene partes que crean y destruyen excitaciones.

## 4. Algebra de creacion y aniquilacion

Las relaciones canonicas implican

$$
[a(\mathbf p),a^\dagger(\mathbf q)] = (2\pi)^3\delta^{(3)}(\mathbf p-\mathbf q),
$$

conmutando entre si los pares $a$ con $a$ y $a^\dagger$ con $a^\dagger$.

Esto generaliza el algebra del oscilador armonico al continuo de momentos.

La delta de Dirac ocupa aqui el papel que antes jugaba la unidad en el oscilador discreto. La interpretacion es simple: no hay un solo oscilador, sino un continuo de osciladores independientes etiquetados por $\mathbf p$.

## 5. Estado de vacio

Se define el vacio $|0\rangle$ como el estado aniquilado por todos los operadores $a(\mathbf p)$:

$$
a(\mathbf p)|0\rangle = 0
\qquad
\text{para todo } \mathbf p.
$$

Este estado no debe pensarse como "la nada", sino como el estado base respecto del cual se construyen todas las excitaciones.

Mas adelante esta idea se volvera aun mas interesante, porque la nocion de vacio puede depender de la descomposicion en modos considerada. Aqui basta con retener que el vacio es un estado fisico del espacio de Fock, no una ausencia metafisica de todo contenido.

## 6. Estados de una y muchas particulas

Aplicando un operador de creacion al vacio obtenemos un estado de una particula:

$$
|\mathbf p\rangle = a^\dagger(\mathbf p)|0\rangle.
$$

Aplicando varios operadores de creacion construimos estados multiparticle:

$$
|\mathbf p_1,\mathbf p_2,\ldots,\mathbf p_n\rangle
= a^\dagger(\mathbf p_1)a^\dagger(\mathbf p_2)\cdots a^\dagger(\mathbf p_n)|0\rangle.
$$

El conjunto de todos esos sectores forma el espacio de Fock.

Una forma util de escribirlo es

$$
\mathcal{F} = \mathbb{C} \oplus \mathcal{H}_1 \oplus \mathcal{H}_2 \oplus \cdots,
$$

donde $\mathbb{C}$ representa el sector de vacio y $\mathcal{H}_n$ el sector de $n$ particulas. Esta suma directa es justo la estructura que permite que el numero de particulas cambie.

## 7. Interpretacion bosonica

Como estamos cuantizando un campo escalar, las excitaciones obedecen estadistica bosonica. Eso se refleja en el hecho de que los operadores de creacion conmutan entre si. La simetrizacion de los estados no es un detalle externo; esta codificada en el algebra misma.

Por ejemplo, intercambiar dos momentos no cambia un estado bosonico de dos particulas:

$$
a^\dagger(\mathbf p_1)a^\dagger(\mathbf p_2)|0\rangle
=
a^\dagger(\mathbf p_2)a^\dagger(\mathbf p_1)|0\rangle.
$$

## 8. Hamiltoniano en terminos modales

El hamiltoniano puede reescribirse como suma continua de osciladores:

$$
H = \int \frac{d^3p}{(2\pi)^3} E_{\mathbf p}
\left(a^\dagger(\mathbf p)a(\mathbf p) + \frac{1}{2}[a(\mathbf p),a^\dagger(\mathbf p)]\right).
$$

La primera parte cuenta excitaciones; la segunda sugiere la energia de punto cero del vacio. En muchos tratamientos introductorios se reordena normalmente el hamiltoniano para centrarse en diferencias de energia fisicamente relevantes.

Ese reordenamiento normal es util, pero no debe ocultar la leccion conceptual: el vacio cuantico ya trae una estructura energetica propia incluso en la teoria libre.

## 9. Operadores de campo y observables

Un operador de campo local no "es" una particula individual. Mas bien actua como objeto capaz de crear o destruir componentes del estado en un punto del espacio-tiempo. Esta es una sutileza importante:

- los operadores $a^\dagger$ crean excitaciones de momento bien definido;
- los campos $\phi(x)$ son superposiciones locales de creacion y aniquilacion;
- los observables fisicos suelen organizarse en correladores y elementos de matriz.

Esto evita una confusion frecuente: el campo cuantico no es simplemente una funcion de onda relativista. Es un operador que actua sobre todo el espacio de Fock y puede conectar sectores con distinto numero de particulas.

## 10. Por que esto resuelve el problema del numero variable de particulas

La respuesta corta es que el espacio de Fock ya contiene sectores con todos los numeros posibles de excitaciones. Una teoria relativista cuantica puede entonces describir:

- procesos sin particulas iniciales o finales;
- estados de una particula;
- colisiones de muchas particulas;
- amplitudes entre sectores de ocupacion diferentes.

La arquitectura que faltaba en la mecanica cuantica de una sola particula aparece aqui de forma natural.

Esa es una de las victorias conceptuales mas limpias de la QFT. No forzamos procesos de creacion y aniquilacion dentro de un formalismo inadecuado: trabajamos directamente en un espacio de estados donde tales procesos tienen cabida desde el principio.

## 11. Advertencias utiles
- El vacio cuantico no es un objeto clasico vacio de contenido.
- Los operadores de creacion y aniquilacion no describen mecanismos mecanicos literales.
- Un campo cuantico no es una "onda de probabilidad" de una particula unica.
- La expansion modal no es una aproximacion; para la teoria libre es una descomposicion estructural exacta.
- La interpretacion en terminos de particulas es especialmente clara en teorias libres o en estados asintoticos.

## Cuaderno asociado

- Consulta los cuadernos asociados de este bloque en [Resumen del modulo](README.md) para reforzar el capitulo con practica guiada.

## 12. Preguntas de comprobacion
- Como se pasa de las relaciones canonicas del campo al algebra de los operadores modales.
- Que es exactamente el espacio de Fock.
- Por que el vacio es el estado base y no la ausencia trivial de todo.
- En que sentido una particula es una excitacion del campo.

## 13. Ejercicios sugeridos

1. Explicar como la promocion de coeficientes modales a operadores permite describir numero variable de particulas.
2. Justificar por que el vacio de Fock no debe confundirse con un vacio clasico sin estructura.
3. Describir la diferencia entre un operador de creacion de momento definido y el campo local $\phi(x)$.

## 14. Cierre

La cuantizacion canonica del campo escalar hace visible la logica profunda de la QFT: no cuantizamos particulas individuales para luego permitir que aparezcan mas, sino que cuantizamos campos cuyos modos admiten excitaciones discretas. Esas excitaciones son las particulas.

Este capitulo es el puente natural entre el oscilador armonico cuantico y la teoria de scattering. Una vez entendido, reglas de Feynman, correladores y amplitudes dejan de parecer piezas separadas.

## 15. Referencias y lecturas recomendadas

- Base: Peskin y Schroeder, cuantizacion canonica del campo escalar.
- Complementaria: Srednicki, espacio de Fock y operadores modales.
- Profundizacion: Tong, presentacion pedagogica del vacio y de las excitaciones del campo.


---

## Navegacion del tutorial

[(anterior) Campo Escalar Clasico y Modos Normales](01_campo_escalar_clasico_y_modos_normales.md) | [(siguiente) Propagador, Causalidad y Funcion de Green](03_propagador_causalidad_y_funcion_de_green.md)
