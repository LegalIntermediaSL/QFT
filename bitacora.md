# Bitacora del Proyecto QFT

## Proposito

Esta bitacora registra el avance del proyecto, las decisiones editoriales, el estado del contenido y los siguientes pasos recomendados. Su funcion es mantener continuidad entre sesiones de trabajo y evitar que el tutorial crezca de forma desordenada.

## Estado general

El proyecto se encuentra en una etapa fundacional. La prioridad actual no es refinar detalles avanzados, sino establecer una base documental robusta desde la que se pueda desarrollar un tutorial completo de Teoria Cuantica de Campos.

## Entrada inicial

### Fecha

2026-04-18

### Situacion encontrada

- El repositorio solo contenia un `README.md` minimo con el nombre del proyecto.
- No existia documentacion de seguimiento.
- No habia historial editorial mas alla del commit inicial.

### Trabajo realizado

- Se redefinio el `README.md` como documento de presentacion del proyecto.
- Se creo `bitacora.md` para registrar avance, decisiones y prioridades.
- Se creo `changelog.md` para ordenar el historial de cambios.

### Decision editorial principal

Se adopta una estrategia de crecimiento por capas:

1. Documentacion base
2. Estructura del temario
3. Desarrollo progresivo de capitulos
4. Ejercicios, referencias y pulido final

Esta decision busca reducir friccion al inicio y facilitar que el proyecto mantenga coherencia a medida que aumente de tamano.

## Criterios de calidad acordados

- Cada seccion debe responder a una necesidad pedagogica clara.
- Las derivaciones deben evitar saltos grandes salvo que se indiquen referencias.
- La notacion debe ser consistente entre modulos.
- El contenido debe poder leerse de forma secuencial, aunque admita consulta puntual.
- La documentacion del proyecto debe actualizarse junto con el contenido tecnico.

## Riesgos identificados

- Crecer en volumen antes de definir una estructura puede volver el tutorial inconsistente.
- Introducir demasiados temas avanzados al principio puede romper la progresion pedagogica.
- Mezclar distintos estilos de notacion sin una convencion central puede volver confuso el material.
- No registrar decisiones editoriales puede generar retrabajo en futuras iteraciones.

## Proximos pasos recomendados

### Prioridad alta

- Crear un indice maestro del tutorial.
- Definir la estructura de carpetas y archivos por modulo o capitulo.
- Fijar convenciones basicas de notacion matematica y estilo.

### Prioridad media

- Redactar un capitulo cero de prerrequisitos.
- Disenar una plantilla reutilizable para cada tema.
- Preparar una bibliografia base comentada.

### Prioridad baja

- Anadir figuras, esquemas o diagramas.
- Incorporar ejercicios graduados por dificultad.
- Preparar una version en ingles o bilingue si el proyecto lo requiere.

## Propuesta de estructura futura

Una organizacion posible del repositorio podria ser:

- `docs/indice.md`
- `docs/00-prerrequisitos/`
- `docs/01-campos-clasicos/`
- `docs/02-cuantizacion-canonica/`
- `docs/03-campos-fermionicos/`
- `docs/04-gauge-y-qed/`
- `docs/05-renormalizacion/`
- `docs/06-temas-avanzados/`

## Nota de seguimiento

Cuando se agreguen capitulos, esta bitacora deberia reflejar:

- que seccion se abrio;
- que objetivos cubre;
- que decisiones de estilo o contenido se tomaron;
- que temas quedaron pendientes.

## Cierre de esta entrada

El proyecto ya cuenta con una base documental minima y coherente. A partir de aqui, el siguiente hito importante es transformar la idea general del tutorial en una arquitectura concreta de contenidos.

## Entrada de desarrollo de contenido

### Fecha

2026-04-18

### Objetivo

Comenzar la redaccion efectiva del tutorial con un bloque inicial autocontenido y legible en secuencia.

### Trabajo realizado

- Se creo la carpeta `Tutorial/`.
- Se creo un indice local en `Tutorial/README.md`.
- Se redacto `Tutorial/conceptos_fundamentales.md`.
- Se añadieron cuatro articulos introductorios sobre relatividad y campos, formulacion lagrangiana, cuantizacion canonica e interacciones.

### Decisiones tomadas

- Empezar por un bloque conceptual antes de entrar en tecnicas mas avanzadas.
- Mantener articulos relativamente breves pero conectados entre si.
- Priorizar claridad de exposicion sobre densidad matematica en esta primera iteracion.

### Pendientes inmediatos

- Crear un capitulo de prerrequisitos matematicos.
- Desarrollar una nota sobre la ecuacion de Dirac y los campos fermionicos.
- Abrir un modulo dedicado a integral de camino.
- Empezar una seccion de ejercicios de comprobacion.
