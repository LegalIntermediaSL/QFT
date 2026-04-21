# Convenciones Globales del Tutorial

Este apendice resume las decisiones editoriales y tecnicas que conviene asumir por defecto en todo el repositorio. Su objetivo no es sustituir al glosario de notacion, sino servir como referencia comun para lectura, escritura y revision de capitulos.

La utilidad de este documento es practica: cuando un tutorial crece, las convenciones inconsistentes generan confusiones innecesarias en signos, factores de normalizacion, indices o notacion de Fourier. Tener un marco comun reduce mucho ese ruido.

## 1. Metrica y espacio-tiempo

- Convencion por defecto: metrica de firma $(+,-,-,-)$.
- Cuatro-vectores: $x^\mu = (t,\mathbf{x})$, $p^\mu = (E,\mathbf{p})$.
- Producto escalar: $p\cdot x = p_\mu x^\mu = Et - \mathbf{p}\cdot \mathbf{x}$.

Si un documento usa una firma distinta, debe declararlo de forma explicita al comienzo. Esta es una de las convenciones mas sensibles a errores de signo, asi que conviene repetirla localmente cuando una derivacion la use de forma critica.

## 2. Unidades

- Convencion por defecto: unidades naturales $c=\hbar=1$.
- En estas unidades, masa, energia e inversa de longitud o tiempo comparten dimension.

Si un capitulo necesita restaurar constantes para claridad fisica, debe decirlo explicitamente. En textos introductorios esto puede ser util cuando se quiere reconectar con intuiciones dimensionales previas.

## 3. Indices

- Indices griegos $\mu,\nu,\rho,\dots$: componentes de espacio-tiempo.
- Indices latinos $i,j,k,\dots$: componentes espaciales o etiquetas discretas segun contexto.
- Indices de grupo, color, sabor o generacion deben explicitarse cuando aparezcan por primera vez en un documento.

Cuando un capitulo use muchos tipos de indices simultaneamente, conviene incluir una breve frase recordatoria. Eso mejora mucho la legibilidad sin recargar la exposicion.

## 4. Fourier y medidas

Por defecto se privilegian convenciones compatibles con QFT relativista:

$$
\phi(x) = \int \frac{d^4p}{(2\pi)^4} e^{-ip\cdot x}\tilde{\phi}(p).
$$

En expansiones modales relativistas es habitual usar medidas del tipo

$$
\int \frac{d^3p}{(2\pi)^3}\frac{1}{\sqrt{2E_{\mathbf p}}}.
$$

Si un documento usa otra normalizacion, debe indicarlo. Este punto es importante porque pequeñas diferencias de convencion cambian factores de $2\pi$, normalizacion de estados y forma de propagadores.

## 5. Espinores y matrices gamma

- Algebra de Clifford: $\{\gamma^\mu,\gamma^\nu\} = 2\eta^{\mu\nu}$.
- Adjunto de Dirac: $\bar{\psi} = \psi^\dagger \gamma^0$.
- Cuando aparezcan $\gamma^5$, $\sigma^{\mu\nu}$ o proyectores quirales, conviene recordarlos en el mismo documento si son centrales para la exposicion.

La base concreta de las matrices gamma puede variar de un texto a otro. Si una derivacion depende de forma visible de usar base de Dirac o base quiral, esa eleccion debe explicitarse localmente.

## 6. Convenciones de propagadores y prescripcion causal

Cuando se use el propagador de Feynman, la prescripcion $i\epsilon$ debe mantenerse visible al menos la primera vez que aparezca en cada documento tecnico importante. Esto evita perder la interpretacion causal del objeto.

Tambien es buena practica no ocultar demasiado pronto la dependencia en el momento o la masa, sobre todo en capitulos pedagogicos donde el lector todavia esta aprendiendo a reconocer la estructura del propagador.

## 7. Criterios editoriales comunes

Cada documento tecnico deberia intentar incluir:

- objetivo;
- prerequisitos implicitos o explicitos;
- idea fisica antes del formalismo;
- al menos una advertencia o error frecuente cuando el tema lo pida;
- preguntas de comprobacion o de estudio;
- referencias y lecturas recomendadas.

Estas pautas no son una camisa de fuerza, pero ayudan mucho a que el tutorial mantenga una voz pedagogica uniforme.

## 8. Relacion con cuadernos

Cuando exista un cuaderno asociado, el documento teorico deberia decir para que sirve:

- comprobar una identidad;
- explorar un ejemplo simbolico;
- resolver un problema guiado;
- revisar una cuenta tipo.

No basta con listar el notebook: conviene indicar su uso pedagogico. Eso facilita que el lector sepa si el cuaderno es complemento conceptual, practica de calculo o apoyo computacional.

## 9. Cuándo repetir una convención localmente

Aunque exista este apendice, conviene repetir una convención dentro del propio documento cuando:

- afecta signos sensibles;
- cambia respecto de la convención global;
- es indispensable para seguir una derivacion concreta.

En otras palabras, este apendice sirve como base comun, pero no elimina la responsabilidad local de hacer legible una derivacion delicada.

## 10. Relacion con otros apendices

- [Glosario de notacion](glosario_notacion.md): definiciones compactas de simbolos y objetos frecuentes.
- [Plantilla editorial de capitulo](plantilla_de_capitulo.md): estructura sugerida para escribir nuevos documentos.

## 11. Cierre

Las convenciones no son un simple detalle editorial. En un tutorial tecnico amplio, funcionan como infraestructura silenciosa: cuando estan bien fijadas, el lector puede concentrarse en la fisica; cuando cambian sin aviso, los errores de signo y normalizacion se multiplican. Este apendice existe para mantener esa infraestructura visible y estable.

---
[Volver a Apendices](README.md)
