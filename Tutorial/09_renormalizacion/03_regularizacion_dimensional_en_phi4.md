# Regularizacion Dimensional en $\phi^4$

**Nivel:** Intermedio  
**Dificultad:** Media-Alta  
**Tiempo estimado:** 25-35 min  
**Prerequisitos recomendados:** [Renormalizacion y Grupo de Renormalizacion](02_renormalizacion_y_grupo_de_renormalizacion.md) · [Resumen del modulo](README.md)


## 1. Proposito

Este documento muestra de forma guiada por que la regularizacion dimensional se vuelve tan util en teoria de campos. El ejemplo elegido es una correccion a un lazo en la teoria escalar $\phi^4$.

## 2. Punto de partida

En $\phi^4$, una correccion de un lazo a la masa conduce a una integral del tipo

$$
I(m) \sim \mu^{4-d}\int \frac{d^dk}{(2\pi)^d}\frac{i}{k^2 - m^2 + i\epsilon},
$$

donde se ha introducido una escala $\mu$ para mantener dimensiones correctas al trabajar en

$$
d = 4 - \varepsilon.
$$

La notacion puede parecer extraña al principio, pero la idea es muy simple: en vez de cortar la integral de manera abrupta, continuamos analiticamente el numero de dimensiones. La divergencia se manifiesta entonces como un polo cuando regresamos al limite fisico $\varepsilon \to 0$.

En lenguaje diagramatico, esta integral aparece ya en la correccion mas elemental al propagador de dos puntos. Aunque el factor combinatorio exacto depende de convenciones, el mensaje conceptual es estable: incluso un solo diagrama de lazo obliga a distinguir entre parametro desnudo, parametro renormalizado y dependencia respecto de una escala.

## 3. Por que introducir $\mu$

La escala $\mu$ no es una decoracion arbitraria. Aparece porque al cambiar el numero de dimensiones tambien cambian las dimensiones de los acoplamientos y de la medida de integracion.

Este detalle tecnico anticipa una leccion fisica profunda: la teoria renormalizada depende de una escala de referencia.

Mas concretamente, en cuatro dimensiones el acoplamiento $\lambda$ de $\phi^4$ es adimensional, pero en $d\neq 4$ deja de serlo. La escala $\mu$ compensa esa diferencia y permite seguir comparando cantidades con dimensiones fisicas correctas.

## 4. Estructura del resultado

Sin desarrollar aqui todos los pasos de integracion, el resultado de este tipo de integral toma una forma esquematica como

$$
I(m) \sim \frac{1}{\varepsilon} + \text{terminos finitos} + \log\frac{\mu^2}{m^2}.
$$

Lo importante pedagogicamente es reconocer tres piezas:

- el polo en $1/\varepsilon$, que codifica la divergencia ultravioleta;
- una parte finita;
- una dependencia logaritmica en la escala $\mu$.

Conviene subrayar que el polo en $1/\varepsilon$ no es una "nueva" divergencia distinta de la ultravioleta habitual. Es la manera en que la regularizacion dimensional la reexpresa algebraicamente.

## 5. Bosquejo del calculo

Sin entrar en todos los detalles tecnicos, la ruta tipica del calculo es:

1. escribir la integral de lazo en $d$ dimensiones;
2. rotar a espacio euclideo cuando conviene para volver convergente la manipulacion;
3. usar identidades gamma estandar para integrar en $d$ dimensiones;
4. expandir el resultado alrededor de $\varepsilon=0$.

Una de las formas canonicas del resultado intermedio es

$$
\int \frac{d^d k_E}{(2\pi)^d}\frac{1}{k_E^2 + m^2}
\propto
(m^2)^{\frac d2 - 1}\Gamma\!\left(1-\frac d2\right).
$$

Esta expresion merece una lectura lenta: la parte de potencia fija como escala la masa, mientras que la funcion gamma concentra la informacion singular asociada al limite $d \to 4$.

Al hacer esa expansion aparece precisamente la combinacion

$$
\Gamma\!\left(1-\frac{d}{2}\right)
\sim
\Gamma\!\left(-1+\frac{\varepsilon}{2}\right),
$$

cuya expansion genera el polo en $1/\varepsilon$. Este es uno de los lugares donde se ve con claridad que la divergencia UV queda traducida a una singularidad en la continuacion analitica.

Una buena intuicion es la siguiente: la integral original "quiere divergir" en cuatro dimensiones, pero al desplazar la cuenta a $4-\varepsilon$ se vuelve algebraicamente controlable. La divergencia no desaparece; queda codificada en la forma singular de la expansion.

## 6. Que se gana frente al cutoff

La regularizacion dimensional organiza las divergencias de forma especialmente limpia:

- no introduce una escala de corte dura en el espacio de momentos;
- preserva bien la simetria gauge en muchos contextos;
- convierte divergencias ultravioletas en polos algebraicos manejables.

Por eso se ha convertido en el lenguaje estandar de gran parte de la QFT moderna.

Ademas, separa de forma muy ordenada las piezas universales del calculo:

- el polo divergente;
- los terminos constantes dependientes del esquema;
- los logaritmos fisicamente relevantes en la escala.

Frente a un cutoff duro, esto suele producir una lectura mas limpia de que parte del resultado es universal y que parte depende del regulador. Con cutoff aparecen a menudo potencias o logaritmos de $\Lambda$ cuya interpretacion puede mezclarse mas con detalles tecnicos del procedimiento.

## 7. Del polo al contratermino

Una vez aislado el termino proporcional a $1/\varepsilon$, la renormalizacion procede absorbiendolo en un contratermino adecuado. No se "borra" la divergencia sin mas: se redefine la relacion entre parametros desnudos y parametros renormalizados.

En el ejemplo de la masa:

- la correccion cuantica produce una parte divergente;
- el contratermino de masa la absorbe;
- la masa fisica queda finita tras imponer la condicion de renormalizacion elegida.

En esquemas MS o $\overline{\mathrm{MS}}$, esta absorcion se hace de manera particularmente simple porque el contratermino se elige para cancelar el polo y, en el caso de $\overline{\mathrm{MS}}$, algunas constantes estandares adicionales. Esto vuelve muy eficiente el calculo de running y funciones beta.

Tambien conviene recordar que en $\phi^4$ no solo puede renormalizarse la masa. A distintos ordenes aparecen renormalizaciones del acoplamiento y de la normalizacion del campo. Este ejemplo debe verse como una puerta de entrada, no como un caso aislado.

## 8. Por que la dependencia en $\mu$ no es un problema

A primera vista puede parecer preocupante que el resultado contenga un logaritmo $\log(\mu^2/m^2)$. Sin embargo, esa dependencia no es un defecto del observable final. Lo que ocurre es que:

- las amplitudes intermedias dependen del esquema y de la escala de renormalizacion;
- los parametros renormalizados tambien dependen de $\mu$;
- la combinacion completa que define una cantidad fisica debe quedar independiente de elecciones arbitrarias.

Esta es exactamente la puerta de entrada al grupo de renormalizacion.

De hecho, una gran virtud pedagogica de la regularizacion dimensional es que hace visible de forma muy transparente la relacion entre divergencias UV y dependencia respecto de $\mu$. Ese es el terreno natural donde aparecen funciones beta y ecuaciones de Callan-Symanzik.

## 9. Ejemplo corto de lectura

Si en una cuenta aparece un termino $1/\varepsilon$, no debe leerse como un fracaso de la teoria, sino como la señal de que la teoria aun no ha sido renormalizada en la escala y el esquema escogidos.

Del mismo modo, si tras renormalizar sobreviven logaritmos grandes como $\log(\mu^2/m^2)$, eso suele indicar que la escala elegida no es la mas conveniente para la cinemática del problema o que conviene reorganizar la expansion mediante running.

## Cuaderno asociado
- `../../Cuadernos/problemas_resueltos/15_regularizacion_dimensional_y_running.ipynb`: usarlo para fijar de forma guiada el papel del polo en $1/\\varepsilon$, de la escala $\\mu$ y de la transicion conceptual desde regularizacion a running.
- `../../Cuadernos/problemas_resueltos/10_interacciones_y_perturbaciones.ipynb`: usarlo como apoyo para repasar la logica diagramatica que da origen a los lazos.
- `../../Cuadernos/problemas_resueltos/09_cuantizacion_del_campo_escalar.ipynb`: usarlo para recordar la teoria libre sobre la que se construye la perturbacion.

## 11. Advertencias utiles

- La regularizacion dimensional no elimina por si sola la necesidad de renormalizar.
- El polo en $1/\varepsilon$ no es el observable final.
- La escala $\mu$ introducida en el calculo no debe confundirse automaticamente con una escala fisica unica del problema.
- En otros contextos tambien pueden aparecer divergencias infrarrojas; aqui el foco esta puesto solo en la estructura ultravioleta.

## 12. Mini mapa conceptual

Este capitulo conecta cuatro piezas del tutorial que conviene mantener juntas:

- los diagramas de lazo del modulo perturbativo;
- la aparicion de divergencias ultravioletas;
- la necesidad de introducir contraterminos;
- el nacimiento del running con respecto a la escala $\mu$.

Si esas cuatro piezas quedan enlazadas, la regularizacion dimensional deja de parecer un truco formal y pasa a verse como el lenguaje natural de la renormalizacion moderna.

## 13. Preguntas de comprobacion

- Por que se introduce la escala $\mu$.
- Que representa el polo en $1/\varepsilon$.
- Por que este esquema resulta especialmente conveniente en teorias gauge.
- En que sentido la funcion gamma "almacena" la divergencia UV al continuar analiticamente la dimension.

## Ejercicios sugeridos

1. Explicar por que al cambiar la dimension del espacio-tiempo aparece una escala auxiliar $\mu$.
2. Describir el papel conceptual del polo en $1/\varepsilon$ antes de absorberlo en contraterminos.
3. Justificar por que este lenguaje resulta especialmente natural para renormalizacion moderna y teorias gauge.

## 14. Referencias y lecturas recomendadas

- Base: Peskin y Schroeder, regularizacion dimensional en teorias escalares.
- Complementaria: Tong, explicacion conceptual del papel de $\varepsilon$ y de la escala $\mu$.
- Profundizacion: textos avanzados de renormalizacion perturbativa y esquemas MS o $\overline{\text{MS}}$.


---

## Navegacion del tutorial

[(anterior) Renormalizacion y Grupo de Renormalizacion](02_renormalizacion_y_grupo_de_renormalizacion.md) | [(siguiente) Funcion Beta y Running Couplings](04_funcion_beta_y_running_couplings.md)
