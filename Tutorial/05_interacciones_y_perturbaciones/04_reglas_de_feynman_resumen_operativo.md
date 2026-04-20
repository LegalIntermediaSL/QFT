# Reglas de Feynman: Resumen Operativo

## 1. Proposito

Este articulo organiza el modulo en una forma mas practica. La idea es convertir el recorrido conceptual de matriz $S$, expansion de Dyson, diagramas y LSZ en una lista de trabajo clara para empezar a calcular amplitudes sencillas sin perder de vista el significado fisico de cada paso.

## 2. Antes de dibujar diagramas

Lo primero nunca es dibujar. Lo primero es identificar:

- que teoria estamos usando;
- cual es su lagrangiana libre;
- cual es su lagrangiana de interaccion;
- que proceso fisico se quiere calcular;
- a que orden del acoplamiento se desea trabajar.

Sin eso, un diagrama no significa nada.

## 3. Extraer ingredientes del lagrangiano

Del lagrangiano se leen las piezas que luego alimentan el calculo:

- propagadores de la parte libre;
- vertices de la parte interactuante;
- indices de espin, sabor, color o gauge si la teoria los tiene;
- factores de signo y normalizacion.

Esta es una leccion importante del modulo: las reglas de Feynman no se memorizan como dibujos aislados, se derivan del lagrangiano.

## 4. Lista operativa minima

Para un proceso perturbativo sencillo, una rutina util es:

1. fijar los estados iniciales y finales;
2. enumerar todos los diagramas del orden deseado;
3. asignar un propagador a cada linea interna;
4. asignar un factor de vertice a cada interaccion local;
5. imponer conservacion del momento en cada vertice;
6. integrar sobre los momentos internos no fijados;
7. sumar todas las contribuciones;
8. amputar y normalizar segun el contexto fisico del calculo.

## 5. Reglas tipicas en teoria escalar

En una teoria escalar libre-interactuante de tipo $\phi^4$ aparecen, de manera esquematica:

- una linea interna con factor

$$
\frac{i}{p^2-m^2+i\epsilon};
$$

- un vertice de cuatro patas controlado por $\lambda$;
- una delta de Dirac que conserva el momento total en cada vertice.

Esto basta para construir los diagramas de arbol mas simples y empezar a ver de donde nacen los diagramas con lazos.

## 6. Que cambia al pasar a teorias mas ricas

Cuando la teoria incluye espin o gauge, la lista operativa sigue siendo la misma, pero se añaden nuevas capas:

- espinores externos para fermiones;
- polarizaciones para bosones vectoriales;
- estructuras matriciales como $\gamma^\mu$;
- factores de grupo para simetrias internas.

Por eso este modulo conviene leerlo como un esqueleto general que luego se especializa en QED, teorias gauge y Modelo Estandar.

## 7. Errores comunes

Al empezar a usar reglas de Feynman, los errores mas frecuentes suelen ser:

- olvidar diagramas compatibles del mismo orden;
- confundir linea interna con particula observable;
- perder factores de signo o simetria;
- interpretar el diagrama como historia literal;
- no distinguir amplitud, elemento de matriz y observable final.

## 8. Ejemplo corto de trabajo

En scattering $2\to2$ escalar a nivel de arbol, una estrategia razonable es:

1. identificar las cuatro patas externas;
2. contar cuantos vertices minimos exige la teoria;
3. escribir el factor analitico del diagrama;
4. extraer la amplitud invariante correspondiente;
5. dejar para una etapa posterior el paso a seccion eficaz.

Esta separacion ayuda a no mezclar niveles conceptuales.

## 9. Puente con los modulos siguientes

Este resumen operativo prepara directamente para:

- fermiones relativistas, donde las lineas externas ya no son escalares;
- QED, donde los vertices cargan estructura vectorial y espinorial;
- renormalizacion, donde aparecen integrales de lazo y dependencia con la escala.

En otras palabras, este documento cierra el modulo `05` y lo convierte en una plataforma de lanzamiento para los modulos tecnicos mas potentes del tutorial.

## 10. Cuaderno asociado

- `../../Cuadernos/ejemplos/06_diagramas_de_feynman_basicos.ipynb`: usarlo para practicar la traduccion entre diagrama y expresion analitica.
- `../../Cuadernos/problemas_resueltos/10_interacciones_y_perturbaciones.ipynb`: usarlo para ordenar el calculo completo de un proceso elemental y comprobar donde aparecen los distintos factores.

## 11. Preguntas de comprobacion

- Que informacion se extrae de la parte libre y cual de la parte interactuante.
- Por que deben sumarse todos los diagramas de un mismo orden.
- Que diferencia hay entre linea externa, linea interna y propagador amputado.
- Por que este modulo no basta todavia para tratar fermiones o gauge con comodidad.

## 12. Referencias y lecturas recomendadas

- Base: Tong, matriz $S$, diagramas y amplitudes.
- Complementaria: Peskin y Schroeder, reglas de Feynman a partir del lagrangiano.
- Profundizacion: Schwartz, enfoque moderno y organizado de calculo perturbativo.


---

## Navegacion del tutorial

[(anterior) Reduccion LSZ y Correladores Amputados](03_reduccion_lsz_y_correladores_amputados.md) | [(siguiente) Motivacion y Ecuacion de Dirac](../06_fermiones_y_dirac/01_motivacion_y_ecuacion_de_dirac.md)
