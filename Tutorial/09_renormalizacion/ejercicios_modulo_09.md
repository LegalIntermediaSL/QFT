# Ejercicios del Modulo 09: Renormalizacion

**Modulo:** 09 — Renormalizacion  
**Nivel:** Intermedio  
**Cuadernos de apoyo:**  
- `../../Cuadernos/problemas_resueltos/15_regularizacion_dimensional_y_running.ipynb`  
- `../../Cuadernos/ejemplos/17_esquema_msbar_y_qed_vs_qcd.ipynb`


## Bloque 1: Verificacion (Nivel 1)

**1.1** El grado superficial de divergencia de un diagrama en $\phi^4$ en $d=4$ es $D = 4 - E$, donde $E$ es el numero de patas externas. Calcula $D$ para los diagramas con $E=2$ (autoenergia), $E=4$ (vertice de cuatro puntos) y $E=6$. Clasifica cada caso como divergente, logaritmicamente divergente o convergente.

**1.2** La regularizacion dimensional reemplaza $d=4$ por $d=4-\varepsilon$. Una integral tipica de loop produce polos en $\varepsilon$:
$$\int\frac{d^dk}{(2\pi)^d}\frac{1}{(k^2+\Delta)^2} = \frac{i}{(4\pi)^2}\left(\frac{2}{\varepsilon} - \ln\Delta + \text{finito}\right).$$
Verifica las dimensiones de masa de ambos lados si se introduce el parametro de escala $\mu^{4-d}$ para mantener la accion adimensional.

**1.3** La ecuacion del grupo de renormalizacion para la masa en $\phi^4$ es:
$$\mu\frac{dm^2}{d\mu} = \gamma_m\cdot m^2, \qquad \gamma_m = \frac{\lambda}{16\pi^2}.$$
Resuelve esta ecuacion y describe como evoluciona $m^2(\mu)$ al aumentar $\mu$. Comenta la relacion con el problema de la jerarquia.

**1.4** La funcion beta de QCD es $\beta(g) = -\frac{g^3}{16\pi^2}\left(\frac{11}{3}C_A - \frac{4}{3}T_F n_f\right)$ con $C_A=3$, $T_F=1/2$, y $n_f$ sabores activos. Para $n_f=6$: calcula el coeficiente y determina su signo. Explica que implica ese signo para el comportamiento de $\alpha_s(Q)$.

**1.5** El esquema $\overline{\text{MS}}$ define los contraterminos de manera que absorban los polos $2/\varepsilon - \gamma_E + \ln(4\pi)$. Explica en palabras por que la eleccion de esquema no afecta a los observables fisicos aunque si a los parametros del lagrangiano.

---

## Bloque 2: Derivacion guiada (Nivel 2)

**2.1** Autoenergia del campo escalar a un loop en $\phi^4$. El diagrama de tadpole da:
$$\Sigma(p^2) = \frac{\lambda}{2}\int\frac{d^4k}{(2\pi)^4}\frac{i}{k^2-m^2+i\epsilon}.$$
- (a) Identifica el grado de divergencia de esta integral.
- (b) Usando regularizacion dimensional, muestra que aparece un polo en $\varepsilon$.
- (c) Escribe el contratermine necesario para renormalizar la masa.

**2.2** Corrimiento al rojo del acoplamiento en QED. La funcion beta de QED es $\beta(e) = e^3/(12\pi^2)$ (un loop).
- (a) Resuelve la ecuacion del grupo de renormalizacion $\mu de/d\mu = \beta(e)$.
- (b) Expresa la solucion en terminos de $\alpha(Q) = e^2(Q)/(4\pi)$.
- (c) Calcula $\alpha(M_Z)/\alpha(m_e)$ usando $M_Z\approx 91$ GeV, $m_e\approx 0.5$ MeV y compara con el valor experimental $\alpha(M_Z)\approx 1/128$.

**2.3** Renormalizabilidad y conteo de parametros. Una teoria es renormalizable si tiene un numero finito de contraterminos.
- (a) Argumenta por que $\phi^4$ en $d=4$ es renormalizable pero $\phi^6$ requiere infinitos contraterminos.
- (b) Explica como este criterio conecta con el concepto de teoria efectiva del modulo 12.
- (c) Clasifica los operadores de un lagrangiano general como relevantes, marginales e irrelevantes segun su dimension de masa.

---

## Bloque 3: Sintesis (Nivel 3)

**3.1** El grupo de renormalizacion como herramienta de prediccion. La asintota libre de QCD ($\alpha_s\to 0$ en el UV) y el confinamiento ($\alpha_s\to\infty$ en el IR) son consecuencias directas del signo de la funcion beta.
- Explica como la medicion de $\alpha_s$ a varias escalas $Q$ constituye una verificacion de la QCD.
- Discute por que el calculo perturbativo es valido para $Q\gg\Lambda_{\text{QCD}}\approx 200$ MeV y no para $Q\sim\Lambda_{\text{QCD}}$.
- Señala que conexion tiene este analisis con el matching de EFTs del modulo 12.

**3.2** Invarianza de Weyl y anomalia de escala. A nivel clasico, la teoria $\phi^4$ sin masa es invariante bajo reescalados $\phi\to\lambda^{-1}\phi$, $x\to\lambda x$. La cuantizacion introduce una escala $\mu$ y rompe esta simetria (anomalia de escala).
- Muestra que la funcion beta no nula implica que la traza del tensor energia-momento no es cero en la teoria cuantica.
- Identifica la relacion con la ecuacion de Callan-Symanzik.

---

## Soluciones sugeridas (Bloque 1)

**1.1** $E=2$: $D=2$ (cuadraticamente divergente). $E=4$: $D=0$ (logaritmicamente divergente). $E=6$: $D=-2$ (convergente).

**1.2** El factor $\mu^{4-d}$ tiene dimension de masa $4-d=\varepsilon$. La integral tiene dimension $[k^d/(k^2)^2] = k^{d-4}$, que con el factor $\mu^\varepsilon$ resulta adimensional en $d=4-\varepsilon$.

**1.3** $m^2(\mu) = m^2(\mu_0)(\mu/\mu_0)^{\lambda/(16\pi^2)}$. La masa crece con la escala, lo que genera el problema de la jerarquia: ajuste fino necesario para mantener $m^2_H\ll M_{\text{Pl}}^2$.

**1.4** Para $n_f=6$: $\beta_0 = 11/3\cdot 3 - 4/3\cdot 1/2\cdot 6 = 11 - 4 = 7 > 0$, luego $\beta(g) < 0$: libertad asintotica.

**1.5** Los observables fisicos son independientes del esquema porque los cambios de esquema son redefiniciones de parametros que dejan invariantes las S-matrices.


---

## Navegacion del tutorial

[(anterior) Esquema MS-barra y QED vs QCD](05_esquema_msbar_y_qed_vs_qcd.md) | [(siguiente) Modelo Estandar](../10_modelo_estandar/README.md)
