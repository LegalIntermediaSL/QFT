# Convenciones Globales del Tutorial

Este apendice resume las decisiones editoriales y tecnicas que conviene asumir por defecto en todo el repositorio. Su objetivo no es sustituir al glosario de notacion, sino servir como referencia comun para lectura, escritura y revision de capitulos.

## 1. Metrica y espacio-tiempo

- Convencion por defecto: metrica de firma $(+,-,-,-)$.
- Cuatro-vectores: $x^\mu = (t,\mathbf{x})$, $p^\mu = (E,\mathbf{p})$.
- Producto escalar: $p\cdot x = p_\mu x^\mu = Et - \mathbf{p}\cdot \mathbf{x}$.

Si un documento usa una firma distinta, debe declararlo de forma explicita al comienzo.

## 2. Unidades

- Convencion por defecto: unidades naturales $c=\hbar=1$.
- En estas unidades, masa, energia e inversa de longitud o tiempo comparten dimension.

Si un capitulo necesita restaurar constantes para claridad fisica, debe decirlo explicitamente.

## 3. Indices

- Indices griegos $\mu,\nu,\rho,\dots$: componentes de espacio-tiempo.
- Indices latinos $i,j,k,\dots$: componentes espaciales o etiquetas discretas segun contexto.
- Indices de grupo, color, sabor o generacion deben explicitarse cuando aparezcan por primera vez en un documento.

## 4. Fourier y medidas

Por defecto se privilegian convenciones compatibles con QFT relativista:

$$
\phi(x) = \int \frac{d^4p}{(2\pi)^4} e^{-ip\cdot x}\tilde{\phi}(p).
$$

En expansiones modales relativistas es habitual usar medidas del tipo

$$
\int \frac{d^3p}{(2\pi)^3}\frac{1}{\sqrt{2E_{\mathbf p}}}.
$$

Si un documento usa otra normalizacion, debe indicarlo.

## 5. Espinores y matrices gamma

- Algebra de Clifford: $\{\gamma^\mu,\gamma^\nu\} = 2\eta^{\mu\nu}$.
- Adjunto de Dirac: $\bar{\psi} = \psi^\dagger \gamma^0$.
- Cuando aparezcan $\gamma^5$, $\sigma^{\mu\nu}$ o proyectores quirales, conviene recordarlos en el mismo documento si son centrales para la exposicion.

## 6. Convenciones de propagadores y prescripcion causal

Cuando se use el propagador de Feynman, la prescripcion $i\epsilon$ debe mantenerse visible al menos la primera vez que aparezca en cada documento tecnico importante. Esto evita perder la interpretacion causal del objeto.

## 7. Criterios editoriales comunes

Cada documento tecnico deberia intentar incluir:

- objetivo;
- prerequisitos implicitos o explicitos;
- idea fisica antes del formalismo;
- al menos una advertencia o error frecuente cuando el tema lo pida;
- preguntas de comprobacion o de estudio;
- referencias y lecturas recomendadas.

## 8. Relacion con cuadernos

Cuando exista un cuaderno asociado, el documento teorico deberia decir para que sirve:

- comprobar una identidad;
- explorar un ejemplo simbolico;
- resolver un problema guiado;
- revisar una cuenta tipo.

No basta con listar el notebook: conviene indicar su uso pedagógico.

## 9. Cuándo repetir una convención localmente

Aunque exista este apendice, conviene repetir una convención dentro del propio documento cuando:

- afecta signos sensibles;
- cambia respecto de la convención global;
- es indispensable para seguir una derivación concreta.

## 10. Relacion con otros apendices

- [Glosario de notacion](glosario_notacion.md): definiciones compactas de simbolos y objetos frecuentes.
- [Plantilla editorial de capitulo](plantilla_de_capitulo.md): estructura sugerida para escribir nuevos documentos.

---
[Volver a Apendices](README.md)
