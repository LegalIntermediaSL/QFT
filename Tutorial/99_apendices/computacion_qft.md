# Herramientas Computacionales en QFT

Este apendice resume herramientas utiles para calculo simbolico, automatizacion y exploracion computacional en teoria cuantica de campos. No pretende sustituir a un curso de software cientifico, sino orientar sobre que tipo de herramienta conviene usar segun el problema.

La idea de fondo es simple: en QFT moderna no todo se hace a mano. Gran parte del trabajo real combina intuicion teorica con sistemas de algebra simbolica, evaluacion numerica y automatizacion de tareas repetitivas.

## 1. FeynCalc (Mathematica)

[FeynCalc](https://feyncalc.github.io/) es una de las herramientas mas usadas para calculos simbolicos en fisica de altas energias.

- **Puntos fuertes**: Manipulacion de algebra de Dirac, trazas gamma, tensores de Lorentz, amplitudes y apoyo para integrales de lazo mediante complementos.
- **Uso tipico**:

```mathematica
(* Ejemplo basico: traza de matrices gamma *)
DiracTrace[GA[mu, nu, rho, sigma]]
```

- **Cuando conviene**: cuando el cuello de botella principal es algebra simbolica relativista pesada.

FeynCalc resulta especialmente comodo si ya se trabaja en Mathematica y se necesita una herramienta madura para pasar de expresiones lagrangianas a amplitudes y simplificaciones algebraicas serias.

## 2. Herramientas en Python

Aunque Mathematica domina buena parte del algebra simbolica tradicional, Python ha ganado mucho terreno para automatizacion, analisis numerico, visualizacion e integracion con pipelines reproducibles.

### SymPy

Es la libreria de algebra simbolica por excelencia en Python. Permite definir algebras, manipular matrices y trabajar con objetos simbolicos de forma bastante flexible.

- **Proyecto sugerido**: utilizar `sympy.physics.hep` para objetos de altas energias y trazas sencillas.
- **Cuando conviene**: para prototipos rapidos, cuadernos reproducibles y flujos totalmente open source.

### PyFeyn2

Herramienta orientada a la creacion de diagramas de Feynman con calidad de publicacion.

- **Instalacion**: `pip install pyfeyn2`
- **Cuando conviene**: cuando se necesita generar diagramas de forma programatica y consistente con un documento o cuaderno.

### pySecDec

Herramienta para evaluacion numerica de integrales de lazo complicadas.

- **Cuando conviene**: cuando la parte simbolica ya esta preparada y el problema real pasa a ser la evaluacion numerica de integrales no triviales.

## 3. Ejemplo: Traza de Dirac en Python

```python
from sympy.physics.hep.gamma_matrices import GammaMatrix as G, gamma_trace
from sympy import symbols

mu, nu = symbols('mu nu')
expr = G(mu) * G(nu)
print(gamma_trace(expr))
```

Este tipo de ejemplo no sustituye a paquetes mas especializados, pero sirve muy bien para cuadernos pedagogicos y comprobaciones pequenas dentro del tutorial.

## 4. Herramientas para fenomenologia y estadistica

En un flujo mas cercano a fenomenologia o analisis de datos, suelen entrar otras herramientas complementarias:

- `pyhf` para ajustes estadisticos y construccion de limites;
- bibliotecas de Python cientifico como `numpy`, `scipy` y `matplotlib`;
- herramientas de Monte Carlo y generadores de eventos en contextos mas avanzados.

La leccion practica es que no existe una unica herramienta universal. El mejor entorno depende de si el problema es algebraico, numerico, estadistico o de visualizacion.

## 5. Comparativa rapida

| Herramienta | Caso de uso ideal | Comentario |
| :--- | :--- | :--- |
| **FeynCalc** | Algebra de Dirac, amplitudes y trazas complejas | Muy potente, pero requiere Mathematica |
| **SymPy** | Prototipos simbolicos y cuadernos reproducibles | Flexible y open source |
| **PyFeyn2** | Diagramas de Feynman programaticos | Bueno para documentacion y figuras |
| **pySecDec** | Integrales de lazo numericas | Especializado |
| **pyhf** | Ajustes y limites estadisticos | Mas orientado a fenomenologia experimental |

## 6. Flujo de trabajo razonable

Una estrategia muy realista para estudiantes e investigadores junior es:

1. entender primero el calculo a mano en un ejemplo pequeno;
2. usar software para comprobar trazas, signos y factores;
3. automatizar solo cuando el problema ya esta conceptualmente claro;
4. documentar bien que parte del resultado es analitica y cual es puramente computacional.

Este orden ayuda a evitar dos errores comunes:

- depender del software sin entender la estructura fisica;
- intentar hacerlo todo a mano cuando el problema ya exige automatizacion seria.

## 7. Casos de uso tipicos

### Si quieres comprobar una traza o una identidad corta

Usa `SymPy` o `FeynCalc`, segun el entorno que ya manejes.

### Si quieres producir una figura limpia de un diagrama

Usa `PyFeyn2` o una herramienta similar de diagramacion.

### Si quieres evaluar una integral de lazo compleja

Piensa en un flujo mixto: algebra simbolica en FeynCalc y evaluacion numerica con `pySecDec` u otra herramienta especializada.

### Si quieres documentar un ejemplo del tutorial

Conviene priorizar Python y notebooks cuando el objetivo principal es pedagogico y reproducible.

## 8. Buenas practicas

- valida siempre con un caso simple conocido;
- deja claras las convenciones de metrica y normalizacion;
- documenta versiones y dependencias si el resultado debe reproducirse;
- no mezcles sin control notacion del tutorial con notacion por defecto del paquete;
- conserva ejemplos minimos que permitan detectar si un cambio de libreria rompió signos o factores.

## 9. Advertencias utiles

- Un resultado computacional no sustituye la interpretacion fisica.
- Distintos paquetes usan convenciones diferentes de signos, metricas o normalizaciones.
- Siempre conviene validar con un caso simple conocido antes de confiar en un pipeline largo.
- La reproducibilidad importa: cuadernos, scripts y versiones de dependencias deben quedar claros.

## 10. Cierre

Las herramientas computacionales no reemplazan la intuicion teorica, pero amplian enormemente el tipo de problemas que pueden abordarse con rigor. Usadas bien, permiten dedicar menos tiempo a algebra mecanica y mas tiempo a interpretar la fisica.

---
[Volver al Índice del Tutorial](../README.md)
