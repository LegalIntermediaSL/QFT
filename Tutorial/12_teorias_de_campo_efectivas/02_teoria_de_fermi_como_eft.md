# Teoria de Fermi como EFT

## 1. Proposito

Este documento muestra uno de los ejemplos mas clasicos y pedagogicos de teoria efectiva: la interaccion debil a baja energia descrita como un operador local de cuatro fermiones.

## 2. Del boson pesado al contacto efectivo

En la teoria electrodébil completa, los procesos debiles cargados estan mediados por el boson $W$.

A nivel esquematico, el acoplamiento relevante tiene la forma

$$
\mathcal{L}_{\mathrm{int}} \sim \frac{g}{\sqrt{2}} J^\mu W_\mu + \text{h.c.},
$$

donde $J^\mu$ es una corriente fermionica izquierda.

Si trabajamos a energias mucho menores que $M_W$, el propagador del $W$ puede expandirse como

$$
\frac{1}{q^2 - M_W^2} \approx -\frac{1}{M_W^2}
\left(1 + \frac{q^2}{M_W^2} + \cdots \right),
$$

siempre que $q^2 \ll M_W^2$.

El primer termino produce una interaccion local efectiva.

Esta expansion resume de manera muy clara la filosofia EFT:

- el propagador completo recuerda que la teoria UV tiene un mediador dinamico;
- la expansion en $q^2/M_W^2$ produce una serie de operadores locales;
- a la precision mas baja basta el primer termino, que se ve como un contacto puntual.

## 3. Operador de Fermi

La teoria efectiva resultante se escribe esquematicamente como

$$
\mathcal{L}_{\mathrm{Fermi}}
= - \frac{G_F}{\sqrt{2}}\, J_\mu J^\mu,
$$

con

$$
G_F \sim \frac{g^2}{M_W^2}.
$$

Mas precisamente, en la normalizacion estandar,

$$
\frac{G_F}{\sqrt{2}} = \frac{g^2}{8M_W^2}.
$$

Esto resume de forma compacta el efecto del boson pesado intercambiado virtualmente.

Si se piensa en un proceso como el decaimiento beta, la teoria completa describe el intercambio virtual de un $W$ entre una corriente leptónica y una hadronica. La EFT reemplaza ese intercambio por un unico vertice local, mucho mas simple de manejar a bajas energias.

## 4. Dimension del operador

En cuatro dimensiones, un fermion tiene dimension de masa

$$
[\psi] = \frac{3}{2}.
$$

Por tanto, un operador de cuatro fermiones tiene dimension

$$
[\bar{\psi}\Gamma\psi\, \bar{\psi}\Gamma\psi] = 6.
$$

Para que la densidad lagrangiana siga teniendo dimension cuatro, el coeficiente debe portar dimension

$$
[G_F] = -2.
$$

Eso es exactamente lo que esperamos de una EFT generada por una escala pesada cuadratica en el denominador.

Este analisis dimensional es extremadamente instructivo porque muestra por que la constante de Fermi no es "solo un numero pequeño": su dimension ya revela que la interaccion esta suprimida por una escala pesada.

## 5. Matching e interpretacion

La idea de matching consiste en exigir que la teoria completa y la EFT reproduzcan la misma fisica IR a la precision deseada.

En este caso:

- la teoria UV usa propagador del boson $W$;
- la EFT usa un contacto local;
- ambas coinciden para $q^2 \ll M_W^2$ al orden dominante.

Este ejemplo deja una leccion central: una interaccion aparentemente no renormalizable puede ser perfectamente buena y precisa dentro de su dominio de validez.

Tambien es un ejemplo historicamente importante porque muestra un cambio de mentalidad. Antes de la formulacion electrodébil completa, la teoria de Fermi parecia una teoria fundamental con problemas UV. Vista hoy como EFT, aparece como una descripcion excelente y conceptualmente correcta de la fisica de baja energia.

## 6. Estructura quiral

La interaccion debil cargada del Modelo Estandar acopla a corrientes izquierdas. Por eso el operador efectivo de Fermi no es un contacto arbitrario entre fermiones, sino que hereda una estructura quiral muy especifica.

Esquematicamente, el tipo de corriente relevante es

$$
J^\mu \sim \bar{\psi}\gamma^\mu (1-\gamma^5)\psi.
$$

Esta estructura importa porque:

- reproduce la violacion de paridad de la interaccion debil;
- restringe que observables y combinaciones de espines son posibles;
- muestra que la EFT conserva informacion fina de la teoria UV, no solo la escala $M_W$.

## 7. Cuando falla la EFT

La teoria de Fermi deja de ser suficiente cuando la energia del proceso ya no es pequeña comparada con $M_W$.

En ese regimen:

- el propagador del $W$ ya no puede reemplazarse por una constante;
- aparecen correcciones de orden $q^2/M_W^2$;
- la descripcion completa electrodébil se vuelve necesaria.

Otra señal de que la EFT se esta estresando es que las amplitudes crecen con la energia de manera que la descripcion puntual deja de ser fiable. Esto no significa que la fisica falle, sino que el mediador real debe reintroducirse explícitamente.

## 8. Ejemplo corto de lectura

El decaimiento beta nuclear puede describirse con gran precision usando una interaccion puntual de cuatro fermiones, aunque en la teoria UV esa interaccion este mediada por un boson gauge masivo. Ese es exactamente el poder de una EFT bien construida.

## 9. Cuaderno asociado

- `../../Cuadernos/problemas_resueltos/17_fermi_y_matching_efectivo.ipynb`: usarlo para seguir el paso entre el propagador del boson pesado y el operador efectivo de Fermi.

## 10. Advertencias utiles

- La teoria de Fermi no es "fundamentalmente incorrecta"; es una EFT valida en un rango de energia bien definido.
- La no renormalizabilidad perturbativa de un operador local no lo hace inutil si la expansion por escalas es controlada.
- El matching depende de convenciones y normalizaciones, pero la logica fisica es estable.

## 11. Preguntas de comprobacion

- Por que el intercambio de un $W$ pesado se vuelve un contacto local a baja energia.
- Que dimension tiene el operador de Fermi.
- Como se relacionan $G_F$, $g$ y $M_W$ a nivel estructural.

## 12. Referencias y lecturas recomendadas

- Base: introducciones al sector debil y a la teoria de Fermi.
- Complementaria: textos de EFT y matching a nivel arbol.
- Profundizacion: SMEFT y operadores semileptonicos.


---

## Navegacion del tutorial

[(anterior) Integrando grados de libertad](01_integrando_grados_de_libertad.md) | [(siguiente) Euler-Heisenberg y operadores efectivos](03_euler_heisenberg_y_operadores_efectivos.md)
