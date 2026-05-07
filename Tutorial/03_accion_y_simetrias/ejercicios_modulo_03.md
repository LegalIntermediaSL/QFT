# Ejercicios del Modulo 03: Accion y Simetrias

**Modulo:** 03 — Accion y Simetrias  
**Nivel:** Fundacional  
**Cuadernos de apoyo:**  
- `../../Cuadernos/problemas_resueltos/08_accion_y_noether.ipynb`  
- `../../Cuadernos/ejemplos/04_accion_y_euler_lagrange.ipynb`  
- `../../Cuadernos/ejemplos/23_noether_y_simetrias.ipynb`


## Bloque 1: Verificacion (Nivel 1)

**1.1** La lagrangiana del campo escalar libre es $\mathcal{L} = \frac{1}{2}(\partial_\mu\phi)^2 - \frac{1}{2}m^2\phi^2$. Escribe las ecuaciones de Euler-Lagrange y verifica que se obtiene la ecuacion de Klein-Gordon $(\partial^2 + m^2)\phi = 0$.

**1.2** La accion $S = \int d^4x\,\mathcal{L}$ es un escalar de Lorentz. ¿Por que $d^4x$ es invariante bajo transformaciones de Lorentz propias (con $\det\Lambda = 1$)?

**1.3** El tensor de energia-momentum canonico es $T^{\mu\nu} = \frac{\partial\mathcal{L}}{\partial(\partial_\mu\phi)}\partial^\nu\phi - g^{\mu\nu}\mathcal{L}$. Calcula $T^{00}$ para el campo escalar libre e interpreta el resultado como densidad de energia.

**1.4** Una simetria continua es una transformacion infinitesimal del campo $\phi \to \phi + \epsilon\,\delta\phi$ que deja $\mathcal{L}$ invariante (salvo derivada total). ¿Que condicion debe satisfacer $\delta\phi$?

**1.5** La carga de Noether asociada a una simetria se define como $Q = \int d^3x\,j^0$. Verifica que $\dot{Q} = 0$ si $\partial_\mu j^\mu = 0$ y el campo decae suficientemente rapido en el infinito espacial.

---

## Bloque 2: Derivacion guiada (Nivel 2)

**2.1** Derivacion del teorema de Noether. Sea $\mathcal{L}(\phi, \partial_\mu\phi)$ con variacion $\phi \to \phi + \epsilon\,\delta\phi$.
- (a) Escribe la variacion $\delta\mathcal{L}$ usando regla de la cadena.
- (b) Usa las ecuaciones de Euler-Lagrange para reescribir $\delta\mathcal{L}$ como una divergencia total.
- (c) Identifica la corriente de Noether $j^\mu = \frac{\partial\mathcal{L}}{\partial(\partial_\mu\phi)}\delta\phi$ y muestra $\partial_\mu j^\mu = 0$.

**2.2** Corriente de energia-momentum. La traslacion espaciotemporal $x^\mu \to x^\mu + a^\mu$ induce $\phi(x) \to \phi(x) - a^\nu\partial_\nu\phi(x)$.
- (a) Aplica el teorema de Noether con el parametro $a^\nu$ para derivar el tensor $T^{\mu\nu}$.
- (b) Muestra que la carga conservada asociada a traslaciones temporales es el hamiltoniano $H = \int d^3x\,T^{00}$.
- (c) Muestra que la carga conservada asociada a traslaciones espaciales es el momento $P^i = \int d^3x\,T^{0i}$.

**2.3** Simetrias internas. Considera el campo escalar complejo $\mathcal{L} = \partial_\mu\phi^*\partial^\mu\phi - m^2\phi^*\phi$ con la simetria $\phi \to e^{i\alpha}\phi$, $\phi^* \to e^{-i\alpha}\phi^*$.
- (a) Calcula la corriente de Noether asociada a esta simetria.
- (b) Muestra que $\partial_\mu j^\mu = 0$.
- (c) Interpreta la carga conservada $Q = \int d^3x\,j^0$ y su signo relativo entre particulas y antiparticulas.

---

## Bloque 3: Sintesis (Nivel 3)

**3.1** El teorema de Noether inverso. Enuncia informalmente la reciproca: dada una ley de conservacion, existe una simetria subyacente. Ilustra con tres ejemplos del Modelo Estandar: conservacion de la carga electrica, del numero barionico y del numero leptonico.

**3.2** Conecta accion y cuantizacion. El principio de accion minima $\delta S = 0$ da las ecuaciones de movimiento clasicas. El formalismo de integral de camino las extiende al regimen cuantico mediante $Z = \int \mathcal{D}\phi\,e^{iS[\phi]}$. Sin hacer el calculo:
- Explica informalmente por que las trayectorias clasicas (con $\delta S = 0$) dominan el limite $\hbar \to 0$.
- Relaciona este resultado con el principio de fase estacionaria.

---

## Soluciones sugeridas (Bloque 1)

**1.1** $\frac{\partial\mathcal{L}}{\partial\phi} = -m^2\phi$, $\frac{\partial\mathcal{L}}{\partial(\partial_\mu\phi)} = \partial^\mu\phi$. Las E-L dan $\partial_\mu\partial^\mu\phi + m^2\phi = 0$, es decir $(\partial^2+m^2)\phi=0$.

**1.2** $d^4x \to |\det\Lambda|\,d^4x = d^4x$ para $\Lambda$ propia.

**1.3** $T^{00} = \dot\phi^2 - \mathcal{L} = \frac{1}{2}\dot\phi^2 + \frac{1}{2}(\nabla\phi)^2 + \frac{1}{2}m^2\phi^2$. Es la suma de energias cinetica, gradiente y masa.

**1.4** La variacion de $\mathcal{L}$ debe ser cero o una derivada total: $\delta\mathcal{L} = \partial_\mu K^\mu$ para algun $K^\mu$.

**1.5** $\dot{Q} = \int d^3x\,\partial_t j^0 = -\int d^3x\,\nabla\cdot\mathbf{j} = 0$ por el teorema de Gauss y las condiciones de contorno.

---

## Navegacion del tutorial

[(anterior) Relatividad y Campos](../02_relatividad_y_campos/README.md) | [(siguiente) Campo Escalar](../04_cuantizacion_del_campo_escalar/README.md)
