# Conceptos Fundamentales de Teoria Cuantica de Campos

## Proposito

Este documento resume las ideas centrales que conviene tener presentes antes de estudiar con detalle la Teoria Cuantica de Campos. No sustituye los capitulos tecnicos, pero ofrece un mapa conceptual que permite entender por que aparecen ciertas estructuras y como se relacionan entre si.

## 1. Que problema intenta resolver la QFT

La mecanica cuantica ordinaria describe sistemas con un numero fijo de grados de libertad y funciona muy bien mientras no sea necesario crear o destruir particulas. La relatividad especial, en cambio, obliga a tratar el espacio y el tiempo de manera unificada y permite procesos energeticos donde la materia puede transformarse en nuevas excitaciones.

Cuando se intenta combinar ambas ideas, aparece una tension profunda:

- la mecanica cuantica no relativista trata a las particulas como objetos primarios;
- la relatividad y la causalidad exigen una formulacion compatible con propagacion local;
- los procesos de altas energias muestran que el numero de particulas no se conserva.

La QFT resuelve esta tension tomando a los campos como objetos fundamentales. Las particulas pasan a interpretarse como cuantos o excitaciones discretas de esos campos.

## 2. Campo

Un campo es una entidad definida en cada punto del espacio-tiempo. Puede ser escalar, vectorial, espinorial o tensorial, segun como transforme bajo cambios de coordenadas o simetrias de Lorentz.

Ideas clave:

- un campo no asigna un unico numero global, sino un valor a cada punto;
- su evolucion recoge informacion local;
- distintas especies de particulas corresponden a distintos campos;
- en el nivel cuantico, el campo se promueve a operador.

Ejemplos:

- campo escalar $\phi(x)$;
- campo electromagnetico $A_\mu(x)$;
- campo fermionico $\psi(x)$.

## 3. Espacio-tiempo y relatividad

La QFT vive sobre un espacio-tiempo relativista. Eso significa que las ecuaciones deben respetar la estructura causal de la relatividad especial y ser covariantes bajo transformaciones de Lorentz.

Esto impone condiciones muy fuertes:

- no puede haber senales fisicas propagandose mas rapido que la luz;
- la descripcion no debe depender del observador inercial elegido;
- los observables locales deben respetar la causalidad microfisica.

Por eso, el lenguaje de campos locales resulta mucho mas natural que el de funciones de onda de una sola particula.

## 4. Simetria

Las simetrias organizan casi toda la teoria. Una simetria es una transformacion que deja invariantes las ecuaciones o la accion del sistema.

Las mas importantes en el arranque de QFT son:

- traslaciones en espacio y tiempo;
- rotaciones;
- transformaciones de Lorentz;
- simetrias internas, como cambios de fase;
- simetrias gauge.

Las simetrias no solo simplifican el formalismo. Tambien determinan cantidades conservadas, restringen terminos posibles en la lagrangiana y guian la construccion de teorias fisicamente consistentes.

## 5. Accion y densidad lagrangiana

La formulacion moderna de una teoria de campos se apoya en la accion:

$$
S = \int d^4x\, \mathcal{L}
$$

donde $\mathcal{L}$ es la densidad lagrangiana. La dinamica se obtiene exigiendo que la accion sea estacionaria frente a variaciones del campo. De ahi emergen las ecuaciones de Euler-Lagrange.

Esta formulacion es central por varias razones:

- hace visibles las simetrias;
- permite una transicion natural al formalismo cuantico;
- generaliza elegantemente desde sistemas mecanicos hasta campos.

## 6. Cuantizacion

Cuantizar significa pasar de una descripcion clasica a una teoria donde las variables dinamicas ya no son numeros ordinarios, sino operadores o amplitudes integradas sobre historias posibles.

En QFT aparecen dos grandes lenguajes:

- cuantizacion canonica;
- integral de camino.

En la cuantizacion canonica, el campo y su momento conjugado satisfacen relaciones de conmutacion o anticonmutacion. En la integral de camino, las amplitudes se obtienen sumando contribuciones de todas las configuraciones del campo ponderadas por $e^{iS}$.

## 7. Particulas como excitaciones

Uno de los cambios conceptuales mas importantes es este: una particula ya no se interpreta como el ladrillo ultimo de la teoria, sino como una excitacion cuantizada de un campo.

Esto permite entender de forma unificada:

- la existencia de cuantos de energia;
- la creacion y aniquilacion de particulas;
- la relacion entre operadores de campo y estados multiparticle;
- el papel del vacio cuantico.

En un campo escalar libre, por ejemplo, los modos normales del campo se comportan como osciladores armonicos cuanticos independientes. Sus cuantos son precisamente las particulas observables asociadas al campo.

## 8. Vacio

El vacio en QFT no es "nada". Es el estado de menor energia del sistema y posee estructura fisica.

Aspectos importantes:

- fluctua cuanticamente;
- puede polarizarse en presencia de interacciones;
- puede no ser trivial si hay ruptura espontanea de simetria;
- define la base sobre la cual se construyen los estados excitados.

Gran parte de la riqueza conceptual de la QFT proviene de que el vacio tiene propiedades dinamicas y no debe confundirse con la ausencia ingenua de contenido fisico.

## 9. Localidad y causalidad

La teoria exige que influencias fisicas no se propaguen fuera del cono de luz. En versiones locales de QFT esto se refleja en condiciones de conmutacion entre observables separados espacialmente.

La idea intuitiva es:

- si dos regiones estan separadas de forma espacial, una medicion local en una no debe alterar instantaneamente un observable local en la otra;
- la teoria puede contener correlaciones cuanticas, pero no violaciones operativas de causalidad relativista.

## 10. Interaccion

Los campos libres son solo el punto de partida. La fisica interesante aparece cuando los campos interactuan. Las interacciones permiten:

- dispersion;
- decaimiento;
- produccion de nuevas particulas;
- correcciones radiativas;
- estructura efectiva a distintas escalas.

En la practica, muchas interacciones se estudian mediante teoria de perturbaciones alrededor de una teoria libre, usando diagramas de Feynman como herramienta organizativa.

## 11. Renormalizacion

Las teorias cuanticas de campos suelen producir integrales divergentes en calculos perturbativos. La renormalizacion es el marco que permite reinterpretar esos infinitos de forma controlada y extraer predicciones fisicas finitas.

Mas que un truco tecnico, la renormalizacion enseña algo profundo:

- los parametros medidos dependen de la escala;
- una teoria efectiva puede ser valida sin ser fundamental;
- distintas escalas de energia pueden requerir distintos lenguajes efectivos.

## 12. Mapa minimo de ideas

Si hubiera que condensar el corazon de la QFT en una secuencia corta, seria algo asi:

1. La relatividad especial exige una formulacion causal y covariante.
2. La fisica cuantica relativista permite crear y destruir particulas.
3. Los campos son los objetos fundamentales mas naturales para describir esto.
4. La accion y la lagrangiana codifican la dinamica y las simetrias.
5. La cuantizacion convierte los campos en entidades capaces de producir cuantos.
6. Las particulas son excitaciones del campo.
7. Las interacciones se estudian con amplitudes, correladores y expansion perturbativa.
8. La renormalizacion conecta parametros, escalas y observables.

## 13. Preguntas guia para seguir estudiando

- Por que una sola particula relativista no basta para describir procesos reales de altas energias
- Como se obtiene la ecuacion de movimiento de un campo a partir de una accion
- Que distingue a bosones y fermiones en el formalismo cuantico
- Como aparecen los operadores de creacion y aniquilacion
- Por que los diagramas de Feynman no son dibujos literales sino terminos de una expansion
- Que significa que una teoria sea renormalizable o efectiva

## 14. Cierre

La QFT puede parecer abrumadora al principio porque mezcla fisica, algebra, geometria, analisis y principios de simetria en un solo lenguaje. Sin embargo, casi todo el edificio descansa sobre unas pocas ideas rectoras: campos, simetria, accion, cuantizacion, causalidad e interaccion. Tener ese mapa desde el inicio vuelve mucho mas legible el resto del tutorial.
