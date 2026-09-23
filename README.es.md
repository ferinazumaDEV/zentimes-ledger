<!-- Mirror of README.md as of 2026-09-23 (same facts, Spanish wording). -->
# zentimes.es — registro público del trabajo

[English](README.md) · **Español**

**Autor:** Fernando Aporta Franco ([ferinazumaDEV](https://github.com/ferinazumaDEV) / [Zentimes](https://zentimes.es))
**Inicio:** 2026-09-23 · **Instrumentos:** The GEO Cookbook v0.1.4 ([tag](https://github.com/ferinazumaDEV/generative-engine-optimization-cookbook/releases/tag/v0.1.4), DOI [10.5281/zenodo.22890558](https://doi.org/10.5281/zenodo.22890558)) y el inspector público de la web

## Qué es este repositorio

Un **registro público, fechado y reproducible** del trabajo hecho en <https://zentimes.es>: qué se midió en las
páginas públicas, con qué instrumento, en qué fecha (UTC) y con qué comando se obtiene el mismo número; los
reglamentos que el inspector público de la web ha impreso, capturados literalmente con su versión; y la
descripción, desde el lado de operaciones, de cómo se construye, despliega y guarda la web, más las decisiones
tomadas con sus cifras de antes y después. Los errores se registran con el mismo detalle que los arreglos: un
registro que solo enseña aciertos no es un registro.

Cada número lleva tres compañeros: su **fecha y hora**, su **instrumento** (una ruta de receta del cookbook
v0.1.4, el inspector con su versión de criterios, o un guion de biblioteca estándar en `tools/`) y el
**comando** que lo reproduce contra la URL pública. Un número sin comando no se escribe. Cómo funciona esto en
detalle, y qué significa y qué no significa cada medición: [METHOD.md](METHOD.md).

## Qué no es este repositorio

- **No es el código fuente de la web.** Nada de aquí construye ni ejecuta zentimes.es. No hay nombres de
  máquina, direcciones, rutas, cuentas, claves ni guiones de despliegue, y no los habrá.
- **No es una promesa de citación por IA.** Ningún número ni etiqueta de este repositorio mide si un motor de
  IA recupera, usa o cita una página, y ninguno lo predice. El cookbook califica el *efecto en el motor* de
  cada una de sus seis técnicas como `experimental`; su esquema declara que ninguna clase de evidencia mide
  retrieval, reranking, generación ni citación; el inspector imprime lo mismo en cada informe. Lo que se mide
  son **precondiciones** de legibilidad —palabras presentes sin JavaScript, hechos tipados que un parser
  extrae, acceso declarado a los crawlers, fragmentos que se sostienen solos, afirmaciones con fuente—, nunca
  el resultado.
- **No es una vista en vivo.** Cada documento es una instantánea fechada en su cabecera. La web cambia; el
  registro no.

## Alcance

- **De quién es la web.** zentimes.es es la web de marca del propio autor; el trabajo que aquí se registra es
  trabajo sobre sus propias páginas, no sobre las de un cliente.
- **Dentro del alcance.** Todo lo que <https://zentimes.es> sirve públicamente: cada URL de su `sitemap.xml`,
  `robots.txt`, `llms.txt`, el inspector público y sus informes.
- **Fuera del alcance.** Cualquier otra web. Cuando aparece otra (la web del cliente a la que enlaza el caso
  público se mide una vez en el CHANGELOG), es una comparación puntual, no un objeto de este registro.
- **Cuándo empieza.** El registro se abrió el 23-09-2026, con el trabajo ya en marcha, y se remonta al
  22-09-2026. Los valores «antes» de la línea base anterior al 22-09-2026 salen de notas internas y no se pueden
  verificar de forma independiente: las páginas anteriores ya no se sirven, así que esas cifras llevan
  `needs-verification` por construcción.

## Cómo leerlo

| Ruta | Qué contiene |
|---|---|
| [`METHOD.md`](METHOD.md) | Los instrumentos, qué mide cada una de las seis recetas y su clase de evidencia, por qué las etiquetas califican precondiciones, la disciplina del contraste, los controles y qué no se mide. |
| [`CHANGELOG.md`](CHANGELOG.md) | El registro fechado, de más reciente a más antiguo, desde el 22-09-2026: qué cambió en la web pública, por qué, cómo se midió y el comando que lo reproduce. Los errores y las retiradas son entradas como cualquier otra. |
| [`audits/`](audits/) | Auditorías fechadas de la superficie pública. Cada número de la tabla resumen enlaza al comando de reproducción de su apéndice. |
| [`criteria/`](criteria/) | Los reglamentos del inspector tal como los imprime la página pública, un fichero por versión de criterios, con las capturas crudas en `captures/`. Un informe que alguien guardó se puede leer contra las reglas que lo produjeron. |
| [`operations/`](operations/) | Stack, pasos de despliegue, los invariantes que bloquean un despliegue, el historial de decisiones y qué puede verificar un cliente desde fuera. Escrito por el lado de operaciones, en español; sin máquinas, rutas, usuarios ni proveedores. |
| [`verification/`](verification/) | Reejecuciones independientes de los comandos publicados: quién ejecutó qué, cuándo y si el número coincidió. Un fichero por reejecución; primera entrada: [`2026-09-23-critic-rerun.md`](verification/2026-09-23-critic-rerun.md). |
| [`tools/`](tools/) | Guiones de Python 3 con biblioteca estándar usados por las auditorías. Los dos que tocan una receta del cookbook ejecutan su propio `reproduce.sh` sin modificar; los dos que reformulan una definición lo dicen en su docstring. |
| [`CITATION.cff`](CITATION.cff) · [`LICENSE`](LICENSE) · [`LICENSES/`](LICENSES/) | Cómo citar este registro (un dataset, versión `2026.09.23`) y los textos completos de las licencias. |

Cuando un hecho no se pudo verificar contra una URL pública o el cookbook fijado, se marca
`needs-verification` en vez de afirmarse. Cuando dos instrumentos discrepan, manda la receta publicada con
DOI, y la discrepancia se anota con los dos valores.

## Cómo reproducir un número

Todos los comandos corren contra la URL pública con `curl`, `perl` y Python 3, sin cuenta en ninguna parte.
Las recetas se bajan del **tag**, nunca de una rama que se mueve:

```sh
curl -sL https://api.github.com/repos/ferinazumaDEV/generative-engine-optimization-cookbook/tarball/v0.1.4 | tar -xz
COOKBOOK=$(ls -d ferinazumaDEV-generative-engine-optimization-cookbook-*/)

# palabras que puede leer en la home un crawler que no ejecuta JavaScript — receta tal como se distribuye
curl -s 'https://zentimes.es/' -o "$COOKBOOK/04-technical/ssr-vs-csr-rendering/before/index.html"
bash "$COOKBOOK/04-technical/ssr-vs-csr-rendering/reproduce.sh" --json | grep before_value
# 526 el 2026-09-23 a las 13:41:52Z (audits/2026-09-23-public-surface.md, A7). La página puede haber cambiado desde entonces.
```

Después, busca el número en la auditoría, lee la entrada del apéndice a la que enlaza y ejecuta ese comando. Si
tu resultado difiere del registrado, la primera pregunta es la fecha: la web se mueve y el registro no. La
segunda es el instrumento: el mismo nombre en otra versión, o un ayudante que «hace lo mismo», es otro
instrumento (en [METHOD.md §1](METHOD.md#1-the-instruments) hay una diferencia de dos palabras que salió de
exactamente eso). Si fecha e instrumento coinciden y los números siguen sin cuadrar, el registro está mal: abre
una issue con tu comando y su salida.

**Dos clases de cambio.** Los cambios en la *web* se registran en [`CHANGELOG.md`](CHANGELOG.md); los cambios en
*este registro* los recoge el historial git del propio repositorio una vez publicado, y ningún otro sitio.

## Licencias

Prosa y datos (todo fichero `.md` y toda captura): **[CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/deed.es)**,
texto completo en [`LICENSE`](LICENSE). Guiones de `tools/`: **MIT**, texto completo en [`LICENSES/MIT.txt`](LICENSES/MIT.txt).
The GEO Cookbook en el que se apoyan las mediciones tiene su propia licencia (prosa CC BY 4.0, código MIT) en su
propio repositorio.

## Siguiente

Planeado, no hecho:

1. Un fichero de datos legible por máquina (una fila por número: marca de tiempo UTC, URL, id o nombre de la
   métrica, valor, instrumento, referencia al comando), para que una reejecución se pueda contrastar con este
   registro de forma mecánica.
2. Un identificador estable por entrada del CHANGELOG y un índice al principio, para que una entrada se pueda
   citar.
3. Una huella SHA-256, junto a cada número, del artefacto *extraído* sobre el que se midió (el texto sin JS, el
   bloque JSON-LD, `robots.txt`, `llms.txt`), no del HTML crudo, cuyo tamaño varía por petición, para que quien
   lee pueda saber si la página que descarga es la que se midió.

---

Fernando Aporta Franco · ferinazumaDEV / Zentimes · <https://zentimes.es>
