# Origen de las Divergencias y Regularizacion

## 1. Proposito

Uno de los rasgos mas sorprendentes de la QFT perturbativa es la aparicion de integrales divergentes. Este documento explica de donde salen y por que la regularizacion es el primer paso necesario para tratarlas con cuidado.

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

## 5. Regularizacion

Regularizar significa introducir un procedimiento temporal que haga finitas las expresiones divergentes. Entre los esquemas mas comunes estan:

- cutoff ultravioleta;
- regularizacion dimensional;
- esquemas con masa auxiliar o reguladores adicionales.

La regularizacion no es todavia la renormalizacion. Es el paso que vuelve las expresiones manipulables.

### Cutoff ultravioleta

La idea mas intuitiva consiste en cortar la integral a momentos $|k| \lesssim \Lambda$. Entonces $\Lambda$ actua como escala reguladora temporal. Este metodo es facil de visualizar, aunque a veces puede ocultar o romper simetrias.

### Regularizacion dimensional

Aqui se continua formalmente el numero de dimensiones a

$$
d = 4 - \varepsilon.
$$

Muchas integrales que divergen en cuatro dimensiones se vuelven finitas para ciertos valores de $d$, y la divergencia reaparece como polos en $1/\varepsilon$ al volver a $d \to 4$.

Este esquema es especialmente valioso porque:

- preserva bien la simetria gauge en muchos contextos;
- organiza las divergencias de forma limpia;
- se ha vuelto lenguaje estandar de gran parte de la QFT moderna.

## 6. Que debe conservar un buen regulador

Un regulador no es solo un truco para obtener numeros finitos. Idealmente deberia:

- separar con claridad la parte divergente de la finita;
- respetar las simetrias relevantes de la teoria;
- poder retirarse al final del calculo sin dejar residuos espurios en observables.

## 7. Preguntas de estudio

- Por que los lazos introducen integrales ultravioletas.
- Que significa regularizar una integral divergente.
- Por que regularizacion y renormalizacion no son exactamente lo mismo.
- Por que la regularizacion dimensional es tan util en teorias gauge.

## 8. Cierre

La regularizacion es el primer gesto de disciplina matematica frente a las divergencias. No resuelve por si sola el problema, pero permite formularlo de manera controlada.

## 9. Referencias y lecturas recomendadas

- Base: Tong, secciones introductorias sobre divergencias UV.
- Complementaria: Peskin y Schroeder, primeros ejemplos de regularizacion perturbativa.
- Profundizacion: Zee, discusion conceptual sobre escalas y estructura ultravioleta.


---

## Navegacion del tutorial

[(anterior) Transformaciones de Bogoliubov y Cambio de Vacio](../08_integral_de_camino/04_bogoliubov_y_cambio_de_vacio.md) | [(siguiente) Renormalizacion y Grupo de Renormalizacion](02_renormalizacion_y_grupo_de_renormalizacion.md)
