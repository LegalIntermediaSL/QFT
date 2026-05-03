# Clasificacion de Campos por Spin y Estados de Wigner

**Nivel:** Fundacional  
**Dificultad:** Media-Alta  
**Tiempo estimado:** 35-50 min  
**Prerequisitos recomendados:** [Representaciones de Lorentz y Espinores](03_representaciones_de_lorentz_y_espinores.md) · [Resumen del modulo](README.md)

## Proposito

Este capitulo desarrolla la clasificacion de Wigner de las particulas relativistas segun su masa y espin o helicidad, y conecta esa clasificacion con los tipos de campo que se usan en QFT.

## 1. Introduccion: de grupos a particulas

En el capitulo anterior se clasificaron las representaciones del grupo de Lorentz. Pero para clasificar particulas fisicas hace falta un paso mas: las particulas no son solo objetos que transforman bajo Lorentz, sino estados del espacio de Hilbert del sistema. La clasificacion relevante es la del grupo de Poincare completo, que incluye tambien traslaciones espacio-temporales.

El analisis sistematico de las representaciones irreducibles unitarias del grupo de Poincare fue realizado por Eugene Wigner en 1939. Sus resultados tienen un significado fisico profundo: cada tipo de particula elemental corresponde a una representacion irreducible del grupo de Poincare.

## 2. El grupo de Poincare

El grupo de Poincare es el grupo de simetrias del espacio-tiempo de Minkowski. Combina:

- traslaciones espacio-temporales: $x^\mu \mapsto x^\mu + a^\mu$;
- transformaciones de Lorentz: $x^\mu \mapsto \Lambda^\mu{}_\nu x^\nu$.

Sus generadores son el 4-momento $P^\mu$ (generador de traslaciones) y el tensor de momento angular $M^{\mu\nu}$ (generador de Lorentz). Las relaciones de conmutacion son

$$
[P^\mu, P^\nu] = 0,
$$
$$
[M^{\mu\nu}, P^\rho] = i(\eta^{\nu\rho}P^\mu - \eta^{\mu\rho}P^\nu),
$$
$$
[M^{\mu\nu}, M^{\rho\sigma}] = i(\eta^{\nu\rho}M^{\mu\sigma} - \eta^{\mu\rho}M^{\nu\sigma} - \eta^{\nu\sigma}M^{\mu\rho} + \eta^{\mu\sigma}M^{\nu\rho}).
$$

## 3. Los operadores de Casimir

Para clasificar representaciones se buscan operadores que conmuten con todos los generadores del grupo, los operadores de Casimir. El grupo de Poincare tiene dos:

El primero es la masa al cuadrado:
$$
P^2 = P^\mu P_\mu = m^2.
$$

El segundo se construye a traves del vector de Pauli-Lubanski

$$
W^\mu = -\frac{1}{2}\epsilon^{\mu\nu\rho\sigma} P_\nu M_{\rho\sigma},
$$

cuyo cuadrado es

$$
W^2 = W^\mu W_\mu = -m^2 s(s+1).
$$

Los valores de estos dos Casimir, $m^2$ y $s$, clasifican completamente las representaciones irreducibles del grupo de Poincare.

## 4. Las clases de Wigner

Dependiendo del signo y valor de $P^2$, las representaciones se dividen en clases:

**Clase 1: particulas masivas** ($P^2 = m^2 > 0$, $P^0 > 0$)

Se puede ir al sistema de referencia en reposo donde $P^\mu = (m, \mathbf{0})$. El subgrupo que deja fijo este momento es el grupo de rotaciones $SO(3)$. Las representaciones se etiquetan por el spin $s = 0, 1/2, 1, 3/2, \ldots$, con $2s+1$ estados de polarizacion.

**Clase 2: particulas no masivas** ($P^2 = 0$, $P^0 > 0$)

No existe sistema de referencia en reposo. El subgrupo de estabilidad del momento nulo es $ISO(2)$, el grupo euclideo del plano. Las representaciones fisicas se etiquetan por la helicidad $\lambda$, que toma valores $\lambda = \pm s$ para un campo de spin $s$. Solo dos estados de polarizacion para $s \geq 1/2$.

**Otras clases:** taquiones ($P^2 < 0$), vacio ($P^\mu = 0$) y casos exoticos que no corresponden a particulas fisicas observadas.

## 5. Particulas masivas y estados de espin

Para una particula masiva de spin $s$, los estados fisicos en el sistema de referencia del centro de masa se etiquetan $|m, s, m_s\rangle$ con $m_s = -s, -s+1, \ldots, s$.

Al ir a un momento arbitrario $\mathbf{p}$, se aplica un boost estandar $L(p)$ que lleva el estado en reposo al estado con momento $\mathbf{p}$:

$$
|p, m_s\rangle = U(L(p))|m, s, m_s\rangle.
$$

Bajo una transformacion de Lorentz general, el estado transforma con una matriz de Wigner $D^{(s)}_{m_s' m_s}(W)$ donde $W = L^{-1}(\Lambda p) \Lambda L(p)$ es la rotacion de Wigner.

## 6. Particulas no masivas y helicidad

Para particulas no masivas, la helicidad es la proyeccion del espin sobre la direccion del momento:

$$
\lambda = \hat{\mathbf{p}} \cdot \mathbf{J}.
$$

Los fotones tienen helicidad $\lambda = \pm 1$ (los dos estados de polarizacion circular). Los gravitones tendrian helicidad $\lambda = \pm 2$. Los neutrinos quirales tienen helicidad definida.

A diferencia del spin, la helicidad es un escalar de Lorentz para particulas no masivas. Bajo rotaciones se preserva, y bajo boosts tambien, aunque la nocion de "direccion del espin" puede cambiar.

## 7. Campo escalar: representacion $(0,0)$

Un campo escalar $\phi(x)$ pertenece a la representacion trivial del grupo de Lorentz. Transforma como

$$
\phi(x) \mapsto \phi(\Lambda^{-1}x).
$$

Solo tiene un grado de libertad interno por punto del espacio. Sus excitaciones son particulas de spin 0. Si el campo es real, la particula es su propia antiparticula (campo de Majorana escalar). Si el campo es complejo, particula y antiparticula son distintas y cargan carga de un U(1).

Ejemplos fisicos: el campo de Higgs (antes de la ruptura espontanea de simetria), el pion neutro, el campo inflaton cosmologico.

## 8. Campo vectorial: representacion $(1/2, 1/2)$

Un campo vectorial $A_\mu(x)$ transforma como un 4-vector:

$$
A_\mu(x) \mapsto \Lambda_\mu{}^\nu A_\nu(\Lambda^{-1}x).
$$

Tiene cuatro componentes, pero no todas son fisicas. Para un boson gauge no masivo las condiciones de gauge eliminan dos, dejando dos grados de libertad fisicos (los dos estados de helicidad $\pm 1$). Para un boson vectorial masivo las condiciones de gauge son distintas y dejan tres grados de libertad (helicidades $-1, 0, +1$).

Ejemplos fisicos: el foton $A_\mu$, los bosones $W^\pm_\mu$ y $Z_\mu$ del Modelo Estandar, los gluones $G_\mu^a$.

## 9. Campo espinorial: representacion $(1/2, 0) \oplus (0, 1/2)$

El espinor de Dirac $\Psi$ vive en la representacion $(1/2, 0) \oplus (0, 1/2)$. Tiene cuatro componentes complejas, que corresponden a dos grados de libertad para la particula (dos proyecciones de spin) y dos para la antiparticula.

La ecuacion de Dirac describe la dinamica de este campo y conecta las dos representaciones quirales mediante el termino de masa. En el limite no masivo los dos espinores de Weyl desacoplan.

Ejemplos fisicos: el electron, el muon, el quark up, el neutrino en su descripcion de Dirac.

## 10. Campo tensorial antisimetrico: representacion $(1,0) \oplus (0,1)$

Un tensor antisimetrico de rango 2 se puede descomponer en sus partes autoduales y antiautoduales. Cada parte corresponde a una de las dos representaciones. El tensor de campo electromagnetico $F_{\mu\nu}$ es el ejemplo principal.

Para el tensor de curvatura en relatividad general aparecen tensores de rango mas alto.

## 11. Correspondencia entre campos y particulas

La tabla siguiente resume la correspondencia:

| Campo | Representacion | Spin | Ejemplo |
|:---|:---|:---|:---|
| Escalar real $\phi$ | $(0,0)$ | 0 | Higgs, pion, axion |
| Escalar complejo $\phi$ | $(0,0)$ | 0 | Campo de Higgs (cargado) |
| Espinor de Weyl $\xi_\alpha$ | $(1/2,0)$ | 1/2 | Neutrino zurdo |
| Espinor de Dirac $\Psi$ | $(1/2,0)\oplus(0,1/2)$ | 1/2 | Electron, quark |
| Espinor de Majorana | $(1/2,0)\oplus(0,1/2)$ | 1/2 | Neutrino de Majorana |
| Vector $A_\mu$ | $(1/2,1/2)$ | 1 | Foton, gluon, $W, Z$ |
| Graviton $h_{\mu\nu}$ | $(1,1)$ | 2 | Graviton |

## 12. Condiciones de gauge y grados de libertad fisicos

Los campos de spin mayor que 0 tienen siempre mas componentes que grados de libertad fisicos. El exceso se elimina con:

- condiciones de gauge (para campos vectoriales gauge);
- ecuaciones de movimiento (la ecuacion de Dirac reduce 4 a 2 grados de libertad por punto);
- condiciones de transversalidad.

En QFT cuantizada, esta reduccion se implementa a traves de condiciones sobre los estados fisicos del espacio de Hilbert.

## 13. El teorema espin-estadistica revisitado

La clasificacion de Wigner conecta el spin con las propiedades de simetria de los estados bajo intercambio de particulas identicas:

- estados de spin entero: simétricos bajo intercambio (bosones, estadistica de Bose-Einstein);
- estados de spin semientero: antisimetricos bajo intercambio (fermiones, estadistica de Fermi-Dirac).

Esta conexion no es un axioma adicional de la teoria cuantica. Es una consecuencia de la simetria de Lorentz, la causalidad y la positividad de la energia. Su demostracion en el formalismo de QFT es uno de los resultados mas elegantes del formalismo.

## 14. Preparacion para los modulos siguientes

Entender la clasificacion de campos por spin es esencial para:

- cuantizar el campo escalar (modulo 04): el tipo mas simple, spin 0;
- cuantizar el campo de Dirac (modulo 06): fermiones, spin 1/2, anticonmutadores;
- construir teorias gauge (modulo 07): campo vectorial, spin 1, fijacion de gauge;
- entender el Modelo Estandar (modulo 10): que campos existen y por que.

## Cuaderno asociado

- Consulta los cuadernos asociados de este bloque en [Resumen del modulo](README.md) para reforzar el capitulo con practica guiada.

## 15. Preguntas de comprobacion

- Cuales son los dos operadores de Casimir del grupo de Poincare y que clasifican.
- Por que una particula no masiva de spin 1 tiene solo dos estados de polarizacion fisicos.
- Que diferencia hay entre el spin de una particula masiva y la helicidad de una no masiva.
- Por que un campo vectorial con cuatro componentes no describe cuatro grados de libertad fisicos.
- Como se relaciona el teorema espin-estadistica con la clasificacion de Wigner.

## 16. Ejercicios sugeridos

1. Para una particula masiva de spin 1, contar los estados de polarizacion en el sistema de reposo y verificar que hay exactamente tres.
2. Mostrar que el vector de Pauli-Lubanski $W^\mu$ satisface $P_\mu W^\mu = 0$.
3. Para el campo escalar libre, verificar que la ecuacion de Klein-Gordon corresponde a la condicion $P^2 = m^2$ sobre los estados de una particula.
4. Comparar el numero de grados de libertad reales del espinor de Dirac antes y despues de imponer la ecuacion de Dirac como vinculos de primera clase.

## 17. Cierre

La clasificacion de Wigner establece que las particulas elementales son inevitablemente estados de una representacion irreducible del grupo de Poincare. Esta es la razon por la que la fisica de particulas no es arbitraria: la simetria del espacio-tiempo, combinada con las exigencias de la mecanica cuantica, determina las posibilidades. Los campos son los objetos de campo que se cuantizan para obtener esas representaciones.

## 18. Referencias y lecturas recomendadas

- Base: Weinberg, vol. I, capitulo 2, clasificacion de Wigner y estados de una particula.
- Complementaria: Tong, notas sobre representaciones del grupo de Poincare y estados asintóticos.
- Profundizacion: Bargmann y Wigner, articulo original de 1948; Streater y Wightman para la formulacion axiomatica.


---

## Navegacion del tutorial

[(anterior) Representaciones de Lorentz y Espinores](03_representaciones_de_lorentz_y_espinores.md) | [(siguiente) Modulo 03: Accion y Simetrias](../03_accion_y_simetrias/README.md)
