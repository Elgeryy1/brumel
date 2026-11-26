# Borradores de publicaciones de lanzamiento (español)

> **BORRADOR. No publicar automáticamente.** Son borradores para que el mantenedor los publique a
> mano. Antes de publicar, comprueba que cada frase sigue coincidiendo con el
> [estado del proyecto](../../../README.md) y con el [plan de lanzamiento](../LAUNCH_PLAN.md).
> En la fase 0 hay que dejar claro que **todavía no hay nada que descargar**.
>
> *This file is intentionally in Spanish (Castilian). The English source is [launch-en.md](launch-en.md).*

---

## 1. Reddit (r/es, r/spain, r/programacion o comunidades similares; fase 0)

**Título:** Estoy empezando un navegador de código abierto basado en Chromium, centrado en eficiencia, privacidad y en no perder lo que tienes abierto. Aún no hay nada que descargar y busco críticas al plan.

**Cuerpo:**

Hola:

He empezado **Brumel**, un navegador de código abierto basado en Chromium. Está en
**pre-desarrollo**: no hay compilaciones ni ejecutables, solo un plan público. Lo publico
ahora porque prefiero acertar con el plan antes que preparar un gran lanzamiento.

Lo que busco:

- **Eficiencia.** Que consuma menos cuando tu equipo lo necesita (jugando, con batería o con
  poca RAM) sin desactivar el sandboxing ni el aislamiento de sitios de Chromium.
- **Memoria.** No perder pestañas, sesiones, borradores ni el contexto de lo que estabas
  haciendo.
- **Web limpia.** Bloqueo nativo de anuncios y rastreadores, sin publicidad propia.
- **Confianza.** Sin telemetría obligatoria, sin cuenta obligatoria y con un registro de
  todas las conexiones que hace el propio navegador.
- **Herramientas del día a día.** Cosas pequeñas que un navegador ya debería hacer: comprimir
  un archivo al subirlo, exportar una tabla a CSV o buscar palabras dentro de un vídeo.

También habrá IA local opcional (modelos pequeños que se ejecutan en tu equipo), desactivada
por defecto y nunca obligatoria.

Lo que **no** prometo: fechas, cifras mágicas de RAM ni que vaya a ser un «asesino de
Chrome». Solo publicaré datos de rendimiento con un benchmark reproducible y los datos en bruto.

Todo es público: hoja de ruta, catálogo de funciones con identificadores y estados, decisiones
de arquitectura y modelo de amenazas.

- Repositorio: https://github.com/Elgeryy1/brumel
- Discusiones: https://github.com/Elgeryy1/brumel/discussions

Me interesa sobre todo saber **qué os hace quedaros con vuestro navegador actual o
abandonarlo**, y qué funciones del plan os parecen innecesarias.

---

## 2. Hilo para X y Bluesky (fase 0)

1/ Estoy creando **Brumel**, un navegador de código abierto basado en Chromium. Eslogan: *Less noise. More control.* Está en pre-desarrollo: todavía no hay compilaciones, solo un plan público. 🧵

2/ La idea: un navegador puede tener cientos de funciones sin que todas estén funcionando siempre. Todo lo opcional se puede desactivar del todo y, desactivado, no debería consumir nada.

3/ Cinco pilares: eficiencia, memoria (no perder tu contexto), web limpia (bloqueo nativo), confianza (sin telemetría ni cuenta obligatorias) y herramientas para el día a día.

4/ La IA local es opcional y gratuita, y funciona en tu propio equipo. Sirve para cosas como agrupar pestañas o encontrar algo en el historial. Viene desactivada y nunca es obligatoria.

5/ Ni fechas ni cifras mágicas de RAM. Los datos de rendimiento solo llegarán con un benchmark reproducible y datos en bruto.

6/ La hoja de ruta, el catálogo de funciones, las decisiones de arquitectura y el modelo de amenazas son públicos. Se agradecen comentarios: github.com/Elgeryy1/brumel

---

## 3. Guion de vídeo corto: TikTok, YouTube Shorts (devlog de la fase 0, unos 45 s)

**[0–3 s]** En pantalla: un navegador con 80 pestañas y el administrador de tareas con la memoria disparada.
**Voz:** «Tu navegador no debería pelearse con tu ordenador».

**[3–12 s]** Corte al repositorio y a la hoja de ruta.
**Voz:** «Estoy empezando Brumel, un navegador de código abierto basado en Chromium. Todavía no hay nada que descargar. Lo estoy construyendo en público desde el primer día».

**[12–30 s]** Cortes rápidos con los cinco pilares en tarjetas de texto.
**Voz:** «Que consuma menos cuando juegas o vas con batería. No perder nunca una sesión. Bloquear anuncios de forma nativa. Sin telemetría ni cuenta obligatorias. Y pequeñas herramientas que resuelven molestias del día a día».

**[30–40 s]** La hoja de propuestas del logo.
**Voz:** «Hasta el logo es todavía un borrador. Dime cuál elegirías tú».

**[40–45 s]** Cierre: «Brumel: Less noise. More control. Enlace en la bio».

> Norma: no mostrar nunca una maqueta como si fuera una función real. Si hay imágenes conceptuales, rotularlas como **Concepto**.

---

## 4. Publicación técnica para la comunidad hispanohablante (fase 1)

**Título:** Cómo mantener un derivado de Chromium mediante una serie de parches

**Cuerpo:** En Brumel fijamos versiones estables de Chromium, mantenemos nuestros cambios como
una serie ordenada de parches, importamos de forma selectiva parches de ungoogled-chromium y
automatizamos los rebases. En este documento explicamos cómo pensamos publicar rápido las
actualizaciones de seguridad y qué partes evitamos tocar a propósito:
https://github.com/Elgeryy1/brumel/blob/main/docs/architecture/UPSTREAM_STRATEGY.md

*(Publicar solo cuando exista la primera compilación reproducible, con tiempos de compilación y espacio en disco reales.)*

---

## 5. Show HN y Product Hunt

Solo se publican en inglés (ver [launch-en.md](launch-en.md)) y **solo** cuando exista una
versión ejecutable (Show HN, alfa pública) o una beta pública (Product Hunt).
