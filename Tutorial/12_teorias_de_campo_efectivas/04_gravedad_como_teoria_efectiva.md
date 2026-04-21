# Gravedad como teoria efectiva

## 1. Proposito

Este documento cierra el modulo mostrando una idea hoy muy extendida: la relatividad general de Einstein puede tratarse como una teoria de campo efectiva perfectamente util a energias muy por debajo de la escala de Planck.

## 2. La tension habitual

En cursos introductorios suele decirse que la gravedad cuantizada perturbativamente "no es renormalizable", y a veces eso se interpreta como si la teoria no sirviera.

La lectura EFT cambia completamente esa intuicion:

- la gravedad no necesita ser una teoria UV completa para producir predicciones IR consistentes;
- basta con reconocer su dominio de validez y organizar las correcciones por escalas.

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

## 4. Que significa esto fisicamente

La teoria de Einstein no desaparece. Al contrario:

- es el termino lider de una expansion muy bien organizada;
- sus correcciones son pequeñas mientras $E \ll M_{\mathrm{Pl}}$;
- la no renormalizabilidad perturbativa solo indica que hara falta nueva fisica o una descripcion UV distinta a energias suficientemente altas.

## 5. Relacion con otros modulos

Este punto conecta muchas piezas del tutorial:

- con renormalizacion: aparecen contraterminos y dependencia con la escala;
- con integral de camino: la accion efectiva organiza la expansion;
- con QFT e informacion: la gravedad semiclasica se usa justamente en un dominio EFT.

Por eso este modulo no es un apendice exotico, sino una forma moderna de releer casi todo el recorrido.

## 6. Escalas y control

Si los procesos relevantes tienen energia o curvatura muy por debajo de la escala de Planck, la EFT gravitatoria permite:

- calcular correcciones sistematicas;
- separar efectos universales de detalles UV desconocidos;
- mantener control sobre el orden de precision deseado.

## 7. Ejemplo corto de lectura

Cuando estudiamos radiacion de Hawking o termicidad cerca de horizontes en un regimen semiclasico, no afirmamos poseer la teoria UV completa de gravedad cuantica. Lo que hacemos es usar una EFT gravitatoria y de campos cuanticos en un dominio donde esa descripcion todavia es fiable.

## 8. Cuaderno asociado

- `../../Cuadernos/ejemplos/15_operadores_efectivos_y_power_counting.ipynb`: usarlo para reforzar la idea general de expansion por operadores y jerarquias de escala, que aqui se aplica al caso gravitatorio.

## 9. Advertencias utiles

- Tratar gravedad como EFT no resuelve por si solo la UV completion.
- La escala relevante puede depender del problema fisico, no solo de una cuenta dimensional ingenua.
- La validez de la expansion debe controlarse comparando curvaturas y energias con la escala de corte.

## 10. Preguntas de comprobacion

- Por que una teoria no renormalizable puede seguir siendo predictiva como EFT.
- Que papel juega el termino de Einstein dentro de la expansion efectiva.
- Como conecta esta lectura con gravedad semiclasica y horizonte de Planck.

## 11. Referencias y lecturas recomendadas

- Base: introducciones pedagogicas a gravedad como EFT.
- Complementaria: Donoghue y revisiones sobre gravedad cuantica efectiva.
- Profundizacion: acciones efectivas gravitatorias y correcciones de baja energia.


---

## Navegacion del tutorial

[(anterior) Euler-Heisenberg y operadores efectivos](03_euler_heisenberg_y_operadores_efectivos.md) | [(siguiente) SMEFT y operador de Weinberg](05_smeft_y_operador_de_weinberg.md)
