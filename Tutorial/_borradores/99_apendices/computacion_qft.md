# Herramientas Computacionales en QFT

El estudio moderno de la Teoría Cuántica de Campos (QFT) se apoya fuertemente en sistemas de computación algebraica para manejar trazas de Dirac, índices tensoriales cálculos de diagramas de Feynman a nivel de lazo.

## 1. FeynCalc (Mathematica)

[FeynCalc](https://feyncalc.github.io/) es el estándar de la industria para cálculos simbólicos en física de altas energías.

- **Puntos fuertes**: Manipulación extremadamente eficiente de álgebra de Dirac, reducción de integrales de lazo (vía FeynHelpers) y generación de amplitudes.
- **Uso típico**:
  ```mathematica
  (* Ejemplo básico: Traza de matrices gamma *)
  DiracTrace[GA[mu, nu, rho, sigma]]
  ```
- **Integración**: Los resultados pueden exportarse en formato UFO (Universal FeynRules Output) para ser procesados por herramientas numéricas o scripts de Python.

## 2. Herramientas en Python (Ecosistema HEP)

Aunque Mathematica es el estándar para el álgebra más pesada, Python ha ganado terreno para la automatización, el análisis estadístico y la generación de diagramas.

### SymPy
Es la librería de álgebra simbólica por excelencia en Python. Permite definir álgebras de Clifford y realizar manipulaciones matriciales.
- **Proyecto sugerido**: Utilizar `sympy.physics.hep` (High Energy Physics) para manejar índices y objetos lorentzianos.

### PyFeyn2
Para la creación de diagramas de Feynman con calidad de publicación.
- **Instalación**: `pip install pyfeyn2`
- **Uso**: Permite definir vértices y propagadores de forma programática.

### pySecDec
Herramienta poderosa en Python para la evaluación numérica de integrales de lazo. Suele recibir sus entradas de FeynCalc o herramientas similares.

## 3. Ejemplo: Traza de Dirac en Python (SymPy)

```python
from sympy.physics.quantum.dagger import Dagger
from sympy.physics.hep.gamma_matrices import GammaMatrix as G, gamma_trace
from sympy import symbols

# Ejemplo de traza de dos matrices gamma
mu, nu = symbols('mu nu')
expr = G(mu) * G(nu)
print(f"Trace(gamma^mu * gamma^nu) = {gamma_trace(expr)}")
```

## 4. Comparativa: ¿Cuándo usar qué?

| Herramienta | Caso de uso ideal | Complejidad |
| :--- | :--- | :--- |
| **FeynCalc** | Cálculos de amplitudes de varios lazos, álgebra de Dirac masiva. | Alta (Requiere Mathematica) |
| **SymPy** | Cálculos algebraicos rápidos, integración con scripts de análisis. | Media (Open Source) |
| **pyhf** | Ajustes estadísticos y modelos de límites (LHC). | Baja (Específico para estadística) |

---
[Volver al Índice del Tutorial](../README.md)
