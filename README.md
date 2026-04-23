# QFT

Tutorial completo sobre Teoria Cuantica de Campos orientado al autoaprendizaje, la consulta progresiva y la construccion de una base solida en fisica teorica moderna.

## Vision del proyecto

Este repositorio nace con la idea de reunir, en un solo lugar, una guia clara y acumulativa para estudiar Teoria Cuantica de Campos (QFT, por sus siglas en ingles). La meta no es solo listar conceptos, sino construir un recorrido que conecte intuicion fisica, formalismo matematico, tecnicas de calculo y aplicaciones contemporaneas.

El tutorial esta pensado como un material vivo. Puede crecer por modulos, notas, derivaciones, ejercicios resueltos, referencias historicas, diagramas y comparativas entre enfoques pedagogicos. El objetivo final es que una persona motivada pueda recorrer desde los fundamentos hasta temas mas avanzados con una progresion razonable.

## Objetivos

- Presentar una ruta de estudio completa y ordenada de Teoria Cuantica de Campos.
- Explicar los fundamentos matematicos y fisicos sin perder continuidad pedagogica.
- Integrar teoria, calculo formal, ejemplos y contexto historico.
- Servir como base para apuntes, clases, talleres o estudio autodidacta.
- Mantener una documentacion clara del avance del proyecto.

## Alcance tematico previsto

El tutorial puede cubrir, entre otros, los siguientes bloques:

1. Prerrequisitos matematicos y fisicos
2. Relatividad especial y simetrias
3. Mecanica cuantica relativista
4. Campo escalar clasico y cuantizacion canonica
5. Campo de Klein-Gordon
6. Campo de Dirac y espinores
7. Campo electromagnetico y cuantizacion gauge
8. Formalismo lagrangiano y accion
9. Simetrias continuas, corrientes conservadas y teorema de Noether
10. Imagen de interaccion y teoria de perturbaciones
11. Diagramas de Feynman y reglas de Feynman
12. Funciones de correlacion y operadores de tiempo ordenado
13. Formalismo de integral de camino
14. Renormalizacion y regularizacion
15. Electrodinamica cuantica como estudio de caso
16. Simetrias gauge no abelianas
17. Ruptura espontanea de simetria
18. Introduccion al Modelo Estandar
19. Ideas de grupo de renormalizacion
20. Temas avanzados y lecturas complementarias

## Enfoque pedagogico

La filosofia del proyecto combina cuatro capas:

- Intuicion: por que aparece cada objeto formal y que problema resuelve.
- Formalismo: definiciones, convenciones, derivaciones y notacion consistente.
- Calculo: tecnicas paso a paso para evitar saltos innecesarios.
- Interpretacion: lectura fisica de los resultados y sus limites.

Siempre que sea posible, cada tema deberia incluir:

- una introduccion conceptual;
- las ecuaciones centrales;
- una derivacion o demostracion guiada;
- un ejemplo minimo funcional;
- ejercicios o preguntas de comprobacion;
- referencias para profundizar.

## Audiencia objetivo

Este material puede ser util para:

- estudiantes de grado avanzado en fisica;
- estudiantes de posgrado que quieran consolidar fundamentos;
- personas autodidactas con base fuerte en mecanica cuantica y relatividad;
- docentes que busquen una estructura reutilizable para cursos y seminarios.

## Estructura documental del repositorio

El contenido tecnico ya supera una simple fase de arranque. El repositorio contiene una ruta curricular visible, modulos tematicos, cuadernos de apoyo, apendices y portadas-resumen para algunos bloques del recorrido:

- [README.md](README.md): presentacion general, objetivos y direccion del proyecto.
- [bitacora.md](bitacora.md): registro narrativo del progreso, decisiones y siguientes pasos.
- [changelog.md](changelog.md): historial de cambios relevantes del repositorio.
- [Tutorial/](Tutorial/README.md): primer bloque de contenido tecnico del tutorial.
- [Herramientas Computacionales](Tutorial/99_apendices/computacion_qft.md): guía sobre FeynCalc y Python-HEP.
- [Plantilla Editorial](Tutorial/99_apendices/plantilla_de_capitulo.md): estructura base sugerida para nuevos capitulos.
- [Cuadernos/](Cuadernos/README.md): notebooks Jupyter para ejemplos y problemas resueltos.
- [Notas/](Notas/README.md): deposito de PDFs, apuntes, resumenes y referencias para ampliar el tutorial.
- [Imagenes/](Imagenes/README.md): recursos visuales para diagramas, figuras y material grafico del proyecto.

Ademas, el repositorio distingue ahora entre contenido publicado y variantes editoriales en revision:

- `Tutorial/`: version canonica y publica del tutorial.
- `Tutorial/_borradores/`: variantes, resúmenes alternativos y versiones en revisión que no forman parte del sitio publico.

## Instalación y Uso

Para trabajar con el proyecto conviene separar dos capas:

- dependencias de cuadernos y cálculo simbólico;
- dependencias para construir y servir el sitio con MkDocs.

Se recomienda crear un entorno virtual e instalar ambas:

```bash
# Crear entorno virtual
python -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate

# Instalar dependencias de cuadernos
pip install -r requirements.txt

# Instalar dependencias de documentación
pip install -r requirements-docs.txt
```

Las bibliotecas principales utilizadas en los cuadernos son `numpy`, `sympy`, `matplotlib`, `ipython`, `pandas` y `scipy`.

Para levantar el sitio localmente:

```bash
mkdocs serve
```

Para validar enlaces locales antes de publicar:

```bash
python check_links.py
```

Y para generar el sitio estático:

```bash
mkdocs build --clean
```

## Hoja de ruta sugerida

### Fase 1. Fundamentos editoriales

- definir estructura de carpetas;
- fijar convenciones de notacion;
- organizar el indice maestro del tutorial;
- preparar la plantilla de cada capitulo.

### Fase 2. Nucleo conceptual

- escribir modulos sobre campos clasicos;
- desarrollar cuantizacion canonica;
- introducir campos escalar, de Dirac y gauge;
- incorporar ejemplos de calculo esenciales.

### Fase 3. Perturbaciones y renormalizacion

- teoria de perturbaciones;
- diagramas de Feynman;
- funciones de Green;
- regularizacion y renormalizacion.

### Fase 4. Consolidacion

- ejercicios resueltos;
- revisiones pedagogicas;
- bibliografia comentada;
- mejoras de estilo, figuras y enlaces cruzados.

## Principios editoriales

- Claridad antes que densidad.
- Rigor sin sacrificar legibilidad.
- Progresion acumulativa entre capitulos.
- Notacion consistente en todo el proyecto.
- Documentacion del proceso, no solo del resultado final.

## Estado actual

El proyecto ya ofrece una primera version navegable del recorrido principal. En este momento existen modulos desde `00_prerrequisitos` hasta `12_teorias_de_campo_efectivas`, junto con cuadernos asociados, apendices y una bibliografia comentada.

La cobertura sigue siendo desigual: los bloques `00` a `05` estan mas consolidados como nucleo pedagogico, mientras que `06` a `12` ya tienen estructura util pero todavia admiten ampliaciones importantes en derivaciones, referencias por documento, ejercicios y ejemplos de calculo.

En la reorganizacion editorial mas reciente se limpiaron del arbol principal varias variantes de capitulos que convivian con la version publica mediante nombres como ` 2.md`. Esas versiones no se perdieron: quedaron archivadas en `Tutorial/_borradores/` para facilitar comparacion, rescate o futura promocion a contenido canonico.

El repositorio tambien esta sincronizado con GitHub y mantiene una validacion local minima antes de publicar:

- `python check_links.py`
- `mkdocs build --clean`

## Como contribuir

Si este repositorio crece de forma colaborativa, conviene proponer cambios que:

- mejoren la precision conceptual;
- corrijan errores de notacion o derivacion;
- anadan ejemplos o ejercicios;
- organicen mejor la secuencia pedagogica;
- documenten decisiones editoriales importantes.

## Licencia y uso

El contenido del proyecto se distribuye bajo la licencia [Creative Commons Attribution 4.0 International](LICENSE.md). Si en el futuro quieres distinguir entre contenido editorial y scripts auxiliares, se puede refinar a un esquema dual.
