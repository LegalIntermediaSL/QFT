# Unidades Naturales y Unidades Fisicas

**Nivel:** Fundacional  
**Dificultad:** Baja  
**Tiempo estimado:** 15-20 min  
**Prerequisitos recomendados:** [Notacion Tensorial y Convenciones](02_notacion_tensorial_y_convenciones.md) · [Resumen del modulo](README.md)


## 1. Proposito

En QFT casi todos los textos trabajan en unidades naturales sin advertirlo explicitamente. Este articulo fija el significado exacto de esa convencion, muestra como recuperar las expresiones con unidades fisicas y sirve como referencia rapida para el resto del tutorial.

## 2. El problema de las constantes universales

La fisica fundamental contiene tres constantes que aparecen en practicamente toda expresion:

| Constante | Simbolo | Valor aproximado | Papel fisico |
|---|---|---|---|
| Velocidad de la luz | $c$ | $3 \times 10^8$ m/s | Relaciona espacio y tiempo |
| Constante de Planck reducida | $\hbar$ | $1.055 \times 10^{-34}$ J·s | Escala de accion cuantica |
| Constante de Boltzmann | $k_B$ | $1.38 \times 10^{-23}$ J/K | Relaciona temperatura y energia |

Estas constantes no tienen contenido fisico propio: son factores de conversion entre unidades que los humanos definieron historicamente de forma independiente (metros, segundos, kilogramos, kelvin). En fisica teorica resulta conveniente elegir unidades en las que algunas de estas constantes valgan exactamente uno.

## 3. Unidades naturales en QFT

La convencion estandar en QFT fija

$$
\hbar = c = 1.
$$

Con esta eleccion:

- la velocidad es adimensional (en unidades de $c$);
- la accion es adimensional (en unidades de $\hbar$);
- longitud y tiempo tienen las mismas dimensiones (ambas son inversas de energia o masa);
- energia, masa y momento son interconvertibles.

La unica dimension independiente que queda es **energia** (o equivalentemente, masa). Por convenio se expresa en electronvoltios (eV) o sus multiplos (MeV, GeV, TeV).

## 4. Tabla de equivalencias dimensionales

Con $\hbar = c = 1$:

| Magnitud | Dimension | Ejemplo |
|---|---|---|
| Masa | $[E]$ | $m_e \approx 0.511$ MeV |
| Momento | $[E]$ | $p$ en MeV |
| Energia | $[E]$ | $E$ en MeV o GeV |
| Longitud | $[E]^{-1}$ | $1$ fm $\approx$ $(197$ MeV$)^{-1}$ |
| Tiempo | $[E]^{-1}$ | tiempo en MeV$^{-1}$ |

La relacion de conversion fundamental es

$$
\hbar c \approx 197 \text{ MeV·fm}.
$$

Esta cifra es la que permite pasar de unidades naturales a unidades del SI cuando se necesita una prediccion experimental.

## 5. Ejemplo: el hamiltoniano del oscilador armonico

En unidades fisicas completas el hamiltoniano cuantico del oscilador armonico es

$$
H = \hbar\omega\left(a^\dagger a + \frac{1}{2}\right),
\qquad E_n = \hbar\omega\left(n + \frac{1}{2}\right).
$$

Con $\hbar = 1$ estas expresiones se simplifican a

$$
H = \omega\left(a^\dagger a + \frac{1}{2}\right),
\qquad E_n = \omega\left(n + \frac{1}{2}\right),
$$

que es la forma que aparece en la mayoria de los textos de QFT. La frecuencia $\omega$ tiene dimension de energia en unidades naturales.

De forma analoga, los operadores de subida y bajada en unidades fisicas son

$$
a = \sqrt{\frac{m\omega}{2\hbar}}\,x + \frac{i}{\sqrt{2m\omega\hbar}}\,p,
$$

que con $\hbar = 1$ pasan a ser

$$
a = \sqrt{\frac{m\omega}{2}}\,x + \frac{i}{\sqrt{2m\omega}}\,p.
$$

## 6. Ejemplo: la relacion de conmutacion

En unidades fisicas:

$$
[x, p] = i\hbar.
$$

Con $\hbar = 1$:

$$
[x, p] = i.
$$

Ambas expresiones describen la misma fisica. La segunda es simplemente mas compacta.

## 7. Como recuperar las unidades fisicas

Dado un resultado en unidades naturales, se pueden recuperar las unidades fisicas por analisis dimensional:

1. Identificar la dimension de energia de la expresion: $[E]^n$.
2. Multiplicar por las potencias adecuadas de $\hbar$ y $c$ hasta obtener las unidades SI deseadas.

**Regla practica**: insertar $\hbar$ y $c$ donde el analisis dimensional lo exija.

### Ejemplo

La longitud de onda de Compton del electron en unidades naturales es

$$
\lambda_C = \frac{1}{m_e} \approx \frac{1}{0.511 \text{ MeV}}.
$$

Para recuperar metros:

$$
\lambda_C = \frac{\hbar}{m_e c} \approx \frac{197 \text{ MeV·fm}}{0.511 \text{ MeV}} \approx 386 \text{ fm}.
$$

## 8. Convencion en este tutorial

A lo largo de este tutorial se trabaja con

$$
\hbar = c = 1
$$

salvo indicacion expresa. Cuando una expresion aparezca sin $\hbar$ o sin $c$, debe leerse bajo esta convencion.

En los articulos donde la convencion se aplica por primera vez se indica explicitamente. La referencia canonica es siempre este articulo.

## 9. Cuadro resumen

$$
\boxed{\hbar = c = 1}
$$

| Lo que desaparece | Lo que queda |
|---|---|
| $\hbar$ en relaciones cuanticas | $[x,p] = i$ |
| $c$ en relatividad | $E^2 = \mathbf{p}^2 + m^2$ |
| Factores $\hbar c$ en longitudes | $\lambda \sim 1/E$ |
| Energias en joules | Energias en eV, MeV, GeV |

## 10. Preguntas de comprobacion

- Por que fijar $\hbar = c = 1$ no pierde informacion fisica.
- Como se determina la dimension de una magnitud en unidades naturales.
- Que cifra permite convertir de MeV$^{-1}$ a femtometros.
- Como se recupera $\hbar$ en una expresion dada en unidades naturales.

## 11. Ejercicios sugeridos

1. Convierte la masa del proton ($938$ MeV) a kg usando $\hbar$ y $c$.
2. Expresa la longitud de onda de Compton del proton en fm y en MeV$^{-1}$.
3. Verifica dimensionalmente que $[x,p] = i\hbar$ es consistente con $[x,p] = i$ cuando $\hbar = 1$.
4. Un campo escalar tiene dimension $[E]^1$ en $d=4$. Comprueba que el termino cinetico del lagrangiano es adimensional.
5. Reescribe $E_n = \hbar\omega(n+\tfrac{1}{2})$ en unidades donde $\hbar \neq 1$ a partir de la expresion en unidades naturales, usando solo analisis dimensional.

## 12. Referencias y lecturas recomendadas

- Zee, *Quantum Field Theory in a Nutshell*: apendice sobre convenciones y unidades.
- Peskin & Schroeder, capitulo 1: discusion inicial de unidades naturales en QFT.
- Tong, *Lectures on Quantum Field Theory*: seccion de convenciones al inicio.


---

## Navegacion del tutorial

[(anterior) Algebra de Lie y Representaciones](07_algebra_de_lie_y_representaciones.md) | [(siguiente) Fundamentos Conceptuales](../01_fundamentos_conceptuales/README.md)
