# Gravedad como teoria efectiva

**Nivel:** Avanzado  
**Dificultad:** Alta  
**Tiempo estimado:** 18-25 min  
**Prerequisitos recomendados:** [Euler-Heisenberg y operadores efectivos](03_euler_heisenberg_y_operadores_efectivos.md) · [Resumen del modulo](README.md)


## 1. Proposito

Este documento cierra el modulo mostrando una idea hoy muy extendida: la relatividad general de Einstein puede tratarse como una teoria de campo efectiva perfectamente util a energias muy por debajo de la escala de Planck.

## 2. La tension habitual

En cursos introductorios suele decirse que la gravedad cuantizada perturbativamente "no es renormalizable", y a veces eso se interpreta como si la teoria no sirviera.

La lectura EFT cambia completamente esa intuicion:

- la gravedad no necesita ser una teoria UV completa para producir predicciones IR consistentes;
- basta con reconocer su dominio de validez y organizar las correcciones por escalas.

Este cambio de perspectiva es paralelo al de la teoria de Fermi: una no renormalizabilidad perturbativa no obliga a descartar la teoria, sino a interpretarla correctamente como descripcion efectiva de baja energia.

## 3. Expansion efectiva gravitatoria

La accion efectiva gravitatoria se organiza como una expansion en curvaturas y derivadas:

$$
S_{\mathrm{eff}} =
\int d^4x \sqrt{-g}\left[
\frac{M_{\mathrm{Pl}}^2}{2}R
+ c_1 R^2
+ c_2 R_{\mu\nu}R^{\mu\nu}
+ c_3 R_{\mu\nu\rho\sigma}R^{\mu\nu\rho\sigma}
+ \cdots
\right].
$$

El primer termino domina a bajas energias. Los demas aparecen suprimidos por la escala efectiva relevante, que en el lenguaje mas simple asociamos a la escala de Planck.

La estructura es la misma que en cualquier EFT:

- el operador de menor dimension compatible con simetrias domina;
- los operadores de dimension mayor corrigen sistematicamente la teoria;
- el error de truncar la expansion puede estimarse por potencias de la escala pequeña sobre la grande.

## 4. Que significa esto fisicamente

La teoria de Einstein no desaparece. Al contrario:

- es el termino lider de una expansion muy bien organizada;
- sus correcciones son pequeñas mientras $E \ll M_{\mathrm{Pl}}$;
- la no renormalizabilidad perturbativa solo indica que hara falta nueva fisica o una descripcion UV distinta a energias suficientemente altas.

En particular, esto significa que tiene sentido calcular correcciones cuánticas gravitatorias de baja energia aunque no poseamos aun la teoria final de gravedad cuántica. La predictividad no desaparece: simplemente queda acotada a un dominio.

## 5. Relacion con otros modulos

Este punto conecta muchas piezas del tutorial:

- con renormalizacion: aparecen contraterminos y dependencia con la escala;
- con integral de camino: la accion efectiva organiza la expansion;
- con QFT e informacion: la gravedad semiclasica se usa justamente en un dominio EFT.

Por eso este modulo no es un apendice exotico, sino una forma moderna de releer casi todo el recorrido.

## 6. Expansion alrededor de espacio casi plano

En muchos calculos EFT se escribe el campo gravitatorio como una perturbacion del fondo,

$$
g_{\mu\nu} = \eta_{\mu\nu} + \frac{h_{\mu\nu}}{M_{\mathrm{Pl}}},
$$

y se trata $h_{\mu\nu}$ como el campo cuantizado de espin dos a baja energia. Esta expansion hace visible la analogia con otras teorias de campo:

- el termino de Einstein fija la dinamica lider;
- los terminos de curvatura cuadratica corrigen los vertices;
- la escala de Planck controla la supresion de interacciones gravitatorias.

## 7. Escalas y control

Si los procesos relevantes tienen energia o curvatura muy por debajo de la escala de Planck, la EFT gravitatoria permite:

- calcular correcciones sistematicas;
- separar efectos universales de detalles UV desconocidos;
- mantener control sobre el orden de precision deseado.

Esto es especialmente importante porque en gravedad la escala relevante no siempre se expresa solo como energia de particulas. En muchos problemas tambien importan invariantes de curvatura, radios caracteristicos o escalas termicas. La pregunta correcta no es solo "cuanta energia tiene el proceso", sino "que tan pequeña es la razon entre la escala fisica del problema y la escala de corte gravitatoria".

## 8. Ejemplo corto de lectura

Cuando estudiamos radiacion de Hawking o termicidad cerca de horizontes en un regimen semiclasico, no afirmamos poseer la teoria UV completa de gravedad cuantica. Lo que hacemos es usar una EFT gravitatoria y de campos cuanticos en un dominio donde esa descripcion todavia es fiable.

## 9. Donde deja de servir

La EFT gravitatoria deja de ser suficiente cuando:

- las energias se acercan a la escala de Planck;
- las curvaturas se vuelven comparables a la escala de corte;
- la expansion en operadores deja de converger de forma controlada.

En ese punto no decimos que las predicciones previas fueran falsas, sino que el dominio de validez se ha agotado.

## Cuaderno asociado
- `../../Cuadernos/ejemplos/15_operadores_efectivos_y_power_counting.ipynb`: usarlo para reforzar la idea general de expansion por operadores y jerarquias de escala, que aqui se aplica al caso gravitatorio.

## 11. Advertencias utiles

- Tratar gravedad como EFT no resuelve por si solo la UV completion.
- La escala relevante puede depender del problema fisico, no solo de una cuenta dimensional ingenua.
- La validez de la expansion debe controlarse comparando curvaturas y energias con la escala de corte.

## 12. Preguntas de comprobacion

- Por que una teoria no renormalizable puede seguir siendo predictiva como EFT.
- Que papel juega el termino de Einstein dentro de la expansion efectiva.
- Como conecta esta lectura con gravedad semiclasica y horizonte de Planck.

## 13. Referencias y lecturas recomendadas

- Base: introducciones pedagogicas a gravedad como EFT.
- Complementaria: Donoghue y revisiones sobre gravedad cuantica efectiva.
- Profundizacion: acciones efectivas gravitatorias y correcciones de baja energia.


---

## Navegacion del tutorial

[(anterior) Euler-Heisenberg y operadores efectivos](03_euler_heisenberg_y_operadores_efectivos.md) | [(siguiente) SMEFT y operador de Weinberg](05_smeft_y_operador_de_weinberg.md)