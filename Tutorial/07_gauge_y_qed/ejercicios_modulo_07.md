# Ejercicios del Modulo 07: Gauge y QED

**Modulo:** 07 — Gauge y QED  
**Nivel:** Nucleo  
**Cuadernos de apoyo:**  
- `../../Cuadernos/problemas_resueltos/13_gauge_fixing_y_scattering_en_qed.ipynb`  
- `../../Cuadernos/ejemplos/16_qed_derivada_covariante_y_ward.ipynb`  
- `../../Cuadernos/problemas_resueltos/17_esquema_msbar_y_qed_vs_qcd.ipynb`


## Bloque 1: Verificacion (Nivel 1)

**1.1** La derivada covariante en QED es $D_\mu = \partial_\mu - ieA_\mu$. Bajo la transformacion gauge $A_\mu \to A_\mu + \partial_\mu\alpha$ y $\psi \to e^{ie\alpha}\psi$, verifica que $D_\mu\psi \to e^{ie\alpha}D_\mu\psi$, es decir, que la derivada covariante transforma como el campo.

**1.2** El tensor de campo electromagnetico es $F_{\mu\nu} = \partial_\mu A_\nu - \partial_\nu A_\mu$. Verifica que $F_{\mu\nu}$ es invariante bajo la transformacion gauge del ejercicio 1.1. Identifica que componentes de $F_{\mu\nu}$ corresponden al campo electrico $\mathbf{E}$ y al magnetico $\mathbf{B}$.

**1.3** En el gauge de Lorenz $\partial^\mu A_\mu = 0$, el propagador del foton en espacio de momentos es:
$$D_{\mu\nu}(k) = \frac{-g_{\mu\nu}}{k^2 + i\epsilon}.$$
Verifica que $k^\mu D_{\mu\nu}(k) \propto k_\nu$. Explica que consecuencia tiene este resultado para amplitudes fisicas (identidad de Ward).

**1.4** El vertice de interaccion de QED produce un factor $-ie\gamma^\mu$ en las reglas de Feynman. Dibuja el diagrama de Feynman a orden mas bajo para la dispersion electron-electron ($e^-e^- \to e^-e^-$) e identifica los propagadores y vertices involucrados.

**1.5** La identidad de Ward-Takahashi en QED establece que $k_\mu\mathcal{M}^\mu = 0$ para amplitudes fisicas, donde $k$ es el cuadrimomento del foton externo. Explica en palabras que simetria garantiza esta identidad y que consecuencia tiene para los grados de libertad fisicos del foton.

---

## Bloque 2: Derivacion guiada (Nivel 2)

**2.1** Amplitud de dispersion Compton $e^-\gamma \to e^-\gamma$ a orden mas bajo. Hay dos diagramas contribuyentes (canal $s$ y canal $u$).
- (a) Escribe las expresiones para las dos amplitudes usando las reglas de Feynman de QED.
- (b) Muestra que la suma de ambos satisface la identidad de Ward al sustituir el vector de polarizacion del foton por su cuadrimomento.
- (c) Identifica en que limite de baja energia se recupera la dispersion Thomson clasica.

**2.2** Fijacion de gauge y grados de libertad. El foton tiene 4 componentes $A_\mu$ pero solo 2 grados de libertad fisicos.
- (a) Explica como el gauge de Lorenz reduce los 4 a 3.
- (b) Explica como la libertad gauge residual en Lorenz reduce los 3 a 2.
- (c) Identifica los dos estados de polarizacion fisica del foton y sus helicidades.

**2.3** La lagrangiana de QED con termino de fijacion de gauge es:
$$\mathcal{L} = -\frac{1}{4}F_{\mu\nu}F^{\mu\nu} + \bar\psi(i\slashed{D}-m)\psi - \frac{1}{2\xi}(\partial^\mu A_\mu)^2.$$
- (a) Deriva el propagador del foton en gauge general $\xi$ a partir de las ecuaciones de movimiento de $A_\mu$.
- (b) Verifica que para $\xi = 1$ (gauge de Feynman) se recupera $D_{\mu\nu} = -g_{\mu\nu}/(k^2+i\epsilon)$.
- (c) Argumenta por que las amplitudes fisicas no deben depender de $\xi$.

---

## Bloque 3: Sintesis (Nivel 3)

**3.1** Conecta QED con el modulo 09 (renormalizacion). La carga del electron recibe correcciones radiativas. El parametro $\alpha = e^2/(4\pi) \approx 1/137$ es medido a bajas energias. A energias $Q^2 \gg m_e^2$, la carga efectiva aumenta segun la funcion beta de QED: $\beta(e) = e^3/(12\pi^2)$.
- Escribe la ecuacion del grupo de renormalizacion para $\alpha(Q)$.
- Calcula a que energia $Q$ la constante $\alpha$ se duplica respecto a su valor a $Q=m_e$.
- Compara con la escala del polo de Landau y comenta la validez del calculo perturbativo.

**3.2** Compara la estructura de QED (grupo $U(1)$) con QCD (grupo $SU(3)$). En QED hay un foton, sin autointeraccion. En QCD hay 8 gluones con autointeraccion.
- Identifica el termino responsable de la autointeraccion de los gluones en la lagrangiana de QCD.
- Explica por que la funcion beta de QCD es negativa (libertad asintotica) mientras la de QED es positiva.
- Señala que consecuencia tiene la libertad asintotica para los calculos perturbativos en QCD.

---

## Soluciones sugeridas (Bloque 1)

**1.1** $D_\mu(e^{ie\alpha}\psi) = (\partial_\mu - ie(A_\mu+\partial_\mu\alpha))e^{ie\alpha}\psi = e^{ie\alpha}(\partial_\mu - ieA_\mu)\psi = e^{ie\alpha}D_\mu\psi$.

**1.2** $F_{\mu\nu}$ es invariante porque $\partial_\mu\partial_\nu\alpha = \partial_\nu\partial_\mu\alpha$. $E^i = F^{0i}$, $B^i = -\frac{1}{2}\varepsilon^{ijk}F_{jk}$.

**1.3** $k^\mu D_{\mu\nu} = -k_\nu/k^2$. La identidad de Ward implica que estados de polarizacion longitudinal y temporal se cancelan en amplitudes fisicas.

**1.4** Canal $t$ (intercambio de foton) + canal $u$ (intercambio cruzado). Dos propagadores de foton, cuatro propagadores de electron, cuatro vertices.

**1.5** La invariancia gauge $U(1)$. Solo 2 de los 4 grados de libertad de $A_\mu$ son fisicos (polarizaciones transversales).


---

## Navegacion del tutorial

[(anterior) Polarizaciones y Sumas de Espin](05_polarizaciones_y_sumas_de_espin.md) | [(siguiente) Integral de Camino](../08_integral_de_camino/README.md)
