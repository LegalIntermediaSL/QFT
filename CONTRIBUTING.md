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
- Preguntas de estudio y Ejercicios.

### 3. Diagramas Mermaid
- Prefiere diagramas detallados (`flowchart TD`) para el flujo conceptual.
- Para reglas de Feynman de QED, utiliza los estilos definidos en `Imagenes/diagramas/qed_rules.md`.

## Proceso de Desarrollo

1. Haz un **Fork** del repositorio.
2. Crea una **Rama** para tu mejora (`git checkout -b feature/nuevo-modulo`).
3. Realiza tus cambios y verifica que los enlaces no estén rotos (puedes usar el script `check_links.py`).
4. Abre un **Pull Request** describiendo detalladamente tus cambios.

---
Mantenemos una comunicación respetuosa y enfocada en la claridad pedagógica. ¡Esperamos tus aportes!
