# Ejercicios del Modulo 08: Integral de Camino

**Modulo:** 08 — Integral de Camino  
**Nivel:** Intermedio  
**Cuadernos de apoyo:**  
- `../../Cuadernos/ejemplos/11_integral_de_camino_y_accion_efectiva.ipynb`  
- `../../Cuadernos/problemas_resueltos/19_correladores_y_accion_efectiva.ipynb`  
- `../../Cuadernos/problemas_resueltos/15_regularizacion_dimensional_y_running.ipynb`


## Bloque 1: Verificacion (Nivel 1)

**1.1** La integral gaussiana funcional es el bloque de construccion basico de la integral de camino libre:
$$\int \mathcal{D}\phi\, e^{-\frac{1}{2}\int\phi K\phi} = (\det K)^{-1/2}.$$
Verifica esta formula en el caso discreto (integral gaussiana ordinaria de $N$ variables) y explica como se generaliza al caso continuo.

**1.2** El funcional generador para la teoria libre con fuente es:
$$Z_0[J] = Z_0[0]\,\exp\!\left(\frac{1}{2}\int d^4x\,d^4y\, J(x)\,\Delta_F(x-y)\,J(y)\right),$$
donde $\Delta_F$ es el propagador de Feynman. Calcula $\langle\phi(x)\phi(y)\rangle_0 = \delta^2\ln Z_0/\delta J(x)\delta J(y)|_{J=0}$ y verifica que el resultado es $\Delta_F(x-y)$.

**1.3** La accion efectiva $\Gamma[\phi_c]$ se define como la transformada de Legendre de $W[J] = -i\ln Z[J]$:
$$\Gamma[\phi_c] = W[J] - \int J\phi_c, \qquad \phi_c = \frac{\delta W}{\delta J}.$$
Verifica que en la aproximacion de arbol $\Gamma[\phi_c] = S[\phi_c]$, es decir, la accion efectiva a nivel clasico coincide con la accion clasica.

**1.4** La relacion entre el correlador de dos puntos completo y el propagador es:
$$G^{(2)}(x,y) = \langle\phi(x)\phi(y)\rangle = \frac{\delta^2 W[J]}{\delta J(x)\delta J(y)}\bigg|_{J=0}.$$
Explica la diferencia entre $G^{(2)}$ (funciones de Green completas con diagramas desconectados) y las funciones de Green conectadas generadas por $W[J]$.

**1.5** La transformacion de Bogoliubov mezcla operadores de creacion y aniquilacion de dos vacios distintos. En el efecto Unruh, el vacio de Minkowski es un estado termico para el observador acelerado. Escribe la relacion de Bogoliubov entre operadores de Rindler y de Minkowski e identifica la temperatura de Unruh $T = a/(2\pi)$.

---

## Bloque 2: Derivacion guiada (Nivel 2)

**2.1** Derivacion del propagador libre via integral de camino. La integral gaussiana en espacio de momentos da:
$$Z_0[J] \propto \exp\!\left(-\frac{1}{2}\int \frac{d^4k}{(2\pi)^4}\frac{J(k)J(-k)}{k^2+m^2-i\epsilon}\right).$$
- (a) Identifica el propagador de Feynman en espacio de momentos $\tilde\Delta_F(k) = 1/(k^2+m^2-i\epsilon)$.
- (b) Explica el papel de la prescripcion $i\epsilon$ para definir correctamente la integral.
- (c) Verifica que en espacio de posiciones $(\partial^2+m^2)\Delta_F(x-y) = -\delta^{(4)}(x-y)$.

**2.2** El potencial efectivo a un loop. Para la teoria $\phi^4$ con $V(\phi) = \frac{m^2}{2}\phi^2 + \frac{\lambda}{4!}\phi^4$, el potencial efectivo a un loop es:
$$V_{\text{eff}}(\phi_c) = V(\phi_c) + \frac{1}{2}\int\frac{d^4k}{(2\pi)^4}\ln\!\left(k^2 + V''(\phi_c)\right) + \cdots$$
- (a) Identifica la divergencia UV de la integral de loop y discute como regularizarla.
- (b) Explica por que $V_{\text{eff}}$ puede tener un minimo desplazado respecto a $V$ clasico.
- (c) Conecta con la ruptura espontanea de simetria del modulo 10.

**2.3** Integral de camino fermionica y variables de Grassmann. Para fermiones se usan variables anticonmutantes $\theta_i\theta_j = -\theta_j\theta_i$.
- (a) Muestra que $\int d\theta\,\theta = 1$ e $\int d\theta\,1 = 0$ (reglas de Berezin).
- (b) Calcula la integral gaussiana fermionica $\int d\bar\theta d\theta\, e^{-\bar\theta M\theta} = \det M$.
- (c) Contrasta con el caso bosonico $\int \mathcal{D}\phi\, e^{-\phi K\phi} = (\det K)^{-1/2}$ y comenta el signo.

---

## Bloque 3: Sintesis (Nivel 3)

**3.1** Conecta la integral de camino con la cuantizacion canonica. Muestra que el elemento de matriz:
$$\langle q_f | e^{-iHT} | q_i\rangle = \int_{q(0)=q_i}^{q(T)=q_f}\mathcal{D}q\, e^{iS[q]}$$
puede derivarse insertando completitudes en el propagador canonico. Identifica los pasos clave de la derivacion y donde aparece la fase de accion.

**3.2** La formula de Gell-Mann-Low y su version funcional. El valor esperado en el vacio de un operador $\hat O$ puede calcularse como:
$$\langle 0|\hat O|0\rangle = \frac{\int\mathcal{D}\phi\, O[\phi]\, e^{iS[\phi]}}{\int\mathcal{D}\phi\, e^{iS[\phi]}}.$$
Explica como esta formula conecta con el calculo perturbativo de diagramas de Feynman al expandir $e^{i S_{\text{int}}}$. Identifica que papel juegan los diagramas de vacio (denominador).

---

## Soluciones sugeridas (Bloque 1)

**1.1** Para $N$ variables: $\int d^N\phi\, e^{-\frac{1}{2}\phi^T K\phi} = (2\pi)^{N/2}(\det K)^{-1/2}$. El limite continuo reemplaza $K$ por el operador diferencial $-\partial^2 + m^2$.

**1.2** $\delta^2\ln Z_0/\delta J\delta J|_0 = \Delta_F(x-y)$ directamente de la forma exponencial gaussiana.

**1.3** En el limite $\hbar\to 0$, la integral de camino esta dominada por el punto de silla $\delta S/\delta\phi=0$, que es la ecuacion clasica. La accion efectiva a ese orden es la accion clasica evaluada en la solucion clasica.

**1.4** $G^{(2)}$ contiene diagramas conectados y desconectados. $W$ genera solo los conectados. La diferencia es un termino $\langle\phi\rangle^2$ en teoria con $\langle\phi\rangle\neq 0$.

**1.5** $a_k^{\text{Rindler}} = \alpha_k b_k + \beta_k b_{-k}^\dagger$ con $|\beta_k|^2 = 1/(e^{2\pi\omega/a}-1)$ (distribucion de Planck). $T_U = a/(2\pi)$ en unidades naturales.


---

## Navegacion del tutorial

[(anterior) Bogoliubov y Cambio de Vacio](04_bogoliubov_y_cambio_de_vacio.md) | [(siguiente) Renormalizacion](../09_renormalizacion/README.md)
