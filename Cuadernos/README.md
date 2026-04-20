# Cuadernos Jupyter

Este directorio reune notebooks de apoyo para el tutorial de Teoria Cuantica de Campos. Su funcion es complementar los documentos en Markdown con ejemplos computacionales, verificaciones simbolicas, ejercicios guiados y problemas resueltos.

## Estructura

- `ejemplos/`: notebooks breves orientados a ilustrar una idea, formula o tecnica.
- `problemas_resueltos/`: notebooks mas largos orientados a resolver ejercicios paso a paso.

## Cobertura actual

### Modulo 00. Prerrequisitos

- problemas resueltos de relatividad especial minima;
- notacion tensorial y convenciones;
- oscilador armonico cuantico;
- simetrias y grupos basicos;
- delta de Dirac y Fourier.

### Modulos 01 a 05 y lectura avanzada

Se añaden notebooks progresivamente para:

- fundamentos conceptuales;
- relatividad y campos;
- accion y simetrias;
- cuantizacion del campo escalar;
- interacciones y perturbaciones;
- modelo estandar como lectura avanzada.

### Modulo 11. QFT, informacion y agujeros negros

Tambien se incorporan cuadernos para:

- entrelazamiento y estados reducidos;
- horizontes y termicidad efectiva;
- radiacion de Hawking y paradoja de la informacion.

## Uso sugerido

Los cuadernos no reemplazan el desarrollo teorico del tutorial. Deben usarse para:

- comprobar identidades y derivaciones;
- explorar casos simples con calculo explicito;
- visualizar relaciones entre magnitudes fisicas;
- practicar con problemas seleccionados.

## Enlace con el tutorial

Cuando un documento teorico cite un cuaderno, conviene indicar explicitamente cual es su funcion. Por ejemplo:

- un notebook de `ejemplos/` puede servir para verificar una identidad, visualizar una relacion o seguir una cuenta corta;
- un notebook de `problemas_resueltos/` puede servir para practicar una derivacion mas larga o revisar una solucion guiada.

Las referencias mas utiles no son solo del tipo "ver notebook X", sino "usar notebook X para comprobar Y".

## Convenciones

- Mantener nombres de archivo numerados y descriptivos.
- Añadir una celda inicial con objetivo, prerequisitos y resultado esperado.
- Preferir notebooks pequeños y enfocados antes que cuadernos demasiado generales.
- Si un notebook depende de librerias externas, documentarlo al inicio.
- Siempre que sea posible, enlazar el notebook con el documento teorico correspondiente del directorio `Tutorial/`.
