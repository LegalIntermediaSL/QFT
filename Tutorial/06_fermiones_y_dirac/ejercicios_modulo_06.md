# Ejercicios del Modulo 06: Fermiones y Dirac

**Modulo:** 06 — Fermiones y Dirac  
**Nivel:** Nucleo  
**Cuadernos de apoyo:**  
- `../../Cuadernos/problemas_resueltos/09_algebra_de_dirac_simbolica.ipynb`  
- `../../Cuadernos/problemas_resueltos/09_bilineales_y_proyectores_quirales.ipynb`  
- `../../Cuadernos/problemas_resueltos/18_corriente_de_dirac_y_limite_no_relativista.ipynb`


## Bloque 1: Verificacion (Nivel 1)

**1.1** La ecuacion de Dirac es $( i\gamma^\mu\partial_\mu - m)\psi = 0$. Verifica que si $\psi$ satisface esta ecuacion, entonces cada componente satisface la ecuacion de Klein-Gordon $(\partial^2 + m^2)\psi = 0$. *(Pista: aplica $(−i\gamma^\mu\partial_\mu − m)$ por la izquierda.)*

**1.2** Las matrices gamma en representacion de Dirac son:
$$\gamma^0 = \begin{pmatrix}\mathbf{1}&0\\0&-\mathbf{1}\end{pmatrix}, \quad \gamma^i = \begin{pmatrix}0&\sigma^i\\-\sigma^i&0\end{pmatrix}.$$
Verifica explicitamente la relacion de anticonmutacion $\{\gamma^\mu,\gamma^\nu\} = 2g^{\mu\nu}$ para los pares $(\mu,\nu) = (0,0)$, $(1,1)$ y $(0,1)$.

**1.3** El bilineal escalar de Dirac es $\bar\psi\psi = \psi^\dagger\gamma^0\psi$. Clasifica los siguientes bilineales segun su transformacion bajo Lorentz (escalar, pseudoescalar, vector, axial, tensor): $\bar\psi\psi$, $\bar\psi\gamma^5\psi$, $\bar\psi\gamma^\mu\psi$, $\bar\psi\gamma^\mu\gamma^5\psi$, $\bar\psi\sigma^{\mu\nu}\psi$.

**1.4** Los operadores de proyeccion quiral son $P_L = \frac{1-\gamma^5}{2}$ y $P_R = \frac{1+\gamma^5}{2}$. Verifica que $P_L^2 = P_L$, $P_R^2 = P_R$ y $P_LP_R = 0$.

**1.5** En el limite no relativista, la ecuacion de Dirac se reduce a la ecuacion de Pauli-Schrodinger. Escribe las dos componentes grandes $\phi$ y las dos componentes pequenas $\chi$ de un espinor de Dirac en reposo, e identifica cual corresponde a particula y cual a antiparticula.

---

## Bloque 2: Derivacion guiada (Nivel 2)

**2.1** Derivacion de la corriente de Noether fermionica. La lagrangiana de Dirac libre es $\mathcal{L} = \bar\psi(i\gamma^\mu\partial_\mu - m)\psi$. Bajo $\psi\to e^{i\alpha}\psi$:
- (a) Calcula la variacion de la lagrangiana a primer orden en $\alpha$.
- (b) Aplica el teorema de Noether para obtener la corriente conservada $j^\mu = \bar\psi\gamma^\mu\psi$.
- (c) Verifica que $\partial_\mu j^\mu = 0$ usando la ecuacion de Dirac.

**2.2** Espinores de Weyl y Majorana. Un espinor de Dirac de 4 componentes puede descomponerse en dos espinores de Weyl de 2 componentes: $\psi = (\xi_\alpha, \bar\eta^{\dot\alpha})^T$.
- (a) Escribe la ecuacion de Dirac sin masa en terminos de $\xi$ y $\bar\eta$.
- (b) Explica que condicion adicional convierte un espinor de Dirac en un espinor de Majorana.
- (c) Argumenta por que los neutrinos podrian ser fermiones de Majorana.

**2.3** Cuantizacion canonica del campo de Dirac. Las relaciones de anticonmutacion son $\{b_{\mathbf{p},s}, b^\dagger_{\mathbf{q},r}\} = \delta^{(3)}(\mathbf{p}-\mathbf{q})\delta_{sr}$.
- (a) Explica por que se usan anticonmutadores en vez de conmutadores para fermiones.
- (b) Muestra que el principio de exclusion de Pauli emerge directamente de $(b^\dagger)^2 = 0$.
- (c) Calcula la densidad de carga $j^0 = \bar\psi\gamma^0\psi$ en terminos de operadores de creacion y aniquilacion para particulas y antiparticulas.

---

## Bloque 3: Sintesis (Nivel 3)

**3.1** Conecta el modulo 06 con el modulo 07 (QED). La interaccion minimal entre un fermiOn y el campo electromagnetico se introduce via la derivada covariante $\partial_\mu \to D_\mu = \partial_\mu - ieA_\mu$.
- Escribe el lagrangiano de QED completo.
- Identifica los tres terminos y su significado fisico.
- Explica por que la quiralidad no esta conservada en QED masiva pero si en QED sin masa.

**3.2** La traza de matrices gamma es fundamental en el calculo de secciones eficaces. Usando las reglas de traza: $\text{Tr}(\gamma^\mu\gamma^\nu) = 4g^{\mu\nu}$ y $\text{Tr}(\gamma^\mu\gamma^\nu\gamma^\rho\gamma^\sigma) = 4(g^{\mu\nu}g^{\rho\sigma} - g^{\mu\rho}g^{\nu\sigma} + g^{\mu\sigma}g^{\nu\rho})$:
- Calcula $\text{Tr}[(\slashed{p}+m)(\slashed{q}+m)]$ donde $\slashed{p} = \gamma^\mu p_\mu$.
- Explica como este resultado aparece en el calculo de la seccion eficaz de dispersion Compton.

---

## Soluciones sugeridas (Bloque 1)

**1.1** Aplicar $(−i\slashed\partial − m)(i\slashed\partial − m) = \partial^2 + m^2$ usando $\{\gamma^\mu,\gamma^\nu\}=2g^{\mu\nu}$.

**1.2** Para $(0,0)$: $(\gamma^0)^2 = \mathbf{1} = g^{00}\cdot 2$. Para $(1,1)$: $(\gamma^1)^2 = -\mathbf{1} = 2g^{11}$. Para $(0,1)$: $\gamma^0\gamma^1 + \gamma^1\gamma^0 = 0 = 2g^{01}$.

**1.3** Escalar, pseudoescalar, 4-vector, 4-vector axial, tensor antisimetrico de rango 2.

**1.4** $P_L^2 = \frac{(1-\gamma^5)^2}{4} = \frac{1 - 2\gamma^5 + (\gamma^5)^2}{4} = \frac{2(1-\gamma^5)}{4} = P_L$ usando $(\gamma^5)^2 = \mathbf{1}$.

**1.5** En reposo: $\phi = $ componentes grandes (particula), $\chi \approx 0$ en el limite $m\to\infty$ (antiparticula en el mar de Dirac).


---

## Navegacion del tutorial

[(anterior) Quiralidad, Weyl y Majorana](05_quiralidad_weyl_y_majorana.md) | [(siguiente) Gauge y QED](../07_gauge_y_qed/README.md)
