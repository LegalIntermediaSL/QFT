# Modulo 02: Relatividad y Campos

## Objetivo

Este modulo explica por que la Teoria Cuantica de Campos no es una decoracion sofisticada de la mecanica cuantica ordinaria, sino el marco natural para describir sistemas cuanticos relativistas con numero variable de particulas.

## Prerequisitos

- [00 Prerrequisitos](../00_prerrequisitos/README.md), en especial relatividad especial minima y notacion tensorial.
- [01 Fundamentos Conceptuales](../01_fundamentos_conceptuales/README.md), sobre todo la idea de campo y principios estructurales.

## Preguntas de comprobacion
- Por que falla la intuicion de una sola particula relativista como fundamento general.
- Que papel juega la relacion relativista entre energia, momento y masa.
- Por que la localidad empuja a formular la teoria en terminos de campos.
- Como se conecta la nocion de campo con la causalidad relativista.

## Documentos del modulo

1. `01_choque_entre_mq_y_relatividad.md`
2. `02_campos_localidad_y_causalidad.md`
3. `03_representaciones_de_lorentz_y_espinores.md`
4. `04_clasificacion_de_campos_por_spin.md`

## Capitulos imprescindibles en primera pasada

- [01 Choque entre MQ y relatividad](01_choque_entre_mq_y_relatividad.md): explica por que una teoria de una sola particula no basta.
- [02 Campos, localidad y causalidad](02_campos_localidad_y_causalidad.md): muestra por que el campo es el objeto correcto.
- [03 Representaciones de Lorentz y espinores](03_representaciones_de_lorentz_y_espinores.md): desarrolla la estructura de grupo que clasifica todos los campos.
- [04 Clasificacion de campos por spin](04_clasificacion_de_campos_por_spin.md): conecta representaciones con particulas fisicas via Wigner.

## Mapa del modulo

```mermaid
flowchart LR
    A["Una particula relativista no basta"] --> B["Numero variable de particulas"]
    B --> C["Campos como objetos fundamentales"]
    C --> D["Localidad y causalidad microfisica"]
```

## Apoyo recomendado

Antes o durante este modulo conviene leer tambien:

- `../01_fundamentos_conceptuales/03_que_es_un_campo_cuantico.md`

## Cuadernos asociados

- `../../Cuadernos/ejemplos/03_campos_y_localidad.ipynb`
- `../../Cuadernos/ejemplos/22_representaciones_de_lorentz.ipynb`
- `../../Cuadernos/problemas_resueltos/07_relatividad_y_campos.ipynb`

Uso sugerido:

- el cuaderno de `ejemplos/03` sirve para reforzar la intuicion de campo local frente a una descripcion de particulas puntuales;
- el cuaderno de `ejemplos/22` construye boosts de Lorentz y compara representaciones espinorial y vectorial con calculos explicitos;
- el de `problemas_resueltos` sirve para consolidar la relacion entre relatividad, numero variable de particulas y causalidad.

## Resultado esperado

Al terminar este bloque, deberia quedar claro que:

- el numero de particulas no puede tratarse como cantidad fija en un marco relativista general;
- las excitaciones fisicas deben organizarse sobre objetos definidos en el espacio-tiempo;
- la QFT no se entiende bien si se aprende solo como una tecnica de diagramas.

## Sintesis del modulo

Este modulo muestra por que la relatividad obliga a abandonar una intuicion ingenua de particulas aisladas y por que la localidad hace del campo el objeto natural de la teoria.

!!! note "Idea clave"
    Relatividad, causalidad y numero variable de particulas no encajan bien en una mecanica cuantica de una sola particula.

!!! warning "Error frecuente"
    Pensar que este bloque solo repite relatividad especial. En realidad introduce la necesidad estructural del lenguaje de campos.

!!! tip "Conexion con el siguiente modulo"
    Si los campos son los objetos correctos, el siguiente problema es describir su dinamica de forma compacta: eso ocurre con accion y lagrangiana.

## Ejercicios sugeridos

1. Explica por que una teoria relativista con numero fijo de particulas resulta insuficiente como marco general.
2. Describe la relacion entre localidad y formulacion en terminos de campos.
3. Explica que significa microcausalidad y por que es una exigencia relativista.
4. Resume por que este modulo prepara el paso natural hacia accion y simetrias.

## Lecturas y referencias recomendadas

- Introductorio: Tong, notas de QFT sobre motivacion relativista.
- Intermedio: Peskin y Schroeder, introduccion conceptual.
- Complementario: Weinberg, volumen I, para una perspectiva mas estructural sobre localidad y simetria.

## Navegacion

Anterior: [01 Fundamentos Conceptuales](../01_fundamentos_conceptuales/README.md)

Siguiente: [03 Accion y Simetrias](../03_accion_y_simetrias/README.md)
