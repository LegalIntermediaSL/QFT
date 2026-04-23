# Matching UV y coeficientes de Wilson

**Nivel:** Avanzado  
**Dificultad:** Alta  
**Tiempo estimado:** 25-35 min  
**Prerequisitos recomendados:** [Doble beta sin neutrinos](07_doble_beta_sin_neutrinos.md) · [Resumen del modulo](README.md)


## 1. Proposito

Este documento cierra la segunda ola avanzada del modulo 12 introduciendo una de las ideas tecnicas mas importantes en EFT: el matching entre una teoria UV y su descripcion efectiva, resumido en coeficientes de Wilson.

## 2. La pregunta central

Cuando decimos que una EFT "recuerda" una teoria mas fundamental, necesitamos una receta para transferir informacion entre ambas.

Esa receta es el matching:

- calculamos una cantidad adecuada en la teoria UV;
- calculamos la misma cantidad en la EFT;
- ajustamos los coeficientes efectivos para que ambas coincidan a baja energia.

## 3. Coeficientes de Wilson

Los coeficientes que multiplican operadores efectivos se conocen como coeficientes de Wilson.

En una expansion esquematica:

$$
\mathcal{L}_{\mathrm{eff}}
= \mathcal{L}_{\mathrm{ligera}}
+ \sum_i C_i(\mu)\,\mathcal{O}_i,
$$

los objetos $C_i(\mu)$ contienen:

- la huella de la teoria UV;
- la dependencia con la escala de renormalizacion;
- la informacion necesaria para conectar observables IR con fisica de alta energia.

No basta con decir que "hay" un operador permitido por simetria. Para hacer fisica cuantitativa necesitamos saber con que peso aparece, y precisamente eso es lo que codifica el coeficiente de Wilson.

## 4. Estructura logica del matching

La idea puede resumirse en una receta:

1. elegir un conjunto de observables o amplitudes apropiadas;
2. evaluarlos en la teoria UV a momentos pequeños frente a la masa pesada;
3. evaluarlos en la EFT con operadores locales;
4. igualar ambos resultados orden por orden en la expansion en $E/\Lambda$.

Lo esencial es comparar cantidades que tengan la misma interpretacion fisica en ambos lenguajes. No se trata de igualar lagrangianos "a ojo", sino de exigir que ambas teorias den la misma fisica de baja energia.

## 5. Matching a nivel arbol

El ejemplo mas simple es exactamente el que ya vimos con la teoria de Fermi:

- la teoria UV tiene intercambio de un boson pesado;
- la EFT tiene un operador local de cuatro fermiones;
- el matching fija el coeficiente del operador comparando ambas amplitudes para $q^2 \ll M^2$.

Esta logica se generaliza a SMEFT, neutrinos pesados, sectores escalares adicionales y muchas otras extensiones.

En terminos muy esquematicos, si en la teoria UV aparece una amplitud

$$
\mathcal{A}_{\mathrm{UV}} \sim \frac{g^2}{q^2-M^2},
$$

entonces para $q^2 \ll M^2$ se expande como

$$
\mathcal{A}_{\mathrm{UV}} \sim -\frac{g^2}{M^2}
\left(
1 + \frac{q^2}{M^2} + \cdots
\right).
$$

La EFT reproduce esta estructura mediante un operador local dominante y, si hace falta mas precision, operadores con derivadas adicionales. Asi se ve con claridad por que el matching genera toda una torre de operadores, no solo uno.

## 6. Matching y running

Matching y running no son lo mismo.

- el matching conecta teorias distintas a una escala de transicion;
- el running describe como cambian coeficientes y parametros dentro de una misma EFT al variar la escala.

En la practica moderna, ambas ideas trabajan juntas:

1. se hace matching a una escala cercana a la masa pesada;
2. se hace correr la EFT hacia energias mas bajas;
3. se comparan observables con el experimento.

Esta separacion conceptual evita otra confusion habitual: el matching responde "que informacion UV entra en la EFT al cruzar un umbral", mientras que el running responde "como evoluciona esa informacion dentro de la EFT al cambiar de escala".

## 7. Dependencia de base y redundancias

Los coeficientes de Wilson dependen de la base operatorial elegida. Esto no significa arbitrariedad fisica, sino que distintos conjuntos de operadores pueden describir la misma fisica si se relacionan mediante:

- ecuaciones de movimiento;
- integraciones por partes;
- redefiniciones de campo;
- identidades algebraicas o de simetria.

Por eso, al comparar resultados de distintos articulos o convenciones, no basta con mirar simbolos: hay que verificar en que base se esta trabajando.

## 8. Lectura fisica

Los coeficientes de Wilson son valiosos porque permiten hablar de nueva fisica sin escribir toda la UV completion cada vez. Son una interfaz entre:

- teorias microscópicas;
- observables accesibles;
- precision experimental;
- jerarquias de escala.

Tambien sirven como lenguaje comun entre comunidades distintas. Una persona puede trabajar en una UV completion concreta y otra en analisis fenomenologico de precision; los coeficientes de Wilson permiten que ambas hablen del mismo contenido IR con una interfaz compartida.

## 9. Ejemplo corto de lectura

Si dos UV completions diferentes producen el mismo operador efectivo pero con distinto coeficiente de Wilson, una EFT bien organizada puede no distinguirlas del todo a una sola escala, pero si cuantificar que tan grandes son sus efectos IR y como evolucionan al correr con la escala.

## 10. Matching a lazo: por que importa

En muchos problemas de precision, el matching a nivel arbol no basta. Los lazos pueden:

- generar operadores que no aparecen a nivel arbol;
- modificar de forma importante los coeficientes ya presentes;
- introducir logaritmos y mezclas entre operadores.

No hace falta dominar aun toda la maquinaria tecnica, pero si conviene registrar la idea: cuando la precision experimental mejora, la EFT exige matching y running cada vez mas refinados.

## Cuaderno asociado
- `../../Cuadernos/ejemplos/19_matching_uv_a_smeft.ipynb`: usarlo para fijar la idea de matching, comparacion de amplitudes y papel de los coeficientes de Wilson.

## 12. Advertencias utiles

- El matching puede hacerse a nivel arbol o a lazo; el segundo caso es tecnicamente mucho mas rico.
- Los coeficientes de Wilson dependen de la base operatorial elegida.
- Dos teorias UV distintas pueden verse muy parecidas desde la EFT en ciertos observables limitados.

## 13. Preguntas de comprobacion

- Que problema resuelve el matching dentro de una EFT.
- Que informacion fisica contienen los coeficientes de Wilson.
- Por que matching y running son ideas complementarias pero no identicas.

## Ejercicios sugeridos

1. Explicar por que no basta con "adivinar" operadores efectivos y hace falta un procedimiento de matching entre la teoria UV y la EFT.
2. Describir que informacion fisica sobre la teoria microscópica queda resumida en los coeficientes de Wilson.
3. Comparar matching y running indicando que pregunta responde cada uno dentro del uso moderno de una EFT.

## 14. Referencias y lecturas recomendadas

- Base: introducciones pedagogicas a SMEFT y coeficientes de Wilson.
- Complementaria: textos sobre matching a nivel arbol y running de operadores efectivos.
- Profundizacion: revisiones modernas sobre EFT de precision y matching a un lazo.


---

## Navegacion del tutorial

[(anterior) Doble beta sin neutrinos](07_doble_beta_sin_neutrinos.md) | [(siguiente) Apendices](../99_apendices/README.md)
