# Algebra Gamma y Bilineales de Dirac

**Nivel:** Nucleo  
**Dificultad:** Media-Alta  
**Tiempo estimado:** 25-35 min  
**Prerequisitos recomendados:** [Cuantizacion de Campos Fermionicos](02_cuantizacion_de_campos_fermionicos.md) · [Resumen del modulo](README.md)


## 1. Proposito

Este documento profundiza en la estructura algebraica que hace posible la ecuacion de Dirac. El objetivo es entender mejor que papel cumplen las matrices gamma, como se organizan los bilineales de Dirac y por que esa clasificacion importa para construir lagrangianas e interacciones.

No se trata solo de una lista de identidades utiles. Las matrices gamma son la forma en que la estructura relativista del espacio-tiempo queda incrustada en el formalismo fermionico.

## 2. Algebra de Clifford

Las matrices gamma satisfacen

$$
\{\gamma^\mu,\gamma^\nu\} = 2\eta^{\mu\nu}.
$$

Esta relacion codifica la metrica del espacio-tiempo dentro del algebra matricial. No es un detalle ornamental: es la condicion que permite linealizar la relacion relativista energia-momento.

En efecto, al buscar una ecuacion lineal en derivadas para fermiones relativistas, la algebra de Clifford garantiza que al cuadrar el operador de Dirac se recupera la estructura tipo Klein-Gordon.

## 3. Bases y representaciones

La algebra puede representarse en distintas bases, entre ellas:

- base de Dirac;
- base de Weyl o quiral.

La eleccion de base no cambia la fisica, pero si cambia que propiedades quedan mas visibles:

- la base de Dirac resulta comoda en el limite no relativista;
- la base de Weyl hace mas transparente la quiralidad.

Esto es una buena leccion general: cambiar de representacion matricial puede simplificar mucho la intuicion sin alterar el contenido fisico del formalismo.

## 4. Objetos derivados frecuentes

Algunos objetos que aparecen una y otra vez son:

$$
\gamma^5, \qquad \sigma^{\mu\nu} = \frac{i}{2}[\gamma^\mu,\gamma^\nu].
$$

Estos operadores ayudan a clasificar corrientes, acoplamientos y transformaciones bajo simetrias.

En particular:

- $\gamma^5$ organiza la estructura quiral;
- $\sigma^{\mu\nu}$ aparece en bilineales tensoriales y en acoplamientos tipo momento magnetico.

## 5. Bilineales de Dirac

Los bilineales se construyen combinando $\psi$ y $\bar{\psi}$ de distintas maneras. Los mas importantes son:

- escalar: $\bar{\psi}\psi$;
- vector: $\bar{\psi}\gamma^\mu\psi$;
- axial vector: $\bar{\psi}\gamma^\mu\gamma^5\psi$;
- pseudoscalar: $\bar{\psi}\gamma^5\psi$;
- tensor: $\bar{\psi}\sigma^{\mu\nu}\psi$.

Esta lista no es solo una taxonomia formal. Indica que tipos de objetos pueden aparecer en una teoria relativista compatible con ciertas simetrias.

Cada uno de estos bilineales transforma de forma distinta bajo Lorentz y bajo simetrias discretas, y por eso no pueden intercambiarse arbitrariamente en una lagrangiana.

## 6. Lectura fisica de algunos bilineales

Dos casos particularmente importantes son:

- $\bar{\psi}\psi$, que aparece en el termino de masa de Dirac;
- $\bar{\psi}\gamma^\mu\psi$, que aparece como corriente electromagnetica.

Eso muestra que la clasificacion algebraica de bilineales tiene una traduccion fisica inmediata.

Tambien es muy util recordar que el axial vector

$$
\bar{\psi}\gamma^\mu\gamma^5\psi
$$

juega un papel central en corrientes quirales y en interacciones débiles.

## 7. Simetrias y restricciones

No cualquier combinacion de campos fermionicos es admisible en una lagrangiana dada. Ademas de Lorentz, suelen entrar en juego:

- simetrias internas;
- paridad;
- conjugacion de carga;
- quiralidad.

Por eso entender bilineales es una herramienta de construccion, no solo de notacion.

Cuando uno quiere decidir que interacciones son compatibles con una teoria, la pregunta correcta no es solo "que indices puedo escribir", sino "como transforma este bilineal bajo las simetrias relevantes".

## 8. Ejemplo corto de lectura

Si una interaccion contiene un campo gauge vectorial $A_\mu$, el bilineal mas natural para acoplarlo no es arbitrario: debe tener tambien estructura vectorial. De ahi aparece de manera muy natural el termino

$$
\bar{\psi}\gamma^\mu\psi\, A_\mu.
$$

Este tipo de razonamiento muestra que muchas formas del lagrangiano no se eligen por gusto, sino por compatibilidad entre representaciones y simetrias.

## Cuaderno asociado
- `../../Cuadernos/ejemplos/09_bilineales_y_proyectores_quirales.ipynb`: usarlo para comparar bilineales de Dirac, recordar la lectura fisica de corrientes vectoriales y axiales y fijar la intuicion de proyectores quirales.
- `../../Cuadernos/problemas_resueltos/09_cuantizacion_del_campo_escalar.ipynb`: usarlo como referencia de contraste con el caso bosonico.
- `../../Cuadernos/problemas_resueltos/06_fundamentos_conceptuales.ipynb`: usarlo para reforzar el hilo entre simetria, campos y objetos admisibles.

## 10. Advertencias utiles

- La eleccion de base para las gamma no cambia la fisica, pero si cambia la comodidad del calculo.
- No todos los bilineales tienen la misma transformacion bajo Lorentz.
- Ver una $\gamma^\mu$ en una expresion no basta para entenderla: importa con que otros objetos esta contraida.
- La clasificacion de bilineales es util precisamente porque evita escribir interacciones con estructura tensorial equivocada.

## 11. Preguntas de comprobacion

- Por que la algebra de Clifford es indispensable para la ecuacion de Dirac.
- Que diferencia hay entre un bilineal escalar y uno vectorial.
- Por que el termino de masa de Dirac y la corriente electromagnetica no usan el mismo bilineal.

## 12. Cierre

Las matrices gamma y los bilineales de Dirac forman el vocabulario basico del sector fermionico relativista. Una vez que este vocabulario se domina, muchas expresiones de QED, del Modelo Estandar y de la fenomenologia fermionica dejan de parecer arbitrarias y se leen como consecuencias directas de simetria y estructura relativista.

## 13. Referencias y lecturas recomendadas

- Base: Peskin y Schroeder, espinores y bilineales de Dirac.
- Complementaria: Tong, presentacion pedagogica de gamma y quiralidad.
- Profundizacion: textos de teoria de grupos y espinores relativistas.


---

## Navegacion del tutorial

[(anterior) Cuantizacion de Campos Fermionicos](02_cuantizacion_de_campos_fermionicos.md) | [(siguiente) Corriente de Dirac y Limite No Relativista](04_corriente_de_dirac_y_limite_no_relativista.md)