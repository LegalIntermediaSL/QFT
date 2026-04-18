# Diagramas de Feynman y Reglas de Calculo

## 1. Introduccion

Los diagramas de Feynman son una de las representaciones visuales mas famosas de la fisica, pero su sentido real suele malinterpretarse. No son dibujitos de trayectorias microscopicas. Son una notacion compacta para terminos de la expansion perturbativa de amplitudes.

## 2. De la serie formal al diagrama

Al expandir la matriz $S$ en la serie de Dyson aparecen productos temporales de campos. Al evaluar sus elementos de matriz, esos productos se reorganizan mediante contracciones y propagadores. El resultado puede codificarse en diagramas.

Cada diagrama representa:

- cierto patron de contracciones;
- un orden determinado en el acoplamiento;
- una contribucion precisa a la amplitud.

## 3. Ingredientes basicos

En un diagrama aparecen tres elementos fundamentales:

- lineas externas, asociadas a estados iniciales y finales;
- lineas internas, asociadas a propagadores;
- vertices, asociados a inserciones del termino de interaccion.

Esta sintaxis visual permite leer de un vistazo la estructura combinatoria del calculo.

## 4. Propagador

El propagador no debe interpretarse ingenuamente como la trayectoria clasica de una particula virtual. Es una funcion de Green del operador cinetico libre, y en espacio de momentos para un campo escalar libre toma la forma tipica

$$
\frac{i}{p^2 - m^2 + i\epsilon}.
$$

Ese factor aparece cada vez que una linea interna transporta momento entre vertices.

## 5. Vertices e interaccion

Un vertice codifica la estructura local de la interaccion. En una teoria $\phi^4$, por ejemplo, un vertice conecta cuatro lineas del campo. El factor asociado depende de la normalizacion elegida, pero esquematicamente esta controlado por el acoplamiento $\lambda$.

De nuevo, el diagrama no inventa la interaccion: la traduce desde la lagrangiana.

## 6. Conservacion del momento

En cada vertice aparece una delta de Dirac que impone conservacion del momento:

$$
(2\pi)^4\delta^{(4)}\left(\sum p_{\text{entrantes}} - \sum p_{\text{salientes}}\right).
$$

Esto refleja la invariancia traslacional de la teoria y conecta el calculo diagramatico con el teorema de Noether.

## 7. Lazos y momentos internos

Cuando un diagrama contiene lazos cerrados, aparecen momentos internos no fijados por las condiciones externas. Debe integrarse sobre ellos:

$$
\int \frac{d^4k}{(2\pi)^4}.
$$

Es justamente aqui donde suelen nacer las divergencias ultravioletas y donde la renormalizacion se vuelve necesaria.

## 8. Arboles y lazos

Conviene distinguir:

- diagramas de arbol, sin lazos, que suelen dar la contribucion dominante a orden mas bajo;
- diagramas con lazos, que incorporan correcciones cuanticas de orden superior.

Esta distincion no es solo topologica. Marca tambien el paso desde efectos basicos de interaccion hacia correcciones radiativas propiamente cuanticas.

## 9. Procedimiento practico de lectura

Al ver un diagrama, una rutina util es:

1. identificar las lineas externas y el proceso considerado;
2. contar vertices para conocer el orden del acoplamiento;
3. asignar propagadores a las lineas internas;
4. imponer conservacion del momento en cada vertice;
5. integrar sobre momentos internos independientes;
6. sumar todos los diagramas del mismo orden compatibles con el proceso.

## 10. Lo que un diagrama no es

Conviene insistir en varios puntos:

- no es la foto de particulas chocando como bolitas;
- no es una cronologia literal del proceso cuantico;
- no es por si solo una probabilidad observable;
- no reemplaza las reglas analiticas: las resume.

## 11. Poder conceptual de la representacion

Pese a estas advertencias, los diagramas son extraordinarios porque permiten:

- organizar calculos largos;
- visualizar canales posibles de interaccion;
- clasificar rapidamente ordenes perturbativos;
- detectar lazos, subdiagramas y origen de divergencias.

Por eso su valor no es solo estetico ni pedagogico: es tambien computacional.

## 12. Preguntas de control

- Que representa exactamente una linea interna.
- De donde sale el propagador escalar.
- Que informacion fisica y algebraica codifica un vertice.
- Por que los lazos obligan a integrar sobre momentos internos.
- Que distingue una amplitud de la interpretacion visual ingenua del diagrama.

## 13. Cierre

Los diagramas de Feynman son la gramatica visual de la teoria de perturbaciones. Entendidos correctamente, muestran como la estructura local de la lagrangiana se convierte en reglas sistematicas para calcular amplitudes observables.
