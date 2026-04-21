# Espinores de Weyl, Majorana y Teoría de Grupos

## 1. El Grupo de Lorentz y sus Representaciones

Para entender profundamente los espinores, debemos abandonar momentáneamente la "intuición de partículas" y mirar las simetrías del espacio-tiempo. El grupo de Lorentz restringido $SO^+(1,3)$ es localmente isomorfo a $SL(2, \mathbb{C})$.

Cualquier campo en QFT debe transformar bajo una representación irreducible del grupo de Lorentz. Estas representaciones se clasifican mediante dos números $(j_L, j_R)$ (donde $j = 0, 1/2, 1, \dots$).

- **Escalar**: $(0,0)$
- **Vector**: $(1/2, 1/2)$
- **Espinor de Weyl Izquierdo**: $(1/2, 0)$
- **Espinor de Weyl Derecho**: $(0, 1/2)$
- **Espinor de Dirac**: $(1/2, 0) \oplus (0, 1/2)$

## 2. Espinores de Weyl

Un espinor de Dirac $\psi$ de 4 componentes puede descomponerse en la **base Quiral** (o base de Weyl) en dos espinores de 2 componentes:

$$\psi = \begin{pmatrix} \psi_L \\ \psi_R \end{pmatrix}$$

Donde los operadores de proyección quiral son:
$$P_L = \frac{1 - \gamma^5}{2}, \quad P_R = \frac{1 + \gamma^5}{2}$$

### Transformación
Bajo una rotación o boost, $\psi_L$ y $\psi_R$ transforman de forma distinta:
- $\psi_L \to e^{i\vec{\theta}\cdot\frac{\vec{\sigma}}{2} - \vec{\beta}\cdot\frac{\vec{\sigma}}{2}} \psi_L$
- $\psi_R \to e^{i\vec{\theta}\cdot\frac{\vec{\sigma}}{2} + \vec{\beta}\cdot\frac{\vec{\sigma}}{2}} \psi_R$

Note que la parte imaginaria (rotación) es igual, pero el boost (parte real) tiene signos opuestos. Esto significa que la quiralidad está íntimamente ligada a cómo el campo percibe el movimiento en el espacio-tiempo.

## 3. Espinores de Majorana

Un espinor de Majorana es aquel que es igual a su propio conjugado de carga:
$$\psi = \psi^C$$

Desde un punto de vista físico, esto significa que **la partícula es su propia antipartícula**.

### El término de masa de Majorana
Mientras que la masa de Dirac conecta $\psi_L$ con $\psi_R$ ($m \bar{\psi}_L \psi_R + h.c.$), la masa de Majorana conecta un componente consigo mismo:
$$\mathcal{L}_{maj} = -\frac{1}{2} M (\psi_L^T C \psi_L + h.c.)$$

Esta distinción es fundamental en la física de neutrinos (mecanismo Seesaw).

## 4. Resumen Comparativo

| Propiedad | Dirac | Weyl | Majorana |
| :--- | :--- | :--- | :--- |
| Componentes | 4 complejas | 2 complejas | 4 (pero $\psi=\psi^C$) |
| Masa | $m \neq 0$ | $m = 0$ (usualmente) | $M \neq 0$ |
| Grados de libertad | 4 (part./anti. + espín) | 2 | 2 |
| Conservación de carga | Sí (U(1)) | Puede | No (rompe L o B) |

## Ejercicios Sugeridos

1. **Invariancia**: Demuestre que el término de masa de Dirac $\bar{\psi}\psi$ es invariante bajo Lorentz usando la descomposición de Weyl.
2. **Matrices Sigma**: Verifique que $\sigma^\mu = (1, \vec{\sigma})$ y $\bar{\sigma}^\mu = (1, -\vec{\sigma})$ permiten escribir la ecuación de Dirac para fermiones sin masa como dos ecuaciones desacopladas de Weyl.
3. **Quiralidad vs Helicidad**: Investigue por qué para partículas con masa, la quiralidad no es una constante del movimiento, mientras que para $m=0$ coincide con la helicidad.
