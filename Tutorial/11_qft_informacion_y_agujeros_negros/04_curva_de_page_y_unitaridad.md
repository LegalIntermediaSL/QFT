# Curva de Page y Unitaridad

**Nivel:** Avanzado  
**Dificultad:** Alta  
**Tiempo estimado:** 18-25 min  
**Prerequisitos recomendados:** [Efecto Unruh y Vacio de Rindler](03_efecto_unruh_y_vacio_de_rindler.md) · [Resumen del modulo](README.md)


## 1. Proposito

Este documento profundiza en una de las formas modernas de formular la paradoja de la informacion: la curva de Page, que organiza como deberia evolucionar la entropia de la radiacion si la evaporacion de un agujero negro fuera unitaria.

Su valor pedagogico es enorme porque traduce una discusion abstracta sobre informacion y gravedad cuantica a una pregunta mucho mas concreta: que forma deberia tener la entropia de la radiacion si la evolucion global no pierde informacion.

## 2. La tension basica

Si la radiacion de Hawking fuera perfectamente termica durante todo el proceso, la entropia de la radiacion exterior seguiria creciendo sin reflejar recuperacion de informacion. Eso parece incompatible con una evolucion unitaria global.

La version ingenua del calculo semiclasico sugiere precisamente ese crecimiento monotono. Por eso la paradoja no se formula solo como una intuicion filosofica, sino como una tension cuantitativa entre termicidad efectiva y unitaridad.

## 3. La idea de la curva de Page

La curva de Page describe de forma esquematica la entropia de entrelazamiento de la radiacion emitida a medida que avanza la evaporacion:

- primero crece;
- alcanza un maximo alrededor del llamado tiempo de Page;
- despues decrece si la informacion total se preserva.

Este comportamiento contrasta con la prediccion semiclasica ingenua de crecimiento monotono.

Si se denota por $S_{\mathrm{rad}}(t)$ la entropia de entrelazamiento de la radiacion exterior, la idea cualitativa puede resumirse como

$$
S_{\mathrm{rad}}(t) \uparrow \quad \text{para } t < t_{\mathrm{Page}},
$$

$$
S_{\mathrm{rad}}(t) \downarrow \quad \text{para } t > t_{\mathrm{Page}},
$$

en una evolucion globalmente unitaria idealizada.

## 4. Por que importa

La curva de Page traduce la paradoja a una pregunta muy precisa:

- o bien la semiclasica falla en algun punto relevante;
- o bien la unitaridad se sacrifica;
- o bien la recuperacion de informacion esta codificada en correlaciones sutiles no capturadas por una lectura termica ingenua.

Eso vuelve el problema mucho mas agudo. Ya no basta con decir que "quizas la informacion se conserva de alguna forma". Hay que explicar como aparece una curva compatible con esa conservacion.

## 5. Unitaridad y descripcion efectiva

La nocion de unitaridad no exige que un subsistema parcial siempre parezca puro. Lo que exige es que el estado global completo evolucione de forma unitaria.

Por eso la clave no es solo estudiar la radiacion como sistema aislado, sino entender:

- que parte del sistema global estamos trazando;
- como evoluciona el entrelazamiento;
- que parte de la termicidad es solo efectiva.

En este lenguaje, el tiempo de Page marca aproximadamente el momento en que la entropia de la radiacion deja de crecer como en una descripcion termica ingenua y empieza a reflejar que la informacion no puede perderse para siempre si el estado global completo sigue siendo puro.

## 6. Lectura con sistemas bipartitos

Una intuicion muy util viene de pensar en un sistema puro dividido en dos subsistemas. Al principio, cuando la radiacion emitida es pequeña, su entropia puede crecer porque esta muy entrelazada con el agujero negro remanente. Pero a medida que la radiacion se convierte en el subsistema mayoritario, la compatibilidad con pureza global obliga a que esa entropia deje de crecer indefinidamente.

Esta es la raiz de la curva de Page: la entropia de un subsistema de un estado puro no puede comportarse arbitrariamente.

## 7. Puente hacia holografia

La curva de Page se ha vuelto central porque conecta la paradoja con ideas holograficas y con desarrollos modernos sobre superficies extremales, islas y reconstruccion de informacion.

No hace falta entrar aqui en toda esa maquinaria. Basta reconocer que:

- la curva de Page ofrece una prueba conceptual muy exigente;
- la holografia sugiere que la unitaridad debe preservarse;
- la descripcion semiclasica ingenua necesita refinarse.

## 8. Ejemplo corto de lectura

Si la entropia de la radiacion creciera para siempre, incluso cuando el agujero negro ya casi se hubiera evaporado por completo, eso seria una fuerte señal de tension con la unitaridad global. La curva de Page resume justamente esta intuicion en una forma cuantitativa idealizada.

Por eso se ha convertido en una especie de test minimo de cualquier propuesta seria para resolver la paradoja de la informacion.

## 9. Cuaderno asociado

- `../../Cuadernos/problemas_resueltos/12_qft_informacion_y_agujeros_negros.ipynb`: usarlo para reforzar la relacion entre termicidad efectiva, entrelazamiento y paradoja de la informacion.

## 10. Advertencias utiles

- La curva de Page es una herramienta conceptual poderosa, no una derivacion completa por si sola.
- Unitaridad global no implica pureza del subsistema radiacion en cada etapa.
- La discusion moderna mezcla QFT, gravedad semiclasica y, en muchos casos, ideas holograficas.
- El tiempo de Page debe entenderse como una escala conceptual de cambio en la estructura del entrelazamiento, no solo como un numero aislado.

## 11. Preguntas de comprobacion

- Que comportamiento cualitativo predice la curva de Page.
- Por que ese comportamiento es relevante para la paradoja de la informacion.
- Como se relaciona la curva de Page con la exigencia de unitaridad global.

## 12. Cierre

La curva de Page vuelve cuantitativa una de las intuiciones mas profundas de la gravedad cuantica contemporanea: si la evaporacion de un agujero negro es compatible con la unitaridad, la entropia de la radiacion no puede crecer para siempre. Entender esta idea prepara de forma natural la entrada a islas, entropia generalizada y reconstruccion holografica.

## 13. Referencias y lecturas recomendadas

- Base: reseñas pedagogicas sobre la curva de Page y paradoja de la informacion.
- Complementaria: revisiones modernas sobre islas, entropia y recuperacion de informacion.
- Profundizacion: textos de holografia y gravedad cuantica semiclasica.


---

## Navegacion del tutorial

[(anterior) Efecto Unruh y Vacio de Rindler](03_efecto_unruh_y_vacio_de_rindler.md) | [(siguiente) Islas y entropia generalizada](05_islas_y_entropia_generalizada.md)