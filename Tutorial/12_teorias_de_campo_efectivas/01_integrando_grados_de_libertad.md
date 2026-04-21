# Integrando grados de libertad: El corazón de las EFT

## 1. La Filosofía de Escalas

En física, rara vez necesitamos conocer la estructura atómica para entender cómo fluye el agua en una tubería. Del mismo modo, en QFT, si estamos interesados en procesos a baja energía ($E \ll \Lambda$), los detalles de lo que ocurre a energías mucho más altas ($\Lambda$) pueden ser simplificados.

Imaginemos una teoría con dos campos:
- $\phi$: un campo ligero de masa $m$.
- $\Phi$: un campo muy pesado de masa $M \gg m$.

Si realizamos un experimento a energías $E \sim m$, no tenemos suficiente energía para crear partículas $\Phi$ reales. Sin embargo, $\Phi$ aparece como **partícula virtual** en los diagramas, afectando a la dinámica de $\phi$.

## 2. El Enfoque de Integral de Camino

Desde el formalismo de integral de camino, podemos "eliminar" el campo pesado $\Phi$ integrando sobre él:

$$Z[J] = \int \mathcal{D}\phi \int \mathcal{D}\Phi \exp(i S[\phi, \Phi] + i \int J\phi)$$

Definimos una **Acción Efectiva** $S_{eff}[\phi]$ tal que:
$$\exp(i S_{eff}[\phi]) = \int \mathcal{D}\Phi \exp(i S[\phi, \Phi])$$

La nueva acción $S_{eff}[\phi]$ contendrá únicamente el campo ligero, pero sus acoplamientos habrán sido modificados por los efectos del campo pesado.

## 3. Clasificación de Operadores

Al expandir $S_{eff}$, obtenemos una serie infinita de operadores locales:
$$\mathcal{L}_{eff} = \mathcal{L}_{d \le 4} + \sum_{n > 4} \frac{c_n}{\Lambda^{n-4}} \mathcal{O}_n$$

Donde $\Lambda \sim M$. Los operadores se clasifican según su dimensión de masa $d$:

1.  **Relevantes ($d < 4$)**: Crecen a bajas energías (ej: términos de masa).
2.  **Marginales ($d = 4$)**: Se mantienen constantes (logarítmicamente) (ej: acoplamientos gauge).
3.  **Irrelevantes ($d > 4$)**: Se desvanecen como $(E/\Lambda)^{n-4}$. 

> [!TIP]
> La razón por la que la QFT estándar funciona tan bien es que a bajas energías los operadores irrelevantes son indetectables. Sin embargo, son precisamente estos operadores los que nos dan pistas sobre la física que hay "más allá" (ej: el decaimiento del protón o las masas de los neutrinos).

## 4. Teorema de Desacoplamiento

El teorema de **Appelquist-Carazzone** establece que, en teorías renormalizables, los efectos de las partículas pesadas se manifiestan únicamente como una redefinición de los parámetros de la teoría ligera (renormalización), salvo por correcciones que desaparecen como $1/M^2$.

## Ejercicios de Reflexión

1.  **La Teoría de Fermi**: Investigue cómo la interacción débil (mediada por los bosones $W$ y $Z$) se reduce a la teoría de Fermi de 4 fermiones cuando $E \ll M_W$. ¿Qué dimensión tiene el operador de Fermi?
2.  **Gravedad**: ¿Por qué decimos que la relatividad general de Einstein es una EFT? ¿Cuál sería la escala $\Lambda$ en este caso?
3.  **Análisis Dimensional**: Verifique por qué un término de interacción $\lambda \phi^6$ en 4 dimensiones tiene una constante de acoplamiento con dimensiones de $[M]^{-2}$.
