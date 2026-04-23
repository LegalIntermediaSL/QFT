# Guía de Contribución - Proyecto QFT

¡Gracias por tu interés en contribuir a este tutorial de Teoría Cuántica de Campos! El objetivo es crear un recurso de alta calidad, pedagógico y técnicamente riguroso.

## Cómo contribuir

Puedes colaborar de varias maneras:
1. **Contenido Técnico**: Añadiendo nuevos módulos o expandiendo los existentes.
2. **Correcciones**: Reportando o corrigiendo erratas matemáticas, de notación o de enlaces.
3. **Interactivos**: Creando o mejorando los Jupyter Notebooks.
4. **Visuales**: Añadiendo diagramas Mermaid o figuras ilustrativas.

## Estándares Técnicos

### 1. Fórmulas Matemáticas (LaTeX)
- Utiliza siempre delimitadores de bloque `$$ ... $$` para ecuaciones importantes.
- Mantén la consistencia con el [Glosario de Notación](Tutorial/99_apendices/glosario_notacion.md).
- Convención de métrica: $(+---)$.

### 2. Estructura de Módulos
Cada nuevo módulo debe seguir el archivo [template_modulo.md](Tutorial/template_modulo.md). Esto incluye:
- Objetivo claro.
- Mapa del módulo (Mermaid).
- Desarrollo teórico.
- Preguntas de comprobacion y ejercicios.

Para los capítulos públicos del recorrido principal, la validación editorial comprueba además una estructura mínima:
- título principal `#`;
- bloque de metadatos (`Nivel`, `Dificultad`, `Tiempo estimado`, `Prerequisitos`);
- sección de `Proposito` u `Objetivo`;
- sección de preguntas de comprobación o estudio;
- sección de referencias;
- sección final de navegación.

### 3. Diagramas Mermaid
- Prefiere diagramas detallados (`flowchart TD`) para el flujo conceptual.
- Para reglas de Feynman de QED, utiliza los estilos definidos en `Imagenes/diagramas/qed_rules.md`.

### 4. Enlaces, navegación y consistencia editorial
- Todo documento nuevo debe enlazar con su contexto: índice de módulo, documento anterior o siguiente cuando aplique, y referencias de apoyo.
- Si un capítulo tiene notebook asociado, conviene citarlo explícitamente y explicar para qué sirve.
- Antes de abrir un PR, ejecuta `python check_links.py`.
- Si modificas la navegación general, actualiza también `mkdocs.yml`, `README.md` y el índice del módulo afectado.
- Si generas una variante, resumen alternativo o borrador de un capítulo ya publicado, guárdalo en `Tutorial/_borradores/` conservando la estructura temática del módulo.
- Evita dejar archivos alternativos en paralelo al contenido público con sufijos como ` 2.md`, porque vuelven ambigua la versión canónica.

### 5. Notebooks
- Mantén nombres numerados y descriptivos.
- Añade una primera celda con objetivo, prerequisitos y resultado esperado.
- Evita mezclar demasiados temas en un mismo cuaderno.
- Si un cuaderno requiere librerías poco comunes, indícalo al inicio y refléjalo en `requirements.txt`.

## Proceso de Desarrollo

1. Haz un **Fork** del repositorio.
2. Crea una **Rama** para tu mejora (`git checkout -b feature/nuevo-modulo`).
3. Instala dependencias según el tipo de cambio:
   - `pip install -r requirements.txt` para cuadernos.
   - `pip install -r requirements-docs.txt` para documentación y sitio.
4. Realiza tus cambios y valida el repositorio:
   - `python check_links.py`
   - `mkdocs build --clean`
5. Abre un **Pull Request** describiendo detalladamente tus cambios.

## Checklist sugerida para un PR

- El contenido nuevo respeta la notación global.
- Los enlaces locales y la navegación del módulo funcionan.
- `mkdocs.yml` refleja los cambios si hay nuevas páginas públicas.
- Los notebooks nuevos o modificados explican su objetivo desde la primera celda.
- La documentación principal quedó sincronizada si cambió el alcance del proyecto.

---
Mantenemos una comunicación respetuosa y enfocada en la claridad pedagógica. ¡Esperamos tus aportes!
