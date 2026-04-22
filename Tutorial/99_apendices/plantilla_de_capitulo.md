# Plantilla Editorial de Capitulo

Esta plantilla propone una estructura minima y reutilizable para mantener coherencia pedagogica entre modulos y documentos tecnicos del tutorial.

No es un molde rigido, pero si una guia para que cada texto nuevo conserve el estilo del proyecto: claridad conceptual, hilo formal legible y utilidad como material de estudio.

## 1. Estructura sugerida

1. **Titulo claro del documento**
   - Debe decir que problema resuelve el texto y en que parte del recorrido cae.

2. **Cabecera didactica**
   - `Nivel`
   - `Dificultad`
   - `Tiempo estimado`
   - `Prerequisitos recomendados`

3. **Objetivo**
   - Que deberia entender el lector al terminar.

4. **Idea fisica**
   - Motivacion conceptual antes de introducir demasiado formalismo.

5. **Desarrollo formal**
   - Definiciones, ecuaciones centrales, convenciones y derivacion minima.

6. **Ejemplo de calculo o lectura**
   - Una cuenta corta o un caso modelo que aterrice el formalismo.

7. **Advertencias o errores comunes**
   - Supuestos faciles de olvidar, signos, unidades, interpretaciones equivocadas frecuentes.

8. **Preguntas de comprobacion**
   - Tres a cinco preguntas breves para consolidar lectura.

9. **Referencias y lecturas recomendadas**
   - Una referencia base.
   - Una referencia complementaria.
   - Una sugerencia de profundizacion opcional.

10. **Navegacion**
   - Enlace al capitulo anterior y al siguiente.

## 2. Plantilla base

```md
# Titulo del capitulo

**Nivel:** ...
**Dificultad:** ...
**Tiempo estimado:** ...
**Prerequisitos recomendados:** ...

## Proposito

## Idea fisica

## Desarrollo formal

## Ejemplo de calculo o lectura

## Advertencias utiles

## Preguntas de comprobacion

## Referencias y lecturas recomendadas

## Navegacion
```

## 3. Criterios editoriales

- Claridad antes que densidad.
- Introducir notacion solo cuando haga falta.
- Declarar convenciones de metrica y unidades si afectan formulas.
- Mantener visible el hilo entre intuicion, formalismo y calculo.
- Cerrar cada documento con al menos una referencia concreta.

## 4. Buenas practicas para este repositorio

- No asumir que el lector recuerda el contenido de un modulo lejano.
- Si una formula depende de signos sensibles, repetir la convencion localmente.
- Evitar parrafos largos cuando una lista corta hace mas legible la estructura.
- Conectar el texto con el resto del tutorial: de donde viene y hacia donde lleva.
- Si existe notebook asociado, decir para que sirve y no solo nombrarlo.

## 5. Errores frecuentes al redactar

- Empezar con formalismo sin decir antes que problema fisico se esta resolviendo.
- Introducir demasiada notacion nueva en el mismo parrafo.
- Cerrar un capitulo tecnico sin advertencias ni preguntas de comprobacion.
- Usar referencias demasiado avanzadas sin ofrecer una opcion de entrada mas amable.
- Escribir un texto correcto pero sin puente claro con el modulo anterior o siguiente.

## 6. Cierre

Una buena plantilla no sirve para uniformar por rigidez, sino para que el lector pueda reconocer rapidamente como estudiar cada documento. Si el formato es consistente, la energia mental se invierte en entender la fisica y no en descifrar la estructura del texto.

---
[Volver a Apendices](README.md)
