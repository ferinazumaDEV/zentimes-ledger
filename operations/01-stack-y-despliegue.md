# Stack y despliegue de zentimes.es

> Aporte de la parte de servidor. Descrito sin nombres de máquina, direcciones, rutas ni usuarios: lo que importa es **cómo** se construye y se publica, no **dónde**.

## Qué es la web

- **Next.js con React** (versiones mayores no anotadas a propósito: son una huella), compilada en modo *standalone* (un servidor Node autocontenido) y con CSS plano, sin framework de estilos.
- **Dos idiomas con rutas distintas**: inglés en la raíz (`/`) y español bajo `/es/`. Cada página existe en los dos y se declaran entre sí con `hreflang`, más `x-default`.
- **El contenido vive en ficheros TypeScript**, no en una base de datos ni en un CMS. Cada texto, cada servicio y cada nota está tipado, y el compilador falla si falta una traducción.
- **Un solo registro de páginas** del que se DERIVAN el `sitemap.xml`, el `llms.txt`, las canónicas y los `hreflang`. Nadie los escribe a mano. Hay aserciones de tipos que fallan en la compilación si una ruta del registro no tiene página o si una página no está en el registro.
- **Datos estructurados JSON-LD** con identificadores `@id` estables, de ámbito de sitio (cuelgan del origen) o de página (cuelgan de la canónica). Un `@id` publicado no se renombra nunca.

## Cómo se publica

Un único comando hace todo el recorrido, y cada paso puede pararlo:

1. **Comprobación de tipos** del proyecto entero.
2. **Compilación** de producción.
3. **Arranque local del resultado compilado** y ejecución de la batería de invariantes (ver `02-guardas.md`) **contra ese servidor local**, no contra la web publicada. Si algo falla, no se publica nada.
4. **Empaquetado** y envío a la máquina que sirve la web, por un canal cifrado.
5. **Comprobación del paquete** en destino antes de tocar nada.
6. **Intercambio reversible**: la versión nueva se extrae al lado de la vigente, se comprueba que tiene lo imprescindible (servidor, estáticos, ficheros públicos) y se intercambian. La anterior queda guardada.
7. **Espera de un 200 real** en `/`, `/sitemap.xml` y `/llms.txt`. No basta con que el proceso arranque.
8. **Vuelta atrás en un paso** si hace falta: el mismo comando con `--rollback` restaura la versión anterior.

También hay un **modo ensayo** (`--dry-run`) que hace los pasos 1 a 3 sin tocar la web publicada.

## Por qué así

- **Derivar en vez de escribir a mano** porque en un solo día (22-09-2026) aparecieron cuatro casos de «dato corregido en un sitio y olvidado en otro»: el titular corregido y la metadescripción no, un recuento arreglado y su lista de tipos no… Un dato no vive donde se escribe; vive en la página, en la metadescripción, en `og:`, en el JSON-LD, en el `llms.txt` y en el comando que lo reproduce.
- **Verificar contra el build local y no contra producción** porque un «0 FAIL» leído sin mirar el destino llegó a validar la web vieja en lugar de la nueva.
