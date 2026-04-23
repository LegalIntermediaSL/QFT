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

## Entrada de ampliacion estructural

### Fecha

2026-04-18

### Objetivo

Convertir el bloque inicial del tutorial en una estructura mas cercana a un curso real, con modulos y subdocumentos mas extensos.

### Situacion detectada

- Los articulos iniciales funcionaban bien como introduccion, pero resultaban demasiado breves para sostener una lectura profunda.
- Varias ideas importantes aparecian apenas enunciadas y no suficientemente desarrolladas.
- La estructura plana de archivos limitaba la posibilidad de crecer por temas.

### Trabajo realizado

- Se reorganizo `Tutorial/` por modulos tematicos.
- Se crearon cuatro carpetas nuevas para relatividad, accion y simetrias, cuantizacion, e interacciones.
- Se añadieron ocho documentos extensos nuevos.
- Las portadas originales pasaron a funcionar como indices de navegacion.
- Se actualizo el `Tutorial/README.md` para reflejar la nueva arquitectura.

### Resultado

El tutorial paso de una coleccion corta de notas introductorias a una base modular con mas de mil lineas de contenido, suficiente para comenzar a desarrollar un recorrido sostenido.

### Pendientes inmediatos

- Incorporar ejercicios y problemas al final de cada modulo.
- Añadir un modulo de prerrequisitos matematicos.
- Abrir el bloque de campos fermionicos.
- Mantener consistencia de estilo y notacion entre los nuevos modulos.

## Entrada de profundizacion de articulos

### Fecha

2026-04-19

### Objetivo

Aumentar la densidad pedagogica de varios articulos clave para que funcionen mejor como material de estudio y no solo como introducciones conceptuales.

### Trabajo realizado

- Se amplió `Tutorial/01_relatividad_y_campos/01_choque_entre_mq_y_relatividad.md`.
- Se amplió `Tutorial/01_relatividad_y_campos/02_campos_localidad_y_causalidad.md`.
- Se amplió `Tutorial/04_interacciones_y_perturbaciones/01_teoria_de_perturbaciones_y_matriz_s.md`.
- Se amplió `Tutorial/04_interacciones_y_perturbaciones/02_diagramas_de_feynman_y_reglas.md`.
- Se añadieron nuevas secciones de contexto, ejemplos conceptuales y ejercicios sugeridos.

### Resultado

Los cuatro documentos pasaron a sumar 686 lineas de contenido, con mejor continuidad entre conceptos, mas advertencias metodologicas y un nivel mas cercano al de un curso escrito.

### Pendientes inmediatos

- Repetir esta profundizacion en los modulos de accion y cuantizacion.
- Añadir ejercicios tambien a los documentos marco.
- Empezar el bloque de fermiones y ecuacion de Dirac.

## Entrada de reorganizacion curricular

### Fecha

2026-04-19

### Objetivo

Pasar de una estructura mixta de notas y modulos a una arquitectura mas curricular, con recorrido numerado, indices mas claros y soporte visual.

### Trabajo realizado

- Se reorganizo `Tutorial/` en bloques `00`, `01`, `02`, etc.
- Se movieron los documentos marco al modulo `01_fundamentos_conceptuales/`.
- Se renumeraron los modulos tecnicos ya existentes.
- Se añadieron `README.md` nuevos para prerrequisitos, fundamentos, Modelo Estandar y apendices.
- Se crearon modulos placeholder para fermiones, gauge, integral de camino y renormalizacion.
- Se incorporaron diagramas Mermaid a la portada principal del tutorial.

### Resultado

El tutorial ahora se parece mas a un curso navegable que a una coleccion de archivos. La progresion conceptual y tecnica queda mas clara desde la carpeta raiz.

## Entrada de cuadernos

### Fecha

2026-04-19

### Objetivo

Abrir un espacio especifico para notebooks Jupyter que complemente el tutorial escrito con ejemplos y problemas resueltos.

### Trabajo realizado

- Se creo el directorio `Cuadernos/`.
- Se separaron las subcarpetas `ejemplos/` y `problemas_resueltos/`.
- Se añadio un `README.md` para documentar el uso de los cuadernos.
- Se crearon dos notebooks iniciales como punto de partida.

### Resultado

El repositorio ya dispone de una zona practica preparada para material computacional y ejercicios guiados, en paralelo al tutorial teorico.

## Entrada de notas de apoyo

### Fecha

2026-04-19

### Objetivo

Crear un espacio donde almacenar material bruto y notas de trabajo que luego puedan convertirse en contenido del tutorial.

### Trabajo realizado

- Se creo el directorio `Notas/`.
- Se añadieron las subcarpetas `pdf/`, `notas_utiles/`, `resumenes/` y `referencias/`.
- Se documento el uso del directorio en `Notas/README.md`.

### Resultado

El proyecto ya cuenta con una zona intermedia entre fuente y publicacion, util para organizar material externo antes de integrarlo en `Tutorial/`.

## Entrada de recursos visuales

### Fecha

2026-04-19

### Objetivo

Crear un espacio especifico para almacenar imagenes, diagramas y material grafico que acompañe el desarrollo del tutorial.

### Trabajo realizado

- Se creo el directorio `Imagenes/`.
- Se añadieron las subcarpetas `diagramas/`, `figuras/`, `referencias/` y `exportadas/`.
- Se documento la carpeta en `Imagenes/README.md`.

### Resultado

El proyecto ya dispone de una zona dedicada a recursos visuales, preparada para alojar figuras pedagogicas y diagramas de apoyo.

## Entrada de ampliacion de modulos avanzados

### Fecha

2026-04-19

### Objetivo

Seguir transformando modulos placeholder en contenido real y no dejar huecos grandes en la progresion del curso.

### Trabajo realizado

- Se desarrollaron contenidos iniciales en `06_fermiones_y_dirac/`.
- Se desarrollaron contenidos iniciales en `07_gauge_y_qed/`.
- Se añadieron bases teoricas para `08_integral_de_camino/`.
- Se añadieron bases teoricas para `09_renormalizacion/`.
- Se ampliaron los `README.md` de estos modulos con mapas y resultados esperados.

### Resultado

La segunda mitad del recorrido del tutorial ya no esta compuesta solo por promesas de contenido, sino por una primera estructura textual consistente sobre fermiones, gauge, integral de camino y renormalizacion.

## Entrada de consolidacion de cuadernos y frontera avanzada

### Fecha

2026-04-19

### Objetivo

Convertir la carpeta `Cuadernos/` en una capa practica real del proyecto y abrir un modulo avanzado que conecte QFT con informacion cuantica y agujeros negros.

### Trabajo realizado

- Se desarrollaron los notebooks de `Cuadernos/ejemplos/01` a `08`.
- Se ampliaron los notebooks de `Cuadernos/problemas_resueltos/06` a `12`.
- Se incorporaron celdas con contexto teorico, formulas en LaTeX y pequenos calculos simbolicos o numericos.
- Se abrio el modulo `Tutorial/11_qft_informacion_y_agujeros_negros/`.
- Se añadieron documentos sobre entrelazamiento, radiacion de Hawking y paradoja de la informacion.
- Se actualizo la navegacion principal del tutorial y la portada de `Cuadernos/`.

### Resultado

La capa de notebooks deja de ser principalmente esqueletica y pasa a funcionar como apoyo pedagogico real. Ademas, el tutorial incorpora una frontera conceptual nueva donde la QFT se conecta con termicidad, entropia y unitaridad en presencia de horizontes.


## Entrada de expansión de frontera y herramientas

### Fecha

2026-04-20

### Objetivo

Lanzar la fase de expansión del tutorial centrada en profundidad técnica de fermiones, introducción a EFT y mejora de la capa práctica y visual.

### Trabajo realizado

- Se definió el Plan de Implementación para la ampliación del proyecto.
- Se estableció el Mapa de Tareas (`task.md`) para el seguimiento del desarrollo.
- Se inició la mejora visual de la documentación.

### Pendientes inmediatos

- Implementar el Mapa de Dependencias Maestro.
- Redactar el contenido de Espinores de Weyl y Majorana.
- Abrir el módulo de Teorías de Campo Efectivas (EFT).
- Desarrollar el notebook de álgebra de Dirac con SymPy.

## Entrada de limpieza editorial y sincronizacion con GitHub

### Fecha

2026-04-23

### Objetivo

Reducir ambiguedad en el repositorio, separar con claridad el contenido publicado del material alternativo y dejar la documentacion de seguimiento alineada con el estado real del proyecto.

### Situacion detectada

- El arbol principal de `Tutorial/` contenia varias variantes de capitulos con sufijos como ` 2.md`.
- Esas variantes no rompian MkDocs porque estaban excluidas del build, pero complicaban la lectura del repositorio y la identificacion de la version canonica.
- La validacion local y la documentacion principal todavia no reflejaban de manera explicita esa diferencia entre contenido publico y borradores.

### Trabajo realizado

- Se movieron 26 variantes editoriales a `Tutorial/_borradores/`, conservando la estructura por modulo.
- Se creo `Tutorial/_borradores/README.md` para documentar el criterio de uso de esa carpeta.
- Se actualizo `mkdocs.yml` para excluir `_borradores/` del sitio publico.
- Se ajusto `check_links.py` para ignorar `_borradores/` durante la validacion de enlaces.
- Se actualizo `CONTRIBUTING.md` con una convencion explicita para borradores y variantes de capitulos.
- Se publico la reorganizacion en GitHub sobre la rama `main`.

### Resultado

El repositorio quedo mas limpio y legible. Ahora existe una separacion clara entre el tutorial canonico y el material alternativo en revision, sin perder versiones utiles para comparacion o rescate posterior.

### Validacion

- `python check_links.py` pasa.
- `mkdocs build --clean` pasa.
- GitHub quedo sincronizado con la reorganizacion reciente.

### Siguientes pasos recomendados

- Revisar `_borradores/` modulo por modulo para detectar si alguna variante mejora al texto publico.
- Continuar la homogeneizacion editorial de los modulos `06` a `12`, sobre todo en ejercicios, referencias y derivaciones.
- Mejorar el historial de commits para que describa con mas precision cambios conceptuales y no solo cambios operativos.

## Entrada de validacion editorial minima

### Fecha

2026-04-23

### Objetivo

Extender la validacion automatica del repositorio para comprobar no solo enlaces y duplicados editoriales, sino tambien una estructura minima comun en los capitulos publicos del recorrido principal.

### Trabajo realizado

- Se amplio `check_links.py` para revisar que los capitulos numerados del tutorial tengan titulo principal, bloque de metadatos, `Proposito` u `Objetivo`, referencias y navegacion final.
- Se completaron con una seccion `Proposito` diez capitulos que todavia no seguian esa estructura minima.
- Se documento la regla en `CONTRIBUTING.md`.

### Resultado

La validacion local y en CI ya no protege solo contra errores tecnicos evidentes. Tambien ayuda a sostener una capa basica de coherencia editorial entre capitulos del recorrido principal.

### Siguiente mejora natural

- Separar en el futuro validaciones de tipo `error` y `warning` para poder endurecer la plantilla sin bloquear paginas legitimas de referencia o experimentacion controlada.

## Entrada de refinamiento de ejercicios y apoyos

### Fecha

2026-04-23

### Objetivo

Mejorar la calidad pedagogica de los ejercicios, especialmente en capitulos avanzados donde varias consignas seguian siendo demasiado generales, y revisar si los cuadernos asociados apuntaban al mejor apoyo disponible.

### Trabajo realizado

- Se revisaron ejercicios de fermiones, renormalizacion, Modelo Estandar, informacion/agujeros negros y EFT para volverlos mas concretos y accionables.
- Se reemplazaron algunas consignas demasiado abiertas por tareas de verificacion, clasificacion, comparacion estructural o lectura de formulas.
- Se ajustaron referencias de cuadernos en el bloque de fermiones para que el apoyo practico sea mas directo y pertinente al tema del capitulo.

### Resultado

El tutorial no solo tiene ya ejercicios en todos los capitulos del recorrido principal, sino que una parte mayor de esos ejercicios pide operaciones intelectuales mas precisas y menos abstractas. Eso mejora su utilidad como material real de estudio y autoevaluacion.
