# El Lagrangiano del Modelo Estandar

## Proposito

El Lagrangiano del Modelo Estandar es una de las expresiones mas densas y exitosas de toda la fisica teorica moderna. Reune en una sola estructura matematica la interaccion fuerte, la interaccion electrodébil, la dinamica de quarks y leptones, el mecanismo de Higgs y la generacion de masas de fermiones, todo ello dentro de una teoria cuantica de campos renormalizable.

Este documento no pretende derivar el Modelo Estandar desde cero, sino ofrecer una lectura estructural de su lagrangiano para entender de que piezas esta compuesto y por que esas piezas tienen esa forma.

## 1. Vision general

El Modelo Estandar se construye sobre el grupo de gauge

$$
SU(3)_c \times SU(2)_L \times U(1)_Y.
$$

Cada factor del grupo controla un tipo de interaccion y determina el contenido de campos gauge correspondiente:

- $SU(3)_c$ describe la cromodinamica cuantica, con los gluones como bosones de gauge;
- $SU(2)_L \times U(1)_Y$ describe el sector electrodébil antes de la ruptura espontanea de simetria;
- la combinacion adecuada despues de la ruptura deja como simetria no rota a $U(1)_{\text{EM}}$.

Desde un punto de vista estructural, el lagrangiano del Modelo Estandar puede dividirse en cuatro bloques:

1. sector de gauge;
2. sector fermionico;
3. sector de Higgs;
4. sector de Yukawa.

## 2. Sector de gauge

El sector de gauge describe la propagacion de los bosones portadores de las interacciones y, en el caso de teorias no abelianas, tambien sus autoacoplamientos.

Los campos de gauge relevantes son:

- $G_\mu^a$ para $SU(3)_c$;
- $W_\mu^a$ para $SU(2)_L$;
- $B_\mu$ para $U(1)_Y$.

Sus tensores de campo se denotan tipicamente por:

$$
G_{\mu\nu}^a, \qquad W_{\mu\nu}^a, \qquad B_{\mu\nu}.
$$

El termino cinetico general toma la forma

$$
\mathcal{L}_{\text{gauge}}
= -\frac{1}{4}G_{\mu\nu}^a G^{a\,\mu\nu}
  -\frac{1}{4}W_{\mu\nu}^a W^{a\,\mu\nu}
  -\frac{1}{4}B_{\mu\nu} B^{\mu\nu}.
$$

Este bloque codifica dos hechos profundos:

- los bosones de gauge se propagan como campos dinamicos reales;
- en los sectores no abelianos, los propios bosones gauge interactuan entre si porque el tensor de campo contiene terminos no lineales.

Eso es exactamente lo que distingue, por ejemplo, a QCD de una teoria puramente abeliana como la electrodinamica clasica.

## 3. Sector fermionico

El sector fermionico describe quarks y leptones, organizados en generaciones. La estructura quiral del Modelo Estandar es uno de sus rasgos mas llamativos: la interaccion debil no trata igual a fermiones zurdos y diestros.

En particular:

- los fermiones zurdos se agrupan en dobletes de $SU(2)_L$;
- los fermiones diestros son singletes respecto de $SU(2)_L$;
- todos llevan hipercarga apropiada bajo $U(1)_Y$;
- los quarks, ademas, transforman bajo color.

Esquematicamente, los terminos cineticos fermionicos se escriben como

$$
\mathcal{L}_{\text{ferm}}
= i\bar{\psi}\gamma^\mu D_\mu \psi,
$$

donde $D_\mu$ es la derivada covariante que contiene los campos gauge y los acoplamientos correspondientes.

Para los dobletes leptónicos zurdos, por ejemplo, aparece una estructura del tipo

$$
i\bar{L}_i \gamma^\mu D_\mu L_i,
$$

y de forma analoga para quarks y singletes diestros.

## 4. Quiralidad y peculiaridad de la interaccion debil

La naturaleza quiral del sector electrodébil no es un detalle tecnico menor. Es una de las marcas experimentales y conceptuales del Modelo Estandar.

Los bosones $W$ se acoplan solo a fermiones zurdos. Esto significa que:

- la simetria electrodébil distingue entre componentes izquierdas y derechas;
- la paridad no se conserva en la interaccion debil;
- la estructura de representaciones del grupo gauge queda fuertemente restringida.

Esta asimetria es una de las razones por las que no puede escribirse ingenuamente un termino de masa fermionica ordinario manteniendo intacta la simetria gauge electrodébil.

## 5. Sector de Higgs

El campo de Higgs se introduce como un doblete complejo de $SU(2)_L$, tipicamente denotado por

$$
H.
$$

Su sector lagrangiano tiene la forma

$$
\mathcal{L}_{\text{Higgs}}
= (D_\mu H)^\dagger (D^\mu H)
  + m^2 H^\dagger H
  - \lambda (H^\dagger H)^2.
$$

Aunque la notacion de signos puede variar segun convenciones, la idea fisica es la misma: el potencial del Higgs se elige de tal forma que el vacio no este en $H=0$, sino en una configuracion con valor esperado no nulo.

Cuando el campo adquiere un valor esperado en el vacio,

$$
\langle H \rangle \neq 0,
$$

la simetria

$$
SU(2)_L \times U(1)_Y
$$

se rompe espontaneamente a

$$
U(1)_{\text{EM}}.
$$

## 6. Ruptura espontanea de simetria y masas gauge

El mecanismo de Higgs permite que los bosones $W^\pm$ y $Z$ adquieran masa sin introducir terminos de masa a mano que romperian explicitamente la invariancia gauge.

Ese es uno de los logros conceptuales centrales del Modelo Estandar:

- la teoria conserva su estructura gauge fundamental;
- la masa emerge tras elegir un vacio no simetrico;
- el foton permanece sin masa porque corresponde a la simetria electromagnetica no rota.

El valor esperado del Higgs, tipicamente alrededor de

$$
v \approx 246 \text{ GeV},
$$

fija la escala electrodébil.

## 7. Sector de Yukawa

El sector de Yukawa describe como quarks y leptones adquieren masa al acoplarse con el campo de Higgs. Este punto es crucial, porque un termino directo del tipo

$$
m\bar{\psi}\psi
$$

no es compatible, en general, con la simetria $SU(2)_L$ antes de la ruptura espontanea.

Por eso se introducen terminos de Yukawa del tipo

$$
\mathcal{L}_{\text{Yukawa}}
= -Y^d_{ij}\,\bar{Q}_i H d_{jR}
   -Y^u_{ij}\,\bar{Q}_i \tilde{H} u_{jR}
   -Y^e_{ij}\,\bar{L}_i H e_{jR}
   + \text{h.c.},
$$

con

$$
\tilde{H} = i\sigma_2 H^*.
$$

Tras la ruptura espontanea de simetria, estos acoplamientos se convierten efectivamente en masas fermionicas.

## 8. Matrices de masa y mezcla

Las matrices de Yukawa no son, en general, diagonales en el mismo sistema de base para todos los campos. Al diagonalizarlas aparecen:

- las masas fisicas de los fermiones;
- la matriz CKM para la mezcla de quarks;
- la matriz PMNS en extensiones o formulaciones donde se incorporan masas de neutrinos.

Esta estructura explica por que el Modelo Estandar no solo predice particulas, sino tambien mezcla entre generaciones y fenomenos de violacion CP.

## 9. Parametros libres

A pesar de su enorme poder predictivo, el Modelo Estandar no fija todos sus parametros desde primeros principios. Bajo el supuesto de masas de Dirac para neutrinos, suele decirse que la teoria depende de 27 parametros libres introducidos a mano, entre ellos:

- las tres constantes de acoplamiento gauge;
- las masas de quarks y leptones cargados;
- las masas de neutrinos;
- los parametros de mezcla CKM;
- los parametros de mezcla PMNS;
- la masa del Higgs y el valor esperado del vacio;
- el angulo $\bar{\theta}$ de QCD;
- la constante cosmologica, si se la incluye en el inventario global.

Esta lista deja ver tanto la potencia como la limitacion del Modelo Estandar: es extraordinariamente preciso, pero no explica por que esos parametros toman los valores observados.

## 10. Renormalizabilidad y poder predictivo

Una de las razones por las que el Modelo Estandar funciona tan bien es que esta construido como una teoria gauge renormalizable. Eso permite que, una vez fijados sus parametros mediante experimento, una enorme cantidad de procesos pueda calcularse de forma sistematica y compararse con precision extrema.

La renormalizabilidad aqui no es un detalle tecnico secundario. Es parte de la razon por la cual el Modelo Estandar se convirtio en la teoria de referencia para la fisica de particulas no gravitatoria.

## 11. Esquema sintético del lagrangiano

De forma muy resumida, suele pensarse el Lagrangiano del Modelo Estandar como

$$
\begin{aligned}
\mathcal{L}_{\text{SM}}
&= \mathcal{L}_{\text{gauge}}
+ \mathcal{L}_{\text{ferm}}
+ \mathcal{L}_{\text{Higgs}}
+ \mathcal{L}_{\text{Yukawa}}.
\end{aligned}
$$

Este esquema no muestra todos los indices, generaciones y estructuras de grupo, pero si deja clara la arquitectura conceptual de la teoria.

## 12. Preguntas de estudio

- Que papel cumple cada factor del grupo $SU(3)_c \times SU(2)_L \times U(1)_Y$.
- Por que los bosones gauge no abelianos se autoacoplan.
- En que sentido la interaccion debil es quiral.
- Por que los fermiones no reciben masa mediante un termino puesto a mano antes de la ruptura espontanea.
- Como transforma el sector de Yukawa los acoplamientos con Higgs en masas fermionicas efectivas.
- Por que la renormalizabilidad es tan importante para el exito predictivo del Modelo Estandar.

## 13. Cierre

El Lagrangiano del Modelo Estandar no es solo una formula larga. Es la compresion extrema de decadas de intuicion fisica, simetria gauge, estructura cuantica y contraste experimental. Leerlo por bloques permite ver que no es una acumulacion arbitraria de terminos, sino una construccion altamente restringida por los principios de la teoria cuantica de campos.
