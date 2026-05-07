# Ejercicios del Modulo 02: Relatividad y Campos

**Modulo:** 02 — Relatividad y Campos  
**Nivel:** Fundacional  
**Cuadernos de apoyo:**  
- `../../Cuadernos/problemas_resueltos/07_relatividad_y_campos.ipynb`  
- `../../Cuadernos/ejemplos/03_campos_y_localidad.ipynb`


## Bloque 1: Verificacion (Nivel 1)

**1.1** Una particula en reposo tiene cuatro-velocidad $u^\mu = (1, 0, 0, 0)$. ¿Que vale $u^\mu u_\mu$? Repite para una particula sin masa con $k^\mu = (\omega, 0, 0, \omega)$.

**1.2** El grupo de Lorentz actua sobre cuatro-vectores como $x^\mu \to \Lambda^\mu_{\ \nu} x^\nu$. Escribe la condicion que debe satisfacer $\Lambda$ para preservar $g_{\mu\nu}x^\mu x^\nu$.

**1.3** Un campo escalar $\phi(x)$ transforma bajo traslaciones como $\phi(x) \to \phi(x+a)$. ¿Como transforma bajo una transformacion de Lorentz $x \to \Lambda x$?

**1.4** Enuncia la condicion de microcausalidad para el campo escalar: el conmutador $[\phi(x), \phi(y)]$ cuando $(x-y)^2 < 0$ (separacion tipo-espacio).

**1.5** Clasifica los siguientes campos segun su spin y estadistica: campo escalar $\phi$, campo de Dirac $\psi_\alpha$, campo electromagnetico $A^\mu$, tensor de Riemann $R^{\mu\nu\rho\sigma}$.

---

## Bloque 2: Derivacion guiada (Nivel 2)

**2.1** El choque entre mecanica cuantica y relatividad. La ecuacion de Schrodinger es $i\hbar\partial_t\psi = H\psi$. Si intentamos hacerla relativista sustituyendo $H = \sqrt{\mathbf{p}^2 + m^2}$:
- (a) Argumenta por que el operador $\sqrt{-\nabla^2 + m^2}$ es no local en espacio de posicion.
- (b) Muestra que la ecuacion de Klein-Gordon $(\partial^2 + m^2)\phi = 0$ es relativista y local.
- (c) Explica el precio que se paga: la existencia de soluciones de energia negativa.

**2.2** Representaciones del grupo de Lorentz. Los generadores del grupo de Lorentz $M^{\mu\nu}$ satisfacen
$$[M^{\mu\nu}, M^{\rho\sigma}] = i(g^{\mu\rho}M^{\nu\sigma} - g^{\mu\sigma}M^{\nu\rho} - g^{\nu\rho}M^{\mu\sigma} + g^{\nu\sigma}M^{\mu\rho}).$$
- (a) Introduce $J^i = \frac{1}{2}\varepsilon^{ijk}M_{jk}$ y $K^i = M^{0i}$. Muestra que satisfacen $[J^i, J^j] = i\varepsilon^{ijk}J^k$, $[J^i, K^j] = i\varepsilon^{ijk}K^k$ y $[K^i, K^j] = -i\varepsilon^{ijk}J^k$.
- (b) Define $A^i = \frac{J^i + iK^i}{2}$ y $B^i = \frac{J^i - iK^i}{2}$. Muestra que $[A^i, A^j] = i\varepsilon^{ijk}A^k$, $[B^i, B^j] = i\varepsilon^{ijk}B^k$ y $[A^i, B^j] = 0$.
- (c) Identifica las representaciones $(j_A, j_B)$ correspondientes a: escalar $(0,0)$, espinor de Weyl izquierdo $(\frac{1}{2}, 0)$, espinor de Weyl derecho $(0, \frac{1}{2})$ y vector $({\frac{1}{2}}, \frac{1}{2})$.

**2.3** Localidad y causalidad. El propagador de Feynman del campo escalar es $\Delta_F(x-y) = \langle 0|T\phi(x)\phi(y)|0\rangle$.
- (a) Explica en que sentido el propagador mide la amplitud de probabilidad de que una particula vaya de $y$ a $x$.
- (b) Para una separacion tipo-espacio, el propagador es distinto de cero pero exponencialmente suprimido: ¿por que esto no viola la causalidad?
- (c) ¿Que papel juega la contribucion de la antiparticula para restaurar la microcausalidad del conmutador?

---

## Bloque 3: Sintesis (Nivel 3)

**3.1** El teorema de Weinberg-Witten dice que no se puede construir un graviton compuesto dentro de una QFT con grupo gauge. Discute informalmente por que la clasificacion de campos por spin sugiere que el spin-2 y la invarianza gauge de los gravitones hacen dificil su descripcion como compuesto en una QFT estandar.

**3.2** Conecta este modulo con el siguiente. El modulo 03 introduce el formalismo lagrangiano. Argumenta por que la invarianza de Lorentz de la accion $S = \int d^4x\,\mathcal{L}$ requiere que $\mathcal{L}$ sea un escalar de Lorentz, y da un ejemplo de termino permitido y uno prohibido para el campo escalar.

---

## Soluciones sugeridas (Bloque 1)

**1.1** Para la particula en reposo: $u^\mu u_\mu = 1$. Para el foton: $k^\mu k_\mu = \omega^2 - \omega^2 = 0$.

**1.2** $\Lambda^T g \Lambda = g$, o equivalentemente $g_{\mu\nu}\Lambda^\mu_{\ \rho}\Lambda^\nu_{\ \sigma} = g_{\rho\sigma}$.

**1.3** Bajo Lorentz, $\phi(x) \to \phi'(x) = \phi(\Lambda^{-1}x)$. Para un escalar no hay indices que girar, solo cambia el argumento.

**1.4** $[\phi(x), \phi(y)] = 0$ para $(x-y)^2 < 0$.

**1.5** $\phi$: spin 0, bosón. $\psi_\alpha$: spin $\frac{1}{2}$, fermión. $A^\mu$: spin 1, bosón. $R^{\mu\nu\rho\sigma}$: spin 2 (parte sin traza), bosón.

---

## Navegacion del tutorial

[(anterior) Fundamentos Conceptuales](../01_fundamentos_conceptuales/README.md) | [(siguiente) Accion y Simetrias](../03_accion_y_simetrias/README.md)
