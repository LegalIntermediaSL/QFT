# QFT, informacion y entrelazamiento

**Nivel:** Avanzado  
**Dificultad:** Alta  
**Tiempo estimado:** 18-25 min  
**Prerequisitos recomendados:** [Modulo anterior](../10_modelo_estandar/README.md) · [Resumen del modulo](README.md)

## Proposito

Este capitulo abre el modulo mostrando que el entrelazamiento, las matrices de densidad reducidas y la informacion accesible por subregiones ya forman parte del lenguaje natural de la QFT.

## 1. Por que este tema pertenece a un tutorial de QFT

Puede parecer que la teoria de la informacion cuantica y la fisica de agujeros negros pertenecen a otra clase de curso. Sin embargo, una mirada mas cuidadosa muestra que muchas de las ideas centrales de estos temas nacen precisamente dentro del lenguaje de la teoria cuantica de campos.

La razon es simple: en QFT el vacio no es una nada trivial. Es un estado altamente estructurado, con correlaciones entre regiones espaciales distintas. Cuando el espacio se divide en subregiones y solo una parte de los grados de libertad es accesible, el estado efectivo deja de ser puro y pasa a describirse por una matriz de densidad reducida.

Ese hecho, que puede formularse sin introducir gravedad, ya contiene la semilla conceptual de temas como:

- entropia de entrelazamiento;
- termicidad efectiva para observadores parciales;
- dependencia del concepto de particula respecto del observador;
- tension entre localidad, horizonte y unitaridad.

## 2. El vacio cuantico como estado correlacionado

En mecanica cuantica elemental solemos pensar en el estado fundamental de un sistema como el estado de menor energia. En QFT esto sigue siendo cierto, pero el contenido fisico es mucho mas rico. El vacio de un campo libre no es simplemente un estado "sin particulas" en un sentido clasico. Es el estado aniquilado por todos los operadores de destruccion:

$$
a_{\mathbf p} |0\rangle = 0
\quad
\text{para todo } \mathbf p.
$$

Sin embargo, ese estado posee correlaciones no triviales entre observables localizados en distintas regiones del espacio-tiempo. Por eso el vacio no se comporta como un producto simple de estados independientes en cada punto del espacio.

De forma esquematica, si dividimos el espacio en una region $A$ y su complemento $\bar A$, el estado global puede ser puro y, aun asi, la descripcion restringida a $A$ ser mixta.

En QFT esta afirmacion adquiere un peso especial porque los grados de libertad viven distribuidos por el espacio continuo. La mera existencia de una frontera entre subregiones ya reorganiza que informacion se considera accesible y cual queda fuera del observador.

## 3. Matrices de densidad reducidas

Si el sistema completo esta descrito por una matriz de densidad $\rho$, el estado efectivo accesible a un observador que solo controla la region $A$ se obtiene trazando sobre los grados de libertad invisibles:

$$
\rho_A = \mathrm{Tr}_{\bar A} \, \rho.
$$

La entropia asociada es la entropia de von Neumann:

$$
S_A = - \mathrm{Tr}(\rho_A \log \rho_A).
$$

Cuando el estado global es puro, esta cantidad mide entrelazamiento entre $A$ y $\bar A$. En sistemas de muchos cuerpos y en QFT, esta entropia suele crecer con el area de la frontera entre regiones, una pista conceptual importante en la conexion con la termodinamica de agujeros negros.

Este comportamiento de tipo area law no debe tomarse como una ley universal sin matices, pero si como una intuicion muy poderosa: en teorias locales, las correlaciones mas intensas suelen concentrarse cerca de la frontera que separa regiones. Esa observacion prepara muy bien el lenguaje entropico de los horizontes.

## 4. Por que la entropia de entrelazamiento importa en QFT

La entropia de entrelazamiento no es un accesorio de moda importado desde la informacion cuantica. En QFT cumple varias funciones profundas:

- cuantifica correlaciones del vacio;
- ayuda a caracterizar fases cuanticas;
- revela la estructura de grados de libertad accesibles e inaccesibles;
- conecta con propiedades termicas efectivas de observadores acelerados o confinados a ciertas regiones.

En otras palabras, la QFT no solo describe amplitudes de scattering. Tambien describe que informacion queda disponible cuando el observador no puede acceder a todo el sistema.

Esta ampliacion de perspectiva es pedagogicamente importante. La misma teoria que antes organizaba campos, propagadores y amplitudes empieza aqui a organizar tambien acceso parcial a la informacion, coarse graining y estados reducidos.

## 5. Observadores, regiones y termicidad efectiva

Una idea que reaparece una y otra vez es que el concepto de particula depende de la forma en que se descompone el campo en modos positivos y negativos. En espacio-tiempo plano esto ya aparece en el efecto Unruh: un observador acelerado interpreta el vacio de Minkowski como un baño termico.

La leccion general es:

- el estado global puede ser puro;
- la descripcion reducida para un observador parcial puede parecer termica;
- esa termicidad no implica necesariamente que el sistema completo haya perdido informacion.

Este punto es esencial para preparar la discusion sobre radiacion de Hawking.

Una moraleja util es que "parecer termico" no equivale automaticamente a "haber destruido informacion". Muchas descripciones termicas en QFT nacen simplemente de ignorar parte de los grados de libertad de un estado global mas rico.

## 6. Localidad y tensiones emergentes

La QFT local fue construida para respetar causalidad relativista. Sin embargo, cuando una particion espacial o un horizonte ocultan parte de los grados de libertad, la descripcion efectiva del subsistema puede parecer no local o termica.

Eso no significa que la teoria fundamental haya abandonado la localidad. Significa que la informacion disponible para un observador parcial se obtiene tras una operacion de traza que descarta variables. El resultado es una teoria efectiva con menos acceso a la informacion microscopica.

Por eso, cuando mas adelante aparezca la frase "la informacion parece perderse", conviene recordar que una parte de la tension puede venir de confundir perdida operativa de acceso con perdida fundamental de unitaridad.

## 7. Hacia agujeros negros

Esta estructura conceptual se vuelve dramaticamente importante en presencia de horizontes. Un agujero negro divide el espacio-tiempo en regiones con accesibilidad distinta para distintos observadores. Si la QFT en espacio-tiempo curvo predice radiacion termica y evaporacion, entonces la informacion codificada en el estado inicial parece quedar en peligro.

La paradoja de la informacion de agujeros negros nace precisamente de este cruce:

- la semiclasica sugiere termicidad;
- la mecanica cuantica exige unitaridad;
- la QFT proporciona el lenguaje para formular la tension.

Lo importante aqui no es resolver ya la paradoja, sino aprender a formularla con cuidado. Gran parte de la confusion historica aparece al mezclar estado global y estado reducido, pureza microscópica y termicidad efectiva, o punto de vista del observador ideal y del observador con acceso parcial.

## 8. Ideas clave para retener

- El vacio en QFT es un estado altamente correlacionado.
- La informacion accesible depende de que region del sistema pueda observarse.
- La entropia de entrelazamiento aparece al restringir el estado global a una subregion.
- Los horizontes convierten este tema en una cuestion fisica central, no solo formal.

## 9. Entrelazamiento y geometria

En desarrollos mas modernos, el entrelazamiento no se estudia solo como una cantidad asociada a una biparticion. Tambien aparece como pista de que la conectividad geometrica y la reconstruccion de regiones en descripciones holograficas pueden estar ligadas a patrones de correlacion cuantica. Para este tutorial basta retener la intuicion: el entrelazamiento no solo cuantifica informacion compartida, sino que parece participar en como se organiza una descripcion espacial coherente.

## 10. Ejemplo corto de lectura

Si el estado global del campo es puro pero solo puede observarse una subregion, la teoria efectiva del subsistema ya no tiene por que seguir siendo pura. Esa simple observacion resume por que entrelazamiento, informacion y acceso parcial aparecen juntos en QFT.

## Cuaderno asociado
- `../../Cuadernos/ejemplos/08_entrelazamiento_y_horizontes.ipynb`: usarlo para reforzar la relacion entre subregiones, matrices reducidas y termicidad efectiva.
- `../../Cuadernos/problemas_resueltos/12_qft_informacion_y_agujeros_negros.ipynb`: usarlo para practicar preguntas conceptuales del modulo.

## 12. Mini mapa de lectura del modulo

Este primer capitulo del modulo conviene leerlo como base de todos los siguientes:

- aqui nace la idea de acceso parcial a la informacion;
- en el efecto Unruh esa idea se convierte en termicidad para observadores acelerados;
- en Hawking reaparece como tension entre termicidad y unitaridad;
- en islas y holografia se reformula como problema de reconstruccion de informacion.

Si esta progresion queda clara, el modulo entero se vuelve mucho mas coherente.

## 13. Ejercicios sugeridos

1. Explicar con tus propias palabras por que un estado global puro puede producir un estado reducido mixto.
2. Relacionar el concepto de entropia de entrelazamiento con la idea de grados de libertad inaccesibles.
3. Discutir por que este tema prepara naturalmente la aparicion de la radiacion de Hawking.
4. Explicar por que una descripcion termica efectiva no implica necesariamente perdida fundamental de unitaridad.

## 14. Referencias y lecturas recomendadas

- Base: reseñas introductorias sobre entrelazamiento en QFT.
- Complementaria: Birrell y Davies para el trasfondo de campos y observadores parciales.
- Profundizacion: textos y notas sobre matrices reducidas, entropia de von Neumann y subregiones en QFT.


---

## Navegacion del tutorial

[(anterior) Neutrinos, Masas y Oscilaciones](../10_modelo_estandar/07_neutrinos_masas_y_oscilaciones.md) | [(siguiente) Agujeros negros, radiacion de Hawking y paradoja de la informacion](02_agujeros_negros_radiacion_de_hawking_y_paradoja_de_la_informacion.md)
