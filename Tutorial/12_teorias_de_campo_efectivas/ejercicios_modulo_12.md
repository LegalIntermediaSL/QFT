# Ejercicios del Modulo 12: Teorias de Campo Efectivas

**Modulo:** 12 — Teorias de Campo Efectivas (EFT)  
**Nivel:** Avanzado  
**Cuadernos de apoyo:**  
- `../../Cuadernos/ejemplos/15_operadores_efectivos_y_power_counting.ipynb`  
- `../../Cuadernos/problemas_resueltos/17_fermi_y_matching_efectivo.ipynb`  
- `../../Cuadernos/ejemplos/18_smeft_y_operador_de_weinberg.ipynb`  
- `../../Cuadernos/problemas_resueltos/19_matching_uv_a_smeft.ipynb`  
- `../../Cuadernos/ejemplos/20_majorana_y_seesaw.ipynb`


## Bloque 1: Verificacion (Nivel 1)

**1.1** El power counting de Weinberg clasifica los operadores de una EFT segun su dimension de masa. En $d=4$, un operador de dimension $n$ produce efectos de orden $(E/\Lambda)^{n-4}$ donde $\Lambda$ es la escala de corte. Clasifica los siguientes operadores en relevantes ($n<4$), marginales ($n=4$) o irrelevantes ($n>4$): $\phi^2$ (dimension 2), $(\partial\phi)^2$ (dimension 4), $\phi^6$ (dimension 6), $(\bar\psi\psi)^2$ (dimension 6).

**1.2** La teoria de Fermi describe las desintegraciones debiles a energias $E\ll M_W$ mediante el operador efectivo de dimension 6:
$$\mathcal{O}_F = \frac{G_F}{\sqrt{2}}(\bar\nu_e\gamma^\mu P_L e)(\bar u\gamma_\mu P_L d) + \text{h.c.}$$
con $G_F/\sqrt{2} = g^2/(8M_W^2)$. Calcula $G_F$ numericamente usando $g\approx 0.65$ y $M_W\approx 80$ GeV. Compara con el valor experimental $G_F\approx 1.17\times 10^{-5}$ GeV$^{-2}$.

**1.3** El operador de Weinberg $\mathcal{O}_5 = \frac{c}{\Lambda}(\overline{L^c}\tilde H)(\tilde H^T L)$ es el unico operador de dimension 5 del SMEFT (invariante bajo el grupo gauge del Modelo Estandar). Tras la ruptura de simetria electrodebil, genera una masa de Majorana para el neutrino:
$$m_\nu \sim \frac{cv^2}{\Lambda}.$$
Para $c\sim 1$ y $m_\nu\sim 0.1$ eV, estima la escala $\Lambda$. Comenta el resultado en relacion con la escala de GUT.

**1.4** El mecanismo seesaw de tipo I introduce neutrinos de Majorana pesados $N_R$ con masa $M\gg v$. La matriz de masa de neutrinos ligeros es $m_\nu\approx -m_D^T M^{-1} m_D$ donde $m_D$ es la masa de Dirac. Verifica dimensionalmente que si $m_D\sim m_t\sim 173$ GeV y $m_\nu\sim 0.1$ eV, entonces $M\sim 10^{15}$ GeV.

**1.5** La lagrangiana de Euler-Heisenberg describe la interaccion entre fotones a bajas energias ($\omega\ll m_e$) tras integrar el electron:
$$\mathcal{L}_{\text{EH}} = \frac{\alpha^2}{90m_e^4}\left[4(F_{\mu\nu}F^{\mu\nu})^2 + 7(F_{\mu\nu}\tilde F^{\mu\nu})^2\right].$$
Identifica la escala de supresion $\Lambda = m_e$ y el operador de dimension 8 involucrado. Explica por que esta interaccion es muy debil a energias opticas ($\omega\sim\text{eV}\ll m_e$).

---

## Bloque 2: Derivacion guiada (Nivel 2)

**2.1** Matching en la teoria de Fermi. Calcula la amplitud de dispersion $\bar\nu_e e^- \to \bar u d$ en el Modelo Estandar a orden arbol intercambiando un $W$:
- (a) Escribe la amplitud en el limite $q^2\ll M_W^2$.
- (b) Aproxima el propagador del $W$: $1/(q^2-M_W^2)\approx -1/M_W^2$.
- (c) Identifica el coeficiente Wilson efectivo resultante y verifica que $C = g^2/(8M_W^2) = G_F/\sqrt{2}$.

**2.2** Power counting en gravedad como EFT. La lagrangiana de Einstein-Hilbert expandida alrededor del espacio plano produce un expansion en potencias de $E/M_{\text{Pl}}$:
$$\mathcal{L}_{\text{grav}} = M_{\text{Pl}}^2 R = M_{\text{Pl}}^2\left[\partial h\partial h + h(\partial h)^2/M_{\text{Pl}} + \cdots\right].$$
- (a) Identifica el propagador del graviton ($E^{-2}$) y el vertice de tres gravitones ($\propto E^2/M_{\text{Pl}}$).
- (b) Muestra que un loop de gravitones produce correcciones de orden $(E/M_{\text{Pl}})^2$.
- (c) Explica por que la gravedad es perturbativamente tratable para $E\ll M_{\text{Pl}}$ pero no unitaria a $E\sim M_{\text{Pl}}$.

**2.3** Coeficientes de Wilson y operadores del SMEFT. El SMEFT organiza las desviaciones del Modelo Estandar en operadores de dimension $d\geq 5$:
$$\mathcal{L}_{\text{SMEFT}} = \mathcal{L}_{\text{SM}} + \sum_i \frac{C_i^{(6)}}{\Lambda^2}\mathcal{O}_i^{(6)} + \cdots$$
- (a) Escribe el operador de cuatro fermiones $(\bar q_L\gamma^\mu q_L)(\bar q_L\gamma_\mu q_L)$ e identifica su dimension de masa.
- (b) Explica como las mediciones de precision electrodebil en LEP ponen limites sobre $C_i/\Lambda^2$.
- (c) Discute como el LHC complementa esas mediciones con busquedas directas de resonancias a escala $\Lambda$.

---

## Bloque 3: Sintesis (Nivel 3)

**3.1** El mecanismo seesaw como EFT. El seesaw tipo I tiene una teoria UV completa (Modelo Estandar + $N_R$) y una EFT a bajas energias (el operador de Weinberg). Al integrar $N_R$ con masa $M$:
- Realiza el matching explicito al nivel de arboles: muestra que el coeficiente del operador de Weinberg es $c/\Lambda = y_\nu^T M^{-1} y_\nu$.
- Explica como la fenomenologia de oscilaciones de neutrinos (que mide $\Delta m^2$) solo puede determinar combinaciones de $y_\nu$ y $M$, no los parametros individuales.
- Discute que evidencia observacional apuntaria directamente a la escala $M$ del seesaw.

**3.2** EFT y el limite del Modelo Estandar. El Modelo Estandar puede interpretarse como la EFT mas general invariante bajo $SU(3)\times SU(2)\times U(1)$ y renormalizable.
- Clasifica los operadores del SMEFT de dimension 6 segun si modifican el sector gauge, el sector fermionico o el sector de Higgs.
- Explica por que ausencia de deviaciones en la fenomenologia de precision implica $\Lambda\gg v$ o coeficientes de Wilson muy pequenos, no la ausencia de fisica nueva.
- Conecta con el problema de la jerarquia del modulo 09: el hecho de que $m_H\ll M_{\text{Pl}}$ requiere ajuste fino de coeficientes en la EFT.

---

## Soluciones sugeridas (Bloque 1)

**1.1** Relevantes: $\phi^2$ ($n=2$). Marginales: $(\partial\phi)^2$ ($n=4$). Irrelevantes: $\phi^6$ ($n=6$), $(\bar\psi\psi)^2$ ($n=6$).

**1.2** $G_F/\sqrt{2} = (0.65)^2/(8\cdot(80)^2)\approx 8.3\times 10^{-6}$ GeV$^{-2}$. Acuerdo razonable con $1.17\times 10^{-5}$ GeV$^{-2}$ (la diferencia incluye correcciones radiativas).

**1.3** $\Lambda\sim cv^2/m_\nu\sim (246)^2/(0.1\times 10^{-9})\sim 6\times 10^{14}$ GeV $\sim 10^{15}$ GeV. Cercano a la escala de GUT, lo que es una coincidencia sugestiva.

**1.4** $M\sim m_D^2/m_\nu\sim (173\text{ GeV})^2/(0.1\text{ eV})\sim 3\times 10^{14}$ GeV $\sim 10^{14}$–$10^{15}$ GeV.

**1.5** La supresion es $(\omega/m_e)^4\sim (1\text{ eV}/0.5\text{ MeV})^4\sim 10^{-24}$: la interaccion luz-luz es completamente despreciable a energias opticas.


---

## Navegacion del tutorial

[(anterior) Matching UV y Coeficientes de Wilson](08_matching_uv_y_coeficientes_de_wilson.md) | [(volver al inicio) Tutorial QFT](../README.md)
