# Majorana y mecanismo seesaw

## 1. Proposito

Este documento cierra la primera capa avanzada del modulo 12 conectando tres ideas: neutrinos de Majorana, operador de Weinberg y mecanismo seesaw.

## 2. La pregunta fisica

El Modelo Estandar minimo no explica de forma natural por que los neutrinos tienen masas tan pequeñas. Una via muy influyente para entenderlo consiste en introducir estados neutros pesados y permitir masa de Majorana.

## 3. Masa de Majorana

Una masa de Majorana identifica una particula con su propia antiparticula. A nivel esquematico, eso significa que el termino de masa viola el numero leptónico total en dos unidades.

En el lenguaje del tutorial, esta idea ya aparecia al discutir quiralidad y fermiones de Majorana. Aqui la reinsertamos dentro de una EFT y de una posible UV completion.

La diferencia con una masa de Dirac no es solo terminologica. Una masa de Dirac conecta componentes izquierdas y derechas conservando numero leptónico global, mientras que una masa de Majorana permite que ese numero deje de ser una simetria exacta.

## 4. Idea minima del seesaw

Supongamos que existe un neutrino derecho pesado $N$ con masa grande $M$ y un acoplamiento de Yukawa al doblete leptónico y al Higgs.

A nivel estructural, tras ruptura espontanea aparece una matriz de masa con dos escalas:

$$
\begin{pmatrix}
0 & m_D \\
m_D & M
\end{pmatrix},
$$

donde $m_D$ es una masa tipo Dirac y $M$ es la escala pesada de Majorana.

Si $M \gg m_D$, el autovalor ligero queda aproximadamente como

$$
m_\nu \sim \frac{m_D^2}{M}.
$$

Esta es la intuicion central del mecanismo seesaw tipo I.

El nombre "seesaw" es muy descriptivo: al aumentar la escala pesada $M$, el modo ligero se hace mas pequeño. Es una forma muy elegante de convertir una gran jerarquia UV en una masa IR minúscula.

## 5. Diagonalizacion intuitiva

Sin entrar en una diagonalizacion completa, la matriz

$$
\begin{pmatrix}
0 & m_D \\
m_D & M
\end{pmatrix}
$$

tiene dos autovalores muy distintos cuando $M \gg m_D$:

- uno pesado, aproximadamente igual a $M$;
- uno ligero, aproximadamente igual a $-m_D^2/M$.

La moraleja fisica es clara: el estado pesado "empuja hacia abajo" la escala del estado ligero. Esta es la razon por la que el seesaw se percibe como un mecanismo natural para neutrinos muy livianos.

## 6. Conexion con el operador de Weinberg

Si integramos el neutrino derecho pesado, la descripcion IR recupera justamente un operador efectivo tipo Weinberg:

$$
\frac{1}{\Lambda}(L H)(L H).
$$

Por eso el seesaw no compite con SMEFT: lo completa conceptualmente como un ejemplo UV que, al bajar de energia, produce el operador efectivo relevante.

En lenguaje EFT, esto es una leccion muy importante: el operador de Weinberg resume la huella IR de muchos mecanismos UV posibles, y el seesaw tipo I es uno de los mas pedagogicos y estudiados.

## 7. Lectura fisica

La palabra "seesaw" refleja bien la intuicion:

- cuanto mas grande es la escala pesada $M$;
- mas pequeno puede resultar el autovalor ligero;
- y mas natural parece la pequeñez de la masa neutrínica.

Esta idea tambien muestra una virtud conceptual de EFT: no necesitamos conocer todos los detalles del sector pesado para entender su huella dominante en bajas energias.

## 8. Ejemplo corto de lectura

Si el acoplamiento de Yukawa genera una escala tipo Dirac del orden electrodébil pero el neutrino estéril pesado vive a una escala mucho mayor, entonces la masa del neutrino ligero queda fuertemente suprimida. La EFT ve solo el resultado final; el seesaw propone un mecanismo UV posible para producirlo.

## 9. Relacion con leptogénesis y fisica UV

Aunque este tutorial no entra en el detalle fenomenologico completo, conviene registrar que los neutrinos pesados del seesaw tambien aparecen en muchos escenarios de leptogénesis y de fisica mas alla del Modelo Estandar. Eso refuerza el interes del mecanismo: no solo explica masas pequeñas, sino que puede conectarse con el origen de asimetrias cosmologicas.

## 10. Cuaderno asociado

- `../../Cuadernos/problemas_resueltos/20_majorana_y_seesaw.ipynb`: usarlo para seguir la estructura matricial minima del seesaw y su reduccion a una masa ligera efectiva.

## 11. Advertencias utiles

- El seesaw tipo I es una posibilidad influyente, no la unica.
- Observar oscilaciones de neutrinos no demuestra por si solo que la masa sea de Majorana.
- El vinculo con doble beta sin neutrinos requiere pasos fenomenologicos adicionales.

## 12. Preguntas de comprobacion

- Que diferencia conceptual hay entre una masa de Dirac y una de Majorana.
- Por que el seesaw produce naturalmente una masa ligera $m_\nu \sim m_D^2/M$.
- Como se conecta el seesaw con el operador de Weinberg en la descripcion efectiva.

## 13. Referencias y lecturas recomendadas

- Base: revisiones introductorias sobre neutrinos y masas de Majorana.
- Complementaria: textos de seesaw tipo I y EFT leptónica.
- Profundizacion: revisiones sobre leptogenesis, neutrinos estériles y doble beta sin neutrinos.


---

## Navegacion del tutorial

[(anterior) SMEFT y operador de Weinberg](05_smeft_y_operador_de_weinberg.md) | [(siguiente) Doble beta sin neutrinos](07_doble_beta_sin_neutrinos.md)
