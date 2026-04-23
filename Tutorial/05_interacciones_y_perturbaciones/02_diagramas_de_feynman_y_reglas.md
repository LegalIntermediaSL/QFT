# Diagramas de Feynman y Reglas de Calculo

**Nivel:** Nucleo  
**Dificultad:** Media  
**Tiempo estimado:** 25-35 min  
**Prerequisitos recomendados:** [Teoria de Perturbaciones y Matriz S](01_teoria_de_perturbaciones_y_matriz_s.md) · [Resumen del modulo](README.md)

## Proposito

Este capitulo traduce la expansion perturbativa en una sintaxis diagramatica operativa y aclara que los diagramas de Feynman organizan amplitudes, no trayectorias microscopicas literales.

## 1. Introduccion

Los diagramas de Feynman son una de las representaciones visuales mas famosas de la fisica, pero su sentido real suele malinterpretarse. No son dibujitos de trayectorias microscopicas. Son una notacion compacta para terminos de la expansion perturbativa de amplitudes.

## 2. De la serie formal al diagrama

Al expandir la matriz $S$ en la serie de Dyson aparecen productos temporales de campos. Al evaluar sus elementos de matriz, esos productos se reorganizan mediante contracciones y propagadores. El resultado puede codificarse en diagramas.

Cada diagrama representa:

- cierto patron de contracciones;
- un orden determinado en el acoplamiento;
- una contribucion precisa a la amplitud.

Ese origen es importante porque evita un error muy comun: el diagrama no es el punto de partida del calculo. El punto de partida real es el lagrangiano y la expansion de Dyson. El diagrama aparece despues, como un sistema de organizacion.

Por eso aprender diagramas de Feynman no deberia convertirse en memorizar iconos aislados. Lo esencial es entender de que termino del lagrangiano nace cada regla.

## 3. Ingredientes basicos

En un diagrama aparecen tres elementos fundamentales:

- lineas externas, asociadas a estados iniciales y finales;
- lineas internas, asociadas a propagadores;
- vertices, asociados a inserciones del termino de interaccion.

Esta sintaxis visual permite leer de un vistazo la estructura combinatoria del calculo.

Ademas, la representacion permite separar de manera intuitiva que partes del problema vienen de la dinamica libre y cuales de la interaccion local. Las lineas internas heredan la cinematica libre; los vertices heredan la estructura del lagrangiano interactuante.

Esa division del trabajo entre propagadores y vertices es una de las razones por las que la notacion diagramatica resulta tan eficiente.

## 4. Propagador

El propagador no debe interpretarse ingenuamente como la trayectoria clasica de una particula virtual. Es una funcion de Green del operador cinetico libre, y en espacio de momentos para un campo escalar libre toma la forma tipica

$$
\frac{i}{p^2 - m^2 + i\epsilon}.
$$

Ese factor aparece cada vez que una linea interna transporta momento entre vertices.

El termino $i\epsilon$ no es un adorno notacional. Codifica la prescripcion correcta para tratar polos y fijar la estructura causal del propagador de Feynman.

En otras palabras, incluso dentro del dibujo hay contenido analitico serio: cada linea interna resume una funcion de Green con propiedades muy precisas.

## 5. Vertices e interaccion

Un vertice codifica la estructura local de la interaccion. En una teoria $\phi^4$, por ejemplo, un vertice conecta cuatro lineas del campo. El factor asociado depende de la normalizacion elegida, pero esquematicamente esta controlado por el acoplamiento $\lambda$.

De nuevo, el diagrama no inventa la interaccion: la traduce desde la lagrangiana.

En teorias mas ricas, distintos vertices pueden coexistir y llevar:

- diferentes constantes de acoplamiento;
- diferentes estructuras de espin;
- indices internos de color o sabor;
- factores de grupo.

Por eso aprender reglas de Feynman no consiste en memorizar dibujos, sino en saber leer el lagrangiano como generador de reglas.

Un buen criterio practico es este:

- mirar la parte cuadratica para identificar propagadores;
- mirar la parte interactiva para identificar vertices;
- usar las simetrias para controlar factores y estructuras permitidas.

## 6. Conservacion del momento

En cada vertice aparece una delta de Dirac que impone conservacion del momento:

$$
(2\pi)^4\delta^{(4)}\left(\sum p_{\text{entrantes}} - \sum p_{\text{salientes}}\right).
$$

Esto refleja la invariancia traslacional de la teoria y conecta el calculo diagramatico con el teorema de Noether.

Asi se ve muy bien que los diagramas no flotan desconectados del resto del formalismo: tambien heredan directamente las simetrias fundamentales de la teoria.

En la practica, estas deltas permiten eliminar parte de las integrales y reducir el calculo a los grados de libertad internos realmente independientes.

## 7. Lazos y momentos internos

Cuando un diagrama contiene lazos cerrados, aparecen momentos internos no fijados por las condiciones externas. Debe integrarse sobre ellos:

$$
\int \frac{d^4k}{(2\pi)^4}.
$$

Es justamente aqui donde suelen nacer las divergencias ultravioletas y donde la renormalizacion se vuelve necesaria.

Los lazos introducen ademas informacion genuinamente cuantica que no existe en un tratamiento puramente clasico o de arbol. Son responsables de desplazamientos de masas, corridas de acoplamientos y muchas de las predicciones de precision mas importantes de la teoria.

Por eso un lazo no es simplemente "un diagrama mas complicado". Marca el punto donde aparecen regularizacion, renormalizacion y dependencia en escala.

## 8. Arboles y lazos

Conviene distinguir:

- diagramas de arbol, sin lazos, que suelen dar la contribucion dominante a orden mas bajo;
- diagramas con lazos, que incorporan correcciones cuanticas de orden superior.

Esta distincion no es solo topologica. Marca tambien el paso desde efectos basicos de interaccion hacia correcciones radiativas propiamente cuanticas.

En ese sentido, un diagrama de arbol suele capturar el esqueleto del proceso, mientras que los lazos capturan su refinamiento cuantico.

## 9. Simetria, factores combinatorios y suma sobre diagramas

Un mismo proceso fisico rara vez queda representado por un unico diagrama. A un orden dado suelen contribuir varios diagramas diferentes, y ademas cada uno puede venir acompañado por factores combinatorios o de simetria.

Esto enseña una leccion importante:

- el significado fisico final nunca pertenece a un diagrama aislado;
- pertenece a la suma coherente de todas las contribuciones pertinentes del orden considerado.

La interferencia entre diagramas es una parte esencial de la prediccion cuantica.

Este punto es crucial porque evita atribuir demasiado significado fisico a un solo grafico aislado. Muchas veces el efecto observable depende precisamente de sumas, cancelaciones o refuerzos entre varias contribuciones.

## 10. Procedimiento practico de lectura

Al ver un diagrama, una rutina util es:

1. identificar las lineas externas y el proceso considerado;
2. contar vertices para conocer el orden del acoplamiento;
3. asignar propagadores a las lineas internas;
4. imponer conservacion del momento en cada vertice;
5. integrar sobre momentos internos independientes;
6. sumar todos los diagramas del mismo orden compatibles con el proceso.

En problemas con espin, color u otros grados de libertad internos, a esa rutina hay que añadir la algebra correspondiente. Por eso la sintaxis visual simplifica mucho, pero no elimina la necesidad de manipular expresiones analiticas con cuidado.

Los diagramas son, por tanto, una interfaz entre intuicion visual y calculo algebraico: ayudan muchisimo, pero no sustituyen la parte analitica del problema.

## 11. Ejemplo conceptual: scattering $2\to2$ en $\phi^4$

Para una teoria $\phi^4$, el proceso mas basico de scattering entre dos particulas entrantes y dos salientes aparece ya con un vertice elemental. A orden mas bajo:

- hay cuatro lineas externas;
- no hay lazos;
- el orden en el acoplamiento es $\lambda$.

A orden superior pueden aparecer diagramas con lazos en los canales usuales, lo que introduce dependencia mas rica en los invariantes cinematicos y obliga a renormalizar.

Este ejemplo es valioso porque muestra, en su forma mas simple, todo el vocabulario del formalismo.

Y lo hace sin ocultar la idea central: incluso el proceso mas sencillo ya enseña como se relacionan orden perturbativo, topologia del diagrama e informacion fisica.

## 12. Lo que un diagrama no es

Conviene insistir en varios puntos:

- no es la foto de particulas chocando como bolitas;
- no es una cronologia literal del proceso cuantico;
- no es por si solo una probabilidad observable;
- no reemplaza las reglas analiticas: las resume.

Insistir en esto al principio evita muchos malentendidos posteriores, sobre todo cuando se empieza a hablar de particulas virtuales como si fueran objetos detectables por si mismos.

## 13. Poder conceptual de la representacion

Pese a estas advertencias, los diagramas son extraordinarios porque permiten:

- organizar calculos largos;
- visualizar canales posibles de interaccion;
- clasificar rapidamente ordenes perturbativos;
- detectar lazos, subdiagramas y origen de divergencias.

Por eso su valor no es solo estetico ni pedagogico: es tambien computacional.

Tambien tienen un valor heuristico muy fuerte. Ayudan a anticipar:

- que procesos estan permitidos o prohibidos;
- que orden en el acoplamiento domina;
- donde cabe esperar divergencias;
- que canales de intercambio pueden contribuir.

## Cuaderno asociado

- Consulta los cuadernos asociados de este bloque en [Resumen del modulo](README.md) para reforzar el capitulo con practica guiada.

## 14. Preguntas de comprobacion
- Que representa exactamente una linea interna.
- De donde sale el propagador escalar.
- Que informacion fisica y algebraica codifica un vertice.
- Por que los lazos obligan a integrar sobre momentos internos.
- Que distingue una amplitud de la interpretacion visual ingenua del diagrama.

## 15. Ejercicios sugeridos

1. Explica por que un diagrama de Feynman debe entenderse como termino de una expansion y no como representacion literal de un suceso microscopico.
2. Describe el papel del propagador, del vertice y de la delta de conservacion del momento en un diagrama sencillo.
3. Compara un diagrama de arbol con uno de lazo y explica que informacion cuantica adicional aparece en el segundo.

## 16. Cierre

Los diagramas de Feynman son la gramatica visual de la teoria de perturbaciones. Entendidos correctamente, muestran como la estructura local de la lagrangiana se convierte en reglas sistematicas para calcular amplitudes observables.

## 17. Referencias y lecturas recomendadas

- Base: Peskin y Schroeder, reglas de Feynman y propagadores.
- Complementaria: Tong, lectura pedagogica de diagramas y amplitudes.
- Profundizacion: Schwartz, organizacion moderna de reglas y calculos perturbativos.


---

## Navegacion del tutorial

[(anterior) Teoria de Perturbaciones y Matriz S](01_teoria_de_perturbaciones_y_matriz_s.md) | [(siguiente) Reduccion LSZ y Correladores Amputados](03_reduccion_lsz_y_correladores_amputados.md)
