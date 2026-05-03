# Ejercicios del Modulo 11: QFT, Informacion y Agujeros Negros

**Modulo:** 11 — QFT, Informacion y Agujeros Negros  
**Nivel:** Avanzado  
**Cuadernos de apoyo:**  
- `../../Cuadernos/ejemplos/08_entrelazamiento_y_horizontes.ipynb`  
- `../../Cuadernos/ejemplos/12_unruh_hawking_y_curva_de_page.ipynb`  
- `../../Cuadernos/problemas_resueltos/20_islas_y_entropia_generalizada.ipynb`  
- `../../Cuadernos/problemas_resueltos/22_holografia_y_reconstruccion_de_informacion.ipynb`


## Bloque 1: Verificacion (Nivel 1)

**1.1** La entropia de entrelazamiento de un sistema bipartito $AB$ es $S_A = -\text{Tr}(\rho_A\ln\rho_A)$ donde $\rho_A = \text{Tr}_B|\psi\rangle\langle\psi|$. Calcula $S_A$ para el estado de Bell $|\psi\rangle = (|00\rangle + |11\rangle)/\sqrt{2}$ y verifica que alcanza el valor maximo $\ln 2$ para un sistema de un qubit.

**1.2** La temperatura de Hawking de un agujero negro de masa $M$ es $T_H = 1/(8\pi G M)$ (en unidades naturales $\hbar=c=k_B=1$). Para un agujero negro de masa estelar $M\sim 3M_\odot\approx 6\times 10^{30}$ kg, calcula $T_H$ y compara con la temperatura del fondo cosmico de microondas $T_{\text{CMB}}\approx 2.7$ K. Comenta si ese agujero negro absorbe o emite radiacion neta en el universo actual.

**1.3** El tiempo de evaporacion de un agujero negro por radiacion de Hawking escala como $t_{\text{evap}}\sim G^2M^3/(\hbar c^4)$. Escribe esta expresion en terminos de la masa de Planck $M_{\text{Pl}} = \sqrt{\hbar c/G}$ y la escala de Planck $t_{\text{Pl}} = \sqrt{\hbar G/c^5}$, y verifica las dimensiones.

**1.4** La curva de Page describe la evolucion de la entropia de la radiacion emitida por un agujero negro. Describe cualitativamente las tres fases: (a) fase inicial (entropia crece), (b) tiempo de Page (entropia maxima), y (c) fase final (entropia decrece). Explica por que la fase (c) es necesaria para la unitaridad de la evolucion cuantica.

**1.5** La formula de la entropia generalizada en el formalismo de islas es:
$$S_{\text{gen}} = \frac{\text{Area}(\partial I)}{4G\hbar} + S_{\text{QFT}}(R\cup I),$$
donde $I$ es la isla y $R$ la region de radiacion. Explica en palabras el significado de cada termino y por que la inclusion de la isla resuelve el problema de la curva de Page.

---

## Bloque 2: Derivacion guiada (Nivel 2)

**2.1** Efecto Unruh y temperatura. Un observador con aceleracion propia $a$ ve el vacio de Minkowski como un estado termico con temperatura $T_U = a/(2\pi)$ (en unidades $\hbar=c=k_B=1$).
- (a) Escribe la metrica de Rindler en coordenadas del observador acelerado y identifica el horizonte de Rindler.
- (b) Explica por que el campo cuantico en el vacio de Minkowski, restringido a la cuña de Rindler, tiene una densidad matricial termica.
- (c) Calcula la aceleracion necesaria para detectar una temperatura de $1$ K y compara con aceleraciones tipicas de laboratorio.

**2.2** Paradoja de la informacion y sus posibles resoluciones. Un agujero negro formado en un estado puro $|\psi\rangle$ emite radiacion de Hawking que parece termica (estado mixto), violando la unitaridad.
- (a) Enuncia claramente la paradoja: que se conserva en QFT vs que predice la relatividad general semiclasica.
- (b) Describe brevemente tres propuestas de resolucion: complementariedad, remnants, e islas/Page curve unitaria.
- (c) Señala que evidencias empiricas o calculables distinguen entre estas propuestas.

**2.3** Holografia y reconstruccion de informacion. La correspondencia AdS/CFT propone que una teoria gravitacional en un espacio AdS$_{d+1}$ es dual a una CFT en su borde $d$-dimensional.
- (a) Explica el significado fisico del diccionario GKPW: $Z_{\text{gravity}}[J] = Z_{\text{CFT}}[J]$.
- (b) Describe como la reconstruccion de operadores del bulk a partir de la frontera (HKLL) esta relacionada con la codificacion cuantica de errores.
- (c) Explica por que la subregion dualidad (subalgebra de operadores del bulk reconstruible desde una subregion del borde) conecta con la entropia de entrelazamiento via la formula RT.

---

## Bloque 3: Sintesis (Nivel 3)

**3.1** Conecta los modulos 08 y 11. La transformacion de Bogoliubov del modulo 08 es el mecanismo matematico comun al efecto Unruh y la radiacion de Hawking. Para el efecto Unruh:
- Muestra que el numero medio de particulas de Rindler en el vacio de Minkowski es $\langle n_\omega\rangle = 1/(e^{2\pi\omega/a}-1)$.
- Identifica que esta es una distribucion de Bose-Einstein con temperatura $T_U = a/(2\pi)$.
- Generaliza el argumento para el caso del agujero negro (temperatura de Hawking) y señala la analogia formal.

**3.2** Entropia de entrelazamiento y area. La formula de Bekenstein-Hawking $S_{BH} = A/(4G\hbar)$ conecta geometria y entropia cuantica.
- Explica por que la entropia de entrelazamiento de campos cuanticos en el vacio diverge en el UV y como se regulariza.
- Discute la hipotesis de que la entropia de Bekenstein-Hawking tiene origen en el entrelazamiento cuantico del campo cruzando el horizonte.
- Conecta con la formula de Ryu-Takayanagi $S_A = \text{Area}(\gamma_A)/(4G)$ en holografia.

---

## Soluciones sugeridas (Bloque 1)

**1.1** $\rho_A = \frac{1}{2}\begin{pmatrix}1&0\\0&1\end{pmatrix}$. $S_A = -\text{Tr}(\rho_A\ln\rho_A) = -2\cdot\frac{1}{2}\ln\frac{1}{2} = \ln 2$.

**1.2** $T_H = \hbar c^3/(8\pi G M k_B)\approx 6\times 10^{-8}$ K $\ll T_{\text{CMB}}$: el agujero negro absorbe mas de lo que emite y no se evapora en el universo actual.

**1.3** $t_{\text{evap}}\sim (M/M_{\text{Pl}})^3 t_{\text{Pl}}$. Para $M=M_{\text{Pl}}$: $t_{\text{evap}}\sim t_{\text{Pl}}\sim 5\times 10^{-44}$ s.

**1.4** (a) Entropia de la radiacion crece porque hay poca correlacion con el agujero negro. (b) En el tiempo de Page, la entropia de la radiacion alcanza $S_{BH}/2$: mitad de la informacion ha salido. (c) La entropia debe decrecer para volver a cero cuando el agujero negro se evapora completamente, coherente con la unitaridad.

**1.5** Primer termino: contribucion gravitacional (area del borde de la isla). Segundo termino: entropia cuantica de campos en la union de isla y region de radiacion. La isla contributions permiten que $S_{\text{gen}}$ siga la curva de Page en lugar de crecer indefinidamente.


---

## Navegacion del tutorial

[(anterior) Holografia y Reconstruccion de Informacion](06_holografia_y_reconstruccion_de_informacion.md) | [(siguiente) Teorias de Campo Efectivas](../12_teorias_de_campo_efectivas/README.md)
