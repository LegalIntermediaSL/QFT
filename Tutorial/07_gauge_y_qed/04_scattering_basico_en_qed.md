# Scattering Basico en QED

**Nivel:** Nucleo  
**Dificultad:** Media-Alta  
**Tiempo estimado:** 18-25 min  
**Prerequisitos recomendados:** [Fijacion de Gauge y Propagador del Foton](03_fijacion_de_gauge_y_propagador_del_foton.md) · [Resumen del modulo](README.md)


## 1. Proposito

Este documento aterriza el modulo con un ejemplo conceptual de scattering en QED. La idea no es completar un calculo fenomenologico largo, sino mostrar como el lagrangiano, las reglas de Feynman y la interpretacion fisica se ensamblan en un proceso concreto.

QED es un laboratorio excelente para aprender esta logica porque una enorme familia de procesos se apoya en una estructura de interaccion sorprendentemente simple.

## 2. El vertice elemental

Toda la complejidad perturbativa de QED nace del termino

$$
-e\bar{\psi}\gamma^\mu A_\mu \psi.
$$

Ese acoplamiento produce el vertice electron-foton y, con el, amplitudes de emision, absorcion e intercambio de fotones virtuales.

Este punto merece resaltarse: una gran variedad de fenomenos distintos puede rastrearse hasta una unica estructura elemental del lagrangiano.

## 3. Ejemplo conceptual: intercambio de foton

Uno de los procesos mas simples consiste en una interaccion entre dos fermiones cargados mediada por intercambio de un foton virtual. La lectura minima del diagrama es:

- dos lineas fermionicas externas representan estados iniciales y finales;
- una linea interna ondulada representa el foton virtual;
- dos vertices aportan factores $-ie\gamma^\mu$;
- el propagador del foton transporta el momento intercambiado.

Aunque este ejemplo suele imaginarse como "una particula emite un foton y la otra lo absorbe", esa imagen debe entenderse solo como apoyo intuitivo. El calculo real trabaja con amplitudes y estados asintoticos, no con una pelicula literal de trayectorias microscopicas.

## 4. Estructura de la amplitud

Sin entrar en toda la algebra de espinores, la amplitud a nivel de arbol tiene una forma esquematica como

$$
\mathcal{M} \sim
\bar{u}(p')\gamma^\mu u(p)\,
\frac{-i\eta_{\mu\nu}}{q^2+i\epsilon}\,
\bar{u}(k')\gamma^\nu u(k),
$$

donde $q$ es el momento transferido.

Esta expresion ya enseña mucho:

- las corrientes fermionicas aparecen en los extremos;
- el propagador del foton conecta ambos vertices;
- la dinamica del proceso esta organizada por la estructura gauge del lagrangiano.

Tambien muestra por que los espinores externos no son un adorno tecnico. Codifican los estados iniciales y finales de fermiones reales, mientras que el propagador interno representa una contribucion virtual que no tiene por que estar on-shell.

## 5. Que se aprende de este ejemplo

Incluso sin completar un calculo de seccion eficaz, este ejemplo deja claras varias ideas:

- el lagrangiano determina el vertice;
- el gauge-fixing permite definir el propagador;
- la amplitud se construye multiplicando corrientes, propagadores y factores de acoplamiento;
- un diagrama de arbol ya captura una prediccion fisica interpretable.

Ademas, deja ver una continuidad útil con el electromagnetismo clasico. En el limite adecuado, el intercambio de un foton virtual entre corrientes cargadas recupera la intuicion de una interaccion electromagnetica mediada por el campo.

## 6. Relacion con procesos reales

La misma logica basica se reutiliza en:

- scattering electron-muon;
- scattering Bhabha;
- aniquilacion $e^+e^- \to \mu^+\mu^-$;
- correcciones radiativas a orden superior.

El valor pedagogico de QED esta en que toda esa familia de procesos nace de una estructura lagrangiana extraordinariamente simple.

## 7. Ejemplo corto de lectura

Si una amplitud contiene dos corrientes fermionicas unidas por un propagador de foton, ya puede verse el nucleo fisico del proceso: una carga electromagnetica influencia a otra mediante el campo gauge. Esa es la version relativista y cuantica del viejo problema de interaccion electromagnetica.

En espacio de momentos, esta lectura se vuelve especialmente nítida: las lineas externas fijan estados asintoticos, el propagador codifica el intercambio y el denominador en $q^2$ anticipa la estructura dinamica asociada al momento transferido.

## 8. Cuaderno asociado

- `../../Cuadernos/problemas_resueltos/13_gauge_fixing_y_scattering_en_qed.ipynb`: usarlo para seguir el esqueleto de una amplitud elemental en QED, distinguiendo vertices, propagador interno y lectura fisica del resultado.
- `../../Cuadernos/ejemplos/06_diagramas_de_feynman_basicos.ipynb`: usarlo para revisar la sintaxis diagramatica y la lectura de propagadores y vertices.
- `../../Cuadernos/problemas_resueltos/10_interacciones_y_perturbaciones.ipynb`: usarlo como apoyo para la logica general del calculo perturbativo.

## 9. Advertencias utiles

- El foton interno del diagrama no es una particula observable en el mismo sentido que un foton externo real.
- La amplitud no es todavia una probabilidad ni una seccion eficaz.
- La estructura de espinores y polarizaciones no debe reducirse a una lectura meramente visual del diagrama.
- Los factores de normalizacion, sumas de espin y promedios sobre polarizaciones son parte esencial del paso a observables.

## 10. Preguntas de comprobacion

- Como se lee la estructura general de una amplitud de arbol en QED.
- Que papel juegan las corrientes fermionicas en los extremos del propagador.
- Por que este ejemplo resume bien la arquitectura del modulo.

## 11. Cierre

Este ejemplo condensa muy bien la logica perturbativa completa: el lagrangiano fija el vertice, el gauge-fixing permite escribir el propagador, los espinores externos representan estados reales y el diagrama organiza la amplitud. Entender bien este esqueleto hace mucho mas natural el salto a procesos mas ricos y a correcciones radiativas.

## 12. Referencias y lecturas recomendadas

- Base: Peskin y Schroeder, amplitudes a arbol en QED.
- Complementaria: Schwartz, procesos relativistas elementales en electrodinamica cuantica.
- Profundizacion: textos de amplitudes y scattering relativista con espinores de Dirac.


---

## Navegacion del tutorial

[(anterior) Fijacion de Gauge y Propagador del Foton](03_fijacion_de_gauge_y_propagador_del_foton.md) | [(siguiente) Polarizaciones y Sumas de Espin en QED](05_polarizaciones_y_sumas_de_espin.md)