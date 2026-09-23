# Qué puede comprobar un cliente por su cuenta

> Todo lo de esta lista se comprueba desde fuera, sin acceso a nada nuestro y sin fiarse de nuestra palabra.

1. **Que el inspector dice lo mismo que la receta.** Cada métrica del inspector que corresponde a una receta del cookbook lleva su identificador (`words_visible_no_js`, `typed_entities`, `ai_user_agents_allowed`, `llms_txt_bytes`) en el HTML como `data-metric` y `data-value`. Se pasa la receta de la versión indicada sobre la misma URL y los números tienen que cuadrar. Si no cuadran, el inspector está mal, no la receta.
2. **Que cada comando publicado reproduce su cifra.** Al lado de cada dato hay un comando `curl`. Se copia, se ejecuta y tiene que salir el mismo número. Si no sale, es un error nuestro.
3. **Que las reglas de valoración son las publicadas.** Cada etiqueta lleva escrita la regla que la decide y la versión de los criterios. Se puede comprobar a mano que la página cumple, o no, lo que la regla dice.
4. **Que los criterios no se cambian a escondidas.** El historial de criterios está en la página del inspector. Una etiqueta puede cambiar sin que cambie la web, y cuando pasa, el historial dice qué regla cambió y por qué.
5. **Que la web cumple lo que predica.** El inspector se puede pasar sobre zentimes.es. Hoy no saca «excelente» en todo, y los motivos están en el historial.
6. **Que las fuentes existen.** Las afirmaciones de las notas y las preguntas frecuentes enlazan a su fuente; los `sameAs` del glosario se comprobaron uno a uno. Cualquiera puede abrirlos.
7. **Que no se promete lo que no se mide.** Ninguna página afirma que una IA vaya a citar a nadie, y el inspector lo dice explícitamente: ninguna comprobación mide citación.
