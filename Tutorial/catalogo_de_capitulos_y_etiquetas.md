# Catalogo de Capitulos, Etiquetas y Prerequisitos

Esta pagina sirve como mapa fino del tutorial. Resume cada capitulo con una etiqueta de uso y una recomendacion minima de lectura previa.

## Leyenda de etiquetas

- `fundacional`: fija lenguaje o intuicion base.
- `tecnico`: introduce una herramienta formal importante.
- `puente`: conecta dos capas del curso.
- `avanzado`: presupone bastante del recorrido anterior.
- `opcional`: util como ampliacion o consulta, no siempre imprescindible para seguir.

## Como leer este catalogo sin perder tiempo

Una regla practica bastante buena es esta:

- prioriza `fundacional` si estas en primera pasada;
- usa `puente` para no perder continuidad entre modulos;
- deja `avanzado` y `opcional` para segunda vuelta o consulta dirigida;
- si dudas, contrasta siempre con los `Capitulos imprescindibles en primera pasada` del `README` del modulo correspondiente.

## Modulo 00. Prerrequisitos

| Capitulo | Etiquetas | Prerequisitos recomendados |
| :--- | :--- | :--- |
| [Relatividad especial minima](00_prerrequisitos/01_relatividad_especial_minima.md) | fundacional | Ninguno |
| [Notacion tensorial y convenciones](00_prerrequisitos/02_notacion_tensorial_y_convenciones.md) | fundacional, tecnico | 00.01 |
| [Oscilador armonico cuantico](00_prerrequisitos/03_oscilador_armonico_cuantico.md) | fundacional, puente | 00.01 |
| [Simetrias y grupos basicos](00_prerrequisitos/04_simetrias_y_grupos_basicos.md) | fundacional | 00.01 |
| [Delta de Dirac y transformadas de Fourier](00_prerrequisitos/05_delta_de_dirac_y_transformadas_de_fourier.md) | fundacional, tecnico | 00.02 |

## Modulo 01. Fundamentos conceptuales

| Capitulo | Etiquetas | Prerequisitos recomendados |
| :--- | :--- | :--- |
| [Conceptos fundamentales](01_fundamentos_conceptuales/01_conceptos_fundamentales.md) | fundacional | 00 completo |
| [Principios estructurales de la QFT](01_fundamentos_conceptuales/02_principios_estructurales_de_la_qft.md) | fundacional | 01.01 |
| [Que es un campo cuantico](01_fundamentos_conceptuales/03_que_es_un_campo_cuantico.md) | fundacional, puente | 01.01, 01.02 |

## Modulo 02. Relatividad y campos

| Capitulo | Etiquetas | Prerequisitos recomendados |
| :--- | :--- | :--- |
| [Choque entre MQ y relatividad](02_relatividad_y_campos/01_choque_entre_mq_y_relatividad.md) | fundacional, puente | 00.01, 01.01 |
| [Campos, localidad y causalidad](02_relatividad_y_campos/02_campos_localidad_y_causalidad.md) | fundacional | 02.01, 01.02 |

## Modulo 03. Accion y simetrias

| Capitulo | Etiquetas | Prerequisitos recomendados |
| :--- | :--- | :--- |
| [Principio de accion y ecuaciones de campo](03_accion_y_simetrias/01_principio_de_accion_y_ecuaciones_de_campo.md) | tecnico, fundacional | 02 completo |
| [Teorema de Noether y simetria](03_accion_y_simetrias/02_teorema_de_noether_y_simetria.md) | tecnico, puente | 03.01, 00.04 |

## Modulo 04. Cuantizacion del campo escalar

| Capitulo | Etiquetas | Prerequisitos recomendados |
| :--- | :--- | :--- |
| [Campo escalar clasico y modos normales](04_cuantizacion_del_campo_escalar/01_campo_escalar_clasico_y_modos_normales.md) | tecnico, puente | 03.01, 00.03, 00.05 |
| [Cuantizacion canonica y espacio de Fock](04_cuantizacion_del_campo_escalar/02_cuantizacion_canonica_y_espacio_de_fock.md) | tecnico, fundacional | 04.01 |
| [Propagador, causalidad y funcion de Green](04_cuantizacion_del_campo_escalar/03_propagador_causalidad_y_funcion_de_green.md) | tecnico, puente | 04.02, 02.02 |

## Modulo 05. Interacciones y perturbaciones

| Capitulo | Etiquetas | Prerequisitos recomendados |
| :--- | :--- | :--- |
| [Teoria de perturbaciones y matriz S](05_interacciones_y_perturbaciones/01_teoria_de_perturbaciones_y_matriz_s.md) | fundacional, tecnico | 04 completo |
| [Diagramas de Feynman y reglas](05_interacciones_y_perturbaciones/02_diagramas_de_feynman_y_reglas.md) | tecnico | 05.01 |
| [Reduccion LSZ y correladores amputados](05_interacciones_y_perturbaciones/03_reduccion_lsz_y_correladores_amputados.md) | puente, tecnico | 05.01, 05.02, 04.03 |
| [Reglas de Feynman: resumen operativo](05_interacciones_y_perturbaciones/04_reglas_de_feynman_resumen_operativo.md) | tecnico, opcional | 05.02, 05.03 |

## Modulo 06. Fermiones y Dirac

| Capitulo | Etiquetas | Prerequisitos recomendados |
| :--- | :--- | :--- |
| [Motivacion y ecuacion de Dirac](06_fermiones_y_dirac/01_motivacion_y_ecuacion_de_dirac.md) | fundacional, puente | 02 completo |
| [Cuantizacion de campos fermionicos](06_fermiones_y_dirac/02_cuantizacion_de_campos_fermionicos.md) | tecnico | 06.01, 04.02 |
| [Algebra gamma y bilineales de Dirac](06_fermiones_y_dirac/03_algebra_gamma_y_bilineales_de_dirac.md) | tecnico | 06.01 |
| [Corriente de Dirac y limite no relativista](06_fermiones_y_dirac/04_corriente_de_dirac_y_limite_no_relativista.md) | puente | 06.01, 06.03 |
| [Quiralidad, Weyl y Majorana](06_fermiones_y_dirac/05_quiralidad_weyl_y_majorana.md) | puente, avanzado | 06.03, 06.04 |

## Modulo 07. Gauge y QED

| Capitulo | Etiquetas | Prerequisitos recomendados |
| :--- | :--- | :--- |
| [Simetria gauge local y derivada covariante](07_gauge_y_qed/01_simetria_gauge_local_y_derivada_covariante.md) | fundacional, puente | 03.02, 06.04 |
| [QED y lagrangiano fundamental](07_gauge_y_qed/02_qed_y_lagrangiano_fundamental.md) | tecnico | 07.01, 06.03 |
| [Fijacion de gauge y propagador del foton](07_gauge_y_qed/03_fijacion_de_gauge_y_propagador_del_foton.md) | tecnico | 07.02, 05.02 |
| [Scattering basico en QED](07_gauge_y_qed/04_scattering_basico_en_qed.md) | puente, tecnico | 07.03, 05.01 |
| [Polarizaciones y sumas de espin en QED](07_gauge_y_qed/05_polarizaciones_y_sumas_de_espin.md) | tecnico, avanzado | 07.04, 06.03 |

## Modulo 08. Integral de camino

| Capitulo | Etiquetas | Prerequisitos recomendados |
| :--- | :--- | :--- |
| [Introduccion a la integral de camino](08_integral_de_camino/01_introduccion_a_la_integral_de_camino.md) | tecnico, puente | 03.01, 04.01 |
| [Funcional generador y correladores](08_integral_de_camino/02_funcional_generador_y_correladores.md) | tecnico | 08.01, 05.03 |
| [Accion efectiva y potencial efectivo](08_integral_de_camino/03_accion_efectiva_y_potencial_efectivo.md) | tecnico, avanzado | 08.02 |
| [Bogoliubov y cambio de vacio](08_integral_de_camino/04_bogoliubov_y_cambio_de_vacio.md) | puente, avanzado | 08.03, 04.02 |

## Modulo 09. Renormalizacion

| Capitulo | Etiquetas | Prerequisitos recomendados |
| :--- | :--- | :--- |
| [Origen de las divergencias y regularizacion](09_renormalizacion/01_origen_de_las_divergencias_y_regularizacion.md) | fundacional, tecnico | 05.02, 08.02 |
| [Renormalizacion y grupo de renormalizacion](09_renormalizacion/02_renormalizacion_y_grupo_de_renormalizacion.md) | fundacional, tecnico | 09.01 |
| [Regularizacion dimensional en phi4](09_renormalizacion/03_regularizacion_dimensional_en_phi4.md) | tecnico | 09.01, 09.02 |
| [Funcion beta y running couplings](09_renormalizacion/04_funcion_beta_y_running_couplings.md) | tecnico, puente | 09.02, 09.03 |
| [Esquema MSbar y QED vs QCD](09_renormalizacion/05_esquema_msbar_y_qed_vs_qcd.md) | avanzado | 09.04, 07.02 |

## Modulo 10. Modelo Estandar

| Capitulo | Etiquetas | Prerequisitos recomendados |
| :--- | :--- | :--- |
| [Lagrangiano del Modelo Estandar](10_modelo_estandar/01_lagrangiano_del_modelo_estandar.md) | avanzado, panoramico | 07 completo, 09 completo |
| [Sector gauge y estructura electrodébil](10_modelo_estandar/02_sector_gauge_y_estructura_electrodebil.md) | avanzado | 07.01, 07.02, 09.04 |
| [Sector fermionico y quiralidad](10_modelo_estandar/03_sector_fermionico_y_quiralidad.md) | avanzado | 06.05, 10.02 |
| [Mecanismo de Higgs y ruptura espontanea](10_modelo_estandar/04_mecanismo_de_higgs_y_ruptura_espontanea.md) | avanzado | 08.03, 10.02 |
| [Yukawas, masas y parametros](10_modelo_estandar/05_yukawas_masas_y_parametros.md) | avanzado | 10.03, 10.04 |
| [Corrientes cargadas y neutras](10_modelo_estandar/06_corrientes_cargadas_y_neutras.md) | avanzado | 10.02, 10.03, 10.04 |
| [Neutrinos, masas y oscilaciones](10_modelo_estandar/07_neutrinos_masas_y_oscilaciones.md) | avanzado, puente | 10.05, 06.05 |

## Modulo 11. QFT, informacion y agujeros negros

| Capitulo | Etiquetas | Prerequisitos recomendados |
| :--- | :--- | :--- |
| [QFT, informacion y entrelazamiento](11_qft_informacion_y_agujeros_negros/01_qft_informacion_y_entrelazamiento.md) | avanzado, fundacional | 08.02 |
| [Agujeros negros, Hawking y paradoja de la informacion](11_qft_informacion_y_agujeros_negros/02_agujeros_negros_radiacion_de_hawking_y_paradoja_de_la_informacion.md) | avanzado | 11.01 |
| [Efecto Unruh y vacio de Rindler](11_qft_informacion_y_agujeros_negros/03_efecto_unruh_y_vacio_de_rindler.md) | avanzado, puente | 08.04, 11.01 |
| [Curva de Page y unitaridad](11_qft_informacion_y_agujeros_negros/04_curva_de_page_y_unitaridad.md) | avanzado | 11.02, 11.03 |
| [Islas y entropia generalizada](11_qft_informacion_y_agujeros_negros/05_islas_y_entropia_generalizada.md) | avanzado | 11.04 |
| [Holografia y reconstruccion de informacion](11_qft_informacion_y_agujeros_negros/06_holografia_y_reconstruccion_de_informacion.md) | avanzado, opcional | 11.05 |

## Modulo 12. Teorias de campo efectivas

| Capitulo | Etiquetas | Prerequisitos recomendados |
| :--- | :--- | :--- |
| [Integrando grados de libertad](12_teorias_de_campo_efectivas/01_integrando_grados_de_libertad.md) | fundacional, avanzado | 09.02 |
| [Teoria de Fermi como EFT](12_teorias_de_campo_efectivas/02_teoria_de_fermi_como_eft.md) | puente | 12.01, 10.06 |
| [Euler-Heisenberg y operadores efectivos](12_teorias_de_campo_efectivas/03_euler_heisenberg_y_operadores_efectivos.md) | avanzado | 12.01, 07.04 |
| [Gravedad como teoria efectiva](12_teorias_de_campo_efectivas/04_gravedad_como_teoria_efectiva.md) | avanzado, opcional | 12.01, 11.02 |
| [SMEFT y operador de Weinberg](12_teorias_de_campo_efectivas/05_smeft_y_operador_de_weinberg.md) | avanzado | 10 completo, 12.01 |
| [Majorana y mecanismo seesaw](12_teorias_de_campo_efectivas/06_majorana_y_mecanismo_seesaw.md) | avanzado | 06.05, 10.07, 12.05 |
| [Doble beta sin neutrinos](12_teorias_de_campo_efectivas/07_doble_beta_sin_neutrinos.md) | avanzado, opcional | 12.06 |
| [Matching UV y coeficientes de Wilson](12_teorias_de_campo_efectivas/08_matching_uv_y_coeficientes_de_wilson.md) | avanzado, tecnico | 12.01, 12.05 |

## Como usar este catalogo

- Si dudas si un capitulo es para primera lectura, mira primero su etiqueta.
- Si quieres entrar por un tema concreto, usa la columna de prerequisitos para evitar saltos demasiado bruscos.
- Si quieres una secuencia ya preparada, consulta tambien [Rutas de lectura](rutas_de_lectura.md).
- Si quieres transformar la eleccion de capitulos en un plan semanal, consulta [Problemas recomendados por semana](problemas_recomendados_por_semana.md).

---

[Volver al indice del tutorial](README.md)
