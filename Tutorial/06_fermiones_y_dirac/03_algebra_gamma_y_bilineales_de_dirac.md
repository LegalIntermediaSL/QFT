# Algebra Gamma y Bilineales de Dirac

## 1. Proposito

Este documento profundiza en la estructura algebraica que hace posible la ecuacion de Dirac. El objetivo es entender mejor que papel cumplen las matrices gamma, como se organizan los bilineales de Dirac y por que esa clasificacion importa para construir lagrangianas e interacciones.

## 2. Algebra de Clifford

Las matrices gamma satisfacen

$$
\{\gamma^\mu,\gamma^\nu\} = 2\eta^{\mu\nu}.
$$

Esta relacion codifica la metrica del espacio-tiempo dentro del algebra matricial. No es un detalle ornamental: es la condicion que permite linealizar la relacion relativista energia-momento.

## 3. Bases y representaciones

La algebra puede representarse en distintas bases, entre ellas:

- base de Dirac;
- base de Weyl o quiral.

La eleccion de base no cambia la fisica, pero si cambia que propiedades quedan mas visibles:

- la base de Dirac resulta comoda en el limite no relativista;
- la base de Weyl hace mas transparente la quiralidad.

## 4. Objetos derivados frecuentes

Algunos objetos que aparecen una y otra vez son:

$$
\gamma^5, \qquad \sigma^{\mu\nu} = \frac{i}{2}[\gamma^\mu,\gamma^\nu].
$$

Estos operadores ayudan a clasificar corrientes, acoplamientos y transformaciones bajo simetrias.

## 5. Bilineales de Dirac

Los bilineales se construyen combinando $\psi$ y $\bar{\psi}$ de distintas maneras. Los mas importantes son:

- escalar: $\bar{\psi}\psi$;
- vector: $\bar{\psi}\gamma^\mu\psi$;
- axial vector: $\bar{\psi}\gamma^\mu\gamma^5\psi$;
- pseudoscalar: $\bar{\psi}\gamma^5\psi$;
- tensor: $\bar{\psi}\sigma^{\mu\nu}\psi$.

Esta lista no es solo una taxonomia formal. Indica que tipos de objetos pueden aparecer en una teoria relativista compatible con ciertas simetrias.

## 6. Lectura fisica de algunos bilineales

Dos casos particularmente importantes son:

- $\bar{\psi}\psi$, que aparece en el termino de masa de Dirac;
- $\bar{\psi}\gamma^\mu\psi$, que aparece como corriente electromagnetica.

Eso muestra que la clasificacion algebraica de bilineales tiene una traduccion fisica inmediata.

## 7. Simetrias y restricciones

No cualquier combinacion de campos fermionicos es admisible en una lagrangiana dada. Ademas de Lorentz, suelen entrar en juego:

- simetrias internas;
- paridad;
- conjugacion de carga;
- quiralidad.

Por eso entender bilineales es una herramienta de construccion, no solo de notacion.

## 8. Ejemplo corto de lectura

Si una interaccion contiene un campo gauge vectorial $A_\mu$, el bilineal mas natural para acoplarlo no es arbitrario: debe tener tambien estructura vectorial. De ahi aparece de manera muy natural el termino

$$
\bar{\psi}\gamma^\mu\psi\, A_\mu.
$$

## 9. Cuaderno asociado

- `../../Cuadernos/problemas_resueltos/09_cuantizacion_del_campo_escalar.ipynb`: usarlo como referencia de contraste con el caso bosonico.
- `../../Cuadernos/problemas_resueltos/06_fundamentos_conceptuales.ipynb`: usarlo para reforzar el hilo entre simetria, campos y objetos admisibles.

## 10. Advertencias utiles

- La eleccion de base para las gamma no cambia la fisica, pero si cambia la comodidad del calculo.
- No todos los bilineales tienen la misma transformacion bajo Lorentz.
- Ver una $\gamma^\mu$ en una expresion no basta para entenderla: importa con que otros objetos esta contraida.

## 11. Preguntas de comprobacion

- Por que la algebra de Clifford es indispensable para la ecuacion de Dirac.
- Que diferencia hay entre un bilineal escalar y uno vectorial.
- Por que el termino de masa de Dirac y la corriente electromagnetica no usan el mismo bilineal.

## 12. Referencias y lecturas recomendadas

- Base: Peskin y Schroeder, espinores y bilineales de Dirac.
- Complementaria: Tong, presentacion pedagogica de gamma y quiralidad.
- Profundizacion: textos de teoria de grupos y espinores relativistas.


---

## Navegacion del tutorial

[(anterior) Cuantizacion de Campos Fermionicos](02_cuantizacion_de_campos_fermionicos.md) | [(siguiente) Corriente de Dirac y Limite No Relativista](04_corriente_de_dirac_y_limite_no_relativista.md)
