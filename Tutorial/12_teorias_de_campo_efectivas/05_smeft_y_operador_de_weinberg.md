# SMEFT y operador de Weinberg

## 1. Proposito

Este documento abre la capa avanzada del modulo 12 mostrando como el propio Modelo Estandar puede verse como el termino lider de una expansion efectiva mas amplia: la SMEFT, o Standard Model Effective Field Theory.

## 2. Del Modelo Estandar a su expansion efectiva

Si la nueva fisica vive a una escala $\Lambda$ mayor que las energias exploradas, la descripcion natural es

$$
\mathcal{L}_{\mathrm{SMEFT}}
= \mathcal{L}_{\mathrm{SM}}
+ \frac{1}{\Lambda} \sum_i c_i^{(5)} \mathcal{O}_i^{(5)}
+ \frac{1}{\Lambda^2} \sum_j c_j^{(6)} \mathcal{O}_j^{(6)}
+ \cdots
$$

La logica es exactamente la misma que en cualquier EFT:

- el Modelo Estandar aparece como termino dominante;
- los operadores de mayor dimension codifican efectos UV;
- las simetrias gauge del Modelo Estandar restringen fuertemente que operadores son posibles.

## 3. Por que SMEFT importa

SMEFT permite hablar de nueva fisica sin comprometerse inmediatamente con una UV completion concreta.

Eso la vuelve muy util para:

- organizar desviaciones pequenas en observables;
- comparar experimentos distintos en un lenguaje comun;
- conectar precision electrodébil, Higgs, sabor y neutrinos.

## 4. El operador de Weinberg

El operador mas celebre de dimension cinco en SMEFT es

$$
\mathcal{O}_W \sim (L H)(L H),
$$

donde $L$ es el doblete leptónico izquierdo y $H$ el campo de Higgs.

Tras la ruptura espontanea, cuando el Higgs adquiere valor esperado $v$, este operador genera una masa efectiva para neutrinos:

$$
m_\nu \sim \frac{v^2}{\Lambda}.
$$

Esto lo convierte en un caso excepcionalmente interesante:

- es el operador de menor dimension mas alla del Modelo Estandar;
- viola numero leptónico en dos unidades;
- sugiere de forma natural masas de Majorana para neutrinos.

## 5. Dimension cinco vs dimension seis

En SMEFT, los operadores de dimension seis suelen corregir:

- acoplamientos gauge;
- interacciones de Higgs;
- corrientes fermionicas;
- procesos de cuatro fermiones.

El operador de Weinberg destaca porque aparece ya en dimension cinco, es decir, con una supresion menos severa que muchos otros efectos UV posibles.

## 6. Lectura fisica

La leccion profunda es que la pequeñez de las masas de neutrinos puede no ser un accidente extraño, sino la huella efectiva de una escala muy alta donde vive nueva fisica que rompe numero leptónico.

## 7. Ejemplo corto de lectura

Si $v \approx 246\,\mathrm{GeV}$ y la escala efectiva asociada al operador de Weinberg es muy grande, entonces el cociente $v^2/\Lambda$ puede producir masas neutrínicas muy pequeñas de forma natural. Esa simple cuenta dimensional ya da una intuicion poderosa de por que SMEFT es tan útil.

## 8. Cuaderno asociado

- `../../Cuadernos/ejemplos/18_smeft_y_operador_de_weinberg.ipynb`: usarlo para fijar la expansion de SMEFT, la posicion especial del operador de dimension cinco y la escala efectiva de masas de neutrinos.

## 9. Advertencias utiles

- SMEFT no es una UV completion; es un lenguaje intermedio organizado por simetrias y escalas.
- El operador de Weinberg no dice por si solo cual es la teoria UV responsable.
- Elegir una base completa de operadores de dimension seis es una tarea tecnica mas rica que lo presentado aqui.

## 10. Preguntas de comprobacion

- Por que el Modelo Estandar puede verse como el termino lider de SMEFT.
- Que hace especial al operador de Weinberg dentro de la expansion.
- Como aparece la estimacion $m_\nu \sim v^2/\Lambda$.

## 11. Referencias y lecturas recomendadas

- Base: reseñas pedagogicas de SMEFT y precision electrodébil.
- Complementaria: revisiones sobre el operador de Weinberg y neutrinos efectivos.
- Profundizacion: bases operatoriales de Warsaw y analisis fenomenologicos modernos.


---

## Navegacion del tutorial

[(anterior) Gravedad como teoria efectiva](04_gravedad_como_teoria_efectiva.md) | [(siguiente) Majorana y mecanismo seesaw](06_majorana_y_mecanismo_seesaw.md)
