# Tutorial de Teoria Cuantica de Campos

Este directorio contiene el cuerpo principal del tutorial. La estructura ya no se organiza como una lista plana de notas, sino como un recorrido curricular: prerrequisitos, fundamentos conceptuales, modulos tecnicos progresivos, lecturas avanzadas y apendices.

La idea de esta organizacion es simple:

- empezar por intuicion y principios;
- pasar despues a formalismo y cuantizacion;
- llegar mas tarde a interacciones, gauge, renormalizacion y teorias fisicas concretas;
- mantener materiales de apoyo separados del hilo principal.

```mermaid
flowchart TD
    subgraph Fundamentos
        A["00 Prerrequisitos"] --> B["01 Fundamentos conceptuales"]
        B --> C["02 Relatividad y campos"]
        C --> D["03 Acción y simetrías"]
    end

    subgraph Cuantizacion ["Cuantización"]
        D --> E["04 Campo escalar (U!Canónica)"]
        E --> F["05 Interacciones (Perturbaciones)"]
        F --> G["06 Fermiones y Dirac"]
        G --> H["07 Gauge y QED"]
    end

    subgraph Avanzado ["Temas Avanzados"]
        H --> I["08 Integral de camino"]
        I --> J["09 Renormalización"]
        J --> K["10 Modelo Estándar"]
        K -- "Efectos Cuánticos" --> L["11 QFT e Información"]
    end

    subgraph Apendices ["Material de Consulta"]
        M["99 Apéndices"]
        N["Computación QFT"]
    end

    D -.-> H
    F -.-> I
    K -.-> M
```

## Ruta recomendada de lectura

Para una experiencia de aprendizaje secuencial, sigue este orden:

| Orden | Módulo | Descripción |
| :--- | :--- | :--- |
| 1 | [00 Prerrequisitos](00_prerrequisitos/README.md) | Herramientas matemáticas y física básica |
| 2 | [01 Fundamentos](01_fundamentos_conceptuales/README.md) | ¿Qué es un campo y por qué QFT? |
| 3 | [02 Relatividad y Campos](02_relatividad_y_campos/README.md) | Localidad y causalidad |
| 4 | [03 Acción y Simetrías](03_accion_y_simetrias/README.md) | Noether y lagrangianos de campo |
| 5 | [04 Campo Escalar](04_cuantizacion_del_campo_escalar/README.md) | Cuantización canónica y Fock |
| 6 | [05 Interacciones](05_interacciones_y_perturbaciones/README.md) | Matriz S y diagramas de Feynman |
| 7 | [10 Modelo Estándar](10_modelo_estandar/README.md) | Aplicación física real (Avanzado) |
| 8 | [11 Fronteras](11_qft_informacion_y_agujeros_negros/README.md) | Hawking e Información (Avanzado) |

---

| [<< Inicio (README Principal)](../README.md) | [Bibliografía >>](99_apendices/bibliografia.md) |
| :--- | :--- |

## Flujo conceptual

```mermaid
flowchart LR
    A["Mecanica cuantica no relativista"] --> B["Numero fijo de particulas"]
    B --> C["Falla en regimen relativista"]
    C --> D["Creacion y destruccion de particulas"]
    D --> E["Campos cuanticos"]
    E --> F["Cuantizacion de modos"]
    F --> G["Particulas como excitaciones del campo"]
    G --> H["Interacciones y amplitudes"]
```

## Estructura actual

### `00_prerrequisitos/`

Bloque de entrada para reunir matematicas y fisica necesarias antes del formalismo principal.

### `01_fundamentos_conceptuales/`

- `01_conceptos_fundamentales.md`
- `02_principios_estructurales_de_la_qft.md`
- `03_que_es_un_campo_cuantico.md`

Este bloque fija el lenguaje: que problema resuelve la QFT, que principios la restringen y por que los campos son mas fundamentales que las particulas.

### `02_relatividad_y_campos/`

- `01_choque_entre_mq_y_relatividad.md`
- `02_campos_localidad_y_causalidad.md`

### `03_accion_y_simetrias/`

- `01_principio_de_accion_y_ecuaciones_de_campo.md`
- `02_teorema_de_noether_y_simetria.md`

### `04_cuantizacion_del_campo_escalar/`

- `01_campo_escalar_clasico_y_modos_normales.md`
- `02_cuantizacion_canonica_y_espacio_de_fock.md`

### `05_interacciones_y_perturbaciones/`

- `01_teoria_de_perturbaciones_y_matriz_s.md`
- `02_diagramas_de_feynman_y_reglas.md`

### `10_modelo_estandar/`

- `01_lagrangiano_del_modelo_estandar.md`

Lecturas avanzadas donde el formalismo se conecta con la teoria fisica concreta mas importante de la fisica de particulas no gravitatoria.

### `11_qft_informacion_y_agujeros_negros/`

- `01_qft_informacion_y_entrelazamiento.md`
- `02_agujeros_negros_radiacion_de_hawking_y_paradoja_de_la_informacion.md`

Modulo de frontera donde la QFT se cruza con teoria de la informacion cuantica, horizontes, termicidad efectiva y la paradoja de la informacion de agujeros negros.

### `99_apendices/`

Espacio reservado para convenciones, ejercicios resueltos y material de consulta:
- [Bibliografía comentada](99_apendices/bibliografia.md)
- [Herramientas Computacionales (FeynCalc/Python)](99_apendices/computacion_qft.md)
- Tablas de notación (Próximamente)

## Arquitectura del Modelo Estandar

```mermaid
flowchart TD
    A["SU(3)c x SU(2)L x U(1)Y"] --> B["Sector gauge"]
    A --> C["Sector fermionico"]
    A --> D["Sector de Higgs"]
    D --> E["Ruptura espontanea de simetria"]
    E --> F["Masas de W y Z"]
    D --> G["Sector de Yukawa"]
    G --> H["Masas de quarks y leptones"]
    C --> I["Quiralidad de la interaccion debil"]
    B --> J["Gluones, W, Z, foton"]
```

## Papel de los articulos originales

Los archivos `articulo_01_...` a `articulo_04_...` se mantienen como portadas de navegacion y resumen ejecutivo de los primeros grandes bloques. Ya no deben leerse como tratamiento principal, sino como indice corto hacia los modulos desarrollados.

## Convenciones

- Se usan unidades naturales cuando simplifican la exposicion: $c=\hbar=1$.
- El signo de la metrica debe declararse en cada documento tecnico cuando sea relevante.
- El foco del tutorial es pedagogico, pero las formulas deben escribirse con notacion estandar de QFT.
- Cada modulo deberia incluir contexto, derivaciones minimas, advertencias, preguntas de estudio y ejercicios.

## Siguiente horizonte

Las extensiones mas naturales del tutorial siguen siendo:

- `06_fermiones_y_dirac/`
- `07_gauge_y_qed/`
- `08_integral_de_camino/`
- `09_renormalizacion/`
- ampliacion de `10_modelo_estandar/`
- consolidacion de `11_qft_informacion_y_agujeros_negros/`
