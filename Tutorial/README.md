# Tutorial de Teoria Cuantica de Campos

Este directorio contiene el cuerpo principal del tutorial. A diferencia de la primera iteracion, el contenido ya no esta organizado como una lista corta de articulos introductorios, sino como un conjunto de modulos con subdocumentos. La idea es que cada modulo tenga una funcion clara dentro de la progresion del curso:

- plantear el problema fisico;
- fijar el lenguaje formal;
- desarrollar herramientas de calculo;
- preparar el paso al modulo siguiente.

## Ruta recomendada de lectura

Si estas empezando desde cero, el orden sugerido es:

1. `conceptos_fundamentales.md`
2. `principios_estructurales_de_la_qft.md`
3. `que_es_un_campo_cuantico.md`
4. `01_relatividad_y_campos/README.md`
5. `02_accion_lagrangiana_y_simetrias/README.md`
6. `03_cuantizacion_del_campo_escalar/README.md`
7. `04_interacciones_y_perturbaciones/README.md`

## Estructura actual

### Documentos marco

- `conceptos_fundamentales.md`: mapa conceptual global del tutorial.
- `principios_estructurales_de_la_qft.md`: principios fisicos y matematicos que restringen y organizan toda teoria cuantica de campos consistente.
- `que_es_un_campo_cuantico.md`: explicacion conceptual y formal de por que los campos cuanticos son los objetos fundamentales y las particulas sus excitaciones.
- `lagrangiano_del_modelo_estandar.md`: panoramica estructurada del Lagrangiano del Modelo Estandar como teoria gauge cuantica renormalizable.

### Modulo 1. Relatividad y campos

- `01_relatividad_y_campos/README.md`
- `01_relatividad_y_campos/01_choque_entre_mq_y_relatividad.md`
- `01_relatividad_y_campos/02_campos_localidad_y_causalidad.md`

### Modulo 2. Accion, lagrangiana y simetrias

- `02_accion_lagrangiana_y_simetrias/README.md`
- `02_accion_lagrangiana_y_simetrias/01_principio_de_accion_y_ecuaciones_de_campo.md`
- `02_accion_lagrangiana_y_simetrias/02_teorema_de_noether_y_simetria.md`

### Modulo 3. Cuantizacion del campo escalar

- `03_cuantizacion_del_campo_escalar/README.md`
- `03_cuantizacion_del_campo_escalar/01_campo_escalar_clasico_y_modos_normales.md`
- `03_cuantizacion_del_campo_escalar/02_cuantizacion_canonica_y_espacio_de_fock.md`

### Modulo 4. Interacciones y perturbaciones

- `04_interacciones_y_perturbaciones/README.md`
- `04_interacciones_y_perturbaciones/01_teoria_de_perturbaciones_y_matriz_s.md`
- `04_interacciones_y_perturbaciones/02_diagramas_de_feynman_y_reglas.md`

## Papel de los articulos originales

Los archivos `articulo_01_...` a `articulo_04_...` se mantienen como portadas de navegacion y resumen ejecutivo de cada bloque. Ya no deben leerse como tratamiento completo de los temas, sino como una puerta de entrada hacia los modulos ampliados.

## Convenciones iniciales

- Se usan unidades naturales cuando simplifican la exposicion: $c = \hbar = 1$.
- El signo de la metrica debe declararse en cada documento tecnico cuando sea relevante.
- El foco del tutorial es pedagogico, pero las formulas deben escribirse con notacion estandar de QFT.
- Cada modulo nuevo deberia incluir contexto, derivaciones minimas, advertencias y continuidad hacia el siguiente bloque.

## Siguiente horizonte

Despues de estos modulos introductorios, la expansion natural del tutorial es:

- campos fermionicos y ecuacion de Dirac;
- cuantizacion del campo electromagnetico;
- integral de camino;
- renormalizacion y grupo de renormalizacion;
- teorias gauge no abelianas.

## Lecturas avanzadas ya disponibles

Estas notas no son el siguiente paso pedagogico obligatorio, pero sirven para mostrar hacia donde apunta el formalismo:

- `lagrangiano_del_modelo_estandar.md`
