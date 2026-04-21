# Matching UV y coeficientes de Wilson

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

## 4. Matching a nivel arbol

El ejemplo mas simple es exactamente el que ya vimos con la teoria de Fermi:

- la teoria UV tiene intercambio de un boson pesado;
- la EFT tiene un operador local de cuatro fermiones;
- el matching fija el coeficiente del operador comparando ambas amplitudes para $q^2 \ll M^2$.

Esta logica se generaliza a SMEFT, neutrinos pesados, sectores escalares adicionales y muchas otras extensiones.

## 5. Matching y running

Matching y running no son lo mismo.

- el matching conecta teorias distintas a una escala de transicion;
- el running describe como cambian coeficientes y parametros dentro de una misma EFT al variar la escala.

En la practica moderna, ambas ideas trabajan juntas:

1. se hace matching a una escala cercana a la masa pesada;
2. se hace correr la EFT hacia energias mas bajas;
3. se comparan observables con el experimento.

## 6. Lectura fisica

Los coeficientes de Wilson son valiosos porque permiten hablar de nueva fisica sin escribir toda la UV completion cada vez. Son una interfaz entre:

- teorias microscópicas;
- observables accesibles;
- precision experimental;
- jerarquias de escala.

## 7. Ejemplo corto de lectura

Si dos UV completions diferentes producen el mismo operador efectivo pero con distinto coeficiente de Wilson, una EFT bien organizada puede no distinguirlas del todo a una sola escala, pero si cuantificar que tan grandes son sus efectos IR y como evolucionan al correr con la escala.

## 8. Cuaderno asociado

- `../../Cuadernos/ejemplos/19_matching_uv_a_smeft.ipynb`: usarlo para fijar la idea de matching, comparacion de amplitudes y papel de los coeficientes de Wilson.

## 9. Advertencias utiles

- El matching puede hacerse a nivel arbol o a lazo; el segundo caso es tecnicamente mucho mas rico.
- Los coeficientes de Wilson dependen de la base operatorial elegida.
- Dos teorias UV distintas pueden verse muy parecidas desde la EFT en ciertos observables limitados.

## 10. Preguntas de comprobacion

- Que problema resuelve el matching dentro de una EFT.
- Que informacion fisica contienen los coeficientes de Wilson.
- Por que matching y running son ideas complementarias pero no identicas.

## 11. Referencias y lecturas recomendadas

- Base: introducciones pedagogicas a SMEFT y coeficientes de Wilson.
- Complementaria: textos sobre matching a nivel arbol y running de operadores efectivos.
- Profundizacion: revisiones modernas sobre EFT de precision y matching a un lazo.


---

## Navegacion del tutorial

[(anterior) Doble beta sin neutrinos](07_doble_beta_sin_neutrinos.md) | [(siguiente) Apendices](../99_apendices/README.md)
