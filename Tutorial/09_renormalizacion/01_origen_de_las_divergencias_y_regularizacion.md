# Origen de las Divergencias y Regularizacion

**Nivel:** Intermedio  
**Dificultad:** Media-Alta  
**Tiempo estimado:** 18-25 min  
**Prerequisitos recomendados:** [Modulo anterior](../08_integral_de_camino/README.md) · [Resumen del modulo](README.md)


## 1. Proposito

Uno de los rasgos mas sorprendentes de la QFT perturbativa es la aparicion de integrales divergentes. Este documento explica de donde salen y por que la regularizacion es el primer paso necesario para tratarlas con cuidado.

La meta no es convertir las divergencias en una rareza algebraica, sino entender que nos dicen sobre la teoria, sus escalas y sus limites de validez.

## 2. Donde aparecen las divergencias

Las divergencias ultravioletas suelen aparecer en diagramas con lazos, donde hay que integrar sobre momentos internos arbitrariamente grandes:

$$
\int \frac{d^4k}{(2\pi)^4}F(k).
$$

Si la funcion $F(k)$ no decrece lo suficiente, la integral diverge.

La intuicion fisica es que los lazos obligan a sumar contribuciones de fluctuaciones cuanticas con todos los momentos internos posibles. La region de gran momento, asociada a distancias muy cortas, es la que suele producir la divergencia ultravioleta.

## 3. Ejemplo orientativo en teoria $\phi^4$

En una teoria con interaccion $\lambda \phi^4$, una correccion de un lazo a la masa conduce a una integral del tipo

$$
I(m) \sim \int \frac{d^4k}{(2\pi)^4}\frac{i}{k^2 - m^2 + i\epsilon}.
$$

Sin entrar aun en todos los pasos tecnicos, esta expresion ya muestra el problema: para momentos muy grandes, el integrando decrece demasiado lentamente y la integral diverge.

Este ejemplo es pedagogicamente importante porque deja ver que:

- la divergencia no aparece en el arbol;
- nace al integrar sobre el momento interno de un lazo;
- el problema esta ligado al comportamiento ultravioleta de la teoria.

## 4. Significado fisico

Estas divergencias no significan simplemente que la teoria sea absurda. Mas bien indican que la teoria explora contribuciones de todas las escalas y que la relacion entre parametros desnudos y observables fisicos es mas sutil de lo que parece a nivel clasico.

Visto de forma moderna, las divergencias son una señal de que estamos intentando describir con un lagrangiano efectivo fluctuaciones de escala arbitrariamente corta. El problema no es solo "infinito matematico", sino como separar de forma consistente fisica a distintas escalas.

## 5. Regularizacion

Regularizar significa introducir un procedimiento temporal que haga finitas las expresiones divergentes. Entre los esquemas mas comunes estan:

- cutoff ultravioleta;
- regularizacion dimensional;
- esquemas con masa auxiliar o reguladores adicionales.

La regularizacion no es todavia la renormalizacion. Es el paso que vuelve las expresiones manipulables y permite identificar con claridad que parte diverge y que parte permanece finita.

## 6. Cutoff ultravioleta

La idea mas intuitiva consiste en cortar la integral a momentos $|k| \lesssim \Lambda$. Entonces $\Lambda$ actua como escala reguladora temporal.

Este metodo es facil de visualizar y muy util para intuicion EFT, porque hace explicita la idea de que no estamos confiando en la teoria por encima de cierta escala. Su inconveniente es que, en algunos contextos, puede ocultar o romper simetrias importantes.

## 7. Regularizacion dimensional

Aqui se continua formalmente el numero de dimensiones a

$$
d = 4 - \varepsilon.
$$

Muchas integrales que divergen en cuatro dimensiones se vuelven finitas para ciertos valores de $d$, y la divergencia reaparece como polos en $1/\varepsilon$ al volver a $d \to 4$.

Este esquema es especialmente valioso porque:

- preserva bien la simetria gauge en muchos contextos;
- organiza las divergencias de forma limpia;
- se ha vuelto lenguaje estandar de gran parte de la QFT moderna.

Para mantener las dimensiones correctas de los acoplamientos suele introducirse una escala auxiliar $\mu$, que anticipa de manera muy natural la dependencia en la escala del grupo de renormalizacion.

## 8. Que debe conservar un buen regulador

Un regulador no es solo un truco para obtener numeros finitos. Idealmente deberia:

- separar con claridad la parte divergente de la finita;
- respetar las simetrias relevantes de la teoria;
- poder retirarse al final del calculo sin dejar residuos espurios en observables.

Esta exigencia explica por que la eleccion del regulador no es inocente. Un regulador mal adaptado puede complicar enormemente el calculo o incluso ocultar la estructura fisica que queremos preservar.

## 9. UV frente a IR

Aunque aqui el foco esta en divergencias ultravioletas, tambien existen divergencias infrarrojas en ciertos contextos, asociadas a momentos pequeños o particulas sin masa. Distinguir ambos tipos desde el principio ayuda a no mezclar problemas conceptualmente distintos.

Las UV hablan de distancias cortas y sensibilidad a altas energias. Las IR hablan de larga distancia, modos blandos o colineales. Ambas requieren cuidado, pero su interpretacion fisica es diferente.

## Cuaderno asociado

- Consulta los cuadernos asociados de este bloque en [Resumen del modulo](README.md) para reforzar el capitulo con practica guiada.

## 10. Preguntas de estudio

- Por que los lazos introducen integrales ultravioletas.
- Que significa regularizar una integral divergente.
- Por que regularizacion y renormalizacion no son exactamente lo mismo.
- Por que la regularizacion dimensional es tan util en teorias gauge.

## 11. Cierre

La regularizacion es el primer gesto de disciplina matematica frente a las divergencias. No resuelve por si sola el problema, pero permite formularlo de manera controlada y preparar el paso decisivo: reinterpretar los parametros de la teoria a traves de la renormalizacion.

## 12. Referencias y lecturas recomendadas

- Base: Tong, secciones introductorias sobre divergencias UV.
- Complementaria: Peskin y Schroeder, primeros ejemplos de regularizacion perturbativa.
- Profundizacion: Zee, discusion conceptual sobre escalas y estructura ultravioleta.


---

## Navegacion del tutorial

[(anterior) Transformaciones de Bogoliubov y Cambio de Vacio](../08_integral_de_camino/04_bogoliubov_y_cambio_de_vacio.md) | [(siguiente) Renormalizacion y Grupo de Renormalizacion](02_renormalizacion_y_grupo_de_renormalizacion.md)