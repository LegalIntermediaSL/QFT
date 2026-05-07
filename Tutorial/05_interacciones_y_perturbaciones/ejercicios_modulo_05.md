# Ejercicios del Modulo 05: Interacciones y Perturbaciones

**Modulo:** 05 — Interacciones y Perturbaciones  
**Nivel:** Nucleo  
**Cuadernos de apoyo:**  
- `../../Cuadernos/problemas_resueltos/10_interacciones_y_perturbaciones.ipynb`  
- `../../Cuadernos/ejemplos/06_diagramas_de_feynman_basicos.ipynb`  
- `../../Cuadernos/problemas_resueltos/12_lsz_y_amplitudes_escalares.ipynb`


## Bloque 1: Verificacion (Nivel 1)

**1.1** La lagrangiana de $\phi^4$ es $\mathcal{L} = \frac{1}{2}(\partial\phi)^2 - \frac{1}{2}m^2\phi^2 - \frac{\lambda}{4!}\phi^4$. Identifica el termino de interaccion y escribe la regla de Feynman del vertice.

**1.2** La matriz $S$ se escribe como $S = \mathbf{1} + iT$ donde $T$ es la amplitud de transicion. Para $2\to2$ scattering, la amplitud invariante $\mathcal{M}$ se define por $\langle f|iT|i\rangle = (2\pi)^4\delta^{(4)}(p_f - p_i)\cdot i\mathcal{M}$. ¿Que expresa la delta de cuatro-momentos?

**1.3** En la teoria de perturbaciones, el potencial de interaccion $V = \frac{\lambda}{4!}\phi^4$ se trata como pequeno. Escribe el operador de dispersion $S$ en la imagen de interaccion a primer orden en $\lambda$.

**1.4** El propagador interno de un campo escalar en un diagrama de Feynman lleva un factor $\frac{i}{p^2 - m^2 + i\epsilon}$. ¿Que significa que el momento $p$ en una linea interna no esta restringido a la capa de masa?

**1.5** Un diagrama de Feynman a orden $\lambda^n$ tiene $n$ vertices. ¿Cuantos vertices tiene el diagrama de arbol de $2\to2$ scattering en $\phi^4$, y cuantos tiene el diagrama de un lazo correspondiente?

---

## Bloque 2: Derivacion guiada (Nivel 2)

**2.1** Expansion de Dyson. La matriz $S$ en la imagen de interaccion es
$$S = T\exp\left(-i\int d^4x\,H_I(x)\right) = \sum_{n=0}^\infty \frac{(-i)^n}{n!}\int d^4x_1\cdots d^4x_n\,T[H_I(x_1)\cdots H_I(x_n)].$$
- (a) Escribe los dos primeros terminos de la expansion.
- (b) Explica el papel del producto ordenado temporalmente $T$.
- (c) Para $H_I = \frac{\lambda}{4!}\phi^4$, identifica el tipo de proceso que aparece a primer orden en $\lambda$ para $2\to2$ scattering.

**2.2** Reglas de Feynman para $\phi^4$. El diagrama de arbol de $2\to2$ scattering tiene un vertice con cuatro patas externas.
- (a) Escribe la amplitud invariante $i\mathcal{M}$ a orden $\lambda$ usando las reglas de Feynman.
- (b) Muestra que $\mathcal{M} = -\lambda$ (no depende de los momentos a este orden).
- (c) Argumenta por que la seccion eficaz total $\sigma \propto |\mathcal{M}|^2$ es proporcional a $\lambda^2$.

**2.3** Reduccion LSZ. El teorema de reduccion LSZ permite obtener amplitudes de dispersion a partir de correladores de campos. Para $2\to2$ scattering:
- (a) Escribe la formula LSZ que relaciona $\langle p_3 p_4|S|p_1 p_2\rangle$ con el correlador de cuatro puntos $\langle 0|T\phi(x_1)\phi(x_2)\phi(x_3)\phi(x_4)|0\rangle$.
- (b) Explica el significado de "amputar" las patas externas.
- (c) Discute como el polo en $p^2 = m^2$ de cada propagador externo garantiza que los estados inicial y final sean particulas en la capa de masa.

---

## Bloque 3: Sintesis (Nivel 3)

**3.1** Teoria de perturbaciones y sus limites. La expansion perturbativa en $\lambda$ solo es valida cuando $\lambda \ll 1$.
- Da un ejemplo de una teoria donde la expansion perturbativa falla: QCD a bajas energias ($\alpha_s \sim 1$).
- Menciona al menos una tecnica no perturbativa: reticulado, dualidades, metodos exactos en 2D.
- Discute como el grupo de renormalizacion puede indicar si la expansion perturbativa es autocongruente a una escala dada.

**3.2** Conecta los diagramas de Feynman con la fisica observable. El diagrama de un lazo en $\phi^4$ a $2\to2$ scattering contribuye a orden $\lambda^2$ y requiere regularizacion.
- Explica que divergencia UV aparece en el calculo del bucle.
- Relaciona este resultado con la necesidad de renormalizacion que se estudiara en el modulo 09.
- Menciona como el grupo de renormalizacion hace fisicamente significativa la dependencia del acoplamiento con la escala de energia.

---

## Soluciones sugeridas (Bloque 1)

**1.1** El termino de interaccion es $-\frac{\lambda}{4!}\phi^4$. La regla de Feynman del vertice es $-i\lambda$ (con el factor $4! = 24$ que cancela las permutaciones de los campos identicos al contraer).

**1.2** La delta $(2\pi)^4\delta^{(4)}(p_f - p_i)$ expresa la conservacion del cuatro-momento total: el momento de los estados finales e iniciales debe coincidir.

**1.3** $S \approx 1 - i\int d^4x\,H_I(x) + \mathcal{O}(\lambda^2)$.

**1.4** Una linea interna de momento $p$ es una particula virtual: no necesita satisfacer $p^2 = m^2$. El momento $p$ se integra sobre todos los valores en los diagramas de lazo.

**1.5** El diagrama de arbol tiene 1 vertice (orden $\lambda$). El diagrama de un lazo tiene 2 vertices (orden $\lambda^2$).

---

## Navegacion del tutorial

[(anterior) Campo Escalar](../04_cuantizacion_del_campo_escalar/README.md) | [(siguiente) Fermiones y Dirac](../06_fermiones_y_dirac/README.md)
