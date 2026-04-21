# Reglas de Feynman y Propagadores: Guia de Consulta Rapida

## Objetivo

Este apendice reune, en una sola pieza, un resumen conceptual de propagadores y reglas de Feynman que aparecen repartidos por varios modulos del tutorial. No sustituye los desarrollos detallados de `04`, `05`, `07`, `09` y `10`, pero sirve como mapa de consulta transversal.

La meta es doble:

- recordar rapidamente que objeto corresponde a cada linea o vertice;
- evitar errores comunes de interpretacion cuando se pasa del lagrangiano al calculo perturbativo.

## 1. Idea general

Las reglas de Feynman son un procedimiento organizado para traducir un lagrangiano en expresiones analiticas para amplitudes perturbativas. En esa traduccion aparecen de forma repetida tres ingredientes:

- lineas externas;
- propagadores;
- vertices.

El principio rector es simple: el lagrangiano libre determina propagadores y la parte interactuante determina vertices.

Dicho de otro modo:

- el sector cuadratico dice como propagan los campos;
- el sector no cuadratico dice como interactuan.

## 2. Propagador escalar libre

Para un campo escalar libre, el propagador de Feynman en espacio de momentos es

$$
\frac{i}{p^2-m^2+i\epsilon}.
$$

Este factor aparece:

- en correladores libres;
- en lineas internas de diagramas escalares;
- como funcion de Green del operador de Klein-Gordon.

Los polos en $p^2=m^2$ recuerdan donde vive el espectro libre de la teoria. El termino $i\epsilon$ no es decorativo: fija la prescripcion causal correcta.

## 3. Propagador fermionico libre

Para un fermion de Dirac libre, el propagador toma la forma

$$
\frac{i(\slashed{p}+m)}{p^2-m^2+i\epsilon}.
$$

Aqui el numerador refleja la estructura espinorial de la teoria. Este objeto prepara la lectura de QED y del sector fermionico del Modelo Estandar.

Una buena manera de leerlo es esta:

- el denominador recuerda la estructura relativista del polo;
- el numerador codifica la parte spinorial necesaria para que el propagador invierta el operador de Dirac.

## 4. Propagador del foton

En teorias gauge, el propagador depende de la fijacion de gauge. En una forma covariante sencilla suele aparecer esquematicamente como

$$
\frac{-ig_{\mu\nu}}{p^2+i\epsilon}
$$

en un gauge covariante adecuado. Lo importante pedagogicamente es recordar que:

- no todos los componentes del potencial gauge son grados de libertad fisicos;
- la fijacion de gauge forma parte del procedimiento bien definido del calculo.

En una gauge covariante general, el propagador puede contener tambien una parte proporcional a $p_\mu p_\nu$, lo que deja aun mas clara la presencia de redundancia gauge en el formalismo intermedio.

## 5. Vertices tipicos

Algunos vertices minimos que se repiten en el tutorial son:

- en $\phi^4$, un vertice de cuatro patas controlado por $\lambda$;
- en QED, un vertice fermion-foton controlado por $e\gamma^\mu$;
- en teorias gauge no abelianas, vertices gauge-autointeractuantes determinados por la estructura del grupo.

La regla general es no memorizar el dibujo primero, sino identificar de que termino de la lagrangiana nace el vertice.

Si el termino de interaccion se entiende bien, el vertice deja de ser un objeto grafico arbitrario y se vuelve una simple traduccion del lagrangiano a espacio de momentos.

## 6. Lineas externas

Las lineas externas representan estados asintoticos de entrada y salida. No se tratan exactamente igual que las internas porque:

- estan asociadas a particulas observables;
- aparecen ligadas a factores de normalizacion;
- en una formulacion mas formal, se conectan con LSZ y la amputacion de correladores.

En el caso fermionico aparecen espinores externos como $u(p)$, $\bar u(p)$, $v(p)$ y $\bar v(p)$; en el caso de gauge, vectores de polarizacion cuando las particulas externas son reales.

## 7. Conservacion del momento

Cada vertice trae asociada una delta de Dirac que impone conservacion del momento. Esa estructura no es accidental: refleja la invariancia traslacional de la teoria y conecta directamente con Noether.

En la practica, esta delta permite eliminar una de las integrales de momento o simplificar de inmediato la estructura del diagrama.

## 8. Arboles y lazos

Conviene distinguir entre:

- diagramas de arbol, que suelen dominar a orden mas bajo;
- diagramas con lazos, que introducen correcciones cuanticas, integrales internas y posibles divergencias ultravioletas.

Esta distincion es esencial para enlazar teoria perturbativa con renormalizacion.

Tambien ayuda a leer el orden perturbativo:

- mas vertices suele significar orden mas alto en el acoplamiento;
- mas lazos suele significar mayor estructura cuantica y mayor sensibilidad a regularizacion.

## 9. Receta de uso rapido

Si quieres montar una amplitud sencilla a partir del lagrangiano:

1. identifica los campos externos del proceso;
2. localiza el termino de interaccion pertinente;
3. escribe el vertice correspondiente;
4. conecta vertices con propagadores internos;
5. añade la delta de conservacion del momento;
6. incorpora factores de normalizacion y espinores o polarizaciones externas;
7. solo al final simplifica algebra e interpreta el resultado.

## 10. Errores de interpretacion frecuentes

- Un propagador no es la trayectoria clasica de una particula virtual.
- Un diagrama no es una cronologia literal del proceso.
- Una amplitud no coincide todavia con un observable experimental final.
- El conjunto fisico relevante es la suma coherente de todos los diagramas del orden considerado.
- No debe confundirse linea externa con particula interna on-shell.

## 11. Puentes dentro del tutorial

Este apendice se conecta especialmente con:

- [Campo escalar y modos normales](../04_cuantizacion_del_campo_escalar/01_campo_escalar_clasico_y_modos_normales.md)
- [Cuantizacion canonica y espacio de Fock](../04_cuantizacion_del_campo_escalar/02_cuantizacion_canonica_y_espacio_de_fock.md)
- [Propagador, causalidad y funcion de Green](../04_cuantizacion_del_campo_escalar/03_propagador_causalidad_y_funcion_de_green.md)
- [Teoria de perturbaciones y matriz S](../05_interacciones_y_perturbaciones/01_teoria_de_perturbaciones_y_matriz_s.md)
- [Diagramas de Feynman y reglas de calculo](../05_interacciones_y_perturbaciones/02_diagramas_de_feynman_y_reglas.md)
- [QED y lagrangiano fundamental](../07_gauge_y_qed/02_qed_y_lagrangiano_fundamental.md)

## 12. Uso recomendado

Este documento funciona mejor como hoja de consulta mientras se estudian otros modulos. La estrategia mas util suele ser:

1. leer primero el desarrollo conceptual en su modulo de origen;
2. volver luego a este apendice para consolidar notacion y patrones;
3. usarlo como referencia rapida al resolver ejercicios o cuadernos.

## 13. Referencias y lecturas recomendadas

- Base: Peskin y Schroeder, reglas de Feynman y propagadores.
- Complementaria: Tong, amplitudes y teoria perturbativa.
- Profundizacion: Schwartz, formulacion moderna de propagadores y amplitudes.
