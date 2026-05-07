# Ejercicios del Modulo 01: Fundamentos Conceptuales

**Modulo:** 01 — Fundamentos Conceptuales  
**Nivel:** Fundacional  
**Cuadernos de apoyo:**  
- `../../Cuadernos/problemas_resueltos/06_fundamentos_conceptuales.ipynb`  
- `../../Cuadernos/ejemplos/02_principios_estructurales_y_restricciones.ipynb`


## Bloque 1: Verificacion (Nivel 1)

**1.1** La mecanica cuantica no relativista trabaja con numero fijo de particulas. Explica en dos o tres frases por que este supuesto falla en el regimen relativista. *(Pista: energias altas implican que la creacion de pares es posible.)*

**1.2** El principio de superposicion en mecanica cuantica y la localidad de la relatividad especial entran en tension. Identifica el conflicto y enuncia como lo resuelve la QFT.

**1.3** Nombra los cuatro principios estructurales que restringen cualquier teoria cuantica de campos consistente: localidad, unitaridad, invarianza de Lorentz y microcausalidad. Da una frase de explicacion para cada uno.

**1.4** ¿Por que se dice que las particulas son excitaciones de campos y no al reves? Formula la respuesta en terminos del numero de grados de libertad de un campo frente a una particula.

**1.5** El teorema de spin-estadistica conecta el spin de una particula con su estadistica cuantica. Enuncia el resultado: ¿que estadistica corresponde a enteros? ¿a semienteros?

---

## Bloque 2: Derivacion guiada (Nivel 2)

**2.1** El problema de la interpretacion probabilistica en MQ relativista. La densidad de probabilidad en mecanica cuantica no relativista es $\rho = |\psi|^2 \geq 0$. La ecuacion de Klein-Gordon admite la corriente $j^\mu = i(\phi^*\partial^\mu\phi - \phi\partial^\mu\phi^*)$.
- (a) Muestra que $\partial_\mu j^\mu = 0$ si $\phi$ satisface Klein-Gordon.
- (b) Muestra que $\rho = j^0$ puede ser negativo para soluciones de energia negativa.
- (c) Explica como la QFT resuelve este problema: $\rho$ se reinterpreta como densidad de carga, no de probabilidad.

**2.2** Principio de microcausalidad. En QFT, para operadores locales $\mathcal{O}(x)$ y $\mathcal{O}(y)$ con separacion tipo-espacio ($(x-y)^2 < 0$):
- (a) Enuncia el requisito $[\mathcal{O}(x), \mathcal{O}(y)] = 0$.
- (b) Explica por que esto es equivalente a prohibir la comunicacion superluminal.
- (c) Argumenta por que su violacion romperia causalidad.

**2.3** La QFT como teoria de muchos cuerpos relativista. En fisica del estado solido, un fonon es una cuasiparticula emergente de los modos de vibracion de una red cristalina.
- (a) Establece la analogia con los campos cuanticos: ¿que papel juega el vacio en QFT respecto al estado fundamental de la red?
- (b) ¿Que proceso del estado solido seria analogo a la creacion de pares?
- (c) ¿Que diferencias fundamentales hay entre los fonones y los bosones de la QFT relativista?

---

## Bloque 3: Sintesis (Nivel 3)

**3.1** Conecta los tres principios centrales del modulo 01 con los formalismos que se desarrollan en el tutorial.
- Explica como la localidad motiva la forma $\mathcal{L}(x) = \mathcal{L}(\phi(x), \partial_\mu\phi(x))$ del lagrangiano.
- Explica como la unitaridad restringe el grupo de simetria gauge.
- Explica como la invarianza de Lorentz clasifica los campos por spin.

**3.2** Resume por que la QFT no es una opcion sino una necesidad: a partir de los principios de relatividad especial, mecanica cuantica y localidad, argumenta que la existencia de campos cuanticos y la creacion y destruccion de particulas es inevitable.

---

## Soluciones sugeridas (Bloque 1)

**1.1** Cuando $E \gtrsim 2mc^2$, la creacion de pares particula-antiparticula es energeticamente posible. Entonces el numero de particulas no puede ser un numero cuantico conservado, y cualquier formalismo de $N$ fijo es inconsistente.

**1.2** La superposicion permite estados no locales; la relatividad exige que no haya senales superluminales. La QFT reconcilia esto imponiendo microcausalidad: conmutadores de observables en regiones causalmente desconectadas son cero.

**1.3** Localidad: la interaccion es puntual en el espacio-tiempo. Unitaridad: la evolucion conserva la norma y la probabilidad total. Invarianza de Lorentz: las leyes fisicas son iguales en todos los marcos inerciales. Microcausalidad: observables en regiones tipo-espacio conmutan.

**1.4** Un campo tiene infinitos grados de libertad (uno por punto del espacio). Una particula tiene finitos. La descripcion fundamental debe ser el campo; la particula surge como cuanto de excitacion.

**1.5** Spin entero: estadistica de Bose-Einstein (bosones). Spin semientero: estadistica de Fermi-Dirac (fermiones).

---

## Navegacion del tutorial

[(anterior) Prerrequisitos](../00_prerrequisitos/README.md) | [(siguiente) Relatividad y Campos](../02_relatividad_y_campos/README.md)
