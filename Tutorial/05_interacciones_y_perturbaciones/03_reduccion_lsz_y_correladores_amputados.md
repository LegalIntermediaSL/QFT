# Reduccion LSZ y Correladores Amputados

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

## 3. Estados asintoticos y campos interpolantes

La idea central es que el campo cuantico actua como operador capaz de crear o destruir excitaciones con los numeros cuanticos apropiados. En un regimen asintotico, esas excitaciones se comportan como particulas libres y pueden asociarse a los estados preparados y detectados en scattering.

Eso permite usar el campo como un puente entre:

- el vacio y los estados multiparticle;
- el lenguaje de correladores y el lenguaje de amplitudes.

## 4. Estructura de polos

Cuando se transforma un correlador a espacio de momentos, las contribuciones asociadas a particulas externas aparecen como polos en

$$
p^2 - m^2.
$$

La intuicion fisica es importante: una particula externa real se reconoce por estar sobre la masa de la teoria efectiva, y esa informacion queda codificada en la estructura analitica del correlador.

## 5. Idea de la reduccion LSZ

El esquema de Lehmann-Symanzik-Zimmermann dice, de manera muy resumida, que para obtener la amplitud de scattering hay que:

1. tomar el correlador temporalmente ordenado adecuado;
2. transformarlo a espacio de momentos;
3. identificar los factores de polo asociados a las lineas externas;
4. amputar esos propagadores externos;
5. poner los momentos externos sobre masa.

Por eso LSZ no es una receta aislada: es la justificacion conceptual de por que las reglas de Feynman producen amplitudes y de por que las lineas externas se tratan de manera especial.

## 6. Que significa amputar

Amputar un correlador significa retirar los propagadores externos que conectan el correlador con los estados asintoticos. Dicho de forma operativa:

- el correlador completo contiene dinamica interna y propagacion externa;
- la amplitud invariante relevante se asocia al nucleo interno;
- la amputacion elimina la parte universal debida a las lineas externas.

Esto explica por que en el lenguaje diagramatico una amplitud suele escribirse a partir de diagramas con patas externas, pero la informacion dinamica esencial vive en el objeto amputado.

## 7. Relacion con la matriz S

En la practica, LSZ conecta los elementos de matriz de $S$ con correladores del vacio. Ese nexo es uno de los puntos mas profundos de la teoria perturbativa: el laboratorio habla en terminos de estados de entrada y salida, mientras que el formalismo de campos habla de correladores y operadores.

La reduccion LSZ traduce entre ambos idiomas.

## 8. Ejemplo conceptual en teoria escalar

Para un proceso escalar $2\to2$, el correlador de cuatro puntos contiene:

- polos externos asociados a las cuatro particulas observables;
- contribuciones internas debidas a vertices y propagadores;
- informacion sobre distintos canales cinematicos.

Al amputar las cuatro patas externas y evaluar sobre masa se obtiene el objeto que, a nivel de arbol, se reconoce como la amplitud $\mathcal{M}$ del proceso.

## 9. Por que esto importa pedagogicamente

Sin esta capa conceptual es facil memorizar reglas de Feynman sin entender de donde vienen. LSZ deja ver que:

- los diagramas no son una magia grafica separada del formalismo;
- las lineas externas no se tratan igual que las internas;
- el correlador es un objeto mas grande que la amplitud fisica final.

## 10. Cuaderno asociado

- `../../Cuadernos/problemas_resueltos/10_interacciones_y_perturbaciones.ipynb`: usarlo para seguir el paso desde correladores a amplitudes en ejemplos escalares sencillos.
- `../../Cuadernos/ejemplos/06_diagramas_de_feynman_basicos.ipynb`: usarlo para comparar la lectura visual del diagrama con el objeto analitico que LSZ ayuda a justificar.

## 11. Advertencias utiles

- LSZ requiere hipotesis sobre estados asintoticos bien definidos; no es una receta universal para cualquier teoria o medio.
- El correlador completo no coincide directamente con la amplitud observable.
- Amputar no significa borrar arbitrariamente lineas del diagrama, sino extraer una estructura fisica bien definida.

## 12. Preguntas de comprobacion

- Por que un correlador contiene mas informacion que una amplitud de scattering.
- Que papel juegan los polos en $p^2-m^2$.
- Que significa amputar una linea externa.
- Por que LSZ ayuda a entender el origen de las reglas de Feynman.

## 13. Referencias y lecturas recomendadas

- Base: Peskin y Schroeder, relacion entre correladores y scattering.
- Complementaria: Tong, discusion introductoria del puente entre funciones de Green y amplitudes.
- Profundizacion: textos formales de QFT sobre representacion de Lehmann y reduccion LSZ.


---

## Navegacion del tutorial

[(anterior) Diagramas de Feynman y Reglas de Calculo](02_diagramas_de_feynman_y_reglas.md) | [(siguiente) Reglas de Feynman: Resumen Operativo](04_reglas_de_feynman_resumen_operativo.md)
