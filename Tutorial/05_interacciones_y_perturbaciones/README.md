# Modulo 05: Interacciones y Perturbaciones

## Objetivo

Este modulo introduce el paso desde teorias libres a teorias interactuantes y presenta el marco perturbativo que conduce a la matriz $S$ y a los diagramas de Feynman.

## Prerequisitos

- [04 Cuantizacion del Campo Escalar](../04_cuantizacion_del_campo_escalar/README.md).
- Comodidad con operadores de creacion y aniquilacion, expansion en modos y lenguaje lagrangiano.

## Documentos del modulo

1. `01_teoria_de_perturbaciones_y_matriz_s.md`
2. `02_diagramas_de_feynman_y_reglas.md`
3. `03_reduccion_lsz_y_correladores_amputados.md`
4. `04_reglas_de_feynman_resumen_operativo.md`

## Capitulos imprescindibles en primera pasada

- [01 Teoria de perturbaciones y matriz S](01_teoria_de_perturbaciones_y_matriz_s.md): introduce el objeto fisico que se quiere calcular.
- [02 Diagramas de Feynman y reglas](02_diagramas_de_feynman_y_reglas.md): organiza la expansion perturbativa.
- [03 Reduccion LSZ y correladores amputados](03_reduccion_lsz_y_correladores_amputados.md): evita que los diagramas se aprendan como pura receta.

## Mapa del modulo

```mermaid
flowchart LR
    A["Teoria libre"] --> B["Separacion L0 + Lint"]
    B --> C["Matriz S"]
    C --> D["Serie de Dyson"]
    D --> E["Diagramas de Feynman"]
    E --> F["LSZ y amputacion"]
    F --> G["Reglas operativas"]
    G --> H["Amplitudes observables"]
```

## Hilo conceptual

Las ideas clave del modulo son:

- una teoria libre no basta para describir procesos fisicos observables;
- las interacciones se codifican localmente en la lagrangiana;
- muchas amplitudes se estudian como expansion en potencias del acoplamiento;
- los diagramas de Feynman son una sintaxis de esa expansion.
- los correladores contienen mas estructura que la amplitud observable;
- LSZ explica por que el paso desde correladores a scattering no es un truco grafico, sino un puente formal.

## Cuadernos asociados

- `../../Cuadernos/ejemplos/06_diagramas_de_feynman_basicos.ipynb`
- `../../Cuadernos/problemas_resueltos/10_interacciones_y_perturbaciones.ipynb`

## Resultado esperado

Al terminar, el lector deberia saber que objeto se calcula en un problema de dispersion, por que un diagrama no es una fotografia del proceso, y como se relacionan correladores, amputacion y amplitudes fisicas.

## Sintesis del modulo

Este modulo convierte la teoria libre en una teoria capaz de describir procesos reales. La matriz S, Dyson, diagramas y LSZ forman aqui el nucleo operativo del scattering perturbativo.

!!! note "Idea clave"
    Los diagramas de Feynman son una sintaxis de la expansion perturbativa, no una fotografia literal del proceso.

!!! warning "Error frecuente"
    Aprender reglas de Feynman sin entender la diferencia entre correlador, amplitud y observable.

!!! tip "Conexion con el siguiente modulo"
    El siguiente bloque repite esta logica en el caso fermionico y completa el repertorio de campos relativistas del curso.

## Ejercicios sugeridos

1. Escribe los tres primeros terminos de la expansion de Dyson y comenta que clase de correcciones representa cada orden.
2. Explica la diferencia entre amplitud, probabilidad, seccion eficaz y observable experimental final.
3. Toma una teoria escalar $\phi^4$ y enumera los ingredientes minimos que necesitas para construir el proceso $2\to2$ a nivel de arbol.
4. Describe verbalmente la idea de amputacion y por que LSZ conecta correladores con scattering.
5. Compara linea externa, linea interna y propagador en un diagrama de Feynman, subrayando que objeto corresponde a estados asintoticos.

## Lecturas y referencias recomendadas

- Introductorio: Tong, notas sobre matriz S y teoria perturbativa.
- Intermedio: Peskin y Schroeder, expansion de Dyson y reglas de Feynman.
- Complementario: notas pedagogicas sobre reduccion LSZ y funciones de Green.
- Complementario: Zee, para reforzar intuicion fisica sobre diagramas y amplitudes.

## Navegacion

Anterior: [04 Cuantizacion del Campo Escalar](../04_cuantizacion_del_campo_escalar/README.md)

Siguiente: [06 Fermiones y Dirac](../06_fermiones_y_dirac/README.md)
