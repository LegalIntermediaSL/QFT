# Changelog

Todos los cambios relevantes de este proyecto se documentan en este archivo.

El formato sigue una adaptacion simple de Keep a Changelog y usa versionado semantico solo como referencia organizativa mientras el repositorio madura.

## [Unreleased]

### Planned

- Crear un capitulo de prerrequisitos matematicos.
- Desarrollar contenido sobre campos fermionicos e integral de camino.
- Incorporar ejercicios y problemas guiados.
- Extender el bloque de renormalizacion y teorias gauge.

### Added

- Carpeta `Tutorial/` como nucleo inicial del contenido tecnico.
- `Tutorial/README.md` con secuencia recomendada de lectura.
- `Tutorial/conceptos_fundamentales.md` como mapa conceptual de entrada a la QFT.
- `Tutorial/articulo_01_relatividad_y_campos.md`.
- `Tutorial/articulo_02_accion_lagrangiana_y_noether.md`.
- `Tutorial/articulo_03_cuantizacion_canonica_del_campo_escalar.md`.
- `Tutorial/articulo_04_interacciones_y_diagramas_de_feynman.md`.
- Modulos `01_relatividad_y_campos/`, `02_accion_lagrangiana_y_simetrias/`, `03_cuantizacion_del_campo_escalar/` y `04_interacciones_y_perturbaciones/`.
- Ocho documentos extensos nuevos que desarrollan en mayor profundidad los bloques introductorios del tutorial.

### Changed

- Los articulos introductorios dejaron de ser el tratamiento principal y pasaron a funcionar como portadas de navegacion hacia modulos mas amplios.
- `Tutorial/README.md` se reorganizo para reflejar la nueva arquitectura modular.
- Se ampliaron varios articulos de los modulos de relatividad y perturbaciones con mas desarrollo conceptual, secciones nuevas y ejercicios sugeridos.
- `Tutorial/` se reorganizo con una estructura curricular numerada, nuevos indices de modulo y diagramas Mermaid en la portada principal.

### Added

- `Tutorial/00_prerrequisitos/README.md`
- `Tutorial/01_fundamentos_conceptuales/README.md`
- `Tutorial/06_fermiones_y_dirac/README.md`
- `Tutorial/07_gauge_y_qed/README.md`
- `Tutorial/08_integral_de_camino/README.md`
- `Tutorial/09_renormalizacion/README.md`
- `Tutorial/10_modelo_estandar/README.md`
- `Tutorial/99_apendices/README.md`
- Directorio `Cuadernos/` con subcarpetas para `ejemplos/` y `problemas_resueltos/`.
- `Cuadernos/README.md` con convenciones y objetivo de los notebooks.
- Dos notebooks base para iniciar ejemplos y problemas resueltos.

## [0.1.0] - 2026-04-18

### Added

- `README.md` expandido con vision, objetivos, alcance tematico y hoja de ruta del proyecto.
- `bitacora.md` con registro inicial del estado del repositorio, decisiones editoriales y siguientes pasos.
- `changelog.md` para centralizar el historial de cambios relevantes.

### Changed

- El repositorio paso de una descripcion minima a una base documental inicial apta para organizar el desarrollo del tutorial.

### Notes

- Esta version marca el arranque formal de la documentacion del proyecto.
- El contenido tecnico del tutorial todavia esta pendiente de desarrollo.
