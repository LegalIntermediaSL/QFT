# Glosario de Notación y Convenciones

Para garantizar la consistencia en todos los módulos del tutorial, se definen a continuación las convenciones estándar utilizadas en este repositorio.

## 1. Espacio-Tiempo y Métrica

- **Firma de la métrica**: Se utiliza la convención de "física de partículas" (West Coast):
  $$\eta_{\mu\nu} = \text{diag}(+1, -1, -1, -1)$$
- **Cuadrivectores**:
  - $x^\mu = (t, \mathbf{x})$
  - $p^\mu = (E, \mathbf{p})$
  - $x_\mu = \eta_{\mu\nu} x^\nu = (t, -\mathbf{x})$
- **Producto escalar**: $p \cdot x = p_\mu x^\mu = Et - \mathbf{p} \cdot \mathbf{x}$.

## 2. Unidades Naturales

Se asumen unidades naturales en la mayoría de los documentos técnicos:
$$c = \hbar = 1$$
En estas unidades, $[\text{masa}] = [\text{energía}] = [\text{tiempo}]^{-1} = [\text{longitud}]^{-1}$.

## 3. Operadores y Cuantización

- **Relaciones de conmutación (Bosones)**: $[a_\mathbf{p}, a_\mathbf{q}^\dagger] = (2\pi)^3 \delta^{(3)}(\mathbf{p}-\mathbf{q})$.
- **Relaciones de anticonmutación (Fermiones)**: $\{a_\mathbf{p}, a_\mathbf{q}^\dagger\} = (2\pi)^3 \delta^{(3)}(\mathbf{p}-\mathbf{q})$.
- **Normalización de estados**: $\langle \mathbf{p} | \mathbf{q} \rangle = (2\pi)^3 2E_\mathbf{p} \delta^{(3)}(\mathbf{p}-\mathbf{q})$ (Normalización relativista).

## 4. Transformadas de Fourier

Para un campo $\phi(x)$, la convención para las transformadas de Fourier es:
$$\phi(x) = \int \frac{d^4p}{(2\pi)^4} e^{-ip \cdot x} \tilde{\phi}(p)$$
$$\tilde{\phi}(p) = \int d^4x e^{ip \cdot x} \phi(x)$$

## 5. Matrices Gamma y Espinores

- **Álgebra de Clifford**: $\{\gamma^\mu, \gamma^\nu\} = 2\eta^{\mu\nu}$.
- **Adjunto de Dirac**: $\bar{\psi} = \psi^\dagger \gamma^0$.
- **Notación de Feynman (Slash)**: $\not{a} = a_\mu \gamma^\mu$.

---
[Volver al Índice del Tutorial](../README.md)
