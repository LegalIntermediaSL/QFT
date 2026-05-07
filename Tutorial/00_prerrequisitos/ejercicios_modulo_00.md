# Ejercicios del Modulo 00: Prerrequisitos

**Modulo:** 00 — Prerrequisitos  
**Nivel:** Fundacional  
**Cuadernos de apoyo:**  
- `../../Cuadernos/problemas_resueltos/01_relatividad_especial_basica.ipynb`  
- `../../Cuadernos/problemas_resueltos/02_notacion_tensorial_y_convenciones.ipynb`  
- `../../Cuadernos/problemas_resueltos/03_oscilador_armonico_cuantico.ipynb`  
- `../../Cuadernos/problemas_resueltos/04_simetrias_y_grupos_basicos.ipynb`  
- `../../Cuadernos/problemas_resueltos/05_delta_de_dirac_y_fourier.ipynb`  
- `../../Cuadernos/problemas_resueltos/23_calculo_funcional.ipynb`


## Bloque 1: Verificacion (Nivel 1)

**1.1** Un foton tiene cuatro-momento $k^\mu = (\omega, \mathbf{k})$ con $\omega = |\mathbf{k}|$. Verifica que $k^\mu k_\mu = 0$ usando la metrica de Minkowski con signo $(+,-,-,-)$.

**1.2** La suma de Einstein conviene sobre indices repetidos: $A^\mu B_\mu = \sum_\mu A^\mu B_\mu$. Escribe explicitamente la contraccion $g^{\mu\nu}g_{\nu\rho}$ y simplifica el resultado.

**1.3** El oscilador armonico cuantico satisface $[a, a^\dagger] = 1$. Calcula $[a, (a^\dagger)^n]$ usando la relacion de conmutacion.

**1.4** La delta de Dirac satisface $\int f(x)\,\delta(x-x_0)\,dx = f(x_0)$. Usando su representacion de Fourier $\delta(x) = \frac{1}{2\pi}\int e^{ikx}\,dk$, verifica que $\delta(-x) = \delta(x)$.

**1.5** Convierte la masa del electron $m_e = 9.109\times10^{-31}$ kg a unidades naturales ($\hbar = c = 1$) y expresa el resultado en MeV.

---

## Bloque 2: Derivacion guiada (Nivel 2)

**2.1** Relacion energia-momento relativista.
- (a) A partir de la invariancia de Lorentz del cuatro-momento $p^\mu p_\mu = m^2$, deduce $E^2 = \mathbf{p}^2 + m^2$.
- (b) Verifica los limites: $E \approx m$ cuando $|\mathbf{p}| \ll m$ y $E \approx |\mathbf{p}|$ cuando $|\mathbf{p}| \gg m$.
- (c) Argumenta por que una particula sin masa se mueve a la velocidad de la luz.

**2.2** El oscilador armonico como prototipo de cuantizacion de campos. El hamiltoniano del oscilador es $H = \omega(a^\dagger a + \frac{1}{2})$.
- (a) Muestra que los estados $|n\rangle = \frac{(a^\dagger)^n}{\sqrt{n!}}|0\rangle$ son autoestados de $H$.
- (b) Interpreta el estado $|0\rangle$ como vacio y $|n\rangle$ como estado de $n$ particulas.
- (c) Explica como esta estructura se generaliza a un campo libre con infinitos modos.

**2.3** Derivada funcional. Sea $S[\phi] = \int d^4x\,\mathcal{L}(\phi, \partial_\mu\phi)$ con $\mathcal{L} = \frac{1}{2}(\partial_\mu\phi)^2 - \frac{1}{2}m^2\phi^2$.
- (a) Calcula $\frac{\delta S}{\delta \phi(x)}$ usando la definicion $\frac{\delta S}{\delta\phi(x)} = \lim_{\epsilon\to0}\frac{S[\phi+\epsilon\delta^{(4)}(y-x)] - S[\phi]}{\epsilon}$.
- (b) Pon a cero el resultado para obtener la ecuacion de Klein-Gordon.

---

## Bloque 3: Sintesis (Nivel 3)

**3.1** El algebra de Lie $\mathfrak{su}(2)$ tiene generadores $J_i$ con $[J_i, J_j] = i\varepsilon_{ijk}J_k$. El Casimir es $J^2 = J_1^2 + J_2^2 + J_3^2$.
- Identifica las representaciones de spin $j = 0, \frac{1}{2}, 1$ y su dimension $2j+1$.
- Explica como las representaciones de $\mathfrak{su}(2)$ clasifican las particulas segun su spin.
- Argumenta por que necesitamos $\mathfrak{su}(2) \times \mathfrak{su}(2) \simeq \mathfrak{so}(3,1)$ para describir el grupo de Lorentz.

**3.2** Resume las relaciones entre los prerrequisitos del modulo.
- Explica como la metrica de Minkowski conecta la relatividad especial con la notacion tensorial.
- Explica como el oscilador armonico conecta la mecanica cuantica con la cuantizacion de campos.
- Explica como la delta de Dirac y Fourier conectan espacio de posicion con espacio de momentos.

---

## Soluciones sugeridas (Bloque 1)

**1.1** $k^\mu k_\mu = g_{\mu\nu}k^\mu k^\nu = \omega^2 - |\mathbf{k}|^2 = 0$ usando $\omega = |\mathbf{k}|$.

**1.2** $g^{\mu\nu}g_{\nu\rho} = \delta^\mu_{\ \rho}$ (identidad matricial, no suma).

**1.3** $[a, (a^\dagger)^n] = n(a^\dagger)^{n-1}$, demostrable por induccion usando $[a, a^\dagger] = 1$.

**1.4** Bajo $x \to -x$ en la representacion de Fourier: $\delta(-x) = \frac{1}{2\pi}\int e^{-ikx}\,dk = \frac{1}{2\pi}\int e^{ikx}\,dk = \delta(x)$.

**1.5** $m_e c^2 = 9.109\times10^{-31} \times (3\times10^8)^2 / 1.602\times10^{-13} \approx 0.511$ MeV.

---

## Navegacion del tutorial

[(siguiente) Fundamentos Conceptuales](../01_fundamentos_conceptuales/README.md)
