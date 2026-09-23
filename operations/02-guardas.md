# Las guardas: qué se comprueba antes de publicar

> Cada despliegue de zentimes.es pasa por una batería de invariantes que se ejecuta **contra el build local** antes de subir nada. Si falla cualquiera, no se publica. Aquí va qué comprueba cada una y **qué la rompe**, porque una guarda que nunca se ha visto fallar no vale.

## La lista de páginas no se escribe a mano

La batería **no lleva lista de páginas**. La saca del propio `sitemap.xml`, que a su vez sale del registro de páginas. Antes tenía la lista escrita a mano: una página nueva se quedaba fuera sin que nadie lo notara, y una rama por defecto la daba por buena. Ahora cualquier ruta que no encaje es un FAIL.

## Los nueve invariantes

| # | Qué comprueba | Qué lo rompe |
|---|---|---|
| 1 | `/llms.txt` está vivo y contiene **todas** las URLs del sitemap | una página nueva que no llega al `llms.txt` |
| 2 | JSON-LD de **entidad** en las dos homes: Person, ProfessionalService, WebSite y PostalAddress, con `@id` y `sameAs` | perder un nodo o un identificador en uno de los dos idiomas |
| 3 | `robots.txt` permite **explícitamente** a los agentes de IA de la lista | un bloqueo, o que un agente deje de estar nombrado |
| 4 | el sitemap declara lo que tiene que declarar | páginas que faltan, o que sobran |
| 5 | canónica y `hreflang` de cada página, contrastadas con el sitemap | una canónica que no coincide con su `<loc>`, o un idioma sin pareja |
| 6 | la palabra «agencia» no aparece | Zentimes es una marca personal, y la batería lo hace cumplir |
| 7 | la raíz es inglés, el español vive en `/es/` y las URLs públicas no se rompen; los títulos esperados **se derivan** del contenido, no se escriben a mano | mover una ruta publicada, o cambiar un título sin que cambie lo que se espera de él |
| 8 | `og:image` en toda página: presente, absoluta y **sirviéndose de verdad** (200) | una imagen que se declara pero no existe |
| 9 | toda página importante es **alcanzable** desde su home | una página huérfana (pasó: se detectó y se enlazó desde el pie) |

## Dos guardas extra

- **Paridad de identificadores de servicio en inglés y español.** Los `@id` de los servicios tienen que ser idénticos en los dos idiomas. Si un idioma renombra uno, falla.
- **Caducidad de la equivalencia con el cookbook.** El inspector de la web afirma que sus métricas coinciden con las recetas del cookbook, **con fecha y versión**. Si esa fecha envejece más de 120 días, la batería falla: una afirmación de equivalencia que nadie revalida se vuelve falsa sin que nadie toque una línea.

## Lo que aprendimos de las guardas, con fecha

- **22-09-2026 — una guarda que no se ejecutaba.** La guarda de paridad EN/ES se escribió por la mañana y se probó rompiéndola en ese momento. Horas después había quedado **detrás de un `exit 0`**, así que no se ejecutaba nunca, y desde fuera tenía la misma cara que una que siempre pasa. Se movió, y se volvió a probar rompiéndola **en el sitio donde vive**.
- **22-09-2026 — una comparación que pasaba por casualidad.** La comprobación de títulos comparaba contra un literal. El título español coincidía; el inglés no, por `&` frente a `&amp;`. El español pasaba solo porque no llevaba ningún `&`. Ahora los títulos esperados se derivan del contenido y se desescapan antes de comparar.
- **La regla que sale de ahí:** una comprobación se da por buena solo después de haberla visto fallar, ya integrada en su sitio.
