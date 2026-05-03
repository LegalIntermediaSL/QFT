# Representaciones de Lorentz y Espinores

**Nivel:** Fundacional  
**Dificultad:** Media-Alta  
**Tiempo estimado:** 35-50 min  
**Prerequisitos recomendados:** [Campos, Localidad y Causalidad Microfisica](02_campos_localidad_y_causalidad.md) · [Resumen del modulo](README.md)

## Proposito

Este capitulo desarrolla la estructura algebraica del grupo de Lorentz, su cubriente doble $SL(2,\mathbb{C})$ y las representaciones espinoriales que clasifican fermiones en QFT.

## 1. Introduccion: por que importa la estructura de grupo

En los capitulos anteriores se acepto que los campos se clasifican por como transforman bajo el grupo de Lorentz. Se mencionaron escalares, vectores y espinores como tipos distintos. Ahora es el momento de hacer eso preciso.

El grupo de Lorentz no solo organiza la cinematica de los campos. Determina cuantas componentes tiene cada campo, que estadistica sigue y que clase de excitaciones puede describir. Por eso entender sus representaciones no es un lujo matematico: es una condicion necesaria para saber de que tipo son los objetos que la teoria maneja.

## 2. El grupo de Lorentz

Las transformaciones de Lorentz son las transformaciones lineales del espacio-tiempo de Minkowski que preservan la forma cuadratica

$$
x^\mu x_\mu = t^2 - \mathbf{x}^2.
$$

El grupo formado por estas transformaciones es el grupo de Lorentz $O(1,3)$. Dentro de el, la componente conexa que contiene la identidad se llama grupo de Lorentz propio y ortocrono $SO^+(1,3)$.

Sus generadores satisfacen las relaciones de conmutacion

$$
[J^{\mu\nu}, J^{\rho\sigma}] = i\left(\eta^{\nu\rho} J^{\mu\sigma} - \eta^{\mu\rho} J^{\nu\sigma} - \eta^{\nu\sigma} J^{\mu\rho} + \eta^{\mu\sigma} J^{\nu\rho}\right).
$$

Este algebra tiene seis generadores: tres generadores de rotaciones $J_i$ y tres generadores de boosts $K_i$.

## 3. La descomposicion en $SU(2) \times SU(2)$

Una manera especialmente util de entender la estructura del algebra de Lorentz consiste en definir las combinaciones lineales

$$
\mathbf{A} = \frac{1}{2}(\mathbf{J} + i\mathbf{K}), \qquad \mathbf{B} = \frac{1}{2}(\mathbf{J} - i\mathbf{K}).
$$

Estos operadores satisfacen relaciones de conmutacion que corresponden a dos copias independientes del algebra $\mathfrak{su}(2)$:

$$
[A_i, A_j] = i\epsilon_{ijk} A_k, \qquad [B_i, B_j] = i\epsilon_{ijk} B_k, \qquad [A_i, B_j] = 0.
$$

Esto significa que el algebra de Lie del grupo de Lorentz es isomorfa, en el sentido complejo, a

$$
\mathfrak{so}(1,3)_\mathbb{C} \cong \mathfrak{su}(2) \oplus \mathfrak{su}(2).
$$

Las representaciones irreducibles del grupo se clasifican entonces por un par de semienteros $(j_A, j_B)$ donde $j_A, j_B \in \{0, \tfrac{1}{2}, 1, \tfrac{3}{2}, \ldots\}$.

## 4. El cubriente doble $SL(2,\mathbb{C})$

El grupo de Lorentz $SO^+(1,3)$ no es simplemente conexo: su grupo fundamental es $\mathbb{Z}_2$. Para describir fermiones necesitamos trabajar con su cubriente doble universal, que es el grupo $SL(2,\mathbb{C})$, el grupo de matrices complejas $2\times 2$ con determinante 1.

La relacion entre $SL(2,\mathbb{C})$ y $SO^+(1,3)$ se establece mediante el mapa

$$
x^\mu \mapsto X = x^\mu \sigma_\mu = \begin{pmatrix} t+z & x-iy \\ x+iy & t-z \end{pmatrix},
$$

donde $\sigma_\mu = (\mathbf{1}, \vec{\sigma})$ con $\vec{\sigma}$ las matrices de Pauli. Una transformacion de Lorentz actua como

$$
X \mapsto N X N^\dagger, \qquad N \in SL(2,\mathbb{C}).
$$

El determinante de $X$ es $\det X = t^2 - \mathbf{x}^2$, que es justamente la forma cuadratica de Minkowski, y la transformacion la preserva porque $\det(N X N^\dagger) = |\det N|^2 \det X = \det X$.

## 5. Espinores de Weyl: la representacion $(1/2, 0)$

La representacion mas basica del grupo de Lorentz, mas alla del escalar $(0,0)$, es la representacion de dimension 2. Hay dos versiones no equivalentes.

La representacion $(1/2, 0)$ es la representacion fundamental de $SL(2,\mathbb{C})$. Un objeto que transforma en esta representacion es un espinor de Weyl zurdo (o punteado en la notacion de van der Waerden):

$$
\xi_\alpha \mapsto N_\alpha{}^\beta \, \xi_\beta, \qquad \alpha, \beta \in \{1,2\}.
$$

La representacion $(0, 1/2)$ es la representacion conjugada. Un espinor de Weyl diestro transforma como

$$
\bar\eta_{\dot\alpha} \mapsto (N^*)_{\dot\alpha}{}^{\dot\beta} \, \bar\eta_{\dot\beta}.
$$

La notacion de punto sobre el indice sirve exactamente para distinguir estas dos representaciones.

## 6. Notacion dotted/undotted de van der Waerden

La notacion estandar en teoria de campos introduce indices con y sin punto para distinguir representaciones quirales:

- Indices sin punto $\alpha, \beta, \ldots$: espinores de Weyl en la representacion $(1/2, 0)$, llamados espinores zurdos.
- Indices con punto $\dot\alpha, \dot\beta, \ldots$: espinores de Weyl en la representacion $(0, 1/2)$, llamados espinores diestros.

La metrica espinorial $\epsilon_{\alpha\beta}$ (con $\epsilon_{12} = -\epsilon_{21} = 1$) eleva y baja indices espinoriales:

$$
\xi^\alpha = \epsilon^{\alpha\beta} \xi_\beta, \qquad \xi_\alpha = \epsilon_{\alpha\beta} \xi^\beta.
$$

Los productos invariantes de Lorentz se construyen contrayendo indices del mismo tipo:

$$
\xi\eta \equiv \xi^\alpha \eta_\alpha = \epsilon^{\alpha\beta}\xi_\beta \eta_\alpha, \qquad \bar\xi\bar\eta \equiv \bar\xi_{\dot\alpha}\bar\eta^{\dot\alpha}.
$$

## 7. Matrices sigma y sigma-bar

Las matrices sigma y sigma-bar proporcionan los bloques de construccion para pasar entre representaciones espinoriales y vectoriales:

$$
\sigma^\mu_{\alpha\dot\alpha} = (\mathbf{1}, \vec\sigma)_{\alpha\dot\alpha}, \qquad \bar\sigma^{\mu\,\dot\alpha\alpha} = (\mathbf{1}, -\vec\sigma)^{\dot\alpha\alpha}.
$$

Con estas matrices se puede descomponer un vector de Lorentz $v^\mu$ en un espinor bivaluado:

$$
v^{\alpha\dot\alpha} = \sigma^\mu{}^{\alpha\dot\alpha} v_\mu.
$$

Esto corresponde a la representacion $(1/2, 1/2)$, que es la del vector de Lorentz.

## 8. El espinor de Dirac

Un espinor de Dirac de 4 componentes combina un espinor de Weyl zurdo y uno diestro:

$$
\Psi = \begin{pmatrix} \xi_\alpha \\ \bar\chi^{\dot\alpha} \end{pmatrix}.
$$

Esta combinacion corresponde a la representacion reducible $(1/2, 0) \oplus (0, 1/2)$. La ecuacion de Dirac mezcla las dos componentes quirales mediante el termino de masa:

$$
(i\gamma^\mu \partial_\mu - m)\Psi = 0.
$$

En la representacion de Weyl, las matrices gamma toman la forma

$$
\gamma^\mu = \begin{pmatrix} 0 & \sigma^\mu \\ \bar\sigma^\mu & 0 \end{pmatrix}.
$$

## 9. Conexion con la estadistica de fermiones

La posibilidad de tener representaciones espinoriales, que requieren una rotacion de $4\pi$ para volver al estado inicial, tiene consecuencias fisicas directas. El teorema espin-estadistica establece que los campos en representaciones de spin semientero deben cuantizarse con anticonmutadores.

Esto no es un postulado separado. Es una consecuencia de la estructura del grupo de Lorentz combinada con las exigencias de causalidad y positividad de la energia. El spin semientero implica estadistica de Fermi-Dirac.

La conexion se puede resumir:

- representaciones con $j_A + j_B \in \mathbb{Z}$: bosones, cuantizacion con conmutadores;
- representaciones con $j_A + j_B \in \mathbb{Z} + 1/2$: fermiones, cuantizacion con anticonmutadores.

## 10. Tabla de representaciones fundamentales

Las representaciones mas importantes en QFT se resumen en la siguiente tabla:

| Representacion | Dimension | Objeto fisico |
|:---|:---|:---|
| $(0,0)$ | 1 | Campo escalar |
| $(1/2, 0)$ | 2 | Espinor de Weyl zurdo |
| $(0, 1/2)$ | 2 | Espinor de Weyl diestro |
| $(1/2, 0) \oplus (0,1/2)$ | 4 | Espinor de Dirac |
| $(1/2, 1/2)$ | 4 | Campo vectorial |
| $(1, 0) \oplus (0, 1)$ | 6 | Tensor antisimetrico |

## 11. Espinores de Majorana

Una posibilidad adicional surge cuando las dos representaciones quirales del espinor de Dirac estan relacionadas por conjugacion. Un espinor de Majorana satisface la condicion

$$
\Psi = \Psi^C \equiv C\bar\Psi^T,
$$

donde $C$ es la matriz de conjugacion de carga. En terminos de componentes de Weyl, esto significa que el espinor diestro es el conjugado del zurdo:

$$
\Psi_M = \begin{pmatrix} \xi_\alpha \\ i\sigma^2 \xi^* \end{pmatrix}.
$$

Los espinores de Majorana tienen la mitad de grados de libertad que los de Dirac. Son su propia antiparticula. Esta propiedad los hace relevantes en supersimetria y en la discusion de masas de neutrinos.

## 12. Invariantes espinoriales y bilineales

Para construir lagrangianos con campos fermionicos hace falta saber que combinaciones son invariantes de Lorentz. Los bilineales fundamentales se construyen con la metrica espinorial o con matrices gamma:

$$
\bar\Psi \Psi = \Psi^\dagger \gamma^0 \Psi \quad \text{(escalar)},
$$
$$
\bar\Psi \gamma^\mu \Psi \quad \text{(vector)},
$$
$$
\bar\Psi \gamma^\mu \gamma^\nu \Psi \quad \text{(tensor)},
$$
$$
\bar\Psi \gamma^5 \Psi \quad \text{(pseudoescalar)},
$$
$$
\bar\Psi \gamma^\mu \gamma^5 \Psi \quad \text{(pseudovector)}.
$$

donde $\gamma^5 = i\gamma^0\gamma^1\gamma^2\gamma^3$.

Estos cinco bilineales forman una base completa del espacio de matrices $4\times 4$ y son los bloques con los que se construyen las interacciones en lagrangianos fermionicos.

## 13. De la representacion a la fisica

La clasificacion de representaciones no es solo taxonomia formal. Tiene consecuencias directas en la construccion de la teoria:

- El tipo de representacion determina el numero de grados de libertad del campo.
- Determina que invariantes pueden escribirse en el lagrangiano.
- Determina la estadistica cuantica.
- Determina como transforma el campo bajo paridad, que intercambia $(j_A, j_B)$ con $(j_B, j_A)$.

Por eso antes de escribir cualquier lagrangiano conviene tener claro en que representacion vive cada campo de la teoria.

## 14. Advertencias de notacion

- En diferentes textos los puntos sobre los indices aparecen o no dependiendo de la convencion. Algunos usan indices con barra, otros con punto.
- La convencion sobre cual componente es zurda y cual es diestra puede variar. Lo importante es la consistencia interna.
- Las matrices sigma de Pauli pueden definirse con signos distintos en diferentes referencias. Conviene fijarse en la metrica de Minkowski usada.

## Cuaderno asociado

- Consulta los cuadernos asociados de este bloque en [Resumen del modulo](README.md) para reforzar el capitulo con practica guiada.

## 15. Preguntas de comprobacion

- Por que el grupo de Lorentz necesita un cubriente doble para describir fermiones.
- Que diferencia hay entre la representacion $(1/2, 0)$ y la $(0, 1/2)$ del grupo de Lorentz.
- Que significa en terminos fisicos que un espinor sea zurdo o diestro.
- Por que un espinor de Majorana tiene la mitad de grados de libertad que uno de Dirac.
- Como se relaciona el spin de una representacion con su estadistica cuantica.

## 16. Ejercicios sugeridos

1. Verificar que la combinacion $\xi^\alpha \eta_\alpha$ es invariante bajo transformaciones de Lorentz usando la propiedad $N^T \epsilon N = \epsilon$ para $N \in SL(2,\mathbb{C})$.
2. Construir explicitamente las matrices gamma en la representacion de Weyl y verificar que satisfacen la algebra de Clifford $\{\gamma^\mu, \gamma^\nu\} = 2\eta^{\mu\nu}$.
3. Mostrar que el bilineal $\bar\Psi\Psi$ es un escalar de Lorentz pero $\Psi^T\Psi$ no lo es.
4. A partir de la tabla de representaciones, identificar que representacion corresponde al campo de Yang-Mills $A_\mu^a$ y al tensor de curvatura $F_{\mu\nu}^a$.

## 17. Cierre

El grupo de Lorentz no es solo la simetria cinematica de la teoria. Es el organizador de todo su contenido de campos. La clasificacion de representaciones por pares $(j_A, j_B)$ proporciona la respuesta sistematica a la pregunta "de que tipo puede ser un campo relativista", y la conexion con $SL(2,\mathbb{C})$ revela por que los fermiones exigen cuantizacion con anticonmutadores.

## 18. Referencias y lecturas recomendadas

- Base: Peskin y Schroeder, capitulo 3, representaciones espinoriales y algebra de Clifford.
- Complementaria: Tong, notas sobre espinores de Weyl y notacion dotted/undotted.
- Profundizacion: Wess y Bagger, formulacion espinorial en SUSY; Streater y Wightman, estructura axiomatica y teorema espin-estadistica.


---

## Navegacion del tutorial

[(anterior) Campos, Localidad y Causalidad Microfisica](02_campos_localidad_y_causalidad.md) | [(siguiente) Clasificacion de Campos por Spin y Estados de Wigner](04_clasificacion_de_campos_por_spin.md)
