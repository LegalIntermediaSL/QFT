# Quiralidad, Espinores de Weyl y Fermiones de Majorana

**Nivel:** Nucleo  
**Dificultad:** Media-Alta  
**Tiempo estimado:** 18-25 min  
**Prerequisitos recomendados:** [Corriente de Dirac y Limite No Relativista](04_corriente_de_dirac_y_limite_no_relativista.md) · [Resumen del modulo](README.md)


## 1. Proposito

Este documento profundiza en la estructura quiral de la teoria fermionica y prepara el lenguaje necesario para entender mejor el Modelo Estandar y varias extensiones de la QFT relativista.

Tambien sirve para evitar una confusion habitual: Dirac, Weyl y Majorana no son solo tres nombres para escribir espinores, sino tres maneras de organizar grados de libertad fermionicos con implicaciones fisicas distintas.

## 2. Quiralidad y proyectores

La quiralidad se organiza mediante los proyectores

$$
P_L = \frac{1-\gamma^5}{2}, \qquad P_R = \frac{1+\gamma^5}{2}.
$$

Aplicados a un espinor de Dirac separan sus componentes izquierda y derecha:

$$
\psi_L = P_L \psi, \qquad \psi_R = P_R \psi.
$$

Estos proyectores satisfacen propiedades sencillas pero muy utiles:

$$
P_L^2=P_L,\qquad P_R^2=P_R,\qquad P_LP_R=0.
$$

Eso refleja que separan de forma limpia dos subespacios quirales complementarios.

## 3. Por que importa la quiralidad

La quiralidad es central porque:

- hace visible la estructura del sector débil;
- permite reorganizar el contenido fermionico de forma mas fina;
- distingue entre masa, simetria y representaciones gauge.

En el limite sin masa, las componentes quirales se desacoplan de forma especialmente clara. Por eso la quiralidad deja de ser una mera herramienta algebraica y se vuelve una forma natural de organizar la teoria.

## 4. Weyl

Un espinor de Weyl describe una sola componente quiral. En muchas formulaciones modernas, especialmente en el Modelo Estandar, este lenguaje resulta mas natural que el espinor de Dirac completo.

La intuicion estructural es:

- Dirac combina dos componentes quirales;
- Weyl aísla una de ellas;
- la interaccion debil actua de forma inherentemente quiral.

En el Modelo Estandar, de hecho, el lenguaje de Weyl suele ser el mas limpio para escribir el contenido fermionico antes de la ruptura electrodébil, porque cada multiplete gauge se organiza naturalmente por componentes quirales.

## 5. Majorana

Un fermion de Majorana satisface, en sentido esquematico, una condicion de realidad relativista: el campo coincide con su conjugado de carga.

Esto significa que:

- partícula y antipartícula no son grados de libertad independientes;
- el lenguaje de Majorana es natural en ciertos contextos mas alla del Modelo Estandar;
- la cuestion es especialmente relevante al discutir neutrinos.

La posibilidad de masas de Majorana esta estrechamente conectada con violacion del numero leptonico y con mecanismos como el seesaw. Por eso este lenguaje termina siendo central en varias discusiones modernas.

## 6. Dirac frente a Weyl frente a Majorana

La comparacion pedagogica minima es:

- Dirac: partícula y antipartícula distintas, dos quiralidades organizadas en un espinor completo;
- Weyl: una sola componente quiral;
- Majorana: campo autocongugado, con restriccion fuerte entre partícula y antipartícula.

No conviene ver estas categorias como compartimentos siempre excluyentes en cualquier contexto. Segun la dimension, las simetrias y la estructura gauge, algunas descripciones son mas naturales que otras y ciertas restricciones pueden o no imponerse consistentemente.

## 7. Ejemplo corto de lectura

Si el sector debil del Modelo Estandar distingue entre componentes izquierdas y derechas, entonces el lenguaje de Weyl deja de ser una sofisticacion opcional y se convierte en una forma natural de leer la teoria.

Ese es el puente conceptual hacia el modulo del Modelo Estandar: la quiralidad no esta ahi por gusto algebraico, sino porque la interaccion debil trata de manera distinta a las componentes zurdas y diestras.

## 8. Cuaderno asociado

- `../../Cuadernos/ejemplos/09_bilineales_y_proyectores_quirales.ipynb`: usarlo para fijar la separacion entre componentes zurda y diestra y reforzar la intuicion de proyectores quirales antes de volver al formalismo completo.
- `../../Cuadernos/problemas_resueltos/06_fundamentos_conceptuales.ipynb`: usarlo para reforzar el papel de simetria y estructura de campos.
- `../../Cuadernos/problemas_resueltos/07_relatividad_y_campos.ipynb`: usarlo como apoyo del trasfondo relativista.

## 9. Advertencias utiles

- Quiralidad y helicidad no son equivalentes en general, aunque se alinean en el limite sin masa.
- Weyl no significa simplemente "la mitad de un Dirac" sin mas cuidado conceptual.
- Majorana no es solo una notacion distinta, sino una restriccion fisica fuerte sobre el campo.
- La posibilidad de escribir una masa de Majorana depende de la estructura de cargas y simetrias de la teoria.

## 10. Preguntas de comprobacion

- Que hacen los proyectores quirales.
- Por que el lenguaje de Weyl es tan natural para el Modelo Estandar.
- En que sentido un fermion de Majorana difiere de uno de Dirac.

## 11. Cierre

Quiralidad, Weyl y Majorana forman un bloque conceptual muy fecundo porque conectan algebra de espinores, estructura gauge y fenomenologia real. Dominar este lenguaje hace mucho mas natural entender por que el sector debil es quiral y por que la naturaleza de la masa de los neutrinos sigue siendo una pregunta abierta de primer nivel.

## 12. Referencias y lecturas recomendadas

- Base: Tong, quiralidad y espinores relativistas.
- Complementaria: Peskin y Schroeder, estructura quiral del sector fermionico.
- Profundizacion: textos de QFT y fenomenologia mas alla del Modelo Estandar sobre Weyl y Majorana.


---

## Navegacion del tutorial

[(anterior) Corriente de Dirac y Limite No Relativista](04_corriente_de_dirac_y_limite_no_relativista.md) | [(siguiente) Simetria Gauge Local y Derivada Covariante](../07_gauge_y_qed/01_simetria_gauge_local_y_derivada_covariante.md)