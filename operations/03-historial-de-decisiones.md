# Historial de decisiones (lado del servidor y de la web)

> Qué se cambió, cuándo y por qué, con lo medido antes y después cuando se midió. Incluye lo que salió mal: un registro que solo enseña aciertos no es un registro.

## 22-09-2026

- **El contacto no funcionaba.** El botón «Escríbeme» era un `mailto:` y, sin cliente de correo configurado, no pasaba nada al pulsarlo. Ahora abre el correo del sistema, y si en 1,2 s la página sigue teniendo el foco, aparece un panel con los proveedores habituales. La elección se recuerda 90 días, sin texto visible.
- **Una cifra falsa en el `llms.txt`.** Decía «four Python libraries» con **cinco** en la lista. Justo en el fichero que existe para que lo lean las máquinas. Ahora el número se deriva de la lista.
- **Afirmaciones de resultado reescritas como capacidad.** Dos textos prometían que una IA **citaría** al cliente, mientras el caso y la página de experimentos declaraban esa medición pendiente. Se reescribieron: se describe lo que se hace y cómo se mide, no un resultado que nadie controla.
- **Apartados nuevos:** notas con fuentes enlazadas al lado de cada afirmación (tres afirmaciones ancladas), un glosario de 16 términos (14 con `sameAs` comprobado uno a uno; dos sin él, porque un `sameAs` a «algo parecido» afirmaría una identidad falsa), preguntas frecuentes (14) y un inspector público. **Sitemap: de 15 a 21 URLs.**
- **El inspector publica un comando al lado de cada cifra**, para que se pueda comprobar sin fiarse. Ese día el propio comando falló varias veces, y se arregló:
  - el del recuento de palabras devolvía **0**: un patrón voraz se comía el documento entero, que llega en una sola línea;
  - el recuento de nodos JSON-LD publicaba **4 tipos** y su comando devolvía **5** (faltaba un nodo anidado);
  - el de `llms.txt` contaba **caracteres** llamándolos **bytes** (8.312 frente a 8.405).
  Desde entonces, **cada comando publicado se ejecuta y tiene que devolver el número que lleva al lado**.
- **El inspector se protege contra peticiones a redes internas.** Valida el destino antes de conectar, rechaza rangos privados y de bucle, vuelve a validar en cada redirección, y corta a los 8 s o a los 2 MB.
- **Primer contraste del inspector con las recetas del cookbook: 4 de 4.** Más tarde se supo que, para el recuento de palabras, ese contraste se había hecho contra una copia **antigua** de la receta (ver 23-09).

## 23-09-2026

- **Menú fijo y por niveles**, que lleva a páginas y no a anclas de la home. Páginas nuevas de servicios, sobre mí y contacto. **Sitemap: 27 URLs.** Medido por un revisor independiente: **60 `@id`, ninguno mal formado, ninguna página sin `hreflang`**.
- **Home aligerada:** resúmenes que enlazan a cada página. Medido: 4 de 4 fragmentos autocontenidos y 5 de 5 afirmaciones ancladas.
- **Cambio de idioma que mantiene la página**, en vez de devolver a la home.
- **El inspector acepta el dominio escrito de cualquier forma.** El campo era de tipo URL y el propio navegador bloqueaba «ejemplo.com» antes de que llegara al servidor.
- **Un fallo del inspector, corregido:** una web que bloqueaba a todos los agentes con la regla del comodín salía como «8 de 8 permitidos». Ahora sigue la norma RFC 9309 igual que la receta del cookbook, probada en siete casos.
- **Un riesgo en los comandos publicados, corregido:** las URLs iban sin comillas, así que un enlace preparado podía hacer ejecutar algo a quien copiara el comando. Ahora van siempre entre comillas.
- **El inspector pasa a valorar cada comprobación**, con una etiqueta, la regla que la decide y una versión de criterios. Sin nota global. Se descartó a propósito una puntuación de 0 a 10 con decimales: los pesos habrían sido inventados.
  - **v2026.09:** primera versión, revisada contra el cookbook antes de publicarse.
  - **v2026.09.1:** exigencia subida. «Excelente» pasa a significar que no queda nada verificable por mejorar en esa área. No se endurecieron el número de palabras ni la cantidad de `sameAs`, porque ningún dato respalda un listón más alto.
  - **v2026.09.2:** la seguridad del transporte (HSTS) sale de «respuesta» y pasa a ser una comprobación propia. Es seguridad, no legibilidad.
- **El contraste de palabras se rehízo.** La copia de la receta usada el 22-09 era antigua: no convertía en espacio las referencias numéricas como `&#x27;`. El inspector daba 524 y la receta real 526. Se alineó el contador con la receta v0.1.4 real y el nuevo contraste, del **23-09-2026 a las 13:32Z, dio 4 de 4** (526, 9, 8 y 9.484).
- **El inspector encontró defectos en nuestra propia web**, que se dejan a la vista:
  - metadescripción de la home con 252 caracteres (la convención es 120-160);
  - la home sin nodo `WebPage`, y las entidades sin `logo` ni `image`;
  - HSTS sin `includeSubDomains`.
- **v2026.10: exigencia de 10, y con fecha de revisión.** Se cierran los huecos que dejaban sacar «excelente» a páginas incompletas:
  - **indexación:** `noindex`, `nosnippet` y `X-Robots-Tag`. Si la página pide no ser indexada, el informe lo avisa arriba del todo, porque manda sobre todo lo demás;
  - **viewport**;
  - **fechas** de publicación y actualización;
  - **autoría** de los artículos;
  - **propiedades mínimas** de cada tipo de datos estructurados;
  - **enlaces salientes** rotos;
  - **cifras con fuente enlazable**, en el mismo párrafo o en una nota al pie.

  Los criterios llevan ahora **fecha de revisión**: si pasan 45 días sin que nadie los revise contra el estado del campo, el despliegue falla. Se probó rompiéndola: con una fecha de 84 días, la batería de invariantes FALLA. Y dentro del ensayo de despliegue completo, con la fecha a **46 días** (un día por encima del tope), el despliegue **se detiene** (salida 1: «llevan 46 días sin revisar, tope 45»). Restaurada la fecha, pasa.

  Dos defectos del instrumento se cazaron antes de publicar:
  - el `alt` sin valor se contaba como ausencia;
  - las notas al pie no contaban como fuente: la Wikipedia salía con «0 de 3», y el control a mano da 3 de 3.

  Hallazgos nuevos en nuestra propia web: la home no declara fechas, y el BlogPosting de una nota no lleva `image`.
