# Reglas de Feynman para QED

Este documento recopila los elementos visuales y algebraicos necesarios para construir amplitudes de dispersión en Electrodinámica Cuántica (QED).

## 1. Propagadores

```mermaid
graph LR
    subgraph Photon ["Fotón (Spin 1)"]
        P1((u)) --- P2((v))
        style P1 fill:#f9f,stroke:#333
        style P2 fill:#f9f,stroke:#333
    end
    Note1["i·D_uv(p) = -i·n_uv / p²"]
```

```mermaid
graph LR
    subgraph Fermion ["Fermión (Spin 1/2)"]
        F1(( )) -- "p" --> F2(( ))
    end
    Note2["i·S(p) = i / (p_slash - m)"]
```

## 2. Vértice de Interacción

```mermaid
graph TD
    A(( )) --- V{{"γμ"}}
    V --- B(( ))
    V --- C(( ))
    style V fill:#fff,stroke:#333,stroke-width:4px
    Note3["Vértice QED = -i·e·γμ"]
```

## 3. Líneas Externas

| Partícula | Entrada | Salida |
| :--- | :--- | :--- |
| **Electrón** | $u(p,s)$ | $\bar{u}(p,s)$ |
| **Positrón** | $\bar{v}(p,s)$ | $v(p,s)$ |
| **Fotón** | $\epsilon_\mu(p,\lambda)$ | $\epsilon_\mu^*(p,\lambda)$ |

## 4. Resumen de Signos

1. **Bucles de Fermiones**: Cada bucle cerrado de fermiones introduce un factor de $(-1)$.
2. **Estadística**: El intercambio de dos fermiones externos introduce un factor de $(-1)$.
3. **Momentos**: La conservación del momento se aplica en cada vértice: $\sum k_{\text{in}} = \sum k_{\text{out}}$.

---
[Volver al Índice del Tutorial](../README.md)
