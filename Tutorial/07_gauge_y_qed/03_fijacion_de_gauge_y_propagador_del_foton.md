# Fijacion de Gauge y Propagador del Foton

**Nivel:** Nucleo  
**Dificultad:** Media-Alta  
**Tiempo estimado:** 18-25 min  
**Prerequisitos recomendados:** [QED y Lagrangiano Fundamental](02_qed_y_lagrangiano_fundamental.md) · [Resumen del modulo](README.md)


## 1. Proposito

Este documento desarrolla con mas detalle una cuestion central de QED: la redundancia gauge obliga a fijar gauge para definir de manera operativa el propagador del foton y organizar los calculos perturbativos.

Es un ejemplo muy valioso porque muestra una leccion general de QFT: el formalismo puede contener redundancias intermedias, pero los observables fisicos deben ser independientes de ellas.

## 2. Redundancia gauge

En QED, el potencial electromagnetico $A_\mu$ no representa por si mismo un conjunto minimo de grados de libertad fisicos. Distintas configuraciones relacionadas por una transformacion gauge describen la misma situacion fisica.

Esto significa que el campo tiene mas componentes que grados de libertad propagantes observables. En particular, un foton sin masa tiene dos polarizaciones fisicas transversas, mientras que el potencial $A_\mu$ parece introducir cuatro componentes. Esa diferencia es precisamente la huella de la redundancia gauge.

## 3. Por que hace falta fijar gauge

Si se intenta invertir directamente el operador cinetico del campo gauge sin imponer una condicion adicional, aparece la redundancia gauge como obstaculo tecnico. La fijacion de gauge elimina esa degeneracion y permite definir un propagador.

En la practica se añade un termino de gauge-fixing al lagrangiano. En la familia covariante suele escribirse de forma esquematica como

$$
\mathcal{L}_{\text{gf}} = -\frac{1}{2\xi}(\partial_\mu A^\mu)^2.
$$

Este termino no introduce nueva fisica observable. Su papel es hacer invertible el operador cinetico en el espacio de campos y permitir que el propagador quede bien definido dentro del calculo perturbativo.

## 4. Gauge de Feynman y gauge de Landau

Dos elecciones frecuentes son:

- gauge de Feynman: $\xi = 1$;
- gauge de Landau: $\xi = 0$ en el sentido apropiado del limite.

El gauge de Feynman es especialmente comodo porque simplifica mucho la forma del propagador:

$$
D_{\mu\nu}(k) = \frac{-i\eta_{\mu\nu}}{k^2 + i\epsilon}.
$$

En una gauge covariante general, la expresion toma la forma

$$
D_{\mu\nu}(k)=\frac{-i}{k^2+i\epsilon}\left[\eta_{\mu\nu}-(1-\xi)\frac{k_\mu k_\nu}{k^2}\right].
$$

Esto hace visible que distintas elecciones de $\xi$ reorganizan la parte longitudinal del propagador sin modificar los observables fisicos finales.

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

En la practica, la identidad de Ward asegura cancelaciones cruciales entre distintas piezas de una amplitud o de una correccion radiativa. Es una de las razones por las que QED mantiene una consistencia tan fina a nivel cuantico.

## 7. Ejemplo corto de lectura

Si una amplitud cambia al reemplazar una polarizacion externa del foton por su momento, algo esta mal en la implementacion del calculo. Esa es una forma rapida y muy usada de reconocer la presencia practica de la identidad de Ward.

Este test operativo no sustituye una demostracion formal, pero sirve como verificacion inmediata de que el calculo no esta violando la estructura gauge de la teoria.

## Cuaderno asociado
- `../../Cuadernos/problemas_resueltos/13_gauge_fixing_y_scattering_en_qed.ipynb`: usarlo para revisar por que la fijacion de gauge es necesaria y como entra el propagador del foton en una amplitud elemental.
- `../../Cuadernos/ejemplos/06_diagramas_de_feynman_basicos.ipynb`: usarlo como apoyo para repasar propagadores, vertices y estructura de amplitudes elementales.

## 9. Advertencias utiles

- Fijar gauge no significa romper la fisica gauge, sino elegir una descripcion operativa.
- El propagador no debe confundirse con una particula clasica recorriendo una trayectoria.
- Un resultado intermedio puede depender del gauge; un observable fisico final no deberia hacerlo.
- Los grados de libertad no fisicos pueden aparecer en el calculo sin que eso implique una contradiccion.

## 10. Preguntas de comprobacion

- Por que la redundancia gauge dificulta invertir el operador cinetico del foton.
- Que papel juega el parametro $\xi$.
- Por que la identidad de Ward importa para la consistencia cuantica de QED.

## Ejercicios sugeridos

1. Explicar por que la simetria gauge introduce una redundancia que debe tratarse antes de calcular propagadores.
2. Describir el significado operativo del parametro de gauge $\xi$ y por que no debe afectar observables fisicos.
3. Relacionar fijacion de gauge, propagador del foton e identidad de Ward en una sola cadena conceptual.

## 11. Cierre

La fijacion de gauge es uno de los mejores ejemplos de una idea general de QFT: a veces el formalismo necesita introducir elecciones auxiliares para poder calcular, pero la fisica final debe ser independiente de ellas. En QED, esta leccion se vuelve visible en la definicion del propagador del foton y en el papel protector de la identidad de Ward.

## 12. Referencias y lecturas recomendadas

- Base: Peskin y Schroeder, gauge-fixing y propagador del foton.
- Complementaria: Tong, notas sobre propagadores gauge e identidad de Ward.
- Profundizacion: Schwartz, tratamiento moderno de gauge y amplitudes en QED.


---

## Navegacion del tutorial

[(anterior) QED y Lagrangiano Fundamental](02_qed_y_lagrangiano_fundamental.md) | [(siguiente) Scattering Basico en QED](04_scattering_basico_en_qed.md)
