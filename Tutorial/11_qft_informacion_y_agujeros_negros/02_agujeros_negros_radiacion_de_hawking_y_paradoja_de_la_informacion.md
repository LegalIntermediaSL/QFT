# Agujeros negros, radiacion de Hawking y paradoja de la informacion

## 1. El escenario

La radiacion de Hawking es uno de los resultados mas sorprendentes del siglo XX porque surge al combinar tres ingredientes que, por separado, parecen perfectamente razonables:

- relatividad general para describir el fondo gravitatorio;
- teoria cuantica de campos para describir materia y radiacion;
- una aproximacion semiclasica en la que el espacio-tiempo se considera clasico, pero los campos que viven sobre el se cuantizan.

El resultado es que un agujero negro no es completamente negro. Emite radiacion con un espectro aproximadamente termico y, por tanto, puede evaporarse.

## 2. Como aparece la radiacion

La explicacion rigurosa usa modos del campo en una geometria con horizonte y compara la definicion de vacio antes y despues de la formacion del agujero negro. La mezcla entre modos positivos y negativos conduce a una ocupacion no trivial de estados para un observador lejano.

La temperatura de Hawking toma la forma

$$
T_H = \frac{\kappa}{2\pi},
$$

donde $\kappa$ es la gravedad superficial, en unidades naturales.

No es necesario imaginar de forma literal pares de particulas "saliendo del vacio" justo en el borde del horizonte, aunque esa imagen popular puede servir como intuicion inicial. Lo fundamental es que la nocion de vacio cambia al comparar observadores y regiones del espacio-tiempo.

## 3. Termicidad y acceso parcial a la informacion

Para un observador asintotico, la radiacion parece termica. Eso ya sugiere una tension: la evolucion de un estado puro hacia una salida termica parece incompatible con la unitaridad.

Hay que distinguir cuidadosamente dos niveles:

- la descripcion semiclasica, donde se traza sobre grados de libertad ocultos tras el horizonte;
- la teoria cuantica completa, donde no deberiamos perder informacion si la evolucion es unitaria.

La dificultad es que la primera descripcion parece robusta, pero la segunda es una exigencia muy fuerte de la mecanica cuantica.

## 4. Formulacion de la paradoja

De forma simplificada, la paradoja puede expresarse asi:

1. una estrella colapsa en un estado cuantico puro;
2. se forma un agujero negro;
3. el agujero negro emite radiacion aproximadamente termica;
4. si la evaporacion se completa y solo queda radiacion termica, el estado final parece mixto;
5. una evolucion pura a mixta viola la unitaridad.

Este razonamiento pone en conflicto tres ideas que nos gustaria conservar:

- unitaridad cuantica;
- validez de la aproximacion semiclasica lejos de la singularidad;
- una nocion razonable de interior y exterior del horizonte.

## 5. Entropia de Bekenstein-Hawking

La termodinamica de agujeros negros sugiere asignar una entropia

$$
S_{\text{BH}} = \frac{A}{4 G},
$$

en unidades naturales apropiadas, donde $A$ es el area del horizonte. Este resultado es extraordinario porque asocia contenido informacional a una superficie, no a un volumen.

Eso sugiere que el numero de grados de libertad relevantes en gravedad cuantica podria organizarse de un modo radicalmente distinto al de una teoria local ordinaria. De aqui nace, entre otras cosas, la intuicion holografica.

## 6. Posibles rutas conceptuales

A lo largo de las ultimas decadas se han explorado varias salidas a la paradoja:

- que la informacion se pierda de verdad, modificando la mecanica cuantica;
- que la evaporacion sea solo aparentemente termica y la informacion salga codificada en correlaciones sutiles;
- que la geometria semiclasica falle antes de lo esperado;
- que la descripcion fundamental de la gravedad sea holografica y preserve unitaridad de manera no obvia desde la perspectiva semiclasica.

La mayoria de los desarrollos modernos favorece fuertemente la idea de que la unitaridad debe sobrevivir, pero el mecanismo exacto depende del marco teorico.

## 7. Por que esto importa para un curso de QFT

La paradoja de la informacion no es solo una curiosidad de relatividad general. Obliga a revisar cuestiones que ya estaban latentes en la QFT:

- que significa una particula;
- como se define el vacio;
- como se reparte la informacion entre subregiones;
- que parte del formalismo depende del observador;
- hasta donde puede empujarse una teoria local sobre un fondo clasico.

Desde este punto de vista, los agujeros negros actuan como un laboratorio extremo para poner a prueba conceptos que nacieron dentro de la teoria cuantica de campos.

## 8. Ideas clave para retener

- La radiacion de Hawking se deriva dentro de QFT en espacio-tiempo curvo.
- La aparente termicidad del espectro es el origen de la tension con la unitaridad.
- La entropia del agujero negro conecta gravedad, termodinamica e informacion.
- La paradoja de la informacion es una ventana hacia la gravedad cuantica, no un detalle tecnico marginal.

## 9. Ejemplo corto de lectura

Si la radiacion observada parece termica, la pregunta correcta no es solo "¿sale calor del agujero negro?", sino "¿de que sistema global se ha trazado informacion para que el observador exterior vea un estado aparentemente termico?". Esa reformulacion vuelve la paradoja mucho mas precisa.

## 10. Cuaderno asociado

- `../../Cuadernos/ejemplos/08_entrelazamiento_y_horizontes.ipynb`: usarlo para conectar termicidad efectiva y acceso parcial a grados de libertad.
- `../../Cuadernos/problemas_resueltos/12_qft_informacion_y_agujeros_negros.ipynb`: usarlo para revisar Hawking, Bekenstein-Hawking y la formulacion basica de la paradoja.

## 11. Ejercicios sugeridos

1. Explicar por que un observador exterior describe un estado reducido y no el estado global completo.
2. Discutir por que la termicidad efectiva no implica automaticamente perdida fundamental de informacion.
3. Relacionar la ley de area de la entropia de Bekenstein-Hawking con la intuicion holografica.

## 12. Referencias y lecturas recomendadas

- Base: reseñas pedagogicas sobre radiacion de Hawking.
- Complementaria: Birrell y Davies, campos cuanticos en espacio-tiempo curvo.
- Profundizacion: revisiones modernas sobre paradoja de la informacion, unitaridad y holografia.


---

## Navegacion del tutorial

[(anterior) QFT, informacion y entrelazamiento](01_qft_informacion_y_entrelazamiento.md) | [(siguiente) Efecto Unruh y Vacio de Rindler](03_efecto_unruh_y_vacio_de_rindler.md)
