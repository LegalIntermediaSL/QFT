# Relatividad Especial Minima

## 1. Proposito

La QFT es inseparable de la relatividad especial. Antes de cuantizar campos, hace falta tener una intuicion firme del espacio-tiempo de Minkowski, de la estructura causal y de la relacion entre energia, momento y masa.

## 2. Espacio-tiempo de Minkowski

La relatividad especial unifica espacio y tiempo en una sola entidad geometrica: el espacio-tiempo. Un evento se especifica por cuatro coordenadas

$$
x^\mu = (t,\mathbf{x})
$$

o, si se mantiene explicitamente la velocidad de la luz,

$$
x^\mu = (ct,\mathbf{x}).
$$

En QFT suele trabajarse en unidades naturales, de modo que $c=1$ y tiempo y longitud comparten las mismas unidades.

## 3. Intervalo relativista

La cantidad fundamental que permanece invariante bajo transformaciones de Lorentz es el intervalo

$$
s^2 = x_\mu x^\mu.
$$

Con la convencion de metrica mas comun en fisica de particulas,

$$
\eta_{\mu\nu} = \mathrm{diag}(1,-1,-1,-1),
$$

se obtiene

$$
s^2 = t^2 - \mathbf{x}^2.
$$

Este numero permite clasificar separaciones entre eventos:

- tipo tiempo: $s^2 > 0$;
- tipo luz: $s^2 = 0$;
- tipo espacio: $s^2 < 0$.

Esta clasificacion es central para entender causalidad en QFT.

Tambien conviene registrar una intuicion importante: si dos observadores inerciales describen el mismo par de eventos, pueden discrepar en las coordenadas temporales y espaciales asignadas, pero no en el signo del intervalo. Por eso la clasificacion causal no depende del observador.

## 4. Cono de luz y causalidad

El cono de luz de un evento separa el espacio-tiempo en regiones causalmente accesibles y no accesibles. Ninguna señal fisica puede propagarse fuera del cono de luz si se respeta la relatividad especial.

En consecuencia:

- un evento de tipo tiempo puede influir causalmente sobre otro;
- un evento de tipo espacio no puede conectarse causalmente con otro mediante una señal subluminal;
- los eventos de tipo luz se conectan por propagacion a velocidad $c$.

La microcausalidad en QFT esta construida precisamente para respetar esta estructura.

El cono de luz no es solo una figura geometrica util. Es el mapa de todas las influencias fisicamente permitidas. Esta idea reaparece una y otra vez en QFT:

- al exigir conmutadores nulos a separacion espacial;
- al interpretar propagadores y funciones de Green;
- al distinguir correlacion cuantica de senalizacion causal.

## 5. Cuatro-vectores

Las cantidades fisicas relativistas se organizan como cuatro-vectores. El ejemplo mas importante es el cuatro-momento

$$
p^\mu = (E,\mathbf{p})
$$

en unidades naturales.

Su norma relativista es

$$
p_\mu p^\mu = E^2 - \mathbf{p}^2.
$$

Para una particula libre de masa $m$, la condicion on-shell es

$$
p_\mu p^\mu = m^2,
$$

de donde sigue la relacion de dispersion

$$
E^2 = \mathbf{p}^2 + m^2.
$$

Esta relacion se llama condicion on-shell porque describe particulas libres fisicas, es decir, excitaciones cuyo cuatro-momento satisface la ecuacion de movimiento relativista. Mas adelante, en lineas internas de diagramas, apareceran momentos off-shell que no obedecen necesariamente esta igualdad.

## 6. Masa, energia y momento

Esta ecuacion resume una enorme cantidad de fisica:

- si $\mathbf{p}=0$, entonces $E=m$;
- si $m=0$, entonces $E=|\mathbf{p}|$;
- a altas energias, la masa puede ser despreciable frente al momento;
- la energia disponible puede convertirse en nuevas excitaciones materiales.

Esta ultima idea es una de las razones por las que una teoria cuantica relativista no puede suponer numero fijo de particulas.

Ese es uno de los choques mas fuertes con la mecanica cuantica no relativista. Si la energia puede transformarse en masa de nuevas particulas, entonces el sector de "numero fijo de particulas" deja de ser estable como descripcion fundamental.

## 7. Transformaciones de Lorentz

Las transformaciones de Lorentz son cambios de observador inercial que preservan el intervalo relativista. Incluyen:

- rotaciones espaciales;
- boosts relativistas.

Una teoria relativista consistente debe mantener la misma forma de sus leyes bajo estas transformaciones. En QFT, esa exigencia determina como transforman los campos:

- escalares;
- vectores;
- espinores;
- tensores.

Por eso la simetria de Lorentz no se reduce a decir que "las ecuaciones se ven bonitas". Tambien decide que tipos de objetos pueden aparecer en la teoria y como deben combinarse en una accion covariante.

## 8. Tiempo propio e invariantes

Para una particula masiva, el tiempo propio $\tau$ satisface

$$
d\tau^2 = dt^2 - d\mathbf{x}^2.
$$

Las cantidades invariantes tienen un papel especial porque no dependen del observador. En QFT, la busqueda de cantidades covariantes o invariantes es una guia sistematica para escribir acciones, amplitudes y terminos lagrangianos.

En cierto sentido, buena parte del estilo moderno de la fisica teorica consiste en esto: escribir la teoria en terminos de objetos cuya forma tenga sentido para cualquier observador inercial.

## 9. Masa invariante de un sistema

Si varias particulas forman un sistema, la masa invariante total viene dada por la norma del cuatro-momento total:

$$
M^2 = P_\mu P^\mu.
$$

Esta cantidad es muy util en scattering y decaimientos, porque permite reconocer umbrales energeticos de produccion y analizar procesos de forma geométrica en el espacio de momentos.

Por ejemplo, si la masa invariante disponible en un sistema inicial no alcanza el umbral de una particula o conjunto de particulas finales, ese proceso simplemente no puede ocurrir. Esta es una forma muy limpia de pensar umbrales sin depender de un sistema de referencia particular.

## 10. Relatividad especial y necesidad de campos

La relatividad especial no es solo un decorado cinemático. Tiene consecuencias profundas para la ontologia de la teoria:

- exige localidad y causalidad relativista;
- obliga a tratar el espacio y el tiempo de forma covariante;
- hace inevitable la posibilidad de creacion y destruccion de particulas cuando la energia es suficiente.

Todo esto empuja de forma natural hacia el lenguaje de campos cuanticos.

## 11. Preguntas de estudio

- Que significa que el intervalo relativista sea invariante.
- Como se distingue una separacion de tipo espacio de una de tipo tiempo.
- Por que la ecuacion $E^2=\mathbf{p}^2+m^2$ es tan importante para el nacimiento de la QFT.
- Que papel cumplen las transformaciones de Lorentz en la clasificacion de campos.

## 12. Ejercicios sugeridos

1. Demuestra que para una particula sin masa se cumple $E=|\mathbf{p}|$.
2. Clasifica como tipo tiempo, luz o espacio una separacion con $t=5$ y $|\mathbf{x}|=3$ en unidades naturales.
3. Explica por que la existencia de umbrales de produccion de particulas es una consecuencia natural de la relatividad especial.

## 13. Cierre

La relatividad especial es el esqueleto cinemático de la QFT. Sin ella, conceptos como causalidad microfisica, covariancia de Lorentz y clasificacion de particulas por masa y espin no tendrian el mismo sentido estructural.

## 14. Referencias y lecturas recomendadas

- Base: notas introductorias de relatividad especial orientadas a fisica teorica.
- Complementaria: Tong, repasos de relatividad y convenciones utiles para QFT.
- Profundizacion: cualquier texto estandar de relatividad especial con cuatro-vectores y transformaciones de Lorentz.


---

## Navegacion del tutorial

[(anterior) Indice del tutorial](../README.md) | [(siguiente) Notacion Tensorial y Convenciones](02_notacion_tensorial_y_convenciones.md)
