# Cuantizacion de Campos Fermionicos

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

## 4. Principio de exclusion

De las relaciones de anticonmutacion se sigue una consecuencia crucial:

$$
\left(b^\dagger\right)^2 = 0,
$$

de forma esquematica sobre un mismo modo.

Esto significa que no pueden colocarse dos fermiones identicos en el mismo estado cuantico. El principio de exclusion de Pauli deja de ser una regla externa y pasa a estar incorporado en la algebra del campo.

## 5. Espacio de Fock fermionico

Al igual que en el caso bosonico, se construye un espacio de Fock, pero ahora sus sectores de ocupacion obedecen estadistica de Fermi-Dirac. Cada modo solo puede estar ocupado por cero o una excitacion fermionica por cada conjunto de numeros cuanticos compatibles.

## 6. Vacio y antiparticulas

La expansion del campo fermionico muestra con claridad una estructura muy elegante:

- los modos positivos se asocian a particulas;
- los modos negativos se reinterpretan como antiparticulas;
- el vacio del campo sirve de estado base sobre el cual ambas pueden crearse.

Este es el tratamiento moderno que reemplaza la intuicion historica del mar de Dirac.

## 7. Relacion con el teorema espin-estadistica

La cuantizacion fermionica no es una convencion opcional. Es la forma compatible con:

- espin semientero;
- invarianza de Lorentz;
- microcausalidad;
- positividad de la energia.

Asi, la estadistica fermionica aparece como consecuencia estructural del formalismo relativista cuantico.

## 8. Importancia para QED y el Modelo Estandar

Sin esta cuantizacion no podria construirse correctamente:

- la electrodinamica cuantica del electron y el positron;
- la teoria de quarks y leptones;
- la estructura fermionica completa del Modelo Estandar.

## 9. Preguntas de estudio

- Por que un campo fermionico necesita anticonmutadores.
- Como aparecen particulas y antiparticulas en la expansion del campo de Dirac.
- De que manera el principio de exclusion emerge del formalismo.
- Por que el espacio de Fock fermionico difiere del bosonico.

## 10. Ejercicios sugeridos

1. Explica por que la ocupacion doble de un mismo modo fermionico queda prohibida algebraicamente.
2. Compara la expansion modal de un campo escalar con la de un campo de Dirac.
3. Describe por que la cuantizacion correcta de fermiones es inseparable del teorema espin-estadistica.

## 11. Cierre

La cuantizacion de campos fermionicos completa una parte esencial del edificio de la QFT: muestra como los fermiones relativistas y sus antiparticulas encajan de forma natural en un formalismo de campos local, covariante y cuantizado.
