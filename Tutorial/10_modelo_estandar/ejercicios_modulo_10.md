# Ejercicios del Modulo 10: Modelo Estandar

**Modulo:** 10 — Modelo Estandar  
**Nivel:** Avanzado  
**Cuadernos de apoyo:**  
- `../../Cuadernos/ejemplos/07_modelo_estandar_panorama.ipynb`  
- `../../Cuadernos/problemas_resueltos/10_mezcla_electrodebil_y_masas_gauge.ipynb`  
- `../../Cuadernos/problemas_resueltos/16_ckm_pmns_y_mezcla_de_sabor.ipynb`  
- `../../Cuadernos/problemas_resueltos/14_neutrinos_y_oscilaciones.ipynb`


## Bloque 1: Verificacion (Nivel 1)

**1.1** El grupo gauge del Modelo Estandar es $SU(3)_c\times SU(2)_L\times U(1)_Y$. Escribe los numeros cuanticos $(T_3, Y, Q)$ de los siguientes campos usando la relacion de Gell-Mann-Nishijima $Q = T_3 + Y/2$: el doublete de Higgs $(H^+, H^0)$, el electron derecho $e_R$, y el quark up izquierdo $u_L$.

**1.2** El mecanismo de Higgs rompe $SU(2)_L\times U(1)_Y\to U(1)_Q$ cuando el campo de Higgs adquiere valor esperado $\langle H\rangle = (0, v/\sqrt{2})^T$ con $v\approx 246$ GeV. Calcula las masas $M_W$ y $M_Z$ en terminos de $v$, $g$ y $g'$. Verifica el valor del angulo de Weinberg $\sin^2\theta_W = 1-(M_W/M_Z)^2$.

**1.3** La matriz CKM $V_{\text{CKM}}$ conecta los autoestados de masa y los de sabor en el sector de quarks. Escribe la corriente cargada que genera desintegraciones como $d\to u\,e^-\bar\nu_e$ e identifica que elemento de la CKM es relevante. Indica el valor aproximado de $|V_{ud}|$ y su implicacion para la tasa de desintegracion beta nuclear.

**1.4** Los bosones $W^\pm$ y $Z^0$ se obtienen por combinacion de los campos de gauge $W^{1,2,3}_\mu$ y $B_\mu$. Escribe explicitamente: $W^\pm_\mu = (W^1_\mu \mp iW^2_\mu)/\sqrt{2}$, $Z_\mu = \cos\theta_W W^3_\mu - \sin\theta_W B_\mu$. Verifica que el foton $A_\mu = \sin\theta_W W^3_\mu + \cos\theta_W B_\mu$ no adquiere masa a traves del mecanismo de Higgs.

**1.5** Las oscilaciones de neutrinos ocurren porque los autoestados de sabor $(\nu_e, \nu_\mu, \nu_\tau)$ no coinciden con los autoestados de masa $(\nu_1, \nu_2, \nu_3)$. La probabilidad de transicion $\nu_\alpha\to\nu_\beta$ es:
$$P(\nu_\alpha\to\nu_\beta) = \left|\sum_i U_{\alpha i}^*U_{\beta i}\,e^{-im_i^2L/(2E)}\right|^2.$$
Para dos generaciones con mezcla $\theta$, muestra que $P(\nu_e\to\nu_\mu) = \sin^2(2\theta)\sin^2(\Delta m^2 L/4E)$.

---

## Bloque 2: Derivacion guiada (Nivel 2)

**2.1** Ruptura espontanea de simetria y masa del Higgs. El potencial del Higgs es $V(H) = -\mu^2|H|^2 + \lambda|H|^4$.
- (a) Muestra que para $\mu^2>0$ el minimo esta en $|H|^2 = v^2/2$ con $v^2 = \mu^2/\lambda$.
- (b) Expande alrededor del minimo: $H = (0,(v+h)/\sqrt{2})^T$ y calcula la masa del boson de Higgs $M_h = \sqrt{2\mu^2} = \sqrt{2\lambda}v$.
- (c) Verifica que $M_h\approx 125$ GeV con $v = 246$ GeV implica $\lambda\approx 0.13$.

**2.2** Corrientes neutras y el descubrimiento del $Z^0$. El sector de corrientes neutras del Modelo Estandar predijo la existencia del $Z^0$ antes de su descubrimiento en 1983.
- (a) Escribe la corriente neutral fermionica $j^\mu_{NC} = \bar f\gamma^\mu(T_3 - Q\sin^2\theta_W)f$ para el electron.
- (b) Identifica los valores del acoplamiento vectorial $g_V = T_3 - 2Q\sin^2\theta_W$ y axial $g_A = T_3$ del electron al $Z^0$.
- (c) Conecta con la asimetria de polarizacion $A_{LR} = (g_L^2-g_R^2)/(g_L^2+g_R^2)$ medida en LEP.

**2.3** Masas de fermiones y acoplamientos de Yukawa. Las masas de quarks y leptones provienen de los terminos de Yukawa $y_f\bar q_L H d_R + \text{h.c.}$ tras la ruptura de simetria.
- (a) Tras $\langle H\rangle = v/\sqrt{2}$, identifica la masa del fermiOn $m_f = y_f v/\sqrt{2}$.
- (b) Para el quark top ($m_t\approx 173$ GeV) calcula su acoplamiento de Yukawa. Discute si el valor es perturbativo.
- (c) Para el electron ($m_e\approx 0.5$ MeV) calcula $y_e$ y comenta la diferencia de 5 ordenes de magnitud con $y_t$.

---

## Bloque 3: Sintesis (Nivel 3)

**3.1** El Modelo Estandar como teoria efectiva. A energias $E\gg M_W$, la simetria electrodebil esta restaurada. A $E\ll M_W$, el Modelo Estandar puede aproximarse por una EFT (conecta con modulo 12):
- Integra formalmente el $W$ para obtener la teoria de Fermi $\mathcal{L}_F = -G_F/\sqrt{2}(\bar\nu_e\gamma^\mu P_L e)(\bar u\gamma_\mu P_L d)$.
- Identifica la relacion $G_F/\sqrt{2} = g^2/(8M_W^2)$.
- Discute la precision de esta aproximacion para $E\ll M_W$ y donde se espera que falle.

**3.2** Anomalias gauge y cancelacion en el Modelo Estandar. Las anomalias triangulares rompen la invariancia gauge a nivel cuantico y hacen la teoria inconsistente. El Modelo Estandar es anomalia-libre por cancelacion entre quarks y leptones dentro de cada generacion.
- Verifica que la condicion $\sum_{\text{fermiones}} Y^3 = 0$ se satisface en una generacion del Modelo Estandar.
- Explica por que esto implica que quarks y leptones no pueden existir independientemente sin romper la consistencia cuantica.

---

## Soluciones sugeridas (Bloque 1)

**1.1** $H^+$: $(T_3=+1/2, Y=+1, Q=+1)$. $H^0$: $(T_3=-1/2, Y=+1, Q=0)$. $e_R$: $(T_3=0, Y=-2, Q=-1)$. $u_L$: $(T_3=+1/2, Y=+1/3, Q=+2/3)$.

**1.2** $M_W = gv/2$, $M_Z = \sqrt{g^2+g'^2}v/2$. $\sin^2\theta_W = g'^2/(g^2+g'^2) = 1-(M_W/M_Z)^2\approx 0.231$.

**1.3** Corriente cargada: $\bar u_L\gamma^\mu V_{ud}d_L W^+_\mu$. $|V_{ud}|\approx 0.974$: quark $d$ decae casi exclusivamente a $u$, lo que explica la larga vida del neutron.

**1.4** El foton no se acopla al Higgs porque $Q_{A_\mu}=0$: el Higgs tiene carga $Q=0$ en el minimo y $A_\mu$ corresponde al generador no roto de $U(1)_Q$.

**1.5** Para dos generaciones: $P = |\cos\theta e^{-im_1^2L/2E}(-\sin\theta)+\sin\theta e^{-im_2^2L/2E}\cos\theta|^2 = \sin^2(2\theta)\sin^2(\Delta m^2 L/4E)$.


---

## Navegacion del tutorial

[(anterior) Neutrinos, Masas y Oscilaciones](07_neutrinos_masas_y_oscilaciones.md) | [(siguiente) QFT, Informacion y Agujeros Negros](../11_qft_informacion_y_agujeros_negros/README.md)
