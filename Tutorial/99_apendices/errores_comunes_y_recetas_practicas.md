# Errores Comunes y Recetas Practicas

Este apendice reune tropiezos frecuentes y pequeñas recetas de trabajo para leer, escribir y calcular dentro del tutorial. No sustituye a los capitulos teoricos, pero ayuda mucho a evitar confusiones repetidas.

## 1. Errores comunes de lectura

- Confundir `campo` con `funcion de onda de una particula`. En QFT, el campo es un operador o una variable fundamental definida en el espacio-tiempo.
- Confundir `correlador` con `amplitud observable`. Los correladores contienen mas informacion; LSZ explica como extraer la amplitud fisica.
- Confundir `quiralidad` con `helicidad`. Coinciden en ciertos limites, pero no son identicas en general.
- Tomar un `diagrama de Feynman` como una fotografia literal del proceso. Es un termino de una expansion perturbativa.
- Leer `regularizacion` y `renormalizacion` como sinonimos. La primera controla divergencias; la segunda reexpresa la teoria en terminos fisicos.
- Pensar que `fijar gauge` rompe la teoria gauge. En realidad elige una descripcion operativa del mismo contenido fisico.
- Confundir `vacio cuantico` con ausencia trivial de todo. El vacio tiene estructura y puede tener energia, entrelazamiento o respuesta dinamica.

## 2. Errores comunes de calculo

- Perder factores de `2\pi` al cambiar entre espacio de posiciones y espacio de momentos.
- Olvidar la prescripcion `i\epsilon` cuando se escribe un propagador por primera vez.
- Mezclar firmas metricas sin declararlo.
- Usar conmutadores donde la teoria exige anticonmutadores fermionicos.
- Olvidar si un momento interno esta `on-shell` o `off-shell`.
- Usar una normalizacion de estados y otra distinta para amplitudes o reglas de Feynman.

## 3. Receta: como leer un lagrangiano

1. Identifica los campos.
2. Distingue terminos cineticos, de masa e interaccion.
3. Pregunta que simetrias parecen respetarse.
4. Busca que terminos mezclan sectores distintos.
5. Pregunta que observables o corrientes sugiere el lagrangiano.

## 4. Receta: como reconocer una simetria

1. Propone una transformacion del campo.
2. Sustituye en la accion o en la densidad lagrangiana.
3. Comprueba si la variacion se anula o es una derivada total.
4. Si la simetria es continua, pregunta por la corriente de Noether asociada.
5. Si es local, pregunta si obliga a introducir conexion o campo gauge.

## 5. Receta: como pasar de lagrangiano a vertices

1. Aisla el termino de interaccion.
2. Identifica que campos se encuentran en ese termino.
3. Lee la estructura de indices y constantes de acoplamiento.
4. Pasa a espacio de momentos con la convencion de Fourier usada.
5. Conserva la delta de cuatro-momento asociada al vertice.

## 6. Receta: como leer un propagador

1. Identifica que operador cinetico esta invirtiendo.
2. Comprueba si la teoria necesita fijacion de gauge o prescripcion causal explicita.
3. Mira donde estan los polos.
4. Pregunta que significan esos polos para el espectro o para estados externos.
5. Distingue si el propagador aparece como linea interna virtual o como bloque de una funcion de Green.

## 7. Receta: como abordar un capitulo tecnico

1. Lee primero proposito y advertencias.
2. Detecta que objetos nuevos aparecen: corriente, propagador, funcional, beta, Wilson.
3. Reescribe a mano dos o tres ecuaciones centrales.
4. Resume en una frase que problema fisico resuelve el capitulo.
5. Solo despues intenta memorizar formulas.

## 8. Receta: como saber si algo es observable o gauge

Hazte estas preguntas:

- cambia bajo una transformacion gauge local?
- depende del parametro de gauge de forma intermedia o final?
- se expresa como amplitud o correlador completo sin amputar?
- necesita estados asintoticos o una proyeccion fisica para adquirir significado experimental?

Regla practica: un resultado fisico final no deberia depender de la eleccion de gauge.

## 9. Receta: como estudiar con notebooks del repositorio

1. Lee primero el capitulo teorico.
2. Usa el notebook para una sola tarea concreta: comprobar una identidad, seguir un ejemplo o ver una cuenta guiada.
3. Anota que parte del notebook refuerza intuicion y cual solo automatiza algebra.
4. Vuelve al texto y resume la idea sin mirar codigo.

## 10. Cierre

Este apendice existe para ahorrar friccion. Muchas dificultades iniciales en QFT no vienen de una idea verdaderamente profunda, sino de confundir niveles de descripcion, mezclar convenciones o perder el hilo entre formalismo y significado fisico.

---

[Volver a Apendices](README.md)
