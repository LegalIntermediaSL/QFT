# Ejercicios del Modulo 04: Cuantizacion del Campo Escalar

**Modulo:** 04 — Cuantizacion del Campo Escalar  
**Nivel:** Nucleo  
**Cuadernos de apoyo:**  
- `../../Cuadernos/problemas_resueltos/09_cuantizacion_del_campo_escalar.ipynb`  
- `../../Cuadernos/ejemplos/05_cuantizacion_del_campo_escalar.ipynb`  
- `../../Cuadernos/ejemplos/08_propagador_libre_y_causalidad.ipynb`


## Bloque 1: Verificacion (Nivel 1)

**1.1** El campo escalar se expande en modos de Fourier como $\phi(\mathbf{x},t) = \int \frac{d^3p}{(2\pi)^3}\frac{1}{\sqrt{2\omega_\mathbf{p}}}\left(a_\mathbf{p}\,e^{ip\cdot x} + a^\dagger_\mathbf{p}\,e^{-ip\cdot x}\right)$ con $\omega_\mathbf{p} = \sqrt{\mathbf{p}^2 + m^2}$. Verifica que esta expresion satisface la ecuacion de Klein-Gordon.

**1.2** La relacion de conmutacion canonica es $[\phi(\mathbf{x},t), \pi(\mathbf{y},t)] = i\delta^{(3)}(\mathbf{x}-\mathbf{y})$. Demuestra que esto es consistente con $[a_\mathbf{p}, a^\dagger_\mathbf{q}] = (2\pi)^3\delta^{(3)}(\mathbf{p}-\mathbf{q})$.

**1.3** El estado de vacio $|0\rangle$ satisface $a_\mathbf{p}|0\rangle = 0$ para todo $\mathbf{p}$. Calcula la energia del vacio $\langle 0|H|0\rangle$ e identifica la divergencia que aparece.

**1.4** La energia normal-ordenada del campo escalar es $H = \int \frac{d^3p}{(2\pi)^3}\,\omega_\mathbf{p}\,a^\dagger_\mathbf{p}a_\mathbf{p}$. ¿Como se interpreta la cantidad $a^\dagger_\mathbf{p}a_\mathbf{p}$ en el estado $|n_\mathbf{p}\rangle$?

**1.5** El propagador de Feynman se define como $\Delta_F(x-y) = \langle 0|T\phi(x)\phi(y)|0\rangle$ donde $T$ es el producto ordenado temporalmente. Escribe $\Delta_F$ en espacio de momentos e identifica el polo en $p^2 = m^2$.

---

## Bloque 2: Derivacion guiada (Nivel 2)

**2.1** Campo escalar clasico y modos normales. El campo libre $\phi(x)$ en espacio de Fourier tiene modos $\tilde\phi(\mathbf{k},t) = \int d^3x\,e^{-i\mathbf{k}\cdot\mathbf{x}}\phi(\mathbf{x},t)$.
- (a) Sustituye la expansion en la ecuacion de Klein-Gordon para mostrar que cada modo satisface $\ddot{\tilde\phi}(\mathbf{k},t) + \omega_\mathbf{k}^2\tilde\phi(\mathbf{k},t) = 0$.
- (b) Identifica la frecuencia $\omega_\mathbf{k}$ y argumenta que cada modo es un oscilador armonico.
- (c) Explica por que la cuantizacion del campo libre es equivalente a cuantizar infinitos osciladores independientes.

**2.2** Espacio de Fock. A partir del vacio $|0\rangle$ y los operadores $a^\dagger_\mathbf{p}$, construye el espacio de Fock:
- (a) Escribe el estado de una particula de momento $\mathbf{p}$: $|\mathbf{p}\rangle = a^\dagger_\mathbf{p}|0\rangle$.
- (b) Calcula la norma $\langle \mathbf{p}|\mathbf{q}\rangle$ y explica el factor de normalizacion que aparece.
- (c) Escribe el operador numero de particulas $N = \int \frac{d^3p}{(2\pi)^3}a^\dagger_\mathbf{p}a_\mathbf{p}$ y verifica que $[N, a^\dagger_\mathbf{p}] = a^\dagger_\mathbf{p}$.

**2.3** Propagador y microcausalidad. El propagador de Feynman en espacio de momentos es $\Delta_F(p) = \frac{i}{p^2 - m^2 + i\epsilon}$.
- (a) Explica el papel de la prescripcion $i\epsilon$ para la integracion en el plano complejo de $p^0$.
- (b) Muestra que el propagador tiene polos en $p^0 = \pm(\omega_\mathbf{p} - i\epsilon)$.
- (c) Argumenta como el contorno de integracion selecciona la solucion de energia positiva para $x^0 > y^0$ y la de energia negativa para $x^0 < y^0$.

---

## Bloque 3: Sintesis (Nivel 3)

**3.1** Divergencia de energia del vacio y su papel en la cosmologia. La contribucion de vacio al hamiltoniano $E_0 = \frac{1}{2}\int \frac{d^3p}{(2\pi)^3}\omega_\mathbf{p}$ diverge cuarticamente en UV.
- Explica que regularizacion (cutoff, dimensional) cambia el valor numerico pero no resuelve el problema conceptual.
- Comenta como la constante cosmologica observada es 120 ordenes de magnitud menor que la prediccion naive de la QFT, y que esto constituye uno de los problemas abiertos mas famosos de la fisica teorica.

**3.2** Del campo escalar al campo de Dirac. El campo escalar tiene conmutadores $[\phi, \pi] = i\delta^{(3)}$. Para fermiones, se usan anticonmutadores $\{\psi, \pi\} = i\delta^{(3)}$. Sin hacer el calculo completo:
- Argumenta por que usar conmutadores para fermiones conduciria a un espectro de energia no acotado inferiormente.
- Relaciona este resultado con el principio de exclusion de Pauli y el teorema spin-estadistica.

---

## Soluciones sugeridas (Bloque 1)

**1.1** Aplica $\partial^2 + m^2$ a la expansion: cada sumando $e^{\pm ip\cdot x}$ da $(-p^2 + m^2)e^{\pm ip\cdot x} = 0$ si $p^2 = m^2$, lo que verifica la ecuacion.

**1.2** Sustituye $\phi$ y $\pi = \dot\phi$ en el conmutador canonico, usa $[a_\mathbf{p}, a^\dagger_\mathbf{q}] = (2\pi)^3\delta^{(3)}(\mathbf{p}-\mathbf{q})$ y obtiene $i\delta^{(3)}(\mathbf{x}-\mathbf{y})$ despues de integrar.

**1.3** $\langle 0|H|0\rangle = \int \frac{d^3p}{(2\pi)^3}\frac{\omega_\mathbf{p}}{2}\cdot(2\pi)^3\delta^{(3)}(0)$, diverge tanto en UV (grandes $|\mathbf{p}|$) como en IR ($\delta(0)$).

**1.4** $a^\dagger_\mathbf{p}a_\mathbf{p}$ es el operador numero de particulas de momento $\mathbf{p}$. En el estado $|n_\mathbf{p}\rangle$ su valor esperado es $n_\mathbf{p}$.

**1.5** $\Delta_F(p) = \frac{i}{p^2 - m^2 + i\epsilon}$. El polo esta en $p^2 = m^2$, es decir, en la capa de masa.

---

## Navegacion del tutorial

[(anterior) Accion y Simetrias](../03_accion_y_simetrias/README.md) | [(siguiente) Interacciones y Perturbaciones](../05_interacciones_y_perturbaciones/README.md)
