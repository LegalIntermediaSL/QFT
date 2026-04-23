# Fijacion de Gauge y Propagador del Foton

## 1. Proposito

Este documento desarrolla con mas detalle una cuestion central de QED: la redundancia gauge obliga a fijar gauge para definir de manera operativa el propagador del foton y organizar los calculos perturbativos.

## 2. Redundancia gauge

En QED, el potencial electromagnetico $A_\mu$ no representa por si mismo un conjunto minimo de grados de libertad fisicos. Distintas configuraciones relacionadas por una transformacion gauge describen la misma situacion fisica.

Esto significa que el campo tiene mas componentes que grados de libertad propagantes observables.

## 3. Por que hace falta fijar gauge

Si se intenta invertir directamente el operador cinetico del campo gauge sin imponer una condicion adicional, aparece la redundancia gauge como obstaculo tecnico. La fijacion de gauge elimina esa degeneracion y permite definir un propagador.

En la practica se añade un termino de gauge-fixing al lagrangiano. En la familia covariante suele escribirse de forma esquematica como

$$
\mathcal{L}_{\text{gf}} = -\frac{1}{2\xi}(\partial_\mu A^\mu)^2.
$$

## 4. Gauge de Feynman y gauge de Landau

Dos elecciones frecuentes son:

- gauge de Feynman: $\xi = 1$;
- gauge de Landau: $\xi = 0$ en el sentido apropiado del limite.

El gauge de Feynman es especialmente comodo porque simplifica mucho la forma del propagador:

$$
D_{\mu\nu}(k) = \frac{-i\eta_{\mu\nu}}{k^2 + i\epsilon}.
$$

## 5. Grados de libertad fisicos

Aunque el propagador use indices $\mu,\nu$ y parezca tratar cuatro componentes por igual, el foton fisico no propaga cuatro polarizaciones observables independientes. Parte de esa estructura corresponde a la redundancia gauge, no a grados de libertad medibles.

Esta es una leccion importante:

- el formalismo intermedio puede contener redundancias;
- los observables finales deben ser gauge invariantes;
- las cantidades no fisicas desaparecen del resultado final correcto.

## 6. Identidad de Ward

La identidad de Ward es la huella cuantica de la simetria gauge en QED. En lenguaje pedagogico, expresa que:

- la conservacion de la corriente sigue restringiendo las amplitudes;
- no cualquier correccion radiativa es compatible con gauge;
- el formalismo perturbativo hereda restricciones estructurales de la simetria clasica.

No hace falta demostrarla aqui de forma completa, pero si conviene entender su papel: ayuda a garantizar que la renormalizacion de QED no destruya la coherencia gauge de la teoria.

## 7. Ejemplo corto de lectura

Si una amplitud cambia al reemplazar una polarizacion externa del foton por su momento, algo esta mal en la implementacion del calculo. Esa es una forma rapida y muy usada de reconocer la presencia practica de la identidad de Ward.

## 8. Cuaderno asociado

- `../../Cuadernos/problemas_resueltos/13_gauge_fixing_y_scattering_en_qed.ipynb`: usarlo para revisar por que la fijacion de gauge es necesaria y como entra el propagador del foton en una amplitud elemental.
- `../../Cuadernos/ejemplos/06_diagramas_de_feynman_basicos.ipynb`: usarlo como apoyo para repasar propagadores, vertices y estructura de amplitudes elementales.

## 9. Advertencias utiles

- Fijar gauge no significa romper la fisica gauge, sino elegir una descripcion operativa.
- El propagador no debe confundirse con una partícula clásica recorriendo una trayectoria.
- Un resultado intermedio puede depender del gauge; un observable fisico final no deberia hacerlo.

## 10. Preguntas de comprobacion

- Por que la redundancia gauge dificulta invertir el operador cinetico del foton.
- Que papel juega el parametro $\xi$.
- Por que la identidad de Ward importa para la consistencia cuantica de QED.

## 11. Referencias y lecturas recomendadas

- Base: Peskin y Schroeder, gauge-fixing y propagador del foton.
- Complementaria: Tong, notas sobre propagadores gauge e identidad de Ward.
- Profundizacion: Schwartz, tratamiento moderno de gauge y amplitudes en QED.


---

## Navegacion del tutorial

[(anterior) QED y Lagrangiano Fundamental](02_qed_y_lagrangiano_fundamental.md) | [(siguiente) Scattering Basico en QED](04_scattering_basico_en_qed.md)
