# EL PRECIO DE TODO — Brand System v1 (locked pending your sign-off)

_2026-11-09 · Canal económico en español · Faceless · Opción B “pizarra”_

## 1. Nombre y handle

- **Nombre del canal:** El Precio de Todo
- **Tagline (recomendada, pendiente de confirmar):** *«Todo tiene un precio — y una historia.»*
- **Handle:** `@elpreciodetodo` está **OCUPADO** en YouTube por un canal preexistente (6 subs, 12 vídeos, creado oct-2025 — sin relación con nosotros; ir a por él vía name-squatting no merece la pena y crearía confusión).
- **Verificado en YouTube (2026-11-09, 404 = disponible al comprobar, la reserva final ocurre al registrarlo):**
  1. `@elprecio_detodo` — opción recomendada por claridad
  2. `@elprecio.detodo` — la más cercana al nombre, pero el punto es más fácil de teclear mal
  3. `@elpreciodetodo_ec` — válida pero “sucia”
- **No verificable desde el sandbox (bloqueado/401):** Instagram, TikTok, X. Al registrar, comprobar en la app: `elprecio_detodo` (o la opción elegida) y variante con `_ec`. Recomendación: asegurar las tres plataformas con el MISMO handle el día 1.
- **Alternativa si prefieres un handle limpio 100%**: cambiar ligeramente a *El Precio de Todo — Economía* como nombre y `@elpreciodetodo_ec`, o pasar a una variante distinta del nombre (p. ej., “La Cuestión del Precio”). Solo si no te cuadra ninguna opción.

## 2. Paleta

| Rol | Hex | Uso |
|---|---|---|
| Pizarra | `#10312B` | Fondo principal (tablero) |
| Pizarra oscura | `#0B241F` | Viñeta, bordes, moneda apagada |
| Tiza crema | `#EDE6D3` | Texto principal, anillos, garabatos |
| Tiza amarilla | `#FFD84D` | Números, slabs de énfasis, logo € |
| Tiza coral | `#FF6B57` | Alertas, flechas de subida, grieta, kicker |

Degradados solo radial en el tablero (centro 42%, +#10312B → #0B241F en esquinas). Nunca sobre imagen real.

## 3. Tipografía

- **Anton** (SIL OFL) — display/titulares, números gigantes, miniaturas. Tabular feel; siempre MAYÚSCULAS.
- **Archivo** (SIL OFL) — cuerpo, taglines, chips de fuente. Regular 400 / Bold 700 (instalados y en `fonts/`).
- **Archivo Black** (SIL OFL) — solo emergencia display.
- Licencia: los `.ttf` de `fonts/` son subconjuntos latin OFL recuperados del repo y renombrados (familia «Archivo»/«Anton»); legítimos para embeber en vídeo.

## 4. Logo / marca

**El símbolo:** moneda de tiza agrietada con € — la fractura = la inflación (“el dinero se queda, el valor se parte”). Círculo doble de tiza + € amarillo partido por una grieta jagged coral. Nunca se recolorea; nunca se estira; la grieta siempre cae en diagonal de arriba-izquierda a abajo-derecha.

**Clearspace:** ≥ 25% del diámetro de la moneda por lado libre de texto/borde. **Tamaño mínimo:** 48 px (avatar), 96 px (vídeo end card).

| Asset | Archivo | Uso |
|---|---|---|
| Isotipo master | `logo-mark.svg` (+ `avatar-800.png`) | Avatar YouTube/IG/X — rendir siempre a 800×800, esquinas redondeadas ya incluidas |
| Lockup horizontal | `logo-lockup.svg` (+ `logo-lockup-1680x560.png`) | About, pantallas finales, cabeceras de artículos |
| Banner canal | `banner.svg` (+ `banner-2560x1440.png`) | Cabecera YouTube — zona segura central 1546×423 conservada (wordmark + marca en el tercio central) |
| Miniatura fórmula | `thumbnail-mock.svg` (+ `thumbnail-mock.png`) | EP01 candidato 1: “+4,0%” gigante amarillo + slab tiza «OTRA VEZ» + fuente micro `ZONA EURO · IPC OCT-2026 · EUROSTAT` |

Las SVGs son maestras (font_colas editables, semilla determinista); los PNG son renders (resvg, Nov 2026). Regenerar siempre con `python3 src/generate_brand_svgs.py` + resvg (ver `BRAND-FINAL.md` §Render).

**Render:**
```bash
pip install resvg-py fonttools
python3 src/generate_brand_svgs.py
python3 -c "import resvg_py; resvg_py.svg_to_bytes(svg_path='banner.svg', width=2560, font_dirs=[os.path.expanduser('~/.fonts')])"
```

## 5. Fórmula de miniaturas (todas las que hagamos)

Fondo pizarra · kicker CORAL tracking ancho (fecha/tema ≤ 4 palabras) · UN número o ≤ 3 palabras en Anton amarillo gigante · UN único garabato coral (círculo/subrayado/flecha) · slab crema con 2 palabras verde pizarra (opcional) · pie con fuente en Archivo tracking ancho. Sin caras, sin clutter. Regla de 5 palabras máximas en la miniatura.

## 6. Sistema de vídeo (para el paso de producción)

- Escenario dead-centre 1920×1080, GSAP + HyperFrames, source chips `BLS · EUROSTAT · BCE · FRED` en toda cifra ≥1.5 s.
- Lower third de fuente: pastilla fina crema 12% opacidad, texto Archivo 24px tracking ancho, esquina inferior derecha del elemento (no del frame).
- Contadores count-up siempre; los números aterrizan y se mantienen ≥ 3 s.
- End card 10 s: isotipo + botón suscribir + teaser siguiente episodio + micro-crédito de fuentes.
- Sting 1.5–2.5 s: tac de tiza + page-flip + sub-bass. Sin multitudes.
- Micro-print «Contenido educativo, no consejo financiero» en toda tarjeta de reglas/dinero.

## 7. Descripción de canal (boilerplate)

> Economía en español con números de verdad. Un ejemplo real, una pregunta, cero jerga. Nuevo episodio cada semana.
> 📊 Fuentes siempre en la descripción de cada vídeo: BLS · Eurostat · ECB · FRED
> ⚠️ Contenido educativo — no es consejo financiero.

## 8. Pendiente de ti (sign-off)

1. Handle: `@elprecio_detodo` / `@elprecio.detodo` / `@elpreciodetodo_ec` / otro
2. Tagline: confirmar *«Todo tiene un precio — y una historia.»* o ajustar
3. OK al isotipo/banner o ajustes de diseño (color de pizarra, slab, grieta)
4. Voz ES (en el paso de build haré audition de 2 candidatas)
