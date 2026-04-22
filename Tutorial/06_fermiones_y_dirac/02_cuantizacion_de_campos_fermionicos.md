# Cuantizacion de Campos Fermionicos

**Nivel:** Nucleo  
**Dificultad:** Media  
**Tiempo estimado:** 25-35 min  
**Prerequisitos recomendados:** [Motivacion y Ecuacion de Dirac](01_motivacion_y_ecuacion_de_dirac.md) · [Resumen del modulo](README.md)


## 1. Proposito

Una vez escrita la ecuacion de Dirac, el siguiente paso es cuantizar el campo fermionico. Esta cuantizacion se parece a la del campo escalar en su estructura general, pero introduce una diferencia decisiva: en lugar de conmutadores aparecen anticonmutadores.

## 2. Campo de Dirac como operador

Al cuantizar, el espinor $\psi(x)$ pasa a ser un operador de campo que puede expandirse en modos positivos y negativos. Esquematicamente:

$$
\psi(x) \sim \int d^3p\left(b(\mathbf{p})u(\mathbf{p})e^{-ip\cdot x} + d^\dagger(\mathbf{p})v(\mathbf{p})e^{ip\cdot x}\right).
$$

Aqui:

- $b(\mathbf{p})$ aniquila una particula fermionica;
- $b^\dagger(\mathbf{p})$ la crea;
- $d(\mathbf{p})$ aniquila una antiparticula;
- $d^\dagger(\mathbf{p})$ la crea.

La estructura formal recuerda a la del campo escalar, pero ya anticipa una diferencia profunda: la estadistica correcta de estos operadores no puede ser bosonica.

## 3. Por que no usar conmutadores ordinarios

Si se cuantizara un campo fermionico con conmutadores ordinarios, aparecerian inconsistencias con:

- positividad de la energia;
- causalidad microfisica;
- teorema espin-estadistica.

La cuantizacion correcta exige relaciones de anticonmutacion del tipo

$$
\{b(\mathbf{p}),b^\dagger(\mathbf{q})\} \propto \delta^{(3)}(\mathbf{p}-\mathbf{q}),
$$

con expresiones analogas para los operadores de antiparticulas.

Con esta eleccion, el Hamiltoniano puede reorganizarse de manera compatible con una interpretacion fisica estable, con contribuciones positivas para particulas y antiparticulas sobre el vacio apropiado.

## 4. Principio de exclusion

De las relaciones de anticonmutacion se sigue una consecuencia crucial:

$$
\left(b^\dagger\right)^2 = 0,
$$

de forma esquematica sobre un mismo modo.

Esto significa que no pueden colocarse dos fermiones identicos en el mismo estado cuantico. El principio de exclusion de Pauli deja de ser una regla externa y pasa a estar incorporado en la algebra del campo.

Ese paso es conceptualmente bellisimo: una propiedad empirica fundamental de la materia se vuelve una consecuencia directa de la estructura algebraica del campo cuantizado.

## 5. Espacio de Fock fermionico

Al igual que en el caso bosonico, se construye un espacio de Fock, pero ahora sus sectores de ocupacion obedecen estadistica de Fermi-Dirac. Cada modo solo puede estar ocupado por cero o una excitacion fermionica por cada conjunto de numeros cuanticos compatibles.

Para un solo modo, la diferencia con el caso bosonico puede resumirse asi:

- bosones: ocupaciones $n = 0,1,2,\dots$;
- fermiones: ocupaciones $n = 0,1$.

Esa diferencia explica por que la materia ordinaria exhibe estructura en capas, presiones de degeneracion y estabilidad colectivas que los bosones no presentan del mismo modo.

## 6. Vacio y antiparticulas

La expansion del campo fermionico muestra con claridad una estructura muy elegante:

- los modos positivos se asocian a particulas;
- los modos negativos se reinterpretan como antiparticulas;
- el vacio del campo sirve de estado base sobre el cual ambas pueden crearse.

Este es el tratamiento moderno que reemplaza la intuicion historica del mar de Dirac.

Comparado con el caso escalar:

- en ambos casos el vacio se define por aniquilacion de los operadores de destruccion;
- en ambos casos aparecen antiparticulas;
- pero solo en el caso fermionico la ocupacion de cada modo queda restringida por anticonmutacion.

## 7. Relacion con el teorema espin-estadistica

La cuantizacion fermionica no es una convencion opcional. Es la forma compatible con:

- espin semientero;
- invarianza de Lorentz;
- microcausalidad;
- positividad de la energia.

Asi, la estadistica fermionica aparece como consecuencia estructural del formalismo relativista cuantico.

Aunque la demostracion rigurosa del teorema espin-estadistica es avanzada, el mensaje central es claro: espin semientero y anticonmutadores no son dos decisiones separadas, sino dos caras de una misma consistencia fisica.

## 8. Anticonmutadores a tiempos iguales

En analogia con los conmutadores canonicos del campo escalar, los campos fermionicos satisfacen relaciones de anticonmutacion a tiempos iguales. Esquematicamente,

$$
\{\psi_\alpha(t,\mathbf{x}), \psi_\beta^\dagger(t,\mathbf{y})\} \propto \delta_{\alpha\beta}\delta^{(3)}(\mathbf{x}-\mathbf{y}).
$$

La forma exacta depende de convenciones, pero la idea importante es que la localidad del campo se codifica directamente en estas relaciones algebraicas.

## 9. Importancia para QED y el Modelo Estandar

Sin esta cuantizacion no podria construirse correctamente:

- la electrodinamica cuantica del electron y el positron;
- la teoria de quarks y leptones;
- la estructura fermionica completa del Modelo Estandar.

## Cuaderno asociado

- Consulta los cuadernos asociados de este bloque en [Resumen del modulo](README.md) para reforzar el capitulo con practica guiada.

## 10. Preguntas de estudio

- Por que un campo fermionico necesita anticonmutadores.
- Como aparecen particulas y antiparticulas en la expansion del campo de Dirac.
- De que manera el principio de exclusion emerge del formalismo.
- Por que el espacio de Fock fermionico difiere del bosonico.

## 11. Ejercicios sugeridos

1. Explica por que la ocupacion doble de un mismo modo fermionico queda prohibida algebraicamente.
2. Compara la expansion modal de un campo escalar con la de un campo de Dirac.
3. Describe por que la cuantizacion correcta de fermiones es inseparable del teorema espin-estadistica.
4. Resume en una frase la diferencia entre vacio bosonico y vacio fermionico.

## 12. Cierre

La cuantizacion de campos fermionicos completa una parte esencial del edificio de la QFT: muestra como los fermiones relativistas y sus antiparticulas encajan de forma natural en un formalismo de campos local, covariante y cuantizado.

## 13. Referencias y lecturas recomendadas

- Base: Srednicki, secciones sobre cuantizacion fermionica.
- Complementaria: Tong, notas sobre campo de Dirac y espacio de Fock fermionico.
- Profundizacion: Peskin y Schroeder, cuantizacion de campos de Dirac y estructura de antiparticulas.


---

## Navegacion del tutorial

[(anterior) Motivacion y Ecuacion de Dirac](01_motivacion_y_ecuacion_de_dirac.md) | [(siguiente) Algebra Gamma y Bilineales de Dirac](03_algebra_gamma_y_bilineales_de_dirac.md)