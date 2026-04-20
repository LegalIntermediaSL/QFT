# Origen de las Divergencias y Regularizacion

## 1. Proposito

Uno de los rasgos mas sorprendentes de la QFT perturbativa es la aparicion de integrales divergentes. Este documento explica de donde salen y por que la regularizacion es el primer paso necesario para tratarlas con cuidado.

## 2. Donde aparecen las divergencias

Las divergencias ultravioletas suelen aparecer en diagramas con lazos, donde hay que integrar sobre momentos internos arbitrariamente grandes:

$$
\int \frac{d^4k}{(2\pi)^4}F(k).
$$

Si la funcion $F(k)$ no decrece lo suficiente, la integral diverge.

## 3. Significado fisico

Estas divergencias no significan simplemente que la teoria sea absurda. Mas bien indican que la teoria explora contribuciones de todas las escalas y que la relacion entre parametros desnudos y observables fisicos es mas sutil de lo que parece a nivel clasico.

## 4. Regularizacion

Regularizar significa introducir un procedimiento temporal que haga finitas las expresiones divergentes. Entre los esquemas mas comunes estan:

- cutoff ultravioleta;
- regularizacion dimensional;
- esquemas con masa auxiliar o reguladores adicionales.

### Regularización Dimensional (DimReg)
Es el método preferido en la física moderna porque, a diferencia del cutoff, preserva la **invariancia gauge** y las simetrías de Lorentz.

- **Idea central**: Evaluar las integrales en $d = 4 - \epsilon$ dimensiones espaciales, donde $d$ es un número complejo.
- **Ventaja**: Las divergencias ultravioletas se manifiestan como polos en $\epsilon$ (términos proporcionales a $1/\epsilon$).
- **Constante de escala**: Para mantener las dimensiones correctas de las constantes de acoplamiento, se introduce una escala de masa arbitraria $\mu$.

La regularización no es todavia la renormalizacion. Es el paso que vuelve las expresiones manipulables.

## 5. Preguntas de estudio

- Por que los lazos introducen integrales ultravioletas.
- Que significa regularizar una integral divergente.
- Por que regularizacion y renormalizacion no son exactamente lo mismo.

## 6. Cierre

La regularizacion es el primer gesto de disciplina matematica frente a las divergencias. No resuelve por si sola el problema, pero permite formularlo de manera controlada.
