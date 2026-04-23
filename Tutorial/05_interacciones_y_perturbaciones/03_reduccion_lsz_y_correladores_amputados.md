# Reduccion LSZ y Correladores Amputados

**Nivel:** Nucleo  
**Dificultad:** Media-Alta  
**Tiempo estimado:** 25-35 min  
**Prerequisitos recomendados:** [Diagramas de Feynman y Reglas de Calculo](02_diagramas_de_feynman_y_reglas.md) · [Resumen del modulo](README.md)


## 1. Proposito

Este articulo aclara un puente que a menudo queda implicito en una primera lectura de QFT: como se pasa desde correladores de campos a amplitudes de scattering. El objetivo es presentar la idea de la reduccion LSZ sin entrar en todos los detalles tecnicos de una demostracion completa, pero dejando claro que relacion une propagadores, correladores y matriz $S$.

## 2. El problema conceptual

En muchos formalismos intermedios lo que la teoria calcula de manera natural son funciones de correlacion, por ejemplo:

$$
\langle 0|T\{\phi(x_1)\phi(x_2)\cdots \phi(x_n)\}|0\rangle.
$$

Sin embargo, lo que el experimento pide no es directamente ese objeto, sino amplitudes entre estados asintoticos de entrada y salida. La pregunta natural es entonces:

- por que los correladores contienen la informacion fisica del scattering;
- que parte de ese correlador corresponde a particulas externas reales;
- como extraer la amplitud fisica util.

Este es uno de los puentes conceptuales mas importantes del formalismo. Sin LSZ es facil aprender a dibujar diagramas y a manipular propagadores sin entender por que esos objetos terminan describiendo cantidades medibles en el laboratorio.

## 3. Estados asintoticos y campos interpolantes

La idea central es que el campo cuantico actua como operador capaz de crear o destruir excitaciones con los numeros cuanticos apropiados. En un regimen asintotico, esas excitaciones se comportan como particulas libres y pueden asociarse a los estados preparados y detectados en scattering.

Eso permite usar el campo como un puente entre:

- el vacio y los estados multiparticle;
- el lenguaje de correladores y el lenguaje de amplitudes.

La palabra "interpolante" ayuda mucho. El campo no coincide sin mas con una particula clasica, pero tiene el solapamiento adecuado con los estados fisicos de una particula para servir de intermediario entre el lenguaje operatorial y el de scattering.

## 4. Estructura de polos

Cuando se transforma un correlador a espacio de momentos, las contribuciones asociadas a particulas externas aparecen como polos en

$$
p^2 - m^2.
$$

La intuicion fisica es importante: una particula externa real se reconoce por estar sobre la masa de la teoria efectiva, y esa informacion queda codificada en la estructura analitica del correlador.

De forma esquematica, cerca de un polo de particula estable aparece un comportamiento como

$$
\frac{Z}{p^2-m^2+i\epsilon},
$$

donde $Z$ representa el residuo asociado a la normalizacion del campo. LSZ explota precisamente esa estructura singular para aislar la contribucion de las patas externas.

## 5. Idea de la reduccion LSZ

El esquema de Lehmann-Symanzik-Zimmermann dice, de manera muy resumida, que para obtener la amplitud de scattering hay que:

1. tomar el correlador temporalmente ordenado adecuado;
2. transformarlo a espacio de momentos;
3. identificar los factores de polo asociados a las lineas externas;
4. amputar esos propagadores externos;
5. poner los momentos externos sobre masa.

Por eso LSZ no es una receta aislada: es la justificacion conceptual de por que las reglas de Feynman producen amplitudes y de por que las lineas externas se tratan de manera especial.

En una version muy resumida, para cada pata externa aparece un factor del tipo $(p_i^2-m^2)$ que cancela el polo correspondiente cuando luego se toma el limite on-shell. Lo que sobrevive tras esa cancelacion es el objeto amputado del que se extrae la amplitud.

## 6. Que significa amputar

Amputar un correlador significa retirar los propagadores externos que conectan el correlador con los estados asintoticos. Dicho de forma operativa:

- el correlador completo contiene dinamica interna y propagacion externa;
- la amplitud invariante relevante se asocia al nucleo interno;
- la amputacion elimina la parte universal debida a las lineas externas.

Esto explica por que en el lenguaje diagramatico una amplitud suele escribirse a partir de diagramas con patas externas, pero la informacion dinamica esencial vive en el objeto amputado.

Vale la pena subrayar una diferencia pedagogica importante:

- una linea externa codifica el acoplamiento del campo con un estado asintotico observable;
- una linea interna forma parte de la dinamica virtual propiamente dicha.

## 7. Relacion con la matriz S

En la practica, LSZ conecta los elementos de matriz de $S$ con correladores del vacio. Ese nexo es uno de los puntos mas profundos de la teoria perturbativa: el laboratorio habla en terminos de estados de entrada y salida, mientras que el formalismo de campos habla de correladores y operadores.

La reduccion LSZ traduce entre ambos idiomas.

Por eso tambien suele escribirse

$$
S = 1 + iT,
$$

y el contenido no trivial del scattering vive en $T$. LSZ ayuda a ver como ese contenido emerge de correladores del vacio.

## 8. Ejemplo conceptual en teoria escalar

Para un proceso escalar $2\to2$, el correlador de cuatro puntos contiene:

- polos externos asociados a las cuatro particulas observables;
- contribuciones internas debidas a vertices y propagadores;
- informacion sobre distintos canales cinematicos.

Al amputar las cuatro patas externas y evaluar sobre masa se obtiene el objeto que, a nivel de arbol, se reconoce como la amplitud $\mathcal{M}$ del proceso.

En una teoria $\phi^4$, por ejemplo, esa amputacion deja de manera transparente el termino de contacto responsable del scattering elemental a arbol. En teorias con intercambios, el mismo procedimiento organiza las contribuciones en canales $s$, $t$ y $u$.

## 9. Por que esto importa pedagogicamente

Sin esta capa conceptual es facil memorizar reglas de Feynman sin entender de donde vienen. LSZ deja ver que:

- los diagramas no son una magia grafica separada del formalismo;
- las lineas externas no se tratan igual que las internas;
- el correlador es un objeto mas grande que la amplitud fisica final.

Tambien deja claro por que los calculos perturbativos suelen tener dos capas:

- primero se construyen funciones de Green mediante reglas de Feynman;
- luego se interpreta el resultado en clave de scattering usando la logica LSZ.

## Cuaderno asociado
- `../../Cuadernos/problemas_resueltos/12_lsz_y_amplitudes_escalares.ipynb`: usarlo para seguir el paso entre correlador completo, amputacion y amplitud escalar elemental de forma guiada.
- `../../Cuadernos/problemas_resueltos/10_interacciones_y_perturbaciones.ipynb`: usarlo para seguir el paso desde correladores a amplitudes en ejemplos escalares sencillos.
- `../../Cuadernos/ejemplos/06_diagramas_de_feynman_basicos.ipynb`: usarlo para comparar la lectura visual del diagrama con el objeto analitico que LSZ ayuda a justificar.

## 11. Advertencias utiles

- LSZ requiere hipotesis sobre estados asintoticos bien definidos; no es una receta universal para cualquier teoria o medio.
- El correlador completo no coincide directamente con la amplitud observable.
- Amputar no significa borrar arbitrariamente lineas del diagrama, sino extraer una estructura fisica bien definida.
- En teorias con confinamiento, particulas inestables o fondos no triviales, la identificacion de estados asintoticos exige mucho mas cuidado.

## 12. Preguntas de comprobacion

- Por que un correlador contiene mas informacion que una amplitud de scattering.
- Que papel juegan los polos en $p^2-m^2$.
- Que significa amputar una linea externa.
- Por que LSZ ayuda a entender el origen de las reglas de Feynman.

## 13. Ejercicios sugeridos

1. Explicar con tus palabras por que una amplitud observable no coincide sin mas con el correlador completo.
2. Describir que informacion fisica se extrae al aislar polos de una funcion de Green.
3. Justificar por que la amputacion de lineas externas no es una operacion arbitraria sino parte del paso hacia el scattering fisico.

## 14. Referencias y lecturas recomendadas

- Base: Peskin y Schroeder, relacion entre correladores y scattering.
- Complementaria: Tong, discusion introductoria del puente entre funciones de Green y amplitudes.
- Profundizacion: textos formales de QFT sobre representacion de Lehmann y reduccion LSZ.

## 15. Cierre

LSZ vuelve inteligible la relacion entre los dos idiomas centrales del curso: correladores y amplitudes. Sin esta pieza, las reglas de Feynman pueden parecer una receta grafica. Con ella, se entiende que el calculo perturbativo es una manera organizada de extraer del correlador el nucleo amputado que conecta con el scattering fisico.


---

## Navegacion del tutorial

[(anterior) Diagramas de Feynman y Reglas de Calculo](02_diagramas_de_feynman_y_reglas.md) | [(siguiente) Reglas de Feynman: Resumen Operativo](04_reglas_de_feynman_resumen_operativo.md)
