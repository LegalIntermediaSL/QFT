# Changelog

Todos los cambios relevantes de este proyecto se documentan en este archivo.

El formato sigue una adaptacion simple de Keep a Changelog y usa versionado semantico solo como referencia organizativa mientras el repositorio madura.

## [Unreleased]

### Planned

- Crear un capitulo de prerrequisitos matematicos.
- Incorporar una segunda pasada de ejercicios y problemas guiados en los modulos `06` a `12`.
- Reforzar referencias por documento y enlaces cruzados entre capitulos y cuadernos.
- Revisar y promover selectivamente borradores de `Tutorial/_borradores/` cuando mejoren la version publica.

### Changed

- Se limpio el arbol canonico de `Tutorial/` moviendo 26 variantes de capitulos con sufijo ` 2.md` a `Tutorial/_borradores/`.
- `mkdocs.yml` ahora excluye `Tutorial/_borradores/` como espacio editorial no publico.
- `check_links.py` ahora ignora `_borradores/` para que la validacion refleje solo el contenido publicado.
- `CONTRIBUTING.md` documenta la nueva convencion para borradores y variantes editoriales.
- `README.md`, `bitacora.md` y `changelog.md` se sincronizan con la reorganizacion reciente del repositorio.

### Fixed

- Se elimino la ambiguedad sobre cual era la version canonica de varios capitulos duplicados.
- La validacion de enlaces vuelve a ser consistente con el contenido realmente publicado en MkDocs.

### Notes

- La rama `main` quedo publicada y sincronizada en GitHub tras la limpieza editorial del 23 de abril de 2026.

### Added

- Carpeta `Tutorial/` como nucleo inicial del contenido tecnico.
- `Tutorial/README.md` con secuencia recomendada de lectura.
- `Tutorial/conceptos_fundamentales.md` como mapa conceptual de entrada a la QFT.
- `Tutorial/portada_01_relatividad_y_campos.md`.
- `Tutorial/portada_02_accion_lagrangiana_y_noether.md`.
- `Tutorial/portada_03_cuantizacion_canonica_del_campo_escalar.md`.
- `Tutorial/portada_04_interacciones_y_diagramas_de_feynman.md`.
- Modulos `01_relatividad_y_campos/`, `02_accion_lagrangiana_y_simetrias/`, `03_cuantizacion_del_campo_escalar/` y `04_interacciones_y_perturbaciones/`.
- Ocho documentos extensos nuevos que desarrollan en mayor profundidad los bloques introductorios del tutorial.

### Changed

- Las portadas introductorias dejaron de ser el tratamiento principal y pasaron a funcionar como indices de navegacion hacia modulos mas amplios.
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
- `Tutorial/99_apendices/plantilla_de_capitulo.md`
- Directorio `Cuadernos/` con subcarpetas para `ejemplos/` y `problemas_resueltos/`.
- `Cuadernos/README.md` con convenciones y objetivo de los notebooks.
- Dos notebooks base para iniciar ejemplos y problemas resueltos.
- Directorio `Notas/` con estructura para `pdf/`, `notas_utiles/`, `resumenes/` y `referencias/`.
- `Notas/README.md` con criterios de uso para alimentar futuras ampliaciones del tutorial.
- Directorio `Imagenes/` con estructura para `diagramas/`, `figuras/`, `referencias/` y `exportadas/`.
- `Imagenes/README.md` para organizar el material visual del proyecto.
- Documentos iniciales para `06_fermiones_y_dirac/`, `07_gauge_y_qed/`, `08_integral_de_camino/` y `09_renormalizacion/`.
- Modulo `Tutorial/11_qft_informacion_y_agujeros_negros/` con dos documentos avanzados.
- `Cuadernos/ejemplos/08_entrelazamiento_y_horizontes.ipynb`.
- `Cuadernos/problemas_resueltos/12_qft_informacion_y_agujeros_negros.ipynb`.

### Changed

- Desarrollo sustancial de los notebooks de `Cuadernos/ejemplos/01` a `08`.
- Desarrollo sustancial de los notebooks de `Cuadernos/problemas_resueltos/06` a `12`.
- `Tutorial/README.md` ahora incluye el modulo avanzado sobre informacion y agujeros negros.
- `Cuadernos/README.md` se amplio para reflejar la nueva cobertura practica del proyecto.
- La serie `articulo_*` se renombro conceptualmente como `portada_*` para evitar la apariencia de numeracion truncada.
- Se completo la navegacion de `mkdocs.yml` para mostrar todos los modulos del recorrido principal.
- Los `README` de modulo ahora incluyen prerequisitos, lecturas recomendadas y enlaces de navegacion secuencial.
- La bibliografia comentada se amplio por nivel y por bloque tematico.
- Los documentos tecnicos de `06_fermiones_y_dirac/`, `07_gauge_y_qed/`, `08_integral_de_camino/` y `09_renormalizacion/` se ampliaron con secciones nuevas, ejemplos orientativos y referencias por documento.
- El modulo `10_modelo_estandar/` se dividio en un panorama general y cuatro documentos tematicos sobre gauge, quiralidad, Higgs y Yukawas.
- Los documentos tecnicos de `00_prerrequisitos/` a `05_interacciones_y_perturbaciones/` quedaron mas homogéneos al añadir advertencias y referencias por documento.
- Se añadió un apéndice de convenciones globales y se reforzó el enlace pedagógico entre capítulos y cuadernos, especialmente en el módulo `10_modelo_estandar/`.
- El modulo `11_qft_informacion_y_agujeros_negros/` se amplió con un documento nuevo sobre efecto Unruh y vacío de Rindler, y sus textos quedaron mejor conectados con cuadernos y referencias.
- El modulo `07_gauge_y_qed/` se amplió con documentos nuevos sobre gauge-fixing, propagador del foton, identidad de Ward y un ejemplo básico de scattering en QED.
- El modulo `09_renormalizacion/` se amplió con documentos nuevos sobre regularizacion dimensional en $\phi^4$ y funcion beta con running couplings.
- El modulo `08_integral_de_camino/` se amplió con documentos nuevos sobre accion efectiva, potencial efectivo y transformaciones de Bogoliubov como puente hacia temas avanzados.
- El modulo `06_fermiones_y_dirac/` recibió una segunda capa de profundizacion con documentos nuevos sobre algebra gamma, bilineales de Dirac, corriente conservada y limite no relativista.
- Se añadió una tercera capa selectiva con nuevos documentos sobre quiralidad/Weyl/Majorana en `06`, polarizaciones y sumas de espín en `07`, esquema $\overline{\text{MS}}$ y comparación QED/QCD en `09`, y curva de Page con unitaridad en `11`.

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
- Se añadió navegacion lineal `(anterior) (siguiente)` al final de los 48 articulos del recorrido principal, incluyendo portadas-resumen y modulos `00` a `11`.
- Se amplió el modulo `05_interacciones_y_perturbaciones/` con nuevos articulos sobre reduccion LSZ, correladores amputados y una sintesis operativa de reglas de Feynman, ajustando tambien la navegacion lineal del tutorial.
- Se reforzó `04_cuantizacion_del_campo_escalar/` con un nuevo articulo sobre propagador, causalidad y funcion de Green, y se añadió un apendice transversal de reglas de Feynman y propagadores para unificar consulta y notacion entre modulos.
- Se profundizó `10_modelo_estandar/` con mezcla electrodébil, angulo de Weinberg, masas de $W/Z$ y una nota nueva sobre corrientes cargadas y neutras; ademas se añadieron ejercicios de modulo en `04` y `05`, y el glosario paso a cubrir tambien conceptos tecnicos ademas de notacion.
- Se añadió una nueva capa de ejercicios de modulo en `06_fermiones_y_dirac/`, `07_gauge_y_qed/` y `10_modelo_estandar/` para equilibrar mejor exposicion teorica y practica guiada.
- Se añadieron una `ruta minima` y una `ruta avanzada` al indice general del tutorial, se creó un apendice nuevo sobre simetrias discretas, CPT y anomalias, y se actualizó `Cuadernos/README.md` con un mapa mas claro de prioridades para futuros notebooks.
- Se añadió un apendice nuevo sobre mezcla de sabor, matriz CKM y matriz PMNS para reforzar el cierre fenomenologico del modulo `10_modelo_estandar/` y enlazar mejor Yukawas, corrientes cargadas, neutrinos y violacion de `CP`.
- Se añadió una nota nueva en `10_modelo_estandar/` sobre neutrinos, masas y oscilaciones; se concretó la hoja de ruta de `Cuadernos/` con nombres y objetivos de notebooks futuros; y se agregó un apendice tecnico sobre anomalia axial y cancelacion de anomalias.
- Comenzó la materializacion de `Cuadernos/` con `ejemplos/08_propagador_libre_y_causalidad.ipynb`, primer notebook nuevo de la hoja de ruta para enlazar propagador libre, prescripcion `i\\epsilon` y microcausalidad.
- Se completó la primera hoja de ruta de `Cuadernos/` con notebooks nuevos sobre LSZ y amplitudes escalares, bilineales y proyectores quirales, gauge-fixing y scattering en QED, mezcla electrodébil y masas gauge, y neutrinos con oscilaciones.
- Se alinearon explicitamente los articulos teoricos de `04`, `05`, `06`, `07` y `10` con los cuadernos nuevos, reforzando las secciones de `Cuaderno asociado` para cerrar el circuito entre lectura teorica y practica guiada.
- Comenzó una segunda ola de `Cuadernos/` con notebooks nuevos para `08_integral_de_camino/`, `09_renormalizacion/` y `11_qft_informacion_y_agujeros_negros/`, y se enlazaron ya desde los README de modulo y articulos teoricos mas afines.
- Comenzó una tercera ola de `Cuadernos/` para los apendices transversales, con notebooks nuevos sobre simetrias discretas y CPT, mezcla de sabor CKM/PMNS, y anomalia axial con cancelacion de anomalias; ademas se añadieron secciones de `Cuaderno asociado` a esos apendices.
- Se completó una pasada de homogeneizacion editorial sobre varios README de modulo y apendices, añadiendo secciones paralelas de `Cuadernos asociados`, `Uso sugerido`, `Resultado esperado` y `Ejercicios sugeridos` para que el tutorial tenga una estructura mas uniforme entre bloques.
- Se añadió una capa extra de detalle matematico en `08_integral_de_camino/02_funcional_generador_y_correladores.md`, `09_renormalizacion/04_funcion_beta_y_running_couplings.md` y `11_qft_informacion_y_agujeros_negros/04_curva_de_page_y_unitaridad.md`, reforzando derivadas funcionales, leyes de running e interpretacion cuantitativa idealizada de la curva de Page.
- Se integro `12_teorias_de_campo_efectivas` al recorrido principal, ampliandolo con articulos sobre integracion de grados de libertad, teoria de Fermi, Euler-Heisenberg y gravedad como EFT, ademas de su insercion en `mkdocs.yml`, `Tutorial/README.md` y la navegacion lineal desde el modulo 11.
- Se arranco una cuarta hoja de ruta de cuadernos para EFT en `Cuadernos/README.md`, con notebooks nuevos dedicados a power counting y matching efectivo.
- Se equilibraron los cuadernos de los modulos `06` a `09` con cuatro nuevos notebooks: `18_corriente_de_dirac_y_limite_no_relativista.ipynb`, `16_qed_derivada_covariante_y_ward.ipynb`, `19_correladores_y_accion_efectiva.ipynb` y `17_esquema_msbar_y_qed_vs_qcd.ipynb`, ademas de actualizar los `README` de cada modulo y `Cuadernos/README.md`.
- Se revisaron numeraciones y enlaces de navegacion del tutorial, corrigiendo la transicion de `portada_04_interacciones_y_diagramas_de_feynman.md` y eliminando el archivo huerfano `03_weyl_majorana_y_teoria_de_grupos.md` en el modulo `06`.
- Se abrio una capa avanzada en `12_teorias_de_campo_efectivas` con `05_smeft_y_operador_de_weinberg.md`, `06_majorana_y_mecanismo_seesaw.md` y los cuadernos `18_smeft_y_operador_de_weinberg.ipynb` y `20_majorana_y_seesaw.ipynb`.
- Se extendio la capa avanzada del modulo `12_teorias_de_campo_efectivas` con `07_doble_beta_sin_neutrinos.md`, `08_matching_uv_y_coeficientes_de_wilson.md` y los cuadernos `21_doble_beta_sin_neutrinos.ipynb` y `19_matching_uv_a_smeft.ipynb`, cerrando una segunda ola sobre fenomenologia leptónica y matching UV -> EFT.
- Se amplio el modulo `11_qft_informacion_y_agujeros_negros` con `05_islas_y_entropia_generalizada.md`, `06_holografia_y_reconstruccion_de_informacion.md` y los cuadernos `20_islas_y_entropia_generalizada.ipynb` y `22_holografia_y_reconstruccion_de_informacion.ipynb`, extendiendo la capa avanzada hacia islas, entropia generalizada y holografia.
- Se homogeneizo la apertura editorial de los cuadernos avanzados mas recientes, añadiendo una seccion explicita de `Resultado esperado` para reforzar consistencia entre notebooks de informacion, EFT, SMEFT, seesaw y holografia.
